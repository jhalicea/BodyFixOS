# BodyFixOS Architecture Baseline Plan

Status: **GREENFIELD ARCHITECTURE CANDIDATE — NO IMPLEMENTATION CLAIM**  
Baseline: `main` @ `64c8226e4b5e59698586e7612acac1166da10384`  
Date: 2026-10-01

## 1. Evidence-backed current state

At this baseline, the public BodyFixOS repository contains a design/roadmap README and no application source tree, test suite, CI workflow, database schema, runtime, deployment configuration or production integration code.

Therefore BodyFixOS must **not** be described as a brownfield implemented software system yet. Its current architecture is conceptual. The next architecture work is greenfield design grounded in verified business workflows and privacy requirements.

## 2. Product boundary — hard invariant

BodyFixOS is an independent software product for BodyFix Clinic operations.

It owns its own:

- repository and local project folder;
- architecture and domain model;
- private operational data stores;
- credentials and secrets;
- tests and evaluation fixtures;
- CI/CD and releases;
- runbooks, backups and recovery procedures;
- security/privacy boundary;
- roadmap and architectural decisions.

BodyFixOS is **not** a HumanOS module, subdirectory, database namespace or internal package.

A future HumanOS integration, if deliberately approved, must be an external connector/API boundary:

```text
HumanOS                         BodyFixOS
   |                               |
   |  explicit versioned contract  |
   +------ connector / API --------+
          narrow scope
          minimal data
          separate identity
          revocable permission
          audit trail
```

No shared database, implicit source imports, shared private-state directory, or automatic HumanOS access to BodyFixOS records is allowed by default.

## 3. Product purpose from current repository evidence

The existing roadmap establishes these product goals:

- preserve a high-touch human-centered client experience;
- standardize discovery/intake, expectations, scheduling, follow-up and service recovery;
- reduce repetitive administrative work with bounded automation;
- track operational outcomes without unsupported medical claims;
- use least-privilege access and deliberate data collection;
- support repeatable operations for future locations and teams.

Those goals drive the architecture; technology choices do not come first.

## 4. Architecturally significant quality attributes

Before selecting frameworks/vendors, BodyFixOS should define testable scenarios for:

### Privacy and data minimization
Collect and retain only information required for legitimate operations. Public code/tests use synthetic data. Private client information never belongs in the public repository.

### Human authority
Automation may recommend, prepare, classify or route work, but consequential client/business actions follow explicit authority rules.

### Reliability
Scheduling, deposits, reminders and follow-up workflows must have visible failure states, retry/recovery behavior and duplicate-prevention where applicable.

### Auditability
Important business/automation actions should be attributable to a human or system identity with timestamps and outcomes.

### Portability
Core business rules should not be inseparable from one scheduling, payment, messaging, AI or cloud provider.

### Modifiability
External vendor integrations should be replaceable through explicit adapter boundaries rather than leaking provider-specific calls across business logic.

### Security
Credentials, client data and privileged operations follow least privilege, environment separation and auditable access.

### Operational simplicity
As an early product, complexity must be justified. The default is the simplest architecture that can safely support current workflows and evidence gathering.

### Recoverability
Backups, exports and tested restore/reconciliation procedures must exist before the system becomes operationally critical.

## 5. Proposed domain map — to validate with workflow evidence

The following is a **target hypothesis**, not an implemented map:

```text
BodyFixOS
|
+-- Client Journey
|   discovery, expectations, intake workflow, follow-up, retention
|
+-- Scheduling & Capacity
|   appointments, availability, rooms/resources, rescheduling/cancellation
|
+-- Payments & Deposits
|   pricing references, deposits, payment status, refund/cancellation rules
|
+-- Service Operations
|   session workflow, operational checklists, service recovery, handoffs
|
+-- Communications
|   reminders, confirmations, follow-up messages, communication preferences
|
+-- Knowledge & Training
|   procedures, protocols, staff guidance, versioned operating knowledge
|
+-- Reporting & Metrics
|   operational metrics, reconciliation, quality indicators
|
+-- Identity / Permissions / Audit
    user identities, roles, approvals, audit events, privacy controls
```

The domain map must be validated against real workflows before code boundaries are frozen.

## 6. Proposed architecture style

### Sensible default: modular monolith first

For an early product with one primary business domain and a small engineering/operations team, the starting target should be a modular monolith unless evidence proves independent services are needed.

That means one deployable application may contain clear internal modules, but modules own their rules/data access and communicate through explicit interfaces.

This avoids premature distributed-system cost while preserving boundaries that could later support extraction if scale, isolation, compliance, ownership or availability needs justify it.

This is a default, not a permanent rule or a claim that BodyFixOS is currently implemented this way.

## 7. External systems as ports/adapters

Potential categories of external dependency should sit behind adapters:

