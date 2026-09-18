# BodyFixOS Vendor / Connector / Exit Register Template

Status: FOUNDATION CANDIDATE
Date: 2026-09-18

Use one record per external provider/product relationship. This register is architecture/risk metadata, not a place for secrets, credentials, PHI, or contract documents containing confidential terms.

## Record

- **Capability:**
- **Relationship type:** PORT | CONNECTOR
- **Provider/product:**
- **Owner:**
- **Risk tier:**
- **Current independence level:** L0 | L1 | L2 | L3 | L4

### Data boundary

- **Approved data classes:**
- **BodyFixOS-owned canonical state:**
- **Provider-held state:**
- **External reference types:**
- **Secrets/credentials location:** reference only; never store secret value here
- **Regulated/compliance scope:** e.g. BAA required? legal review status?

### Interface

- **Port/connector interface:**
- **Provider adapter/connector path:**
- **Open standard/protocol used:**
- **Canonical BodyFixOS events produced/consumed:**
- **Idempotency/replay mechanism:**

### Exit

- **Export mechanism:**
- **Import mechanism:**
- **Fallback provider/path:**
- **Known non-portable state:**
- **Estimated switching time:**
- **Expected downtime:**
- **Contract renewal/termination dependencies:**
- **Termination assistance/export obligations reviewed:** YES | NO | N/A

### Evidence

- **Fake adapter available:** YES | NO | N/A
- **Shared contract suite:** path/result
- **Last exit drill date:**
- **Exit drill target:**
- **Observed switching time:**
- **Observed data loss/gaps:**
- **Reconciliation result:**
- **Rollback result:**
- **Resulting independence level:**
- **Open blockers:**

## Independence definitions

- **L0 — Provider-leaky:** provider concepts/proprietary state leak into the BodyFixOS domain.
- **L1 — Exportable:** canonical data exports in documented/open formats.
- **L2 — Replaceable:** fake/alternate adapter passes contracts and a bounded switch is possible.
- **L3 — Deployable elsewhere:** capability moves to another compatible environment and exit/restore runbook passes.
- **L4 — Self-operated:** BodyFixOS/SystemFIX operates the infrastructure.

## Rule

Do not upgrade the independence level based on architecture intent alone. Upgrade only from evidence.
