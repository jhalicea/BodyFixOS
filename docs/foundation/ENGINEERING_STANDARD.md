# BodyFixOS Engineering Standard v0.2

Status: FOUNDATION CANDIDATE
Date: 2026-09-18
Scope: product architecture, software delivery, security, AI, integrations, portability, and reliability

## 1. Sovereign core

BodyFixOS is designed to remain independent of any single external SaaS or infrastructure provider while still interoperating deeply with useful external services.

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

Independence means tested exit ability, not maximum self-operation.

External authorities may remain authoritative for facts they legally or operationally control. Example: a payment processor is authoritative for network authorization, settlement, payout, fee, and dispute facts. BodyFixOS remains authoritative for business meaning such as order, package balance, appointment relationship, refund reason, and internal ledger. These truths are reconciled rather than conflated.

## 2. Ports versus connectors

External relationships are classified before implementation.

### Ports — replaceable infrastructure

A port exists when BodyFixOS wants to preserve the capability while being able to replace the implementation.

Candidate ports:
- payments;
- SMS transport;
- email transport;
- AI/model inference;
- authentication provider;
- object storage.

Rules:
- port signatures use BodyFixOS concepts, never provider types;
- provider payloads terminate at an anti-corruption adapter;
- domain code never imports a provider SDK directly;
- adapters translate provider events into canonical BodyFixOS events;
- high-lock-in/high-risk ports ship with a fake adapter and shared contract tests;
- provider-specific identifiers are mapped through external references.

### Connectors — deliberate interoperability

A connector exists when BodyFixOS intentionally works with another business system.

Examples:
- Google/Apple/Microsoft calendars;
- QuickBooks/accounting;
- Zapier/Make;
- review platforms;
- ad platforms;
- external CRM/data imports;
- Vagaro/Acuity/other incumbent migration importers.

Rules:
- scoped OAuth/API keys;
- explicit inbound/outbound data classes;
- canonical BodyFixOS IDs remain internal authority;
- provider IDs live in mapping records;
- import/export semantics are documented;
- webhook/event processing is idempotent;
- disconnect/reconnect degrades safely;
- connectors do not grant external content authority over BodyFixOS tools or policy.

## 3. Lean now, portable later

V1 may use managed infrastructure to reduce operational burden.

Do not self-build commodity network infrastructure merely to claim independence. Card networks, carrier SMS, email transport/deliverability, DNS/certificates, and similar infrastructure should remain rented unless a concrete requirement says otherwise.

Build the product layer:
- segments, campaigns, consent, suppression, message history;
- orders, ledger, package logic;
- model prompts/policies/evals;
- storage semantics and ownership.

Rent the transport/execution underneath through replaceable ports.

Prefer open standards and open formats when they satisfy the requirement: PostgreSQL, S3-compatible object APIs, OIDC/OAuth2, OpenAPI, OpenTelemetry, ICS/CalDAV, JSON/CSV exports. Provider SDKs remain contained inside adapters.

Self-hosting should be possible through containerized/12-factor design, but is not a default product promise. Dedicated managed deployments may precede customer-operated/on-prem deployments.

## 4. Independence levels and exit drills

Assess independence per capability:

- **L0 — Provider-leaky:** provider concepts/proprietary state leak into BodyFixOS domain logic.
- **L1 — Exportable:** canonical data can be exported in documented/open formats.
- **L2 — Replaceable:** fake/alternate implementation passes shared contracts and a bounded provider switch is possible.
- **L3 — Deployable elsewhere:** capability can move to another compatible host/environment and the exit/restore runbook has passed.
- **L4 — Self-operated:** BodyFixOS/SystemFIX operates the underlying infrastructure.

Targets:
- provider capabilities: L2 by SystemFIX launch where commercially important;
- database/compute/storage: L3 where justified;
- L4 only when driven by customer/regulatory/security/economic evidence.

Exit drills must record:
- exact capability/provider;
- starting independence level;
- export/import mechanism;
- fallback provider or target environment;
- observed switching time;
- data/state that could not migrate;
- downtime;
- reconciliation differences;
- rollback;
- resulting independence level.

Replacement is trigger-based, not calendar-based. Valid triggers include security/privacy failure, unacceptable reliability, cost threshold, regulatory/customer need, missing capability, hostile terms, provider shutdown/outage, or an exit drill exposing unacceptable lock-in.

## 5. Architecture style

Start as a modular monolith.

Requirements:
- clear module public interfaces;
- no cross-module database shortcuts without an explicit contract;
- event interfaces for cross-domain reactions where appropriate;
- mechanically enforce boundaries as the codebase grows;
- extract a service only when operational evidence justifies independent deployment.

Do not wrap React, Next.js, or PostgreSQL behind fake universal abstractions solely for symmetry. Abstract business/provider boundaries where replacement/interoperability risk is real.

## 6. Data authority and expensive-to-retrofit invariants

PostgreSQL is the leading system-of-record candidate.

Research 002 must explicitly address:
- organization/tenant;
- canonical identity;
- auth-subject linkage;
- roles/permissions;
- timezone/time representation;
- booking concurrency;
- client;
- consent history;
- suppression/opt-out ownership;
- money/ledger;
- reconciliation;
- audit/provenance;
- retention/amendment;
- external references;
- canonical domain events;
- idempotency keys;
- data classification;
- AI provenance.

Avoid speculative schema for distant features such as gift cards/tips/memberships until needed.

### External references

Provider-specific IDs must not become primary business identity.

