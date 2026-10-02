#!/usr/bin/env python3
"""Build a read-only BodyFix/BodyFixOS document register from explicit local roots.

The tool never moves, renames, deletes, edits, uploads, commits, or opens document
contents. It records metadata and SHA-256 hashes so duplicates can be reconciled
before any cleanup.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import pathlib
from datetime import datetime, timezone


DOCUMENT_SUFFIXES = {
    ".md", ".txt", ".pdf", ".doc", ".docx", ".rtf",
    ".xls", ".xlsx", ".csv", ".ppt", ".pptx", ".pages", ".numbers", ".key",
    ".json", ".yaml", ".yml",
}

SKIP_DIRS = {
    ".git", "node_modules", ".next", "dist", "build", ".venv", "venv",
    "__pycache__", ".Trash", "Library", "Applications",
}

BODYFIX_HINTS = {
    "bodyfix", "body fix", "structural", "clinic", "massage", "ganesha",
    "intake", "assessment", "deposit", "cancellation", "client", "vagaro",
    "sop", "manual", "protocol", "pricing", "brand", "follow-up", "followup",
}


def sha256(path: pathlib.Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def classify_filename(path: pathlib.Path) -> tuple[str, str, str | None]:
    name = path.stem.lower()

    if any(token in name for token in ("archive", "legacy", "old", "obsolete")):
        return "LEGACY_SUPERSEDED", "LOW", "99_archive/"
    if any(token in name for token in ("import", "export", "migration")):
        return "IMPORT_UNRECONCILED", "MEDIUM", "90_imports/"
    if any(token in name for token in ("architecture", "adr", "engineering")):
        return "UNKNOWN", "MEDIUM", "07_architecture/"
    if any(token in name for token in ("privacy", "security", "consent", "incident")):
        return "UNKNOWN", "MEDIUM", "06_security_privacy/"
    if any(token in name for token in ("schedule", "deposit", "payment", "cancel")):
        return "UNKNOWN", "MEDIUM", "04_scheduling_payments/"
    if any(token in name for token in ("intake", "follow", "retention", "journey")):
        return "UNKNOWN", "MEDIUM", "03_client_journey/"
    if any(token in name for token in ("manual", "training", "protocol", "method")):
        return "UNKNOWN", "MEDIUM", "08_training_manuals/"
    if any(token in name for token in ("brand", "marketing", "campaign", "social")):
        return "UNKNOWN", "MEDIUM", "09_brand_marketing/"
    if any(token in name for token in ("metric", "report", "dashboard", "kpi")):
        return "UNKNOWN", "MEDIUM", "10_metrics_reporting/"
    if any(token in name for token in ("workflow", "automation", "zapier", "n8n", "integration")):
        return "UNKNOWN", "MEDIUM", "05_automation_integrations/"
    if any(token in name for token in ("room", "supply", "operation", "opening", "closing")):
        return "UNKNOWN", "MEDIUM", "02_clinic_operations/"
    if any(token in name for token in ("product", "roadmap", "offer", "pricing")):
        return "UNKNOWN", "MEDIUM", "01_product/"

    return "UNKNOWN", "LOW", None


def looks_relevant(path: pathlib.Path) -> bool:
    lower = str(path).lower().replace("_", " ").replace("-", " ")
    return any(hint in lower for hint in BODYFIX_HINTS)


def iter_documents(root: pathlib.Path, include_all: bool):
    for path in root.rglob("*"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if not path.is_file() or path.suffix.lower() not in DOCUMENT_SUFFIXES:
            continue
        if include_all or looks_relevant(path):
            yield path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", action="append", required=True, help="Explicit root to scan; repeat as needed.")
    parser.add_argument("--output-dir", required=True, help="Dedicated output directory for the register.")
    parser.add_argument(
        "--include-all-documents",
        action="store_true",
        help="Include every supported document under the explicit roots, not only BodyFix-like names/paths.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    output_dir = pathlib.Path(args.output_dir).expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    records = []
    hashes: dict[str, list[str]] = {}

    for root_text in args.root:
        root = pathlib.Path(root_text).expanduser().resolve()
        if not root.exists():
            records.append({
                "current_path": str(root),
                "authority_status": "UNKNOWN",
                "notes": "Requested scan root does not exist",
            })
            continue

        for path in iter_documents(root, args.include_all_documents):
            stat = path.stat()
            digest = sha256(path)
            doc_class, confidence, proposed = classify_filename(path)
            hashes.setdefault(digest, []).append(str(path))
            records.append({
                "document_id": "",
                "title": path.stem,
                "current_path": str(path),
                "file_type": path.suffix.lower().lstrip("."),
                "document_class": doc_class,
                "sensitivity": "UNKNOWN",
                "version_or_date": "",
                "authority_status": "UNKNOWN",
                "hash": digest,
                "duplicate_of": "",
                "conflicts_with": "",
                "proposed_destination": proposed or "",
                "confidence": confidence,
                "action": "REVIEW",
                "size_bytes": stat.st_size,
                "modified_utc": datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc).isoformat(),
                "notes": "Metadata-only inventory; document contents were not opened.",
            })

    canonical_for_hash = {digest: paths[0] for digest, paths in hashes.items() if len(paths) > 1}
    for record in records:
        digest = record.get("hash")
        current = record.get("current_path")
        if digest in canonical_for_hash and current != canonical_for_hash[digest]:
            record["document_class"] = "DUPLICATE_VERIFIED"
            record["duplicate_of"] = canonical_for_hash[digest]
            record["action"] = "QUARANTINE_AFTER_AUTHORITY_REVIEW"
            record["confidence"] = "HIGH"

    records.sort(key=lambda row: row.get("current_path", ""))
    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    csv_path = output_dir / f"BODYFIX_DOCUMENT_REGISTER_{timestamp}.csv"
    json_path = output_dir / f"BODYFIX_DOCUMENT_REGISTER_{timestamp}.json"

    fields = [
        "document_id", "title", "current_path", "file_type", "document_class",
        "sensitivity", "version_or_date", "authority_status", "hash", "duplicate_of",
        "conflicts_with", "proposed_destination", "confidence", "action", "size_bytes",
        "modified_utc", "notes",
    ]
    with csv_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(records)

    json_path.write_text(json.dumps(records, indent=2, sort_keys=True), encoding="utf-8")

    print(f"BodyFix document inventory complete: {len(records)} records")
    print(f"CSV:  {csv_path}")
    print(f"JSON: {json_path}")
    print("No document was moved, renamed, deleted, edited, uploaded, committed, or opened for content inspection.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
