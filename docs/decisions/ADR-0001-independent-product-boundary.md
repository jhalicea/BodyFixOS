# ADR-0001 — BodyFixOS Is an Independent Product Boundary

ADR means **Architecture Decision Record**: a durable record of a significant architecture decision, its context, alternatives and consequences.

Status: **PROPOSED / OWNER-DIRECTED — EXPLICIT REPOSITORY RATIFICATION REQUIRED**  
Date: 2026-10-01

## Context

HumanOS and BodyFixOS solve different problems and have different data, privacy, operational, release and failure domains. Prior architectural discussion risked describing BodyFixOS as if it were an internal HumanOS module.

The owner has explicitly required the products to remain separate in GitHub and on the development machine.

## Decision

BodyFixOS is an independent software product with its own repository, local project directory, architecture, data stores, credentials, tests, Continuous Integration/Continuous Delivery or Deployment configuration when implemented, releases, backups, runbooks and security/privacy boundary.

HumanOS must not own or embed BodyFixOS source code or private operational data.

A future integration may be created only as an explicit versioned connector / Application Programming Interface (API) contract with:

- a documented contract;
- separate identities/credentials;
- least-privilege scopes;
- minimal data transfer;
- audit evidence;
- revocation;
- independent failure/recovery behavior.

No `HumanOSPort` placeholder is created inside the BodyFixOS domain merely to anticipate a future relationship. The connector is designed only when an approved integration need exists.

## Explicitly rejected coupling

- placing BodyFixOS source inside the HumanOS repository;
- treating BodyFixOS as a HumanOS domain/module;
- sharing a database by default;
- importing one product's internal packages into the other;
- sharing private runtime-state directories;
- allowing HumanOS unrestricted access to BodyFixOS client/business data;
- requiring HumanOS for BodyFixOS to build, test, deploy or recover;
- requiring BodyFixOS for HumanOS to build, test, deploy or recover.

## Consequences

Positive:
- clearer ownership and security boundaries;
- independent release cadence and recovery;
- lower accidental data coupling;
- easier future replacement of either product;
- a connector can be threat-modeled and versioned explicitly.

Costs:
- duplicated project-level engineering setup where appropriate;
- integration requires a deliberate contract rather than direct internal calls;
- shared ideas must be copied as patterns/standards or extracted deliberately, not inherited implicitly.

## Reversibility

This is a **Reversibility Class R3** decision: reversing it would be expensive and could create data/security/release coupling. This classification is independent of any GREEN / AMBER / RED delegation/authority lane.

A reversal requires a concrete product requirement, alternatives/tradeoff analysis, migration/recovery plan, privacy/security analysis, independent review, and explicit owner ratification.

## Judgment Disclosure

Judgment introduced: treating product independence as a hard architecture boundary rather than a loose organizational preference.

Evidence basis: explicit owner direction plus the products' different problem/data/release domains.

Alternative considered: BodyFixOS as an internal HumanOS module. Rejected because it couples unrelated product/data/security lifecycles and contradicts owner direction.

Enforcement state: **DOCUMENTED**. This ADR does not by itself enforce the boundary. Source-import fitness tests and repository/process controls are separate evidence.

Ratification state: this repository version must record explicit owner ratification before the status changes to ACCEPTED.
