# BodyFixOS

### Business systems and responsible automation for a premium corrective-bodywork practice.

BodyFixOS is an applied systems-design project for **BodyFix Clinic**. It translates more than a decade of hands-on service experience into clear workflows, measurable operations, privacy-conscious automation, and a consistent client journey.

> **Status:** public design and implementation roadmap. This repository does not claim that every described capability is deployed.

## Why this project exists

Service businesses often depend on knowledge that lives only in the practitioner's head. BodyFixOS explores how to turn that experience into a reliable operating system without making the client experience mechanical or replacing professional judgment.

## System goals

- Preserve a high-touch, human-centered client experience
- Standardize intake, assessment, scheduling, follow-up, and service recovery
- Reduce repetitive administrative work through bounded automation
- Track operational outcomes without making unsupported medical claims
- Protect client information through least-privilege access and deliberate data collection
- Create repeatable systems that can support future locations and teams

## Architecture

| Layer | Responsibility |
|---|---|
| Client journey | Discovery, intake, expectations, follow-up, retention |
| Practice operations | Scheduling, deposits, rooms, supplies, and quality checks |
| Knowledge system | Protocols, training material, decisions, and versioned procedures |
| Automation | Reminders, routing, reporting, and human-approved actions |
| Governance | Privacy, permissions, auditability, and claims discipline |

The current public repository is still a design/roadmap repository, not an implemented production system. The architecture baseline is being developed as greenfield work and must distinguish proposed target structure from verified implementation.

## Current public work

- Domain model and operating boundaries
- Client-journey and workflow mapping
- Privacy and authorization requirements
- Automation opportunity analysis
- Metrics and acceptance-test design
- Software architecture and engineering baseline

## Planned implementation slices

1. Public architecture and glossary
2. Privacy-safe synthetic workflow demonstrations
3. Scheduling and follow-up adapters
4. Operational dashboard prototype
5. Recovery, duplication, and failure-path tests

## Relationship to HumanOS

BodyFixOS and HumanOS are **separate software products** with separate repositories, local project folders, architecture, storage, credentials, tests, releases, backups, and security/privacy boundaries.

BodyFixOS may reuse general engineering principles learned from HumanOS—human authority, explicit permissions, durable evidence, honest capability labels, provider independence—but it does not inherit HumanOS internals or private state.

If a future integration is approved, it must use an explicit, narrow, versioned connector/API with separate identity, permissions, data ownership, auditability, and revocation. The products do not share a database or import each other's internal source code by default.

See `docs/decisions/ADR-0001-independent-product-boundary.md`.

## Safety boundary

This repository contains no client records or private clinical notes. Examples will use synthetic data. BodyFixOS supports business operations and professional workflows; it does not diagnose medical conditions or replace licensed clinical judgment.

---

**Designed by [Jon Alicea](https://github.com/jhalicea)** — Licensed Massage Therapist and applied AI systems builder.