```text
BodyFixOS application/domain
        |
        +-- SchedulingPort  -> scheduling vendor adapter
        +-- PaymentPort     -> payment processor adapter
        +-- MessagingPort   -> SMS/email provider adapter
        +-- CRMPort         -> CRM/client-management adapter if used
        +-- AutomationPort  -> workflow/automation platform adapter if used
        +-- AIServicePort   -> optional bounded AI provider adapter
        +-- HumanOSPort     -> future optional HumanOS connector only
```

The domain layer should not know provider SDK details.

## 8. Data architecture principles

Before defining tables/schemas, classify data by purpose and sensitivity.

At minimum distinguish:

- public/business-reference data;
- operational configuration;
- client contact/appointment data;
- payment-status references/tokens (avoid storing raw payment credentials where a processor can own them);
- private service/assessment records if later required;
- audit/event records;
- analytics/derived metrics;
- synthetic test fixtures.

Each category requires explicit owner, retention, export/deletion expectations, access policy and backup/recovery behavior.

BodyFixOS should not copy all vendor data locally merely because an API makes it available.

## 9. Automation architecture

Automation should progress from deterministic workflows to AI assistance only where the outcome can be verified.

Suggested authority tiers:

### GREEN — read/prepare/reversible
Examples: calculate a report, prepare a draft reminder, detect missing fields, generate an internal checklist.

### AMBER — operational write with recovery
Examples: update a non-destructive internal status, create a draft follow-up, prepare a schedule change for approval.

### RED — consequential external action
Examples: charge/refund money, send sensitive client communications, cancel appointments, delete records, change permissions, deploy production changes.

RED actions require explicit approval/policy enforcement outside the model or workflow engine.

## 10. Security and privacy architecture

Before production implementation, create:

- data-flow diagram and trust boundaries;
- threat model;
- identity/authentication design;
- authorization model;
- secrets policy;
- vendor/subprocessor inventory;
- audit requirements;
- retention/export/deletion policy;
- backup/recovery procedure;
- incident-response runbook;
- synthetic-data test policy.

If future workflows involve regulated health information or other legally protected data, applicable obligations and vendor agreements must be evaluated before those workflows are enabled. Architecture documents should state verified requirements rather than assuming a regulatory classification.

## 11. Engineering baseline to establish before implementation

The first implementation ADRs should deliberately choose and record:

- primary language/runtime;
- application/web framework;
- database/storage;
- local development environment;
- IDE/editor-neutral tooling requirements;
- package/dependency manager;
- formatter/linter/type checking;
- unit/integration/end-to-end testing strategy;
- migrations;
- CI/CD;
- hosting/deployment environment;
- configuration/secrets management;
- logging/metrics/tracing/alerting;
- backup/restore;
- versioning/release/rollback;
- dependency/security scanning.

No technology should be inserted merely because HumanOS uses it. Reuse patterns when they fit; preserve product independence.

## 12. Proposed repository structure — target, not implemented

```text
BodyFixOS/
|
+-- README.md
+-- docs/
|   +-- architecture/
|   +-- decisions/
|   +-- security/
|   +-- runbooks/
|   +-- product/
|
+-- src/ or app/
|   +-- client_journey/
|   +-- scheduling/
|   +-- payments/
|   +-- service_operations/
|   +-- communications/
|   +-- knowledge/
|   +-- reporting/
|   +-- identity_audit/
|   +-- integrations/
|
+-- tests/
+-- scripts/
+-- infrastructure/   # only if/when infrastructure-as-code exists
+-- .github/workflows/
```

The final structure follows the chosen language/framework and validated module boundaries; these names are illustrative.

## 13. Architecture documentation set

The first architecture milestone should produce:

1. System Context (C4 L1)
2. Container/application view (C4 L2)
3. Domain/bounded-context map
4. Client/business workflow map
5. Data classification + ownership/lifecycle map
6. Trust-boundary/threat model
7. Integration/vendor adapter map
8. Deployment/build/release map
9. Quality-attribute scenarios
10. ADR register
11. Engineering baseline
12. Runbook/recovery skeleton

## 14. First thin vertical slice

Do not build the entire clinic operating system first.

After architecture baseline approval, select one small real workflow that can be tested end-to-end with synthetic/private-safe data. Example categories include a bounded appointment/follow-up workflow or an internal operational checklist.

The slice should demonstrate:

`input → validation → domain rule → persistence/integration → visible result → audit evidence → failure/recovery → tests`

Only after observing the slice should the architecture expand.

## 15. Anti-drift rules

- Every major structural/security/data decision gets an ADR.
- Architecture diagrams state `AS-BUILT` or `TARGET`; never blur them.
- Public documentation cannot claim a capability based only on a plan.
- CI eventually checks important dependency/boundary rules.
- Each release reviews architecture drift and vendor/data-boundary changes.
- Generated evidence belongs in designated artifact locations, not the repository root.
- Worktrees, backups and migration exports have designated local locations separate from the canonical repository.
- BodyFixOS remains independently buildable, testable, deployable and recoverable without HumanOS.
