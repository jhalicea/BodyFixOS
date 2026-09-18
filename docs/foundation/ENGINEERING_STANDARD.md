# BodyFixOS Engineering Standard v0.1

Status: FOUNDATION CANDIDATE
Date: 2026-09-18
Scope: product architecture, software delivery, security, AI, integrations, and reliability

## 1. Sovereign core

BodyFixOS is designed to become independent of any single external SaaS or infrastructure provider.

BodyFixOS owns:
- booking and availability semantics;
- CRM/client lifecycle;
- intake/consent;
- assessment/session/clinical workflows;
- package/ledger business rules;
- conversation and campaign history;
- automation policy;
- AI policy/orchestration;
- analytics;
- permissions, audit, retention, and product configuration.

Infrastructure providers are replaceable rails. They do not own canonical BodyFixOS state.

## 2. Lean now, portable later

V1 may use managed infrastructure to reduce operational burden, but every external provider must sit behind a BodyFixOS-owned interface.

Do not self-build commodity network infrastructure merely to claim independence. Independence means portable data, replaceable adapters, open formats, and an owned domain model.

## 3. Architecture style

Start as a modular monolith.

Requirements:
- clear module public interfaces;
- no cross-module database shortcuts without an explicit contract;
- event interfaces for cross-domain reactions where appropriate;
- mechanically enforce boundaries as the codebase grows;
- extract a service only when operational evidence justifies independent deployment.

## 4. Data authority

PostgreSQL is the leading system-of-record candidate.

Expensive-to-retrofit invariants must be designed before live use:
- organization/tenant;
- identity and roles;
- timezone/time representation;
- money representation;
- booking concurrency;
- consent history;
- audit/provenance;
- retention/amendment.

Avoid speculative schema for distant features.

## 5. AI no-authority model

AI output is always labeled as draft, suggestion, classification, or summary until accepted by deterministic policy or an authorized human.

Rules:
- minimize context before sending data to a model;
- schema-validate structured AI outputs;
- preserve prompt/model/version provenance for material AI behavior;
- adversarial/prompt-injection evals are required before AI can influence consequential workflows;
- no AI direct authority over payments, finalized notes, consent, permissions, deletion, or medical clearance;
- maintain a kill switch and safe no-AI operation.

## 6. Provider/data-class gate

Maintain a vendor/tool register.

Each provider/adapter declares the data classes it is permitted to receive. Future CI/runtime controls should fail closed if a flow sends an unapproved class to a provider.

Example classes:
PUBLIC,
BUSINESS_INTERNAL,
CONTACT_DATA,
FINANCIAL_METADATA,
HEALTH_ADJACENT,
CLINICAL,
AUTH_SECRET,
PAYMENT_CARD (must remain processor-tokenized, not application-stored).

Provider approval does not imply every feature of that provider is approved.

## 7. Scheduling correctness

Availability is a correctness domain, not just UI.

Requirements:
- UTC instants plus IANA timezone per location;
- buffers included in blocked time;
- holds represented durably;
- provider/resource/room collisions prevented at database level;
- stale holds cleared safely;
- rate limits against hold-hoarding abuse;
- privacy-preserving account discovery behavior;
- concurrency tests with many simultaneous requests for the same slot.

## 8. Event/idempotency contract

Assume at-least-once delivery.

Every side-effecting consumer must be replay-safe. Deduplication must be atomic with the effect where possible. External providers should use provider idempotency keys when supported.

Required states:
pending,
processing,
succeeded,
retryable_failure,
dead_letter.

Incoming webhooks require signature verification, event identity, replay protection, and durable evidence appropriate to sensitivity.

## 9. Clinical records and retention

Finalized records are not silently overwritten.

Corrections use amendments containing author, timestamp, reason, and changed content. Deletion/export behavior must honor applicable retention requirements and legal holds.

Retention schedules require legal/compliance review before live clinic deployment.

## 10. Security and access

- least privilege;
- staff MFA;
- explicit permission matrix;
- sensitive-read auditing where appropriate;
- audited break-glass access;
- signed/expiring file URLs;
- upload validation/scanning;
- secrets outside Git;
- staging uses synthetic data;
- production data never becomes default development context.

## 11. Risk-tiered delivery

Tier 0 — docs/copy/styling.
Tier 1 — normal features.
Tier 2 — auth, tenant isolation, money, consent, clinical records, migrations, AI policy, retention, destructive actions, external data flows.

Tier 2 requires:
- explicit threat-model note;
- stronger owner/codeowner review;
- failure/recovery tests;
- no AI-only approval.

## 12. Operational readiness

Before BodyFixOS becomes the clinic's primary system:
- restore drill passes;
- booking concurrency tests pass with zero double-bookings;
- payment reconciliation matches to the cent;
- provider outage/fallback runbook exists;
- incident/breach response runbook exists;
- backups/PITR are verified;
- monitoring and alerting are active;
- rollback path is tested;
- controlled pilot remains stable for an agreed observation period.

## 13. Accessibility and communications

Public booking targets WCAG 2.2 AA.

Email/SMS architecture must separate transactional from marketing consent and sending streams. Consent/opt-out history is canonical BodyFixOS data.

## 14. SystemFIX extraction

Reusable product structure may later become SystemFIX. Client data and proprietary BodyFix method content do not cross that boundary implicitly.

Generic primitives should be tagged as universal/configurable/proprietary/private as the system matures.
