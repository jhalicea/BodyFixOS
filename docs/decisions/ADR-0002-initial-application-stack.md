# ADR-0002 — Initial BodyFixOS Application Stack

ADR means **Architecture Decision Record**: a durable record of a significant architecture decision, its context, alternatives and consequences.

Status: **PROPOSED FOR REPOSITORY RATIFICATION — RECONSTRUCTED FROM PRIOR OWNER DECISION**  
Decision lineage date: 2026-09-18  
Repository reconstruction date: 2026-10-01

## Context

BodyFixOS had already progressed beyond a completely undecided technology stack in prior owner-directed architecture work. The repository baseline later described the stack as if it had not been chosen, creating exactly the kind of architectural memory drift this project is intended to prevent.

This record reconstructs that prior decision so it can be reviewed and explicitly ratified in the repository rather than relying on conversational memory.

## Decision to ratify

Initial BodyFixOS application direction:

- **TypeScript** as the primary application language;
- **Next.js** as the initial application/web framework;
- **PostgreSQL** as the canonical relational database;
- managed **Supabase** services initially where they reduce operational burden, while preserving provider exit paths;
- **modular monolith** architecture rather than microservices as the starting deployment shape;
- **Python deferred** unless a concrete future workload justifies a separate Python service/tool;
- database authorization/tenant boundaries should use PostgreSQL/Supabase controls such as **RLS (Row-Level Security)** where the data model actually requires tenant/location/user isolation;
- Artificial Intelligence (AI) capabilities remain optional/bounded and must not become a prerequisite for core deterministic operations.

## Provider-independence interpretation

Supabase is an implementation provider, not the architecture owner.

BodyFixOS must own:

- domain language and business rules;
- canonical database schema/migrations;
- application behavior;
- export/recovery expectations;
- provider-neutral tests for critical business rules;
- documented exit/replacement requirements for infrastructure that becomes operationally critical.

The architecture should use provider abstractions only where they solve a real replacement/testing/security problem. It must not wrap every external feature merely to appear provider-neutral.

## Why this direction

The decision favors:

- one primary language across early product development;
- a web stack aligned with the owner's prior JavaScript/React experience;
- relational integrity for scheduling, deposits, clients, permissions and audit relationships;
- managed infrastructure to reduce early operations burden;
- a modular monolith to avoid premature distributed-system complexity;
- the ability to introduce Python later for a workload that actually benefits from it instead of maintaining two application stacks from day one.

## Alternatives considered / historical context

Earlier BodyFix/SystemFIX exploration included a React/Next.js front end with a possible Python/FastAPI backend. Later architecture work narrowed the initial product direction to TypeScript-only with Next.js and PostgreSQL/Supabase, explicitly deferring Python.

This ADR records the later decision as the candidate canonical direction.

## Consequences

Positive:

- fewer languages/runtimes during the first implementation;
- simpler development/release model;
- direct fit with Next.js/TypeScript ecosystem;
- PostgreSQL provides strong relational constraints and mature migration/backup tooling;
- managed Supabase can accelerate authentication/storage/database operations while the product remains small;
- modular monolith keeps transactions and debugging simpler than early microservices.

Costs/risks:

- managed Supabase features can create provider coupling if provider-specific behavior leaks broadly through the application;
- Next.js server/client boundaries require deliberate security and data-access design;
- Row-Level Security rules require explicit tests; a policy that exists but is not tested can create false confidence;
- Python-specific libraries would require a later service/tool boundary if genuinely needed.

## Reversibility

- TypeScript/Next.js framework choice: **Reversibility Class R2** — meaningful migration cost but recoverable.
- PostgreSQL canonical data model: **Reversibility Class R3** once production data depends on it — expensive to reverse and migration-sensitive.
- Supabase hosting/provider choice: intended as **Reversibility Class R2** if exit/export/restore is continuously tested.

Reversibility Class is separate from GREEN / AMBER / RED delegation/authority lanes.

## Verification before implementation promotion

Before this decision is treated as implemented:

1. validate the first real clinic workflow and quality attributes;
2. confirm current Next.js/TypeScript/PostgreSQL/Supabase versions and support requirements at implementation time;
3. define package manager, formatting/lint/type-checking, testing and migration tooling;
4. define local/development/test/production environment boundaries;
5. test database backup/export/restore and provider exit assumptions before critical data depends on them;
6. define Row-Level Security only where the concrete authorization model requires it and test both allowed and denied paths.

## Judgment Disclosure

Judgment: this ADR chooses to restore a prior owner-directed decision rather than reopen the stack from zero.

Evidence quality: the decision is preserved in prior project/conversation records, but the current public repository did not previously contain an immutable accepted stack ADR.

Uncertainty: exact package versions, deployment topology, authentication implementation, and whether every Supabase service will be used remain undecided.

Ratification requirement: the owner must explicitly accept, amend, or reject this reconstructed record before its status changes to ACCEPTED.
