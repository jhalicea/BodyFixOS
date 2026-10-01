# ADR-0001 — BodyFixOS Is an Independent Product Boundary

Status: **PROPOSED / OWNER-DIRECTED**  
Date: 2026-10-01

## Context

HumanOS and BodyFixOS solve different problems and have different data, privacy, operational, release and failure domains. Prior architectural discussion risked describing BodyFixOS as if it were an internal HumanOS module.

The owner explicitly requires the products to remain separate in GitHub and on the development machine.

## Decision

BodyFixOS is an independent software product with its own repository, local project directory, architecture, data stores, credentials, tests, CI/CD, releases, backups, runbooks and security/privacy boundary.

HumanOS must not own or embed BodyFixOS source code or private operational data.

A future integration may be created only as an explicit versioned connector/API with:

- a documented contract;
- separate identities/credentials;
- least-privilege scopes;
- minimal data transfer;
- audit evidence;
- revocation;
- independent failure/recovery behavior.

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
- connector can be threat-modeled and versioned explicitly.

Costs:
- duplicated project-level engineering setup where appropriate;
- integration requires a deliberate contract rather than direct internal calls;
- shared ideas must be copied as patterns/standards or extracted deliberately, not inherited implicitly.

## Revisit condition

This decision may be revisited only if there is a concrete product requirement that cannot reasonably be satisfied through an external contract. Any proposed reversal is a RED architecture decision and requires an explicit migration, privacy/security analysis and owner approval.
