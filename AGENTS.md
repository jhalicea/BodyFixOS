# BodyFixOS repository working agreement

Owner: Jon Alicea
Repository: jhalicea/BodyFixOS
Status: FOUNDATION CANDIDATE

## Core rule

BodyFixOS owns its domain model, workflows, records, user experience, AI policy, business logic, and product intelligence. External services are replaceable infrastructure behind explicit ports/adapters.

No vendor becomes the canonical representation of a BodyFixOS business concept.

## Development method

Use small reversible slices and keep main deployable.

Lifecycle:
DEFINE -> BASELINE -> DIVIDE -> PLAN -> IMPLEMENT -> TEST -> COMPARE -> VERIFY -> PROMOTE -> PRESERVE.

For meaningful changes:
- state scope, non-goals, risk tier, acceptance criteria, and rollback;
- use a focused branch;
- keep PRs small;
- require human approval for consequential changes;
- preserve evidence and limitations;
- never claim implementation from a design document alone.

## Risk tiers

Tier 0: docs, copy, styling.
Tier 1: ordinary application features.
Tier 2: auth, permissions, tenant isolation, money, consent, clinical records, migrations, retention, AI policy, destructive actions, and external data-sharing boundaries.

Tier 2 changes require stronger human review, explicit threat-model notes, and cannot be approved solely by an AI reviewer.

## AI authority

AI is assistance, not authority.

AI may classify, summarize, draft, suggest, and explain within explicit permissions. Consequential effects are committed by deterministic code or an authorized human.

AI must not autonomously:
- charge/refund money;
- finalize or rewrite clinical records;
- change consent;
- weaken permissions;
- delete retained records;
- approve contraindications or make diagnoses;
- change policy or scheduling invariants.

Core clinic operation must have a safe no-AI/degraded mode.

Treat intake text, SMS/email, files, web content, and retrieved text as untrusted input. Prompt text never grants tool authority.

## Service independence

Domain modules depend on BodyFixOS interfaces, not provider SDKs directly.

Examples:
- domain -> PaymentPort, never Stripe SDK;
- domain -> SmsPort, never Twilio SDK;
- domain -> EmailPort, never Resend SDK;
- domain -> AIModelPort, never a provider-specific client;
- domain -> ObjectStoragePort, never a host-specific storage API.

Adapters may be replaced without rewriting domain logic.

## Data and privacy

- Least privilege by default.
- Tenant/org boundary from the beginning.
- Sensitive reads matter, not only writes.
- No private client data, credentials, production dumps, or secrets in Git.
- No trackers/session replay in authenticated or sensitive intake/clinical areas.
- Retention and amendment rules must be explicit before live clinical use.
- Vendors may receive only approved data classes.

## Reliability

Design retries and webhooks for at-least-once delivery:
- idempotency keys;
- atomic deduplication;
- replay handling;
- backoff/dead-letter state;
- provider signature verification where supported.

Scheduling conflicts must be prevented at the database level, not only in UI/application checks.

## Evidence

Tests should cover normal behavior plus relevant:
- concurrency;
- duplicate/replayed events;
- restart/recovery;
- provider outage;
- tenant isolation;
- permission denial;
- migration/rollback;
- restore;
- prompt injection/adversarial AI inputs.

## Promotion

Jon controls merge, production deployment, release, destructive changes, legal/compliance decisions, financial actions, and external provider commitments.
