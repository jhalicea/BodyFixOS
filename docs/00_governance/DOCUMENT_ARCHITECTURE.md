# BodyFixOS Document & Manual Architecture

Status: **CANDIDATE — LOCAL INVENTORY REQUIRED BEFORE MOVES**  
Date: 2026-10-01

## Purpose

BodyFixOS has software/product documentation in GitHub and a larger body of clinic manuals, operating procedures, brand material, workflow notes, exports and historical files on the owner's computer. Those are not all the same kind of record and should not be mixed into one repository merely for convenience.

This standard creates a durable classification model so the local document cleanup can identify one source of truth, preserve history, and keep private clinic material out of public Git.

## Two document worlds

### 1. Repository-safe product/software documentation

Lives in the BodyFixOS repository when it is safe for public source control and belongs with the software/product architecture.

Examples:

- Architecture Decision Records (ADRs — Architecture Decision Records);
- software architecture;
- public product requirements;
- synthetic workflow examples;
- engineering standards;
- test/runbook documentation that contains no secrets/private client data;
- public glossary and capability boundaries.

### 2. Private BodyFix Clinic operational knowledge

Lives in a **separate BodyFix private document root on the local computer or approved private storage**, never inside HumanOS and never automatically inside the public BodyFixOS repository.

Examples:

- clinic operating manuals;
- internal Standard Operating Procedures (SOPs);
- private pricing/financial planning;
- staff training material not intended for public release;
- vendor contracts/account material;
- real client forms/records;
- private service/assessment procedures;
- internal brand/marketing plans;
- private automation credentials/configuration;
- exports/backups containing operational data.

The exact local private root must be chosen after inventory. It must be separate from `~/.humanos` and from iCloud-synchronized development repositories.

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

## Proposed topical taxonomy

Use the taxonomy as a classification model first. Do not create/move files until the inventory shows which categories are actually needed.

```text
00_governance/
  document-registers
  decision/index material
  document standards

01_product/
  product vision
  requirements
  roadmap
  offer/service model

02_clinic_operations/
  opening/closing procedures
  room/resources/supplies
  service recovery
  staff operations

03_client_journey/
  discovery
  intake
  expectations
  follow-up
  retention

04_scheduling_payments/
  scheduling rules
  cancellation/deposit policies
  payment/reconciliation procedures

05_automation_integrations/
  workflow designs
  vendor integration notes
  automation runbooks

06_security_privacy/
  data classification
  access/privacy procedures
  incident/recovery procedures

07_architecture/
  software architecture
  data/integration architecture
  Architecture Decision Records

08_training_manuals/
  practitioner/staff training
  method/protocol manuals

09_brand_marketing/
  brand standards
  messaging
  campaigns/content systems

10_metrics_reporting/
  metrics definitions
  operating reports
  reconciliation definitions

90_imports/
  unreconciled imported material

99_archive/
  superseded history
  dated legacy packages
```

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
| `hash` | Checksum used for duplicate verification where useful |
| `duplicate_of` | Canonical document ID/path when proven duplicate |
| `conflicts_with` | Conflicting document ID/path if content disagrees |
| `proposed_destination` | Target path after cleanup |
| `confidence` | High / medium / low |
| `action` | Keep / move / quarantine / reconcile / archive |
| `notes` | Provenance, owner decision or uncertainty |

## Source-of-truth rule

A prettier PDF is not automatically the source of truth. A newer modified date is not automatically the source of truth. A GitHub copy is not automatically the source of truth.

Authority is determined from provenance, owner decisions, version history, referenced operational use, and content reconciliation.

When two documents disagree, preserve both and mark a conflict until the owner or authoritative evidence resolves it.

## Move/delete rule

1. Inventory first.
2. Take/check backup.
3. Compute checksums for important candidates.
4. Identify registered Git repositories/worktrees before moving their contents.
5. Move only high-confidence items to approved destinations.
6. Unknown or disputed material goes to dated quarantine/archive, never directly to Trash.
7. Verify links, repository state, application behavior, and document readability after moves.
8. Deletion happens later and separately after retention/verification.

## Naming and versioning

Use stable descriptive names. For user-facing revisions, use simple version suffixes such as `v1`, `v2`, `v3`.

Do not use filenames such as `fixed`, `corrected`, `latest`, `new`, `final-final`, or similar failure/debug labels as the versioning system.

## Relationship to HumanOS

HumanOS may later access explicitly approved BodyFixOS/BodyFix records only through a controlled connector contract. Organizing files near one another on a computer never grants cross-product access.

BodyFixOS private operational documents must not be placed under `~/.humanos` merely so HumanOS can find them.

## Judgment Disclosure

The category names and proposed taxonomy are organizational judgments intended to make the cleanup tractable. They are not a claim that the owner's current computer already follows this structure. The final local tree should be adjusted from the actual inventory instead of forcing every historical file into a preconceived folder.
