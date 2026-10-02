# BodyFixOS Document & Manual Architecture

Status: **CANDIDATE — LOCAL INVENTORY REQUIRED BEFORE MOVES**  
Date: 2026-10-01

## Purpose

BodyFixOS has software/product documentation in GitHub and BodyFix Clinic already has a larger private body of manuals, operating procedures, brand material, workflow notes, forms, exports and historical files. Those are different record systems and should not be collapsed into one repository merely for convenience.

This standard creates a durable classification model so local cleanup can recover the existing BodyFix master document system, identify sources of truth, preserve history, and keep private clinic material out of public Git.

## Two document worlds

### 1. Repository-safe BodyFixOS product/software documentation

Lives in the BodyFixOS repository only when it is safe for public source control and belongs with software/product engineering.

Examples:

- ADRs (Architecture Decision Records);
- software architecture;
- public product requirements;
- synthetic workflow examples;
- engineering standards;
- test/runbook documentation that contains no secrets/private client data;
- public glossary and capability boundaries.

### 2. Private BodyFix Clinic master system

Lives in a **separate BodyFix private document root on the local computer or approved private storage**, never inside HumanOS and never automatically inside the public BodyFixOS repository.

Examples:

- company/current operating binder;
- booking/client-management procedures;
- client forms and documentation;
- policies/compliance working material;
- marketing/client education;
- sales/conversion systems;
- private BodyFix Structural Method training manuals/protocols;
- operations/staff training;
- finance/pricing/capacity records;
- expansion/school planning;
- assets/media library;
- historical archive.

The exact local private root must be recovered/approved through the inventory. It must be separate from `~/.humanos` and from iCloud-synchronized development repositories.

## Preserve the existing BodyFix master-system taxonomy

BodyFix already has an established numbered master-system/folder model from prior business work. The local cleanup must **recover and reconcile that existing structure instead of inventing a second competing folder taxonomy**.

This repository document intentionally does not replicate all private master-system contents. The local/private document register is the correct place to map the owner's established numbered folders, manuals, working addenda, exports and archives.

If the existing master-system structure has gaps, the cleanup should propose a versioned amendment rather than silently replacing it.

## Document classes

Every discovered BodyFix/BodyFixOS document receives exactly one primary class:

- `PUBLIC_REPO_SOURCE` — canonical repository-safe product/software source document.
- `PRIVATE_SOURCE_OF_TRUTH` — canonical private clinic/business document.
- `GENERATED_EXPORT` — PDF, rendered copy, report, screenshot, or other output derived from a source.
- `IMPORT_UNRECONCILED` — imported material not yet reconciled against canonical state.
- `REFERENCE_EXTERNAL` — third-party/reference material, not BodyFix-authored canonical truth.
- `LEGACY_SUPERSEDED` — preserved historical version with a known replacement.
- `DUPLICATE_VERIFIED` — byte/content duplicate verified against a canonical copy.
- `UNKNOWN` — classification or authority is not yet known; blocks deletion.

Sensitivity is a separate axis:

- `PUBLIC`
- `INTERNAL`
- `CONFIDENTIAL`
- `CLIENT_PRIVATE`
- `SECRET_CREDENTIAL` — credentials should normally move to a secrets system, not remain as ordinary documents.

## Document register

Before moving a document, record:

| Field | Meaning |
|---|---|
| `document_id` | Stable BodyFix document identifier once assigned |
| `title` | Human-readable title |
| `current_path` | Exact current local path |
| `file_type` | Markdown, Word, PDF, spreadsheet, image, etc. |
| `document_class` | One class from this standard |
| `sensitivity` | Public/internal/confidential/client-private/secret |
| `version_or_date` | Existing version/date if known |
| `authority_status` | Canonical / candidate / export / superseded / unknown |
| `master_system_location` | Existing private BodyFix numbered folder/subfolder when known |
| `hash` | Checksum used for duplicate verification where useful |
| `duplicate_of` | Canonical document ID/path when proven duplicate |
| `conflicts_with` | Conflicting document ID/path if content disagrees |
| `proposed_destination` | Target path after cleanup |
| `confidence` | High / medium / low |
| `action` | Keep / move / quarantine / reconcile / archive |
| `notes` | Provenance, owner decision or uncertainty |

## Master-system reconciliation procedure

For every discovered private BodyFix document:

1. identify whether the document is already named/referenced by the established BodyFix master system, Current Version Index, Pending Addendum Ledger, operating binder, or archive structure;
2. determine whether the file is a source document, generated export, working addendum, reference, duplicate, or superseded copy;
3. compare version/date/provenance against other copies without assuming the newest modified timestamp is authoritative;
4. assign the existing master-system location when known;
5. preserve conflicts until reconciled;
6. move only after backup, checksum, confidence and owner/authority requirements are satisfied;
7. update the private Current Version Index/register after a verified move.

## Source-of-truth rule

A prettier PDF is not automatically the source of truth. A newer modified date is not automatically the source of truth. A GitHub copy is not automatically the source of truth.

Authority is determined from provenance, owner decisions, version history, referenced operational use, and content reconciliation.

When two documents disagree, preserve both and mark a conflict until the owner or authoritative evidence resolves it.

## Working addenda

Pending addenda and inventory notes are evidence of work that has **not yet been merged into the private master system**. They should be preserved as `IMPORT_UNRECONCILED` or equivalent pending material until the affected master documents are reconciled.

Do not treat a pending addendum as automatically authoritative merely because it is newer.

## Move/delete rule

1. Inventory first.
2. Take/check backup.
3. Compute checksums for important candidates.
4. Identify registered Git repositories/worktrees before moving their contents.
5. Move only high-confidence items to approved destinations.
6. Unknown or disputed material goes to dated quarantine/archive, never directly to Trash.
7. Verify links, repository state, application behavior, and document readability after moves.
8. Update the private document register/Current Version Index after verification.
9. Deletion happens later and separately after retention/verification.

## Naming and versioning

Use stable descriptive names. For user-facing revisions, use simple version suffixes such as `v1`, `v2`, `v3`.

Do not use filenames such as `fixed`, `corrected`, `latest`, `new`, `final-final`, or similar failure/debug labels as the versioning system.

## Relationship to HumanOS

HumanOS may later access explicitly approved BodyFixOS/BodyFix records only through a controlled connector contract. Organizing files near one another on a computer never grants cross-product access.

BodyFixOS private operational documents must not be placed under `~/.humanos` merely so HumanOS can find them.

## Judgment Disclosure

This document deliberately preserves the owner's existing BodyFix master-system concept rather than introducing a new topical folder tree. The exact local private root, duplicate resolution and any amendment to the existing numbered system remain pending the machine-local inventory and owner ratification.
