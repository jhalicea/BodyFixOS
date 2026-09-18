# BodyFixOS Research Intake / Review Backlog

Status: REVIEW QUEUE — NOT IMPLEMENTED
Date: 2026-09-18

This list preserves useful engineering findings that should not be silently turned into code before the relevant slice exists.

## Adopted foundation concepts

- sovereign core / replaceable infrastructure;
- modular monolith first;
- AI no-authority and no-AI degraded mode;
- tenant/identity/time/money/audit shapes designed early;
- database-enforced booking concurrency;
- at-least-once/idempotent event assumptions;
- immutable-finalized-record plus amendment model;
- vendor/data-class gate;
- risk-tiered development and human promotion;
- restoration/fallback/incident readiness.

## Review when implementation reaches the area

1. Managed Postgres/Supabase versus another Postgres host; verify portability and any required BAA/security plan at signup.
2. Drizzle versus Kysely after first SQL migrations are designed.
3. pg-boss versus Graphile Worker after job semantics are known.
4. SMS provider comparison; verify compliance, regional behavior, pricing, delivery evidence, and health-data restrictions before selection.
5. Email provider comparison; verify inbound support, transactional/marketing separation, deliverability tooling, security terms, and portability.
6. AI provider selection for v1; start with one behind AIModelPort and add a second only for evidence-backed need.
7. Hosting choice based on long-running worker, network, security, backup, observability, and future regulated-mode needs.
8. Branch protection/CODEOWNERS/CI policy once starter repository files exist.
9. Vendor register schema and executable data-class CI gate.
10. Read-access audit/break-glass design.
11. Incident/breach notification runbook with legal review.
12. Clinical retention schedule with legal review.
13. File-upload scanning and metadata policy.
14. SPF/DKIM/DMARC and domain/sender separation.
15. One-way ICS first; two-way calendar synchronization only after core booking is stable.
16. Temporal only after workflow complexity proves Postgres jobs insufficient.
17. SystemFIX multi-tenant admin/billing only after BodyFix clinic proof.
18. Marketing campaign builder and full unified inbox after the core client lifecycle is stable.

## V1 product loop

BOOK -> HOLD -> PAY -> INTAKE -> PREP -> SERVE -> DOCUMENT -> FOLLOW UP

Everything else remains subordinate to proving this loop reliably.