Use a normalized external reference mapping concept such as:
- entity type;
- internal entity ID;
- provider;
- external object type;
- external ID;
- metadata/version as needed.

Avoid scattered columns such as `stripe_customer_id`, `twilio_contact_id`, or `google_event_id` across domain tables unless an ADR proves a compelling exception.

## 7. Canonical provider events and anti-corruption

Provider payloads never flow directly into domain logic.

Examples:
- provider `payment_intent.succeeded` -> BodyFixOS `PaymentCaptured`;
- provider delivery webhook -> BodyFixOS `MessageDeliveryConfirmed`.

Persist raw provider evidence only where justified by troubleshooting/audit/privacy requirements; domain behavior consumes canonical normalized events.

## 8. AI no-authority model

AI output is always labeled as draft, suggestion, classification, or summary until accepted by deterministic policy or an authorized human.

Rules:
- minimize context before sending data to a model;
- schema-validate structured AI outputs;
- preserve prompt/model/version provenance for material AI behavior;
- adversarial/prompt-injection evals are required before AI can influence consequential workflows;
- no AI direct authority over payments, finalized notes, consent, permissions, deletion, or medical clearance;
- maintain a kill switch, cost cap, and safe no-AI operation;
- source text should remain available when embeddings/derived representations are used so they can be regenerated with another model.

## 9. Provider/data-class and exit register

Maintain a vendor/tool register.

Each provider/adapter/connector declares:
- capability;
- relationship type: PORT or CONNECTOR;
- provider/product;
- approved data classes;
- BodyFixOS-owned state;
- provider-held state;
- external IDs/reference types;
- export mechanism;
- fallback provider/path;
- contract renewal/termination dependency;
- BAA/compliance scope where applicable;
- estimated switching time;
- current L0-L4 independence level;
- last exit-drill date/result;
- known migration gaps.

Future CI/runtime controls should fail closed if a flow sends an unapproved data class to a provider.

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

## 10. Scheduling correctness

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

## 11. Event/idempotency contract

Assume at-least-once delivery.

Every side-effecting consumer must be replay-safe. Deduplication must be atomic with the effect where possible. External providers should use provider idempotency keys when supported.

Required states:
pending,
processing,
succeeded,
retryable_failure,
dead_letter.

Incoming webhooks require signature verification, event identity, replay protection, and durable evidence appropriate to sensitivity.

Where an external side effect cannot be atomically committed with local state, record intent before send, use provider idempotency mechanisms when available, and reconcile afterward.

## 12. Money and reconciliation

Store money as integer minor units plus currency.

BodyFixOS owns its internal business ledger. Processor settlement/payout/dispute records are external authoritative facts and must be reconciled against that ledger.

Reconciliation must support:
- amount/fee/payout differences;
- missing/duplicate payments;
- refunds;
- disputes/chargebacks;
- provider status drift;
- package/session credit implications;
- human-visible unresolved discrepancies.

"Payments reconciled to the cent" is an operational-readiness gate for live primary use.

## 13. Clinical records and retention

Finalized records are not silently overwritten.

Corrections use amendments containing author, timestamp, reason, and changed content. Deletion/export behavior must honor applicable retention requirements and legal holds.

Retention schedules require legal/compliance review before live clinic deployment.

## 14. Security and access

- least privilege;
- staff MFA;
- explicit permission matrix;
- sensitive-read auditing where appropriate;
- audited break-glass access;
- signed/expiring file URLs;
- upload validation/scanning;
- secrets outside Git;
- staging uses synthetic data;
- production data never becomes default development context;
- AI agents/developer tools receive synthetic/test credentials only.

## 15. Risk-tiered delivery

Tier 0 — docs/copy/styling.
Tier 1 — normal features.
Tier 2 — auth, tenant isolation, money, consent, clinical records, migrations, AI policy, retention, destructive actions, external data flows, provider-boundary/exit changes.

Tier 2 requires:
- explicit threat-model note;
- stronger owner/codeowner review;
- failure/recovery tests;
- no AI-only approval;
- updated vendor/exit register when provider state or data flows change.

## 16. Operational readiness

Before BodyFixOS becomes the clinic's primary system:
- restore drill passes;
- booking concurrency tests pass with zero double-bookings;
- payment reconciliation matches to the cent;
- provider outage/fallback runbook exists;
- incident/breach response runbook exists;
- backups/PITR are verified;
- monitoring and alerting are active;
- rollback path is tested;
- controlled pilot remains stable for an agreed observation period;
- critical provider exit paths are at least documented and their independence level is explicit.

## 17. Accessibility and communications

Public booking targets WCAG 2.2 AA.

Email/SMS architecture must separate transactional from marketing consent and sending streams.

BodyFixOS owns:
- consent evidence;
- opt-out state;
- suppression list where legally/operationally appropriate;
- canonical conversation history;
- campaign/business meaning.

Transport-provider suppression/delivery facts are reconciled/imported so switching providers does not erase compliance state.

## 18. Connectors and migration as product capabilities

SystemFIX customers will arrive with incumbent systems.

Migration connectors/importers should support open formats first and high-value incumbent systems when demand justifies them.

A migration connector must:
- map external IDs through `external_refs`;
- preserve source provenance;
- report unmapped/invalid records;
- be rerunnable/idempotent where feasible;
- never silently coerce clinical/financial meaning;
- produce a reconciliation report.

## 19. SystemFIX extraction

Reusable product structure may later become SystemFIX. Client data and proprietary BodyFix method content do not cross that boundary implicitly.

Generic primitives should be tagged as universal/configurable/proprietary/private as the system matures.
