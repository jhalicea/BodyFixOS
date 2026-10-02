# BodyFixOS Research Intake / Review Backlog

Status: REVIEW QUEUE — NOT IMPLEMENTED
Date: 2026-09-18

This list preserves useful engineering findings that should not be silently turned into code before the relevant slice exists.

## Adopted foundation concepts

- sovereign core / replaceable infrastructure;
- ports versus connectors;
- anti-corruption adapters;
- canonical internal IDs plus external_refs;
- fake adapters + shared contract tests for high-risk ports;
- independence measured L0-L4 with exit drills;
- trigger-based replacement rather than calendar-based rewrites;
- standards/open formats preferred where they fit;
- modular monolith first;
- AI no-authority and no-AI degraded mode;
- tenant/identity/time/money/audit shapes designed early;
- database-enforced booking concurrency;
- at-least-once/idempotent event assumptions;
- payment reconciliation as a first-class feature;
- immutable-finalized-record plus amendment model;
- vendor/data-class/exit register;
- risk-tiered development and human promotion;
- restoration/fallback/incident readiness.

## Review when implementation reaches the area

1. Managed Postgres/Supabase versus another Postgres host; verify portability and any required BAA/security plan at signup. Prefer standard Postgres access/migrations and avoid unnecessary vendor-specific business logic.
2. Server-only database access versus any browser-direct managed-database API. Current architecture preference: BodyFixOS server/application policy is the primary data door.
3. Drizzle versus Kysely after first SQL migrations are designed.
4. pg-boss versus Graphile Worker after job semantics are known; do not invent a proprietary job engine without evidence.
5. SMS provider comparison; verify compliance, regional behavior, number portability, registration migration, pricing, delivery evidence, health-data restrictions, and observed switch time.
6. Email provider comparison; verify inbound support, transactional/marketing separation, deliverability tooling, suppression export, DNS cutover, security terms, and portability.
7. AI provider selection for v1; start with one behind AIModelPort. Preserve source text, prompts, model versions, and evals so a future switch/re-embedding is possible.
8. Auth provider selection; own canonical user IDs/permission model and link external auth subjects through external_refs. Verify password-hash/MFA export limitations before signup.
9. Object-storage provider; prefer portable/S3-compatible semantics where suitable and document key/encryption ownership.
10. Hosting choice based on long-running worker, network, security, backup, observability, future regulated-mode needs, and exit/restore path.
11. Branch protection/CODEOWNERS/CI policy once starter repository files exist.
12. Vendor register schema and executable data-class + exit metadata gate.
13. Read-access audit/break-glass design.
14. Incident/breach notification runbook with legal review.
15. Clinical retention schedule with legal review.
16. File-upload scanning and metadata policy.
17. SPF/DKIM/DMARC and domain/sender separation.
18. One-way ICS first; two-way calendar synchronization only after core booking is stable.
19. Temporal only after workflow complexity proves Postgres jobs insufficient.
20. SystemFIX multi-tenant admin/billing only after BodyFix clinic proof.
21. Marketing campaign builder and full unified inbox after the core client lifecycle is stable.
22. Migration/import connectors for Vagaro/Acuity/CSV after Research 002 defines external_refs/provenance and before SystemFIX customer onboarding.
23. Exit drills: database restore to another Postgres host, fake provider mode, payment adapter contract test, SMS staging substitution, object-store copy/restore.
24. Licensing/IP review: dependency license scanning/allowlist, AGPL review, provider terms/data-training review, and SystemFIX trademark/legal review. Treat as legal/product risk, not a blocker to architecture research unless a selected dependency triggers it.
25. Repository backup/mirror strategy; GitHub is canonical development evidence but not the sole backup.

## Vendor/connector register fields

- capability;
- PORT or CONNECTOR;
- provider/product;
- approved data classes;
- BodyFixOS-owned state;
- provider-held state;
- external reference types;
- export mechanism;
- fallback provider/path;
- contract renewal/termination notes;
- compliance/BAA applicability where relevant;
- estimated switching time;
- current independence level;
- last exit drill;
- observed blockers/data-loss risk.

## Research 002 invariants

- organization/tenant;
- identity;
- auth-subject linkage;
- permissions;
- time/timezone;
- booking concurrency;
- client;
- consent;
- suppression/opt-out ownership;
- money/ledger;
- reconciliation;
- audit;
- retention/amendments;
- external_refs;
- canonical domain/provider events;
- idempotency keys;
- data classification;
- AI provenance.

## V1 product loop

BOOK -> HOLD -> PAY -> INTAKE -> PREP -> SERVE -> DOCUMENT -> FOLLOW UP

### Slice 1 architecture proof

BOOK -> HOLD -> PAY must also establish:
- canonical internal IDs;
- external_refs;
- PaymentPort;
- FakePaymentAdapter;
- first real payment adapter;
- shared contract tests;
- canonical PaymentCaptured-style event;
- webhook/idempotency rules;
- processor reconciliation.

Everything else remains subordinate to proving the core loop reliably.
