#!/usr/bin/env python3
"""Fail when BodyFixOS source code directly imports HumanOS internals.

This is intentionally narrow: documentation may discuss HumanOS, while application
source may not import HumanOS packages/modules. A future approved integration must
use an external connector contract instead of an internal source dependency.
"""

from __future__ import annotations

import ast
import pathlib
import re
import sys


REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
SOURCE_ROOT_NAMES = ("src", "app", "lib", "packages", "server", "components")
CODE_SUFFIXES = {".py", ".js", ".jsx", ".ts", ".tsx", ".mjs", ".cjs"}
EXCLUDED_PARTS = {"node_modules", ".next", ".git", ".venv", "venv", "dist", "build"}


def iter_source_files():
    seen = set()
    for root_name in SOURCE_ROOT_NAMES:
        root = REPO_ROOT / root_name
        if not root.exists():
            continue
        for path in root.rglob("*"):
            if not path.is_file() or path.suffix not in CODE_SUFFIXES:
                continue
            if set(path.relative_to(REPO_ROOT).parts) & EXCLUDED_PARTS:
                continue
            if path in seen:
                continue
            seen.add(path)
            yield path


def python_imports_humanos(path: pathlib.Path):
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    findings = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name.lower().startswith("humanos"):
                    findings.append((node.lineno, alias.name))
        elif isinstance(node, ast.ImportFrom) and node.module:
            if node.module.lower().startswith("humanos"):
                findings.append((node.lineno, node.module))
    return findings


def javascript_imports_humanos(path: pathlib.Path):
    text = path.read_text(encoding="utf-8")
    pattern = re.compile(
        r"(?:from\s+|import\s*\(|require\s*\()\s*['\"]([^'\"]+)['\"]",
        re.MULTILINE,
    )
    findings = []
    for match in pattern.finditer(text):
        module = match.group(1)
        normalized = module.lower().replace("-", "").replace("_", "")
        if normalized.startswith("humanos") or "/humanos" in normalized:
            line = text.count("\n", 0, match.start()) + 1
            findings.append((line, module))
    return findings


def main() -> int:
    violations = []
    for path in iter_source_files():
        try:
            if path.suffix == ".py":
                findings = python_imports_humanos(path)
            else:
                findings = javascript_imports_humanos(path)
        except (SyntaxError, UnicodeDecodeError) as exc:
            print(f"Could not inspect {path.relative_to(REPO_ROOT)}: {exc}", file=sys.stderr)
            return 2

        for line, module in findings:
            violations.append(
                f"{path.relative_to(REPO_ROOT)}:{line}: direct HumanOS import {module!r}"
            )

    if violations:
        print(
            "BodyFixOS and HumanOS are independent products. Direct HumanOS source "
            "imports are prohibited; use a separately approved external connector contract.",
            file=sys.stderr,
        )
        for violation in violations:
            print(f"- {violation}", file=sys.stderr)
        return 1

    print("BodyFixOS product-boundary source-import check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
