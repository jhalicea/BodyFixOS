# BodyFixOS repository working agreement

Owner: Jon Alicea  
Repository: `jhalicea/BodyFixOS`  
Status: **CANDIDATE — OWNER RATIFICATION REQUIRED**

## Start here

Before meaningful BodyFixOS architecture, implementation, security, document-organization, or integration work, read:

- `docs/architecture/ARCHITECTURE_BASELINE_PLAN.md`
- `docs/decisions/ADR-0001-independent-product-boundary.md`
- `docs/decisions/ADR-0002-initial-application-stack.md`
- `docs/00_governance/DOCUMENT_ARCHITECTURE.md`

Do not infer current implementation from a roadmap or architecture document. Distinguish DOCUMENTED, TESTED, ENFORCED, PROPOSED and UNKNOWN states.

## Product boundary

BodyFixOS is its own software product. It has its own repository, local project folder, architecture, data, secrets, tests, releases, documentation, private state and recovery model.

BodyFixOS is not a HumanOS module.

Do not:

- place BodyFixOS source inside HumanOS;
- place HumanOS source inside BodyFixOS;
- directly import HumanOS internals;
- share databases or private-state directories by default;
- put BodyFixOS private operational data under `~/.humanos`;
- assume a future HumanOS integration exists.

A future HumanOS relationship requires an explicit external versioned connector / Application Programming Interface (API) contract, separate identity, least-privilege scopes, minimal data transfer, audit evidence and revocation.

## Development method

Use small reversible slices and keep the canonical branch recoverable.

Lifecycle:

`DEFINE -> BASELINE -> DIVIDE -> PLAN -> IMPLEMENT -> TEST -> COMPARE -> VERIFY -> PROMOTE -> PRESERVE`

For meaningful changes:

- state scope, non-goals, acceptance criteria and rollback/recovery;
- classify the architecture decision's Reversibility Class separately from authority/delegation;
- use a focused branch and Pull Request (PR);
- preserve evidence and limitations;
- require explicit human ratification where governance/product/security/data decisions demand it;
- never claim implementation or enforcement from a document alone.

## Authority and reversibility are separate

GREEN / AMBER / RED, when used in the governing delegation model, describe **who may decide/execute**.

Architecture reversibility uses:

- **R1** — two-way door / cheap to reverse;
- **R2** — coordinated but recoverable;
- **R3** — one-way or expensive to reverse.

R3 decisions are never independently Artificial Intelligence (AI)-executable. Human ratification is mandatory.

## Judgment Disclosure

Delegated architecture/governance work must disclose:

- judgments introduced;
- alternatives considered;
- assumptions/uncertainty;
- evidence state;
- Reversibility Class;
- authority/delegation lane where relevant;
- ratification required;
- rollback/supersession path.

Mechanical edits are not the same as judgment approval.

## Initial architecture direction

The candidate initial direction is a TypeScript modular monolith using Next.js and PostgreSQL, with managed Supabase infrastructure initially and Python deferred unless evidence justifies it. See `ADR-0002` for the reconstructed decision and ratification status.

Do not silently replace this stack because a new tool/model prefers something else. Amend/supersede the Architecture Decision Record (ADR) with evidence.

## Build versus buy

Before building scheduling, payments, messaging, identity, analytics, automation, or other commodity capabilities, compare:

- product differentiation;
- operational burden;
- security/privacy requirements;
- cost/time-to-learning;
- vendor capability;
- data ownership;
- realistic exit path.

A provider is not automatically bad. Independence means the product retains the business meaning/data/control it actually needs and can exit critical providers where the cost is justified.

## Ports/adapters

Do not create abstraction theater.

Create a port/adapter seam only when a concrete need exists, such as:

- multiple implementations/providers;
- a meaningful provider-exit requirement;
- a fake implementation needed for reliable tests;
- provider-specific types leaking into domain logic;
- a security/reliability choke point.

No `HumanOSPort` placeholder is permitted merely because a future connector is imaginable.

## AI and automation authority

AI is assistance, not the permission system.

Treat inbound client messages, email/SMS, files, web content and retrieved text as untrusted input. Prompt text never grants tool authority.

Before any AI/agent can combine untrusted inbound content, private data and external actions, require controls outside the model:

- explicit agent/system identity;
- scoped credentials/capabilities;
- input trust classification;
- human approval for sensitive/consequential outbound communication;
- action/spend/rate caps;
- idempotency/duplicate protection;
- durable audit trail;
- kill switch/revocation;
- deterministic policy checks;
- failure/recovery procedure;
- adversarial evaluation including prompt injection and data leakage.

Core clinic operation needs a safe no-AI/degraded mode.

## Data, privacy and compliance

- Least privilege by default.
- No private client data, credentials, production dumps or secrets in public Git.
- Real client data does not enter ordinary development/AI-agent context; use synthetic data outside approved private production workflows.
- Data ownership, retention, export/deletion and backup/recovery must be explicit.
- Vendors receive only approved data classes.
- Do not guess legal/regulatory status. Confirm concrete workflow/jurisdiction/vendor obligations and obtain qualified legal/compliance review when needed.

## Reliability

Where applicable, design external-event processing for duplicates/retries:

- idempotency keys;
- atomic deduplication;
- replay handling;
- retry/backoff/dead-letter state when justified;
- provider signature verification where supported;
- record intent before external side effect when appropriate;
- reconciliation against externally authoritative facts such as payment settlement/dispute state.

Scheduling conflicts should ultimately be protected by durable data constraints/transactions where the chosen workflow requires it, not only user-interface checks.

## Documentation and manuals

Repository-safe software/product documentation may live under `docs/`.

Private clinic manuals, client records, internal operating material, contracts, credentials and other sensitive documents belong in a separate BodyFix private document root, not the public repository and not HumanOS private state.

Use `docs/00_governance/DOCUMENT_ARCHITECTURE.md` and a document register before moving/deleting historical files.

Unknown or conflicting documents are quarantined/preserved until reconciled; they are not deleted because a filename looks old.

## Terminology

When writing training/explanatory material for the owner, expand abbreviations on first meaningful use, for example:

- `MVC (Model-View-Controller)`
- `API (Application Programming Interface)`
- `CI (Continuous Integration)`

Avoid opaque status shorthand such as `CI GREEN`; write `Continuous Integration checks passed`.

## Promotion

Jon controls merge, production deployment, destructive cleanup, legal/compliance conclusions, financial actions, product-boundary changes, and external provider commitments.
