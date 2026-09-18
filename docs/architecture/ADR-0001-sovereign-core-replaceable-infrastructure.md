# ADR-0001 — Sovereign Core, Ports, Connectors, and Tested Exit Ability

Status: ACCEPTED — IMPLEMENTATION PENDING
Date: 2026-09-18
Owner: Jon Alicea

## Context

BodyFixOS is intended to become a complete business operating platform and later seed SystemFIX.

The original sovereignty requirement was directionally correct but too broad: external infrastructure that should be replaceable is not the same as an external business system we intentionally integrate with, and true independence is not measured by how much infrastructure we operate ourselves.

SystemFIX customers will also need migration from incumbent products, so integration/import boundaries must be first-class architecture rather than afterthoughts.

## Decision

### 1. BodyFixOS owns the domain

BodyFixOS owns its domain logic, data model, workflows, UX, AI policies, canonical business records, product intelligence, and internal IDs.

No external product becomes the canonical representation of a BodyFixOS business concept.

External systems may remain authoritative for external facts they control. Payment processors, for example, remain authoritative for network authorization, settlement, payout, fee, and dispute facts. BodyFixOS reconciles those facts against its own ledger/business records.

### 2. Classify external relationships as PORT or CONNECTOR

**PORT:** replaceable infrastructure used to execute a BodyFixOS capability.

Examples:
- PaymentPort
- SmsPort
- EmailPort
- AIModelPort
- AuthPort
- ObjectStoragePort

**CONNECTOR:** deliberate interoperability with an external business system.

Examples:
- calendars;
- accounting;
- ad platforms;
- review platforms;
- Zapier/Make;
- incumbent CRM/booking imports such as Vagaro/Acuity.

Ports optimize for substitution. Connectors optimize for stable interoperability, import/export, reconnect behavior, and scoped permissions.

### 3. Anti-corruption boundary

Provider-specific SDKs, types, payloads, and event names terminate inside platform/adapter or connector code.

Provider events are translated to BodyFixOS events before domain consumption.

Examples:
- provider `payment_intent.succeeded` -> `PaymentCaptured`;
- provider delivery webhook -> `MessageDeliveryConfirmed`.

Provider object types never appear in domain port signatures.

### 4. External references

BodyFixOS internal IDs are canonical.

Provider IDs are represented through an external-reference mapping rather than provider-specific columns scattered through domain tables.

Minimum conceptual fields:
- entity_type;
- entity_id;
- provider;
- external_type;
- external_id;
- optional metadata/version.

### 5. Prove ports with contract tests

A port with one adapter is only a portability hypothesis.

For high-lock-in/high-risk ports, the first real adapter should be accompanied by:
- a fake adapter;
- a shared contract-test suite;
- a dev/test mode that needs no live vendor call;
- a documented exit path.

Future alternate adapters must pass the same contract.

### 6. Independence ladder

Per capability:
- L0 — provider concepts leak into the domain;
- L1 — canonical data exports in documented/open formats;
- L2 — fake/alternate implementation passes contracts and a bounded switch is possible;
- L3 — capability can move to another compatible host/environment and a tested exit/restore runbook passes;
- L4 — BodyFixOS/SystemFIX self-operates the underlying infrastructure.

Target L2 for commercially important provider capabilities by SystemFIX launch, L3 for database/compute/storage where justified, and L4 only from a concrete customer/regulatory/security/economic requirement.

### 7. Exit drills and replacement triggers

Portability must be tested.

Exit drills record switching time, migration gaps, downtime, reconciliation differences, rollback, and resulting independence level.

Provider replacement is trigger-based:
- security/privacy failure;
- reliability failure;
- cost threshold;
- customer/regulatory requirement;
- missing capability;
- hostile terms/shutdown;
- failed exit drill.

Calendar phases do not justify rewriting working infrastructure.

### 8. Standards first

Prefer open standards/formats where they meet requirements because they reduce migration cost.

Do not abstract React, Next.js, or PostgreSQL behind meaningless universal interfaces. Abstract real provider/domain boundaries.

### 9. Managed infrastructure and self-hosting

Managed infrastructure is allowed and often preferred in v1.

BodyFixOS should remain containerizable, 12-factor/configurable, portable, and recoverable, but customer self-hosting/on-prem is not promised until demand justifies the support/compliance burden.

## Consequences

Positive:
- external services can be replaced without domain rewrites;
- connectors can remain permanently useful without being treated as temporary dependencies;
- migration from incumbent systems becomes a product capability;
- provider-specific concepts remain contained;
- portability can be measured with evidence;
- managed infrastructure remains compatible with long-term sovereignty.

Costs:
- adapter/connector interfaces require deliberate design;
- contract tests and exit drills add engineering work;
- some provider-held state cannot be migrated perfectly;
- reconciliation becomes a first-class operational responsibility.

## CI enforcement target

When application code exists, enforce where practical:
- provider SDK imports banned outside approved adapter/connector areas;
- provider types banned in domain port signatures;
- provider-specific ID columns banned outside approved external-reference/integration storage unless an ADR grants an exception;
- high-risk ports require shared contract tests;
- outbound data classes require provider approval.

## Verification

This ADR is architecture policy only until implementation evidence exists.

Research 002 and Slice 1 must demonstrate the pattern with:
- canonical internal IDs;
- external references;
- canonical provider events;
- PaymentPort;
- FakePaymentAdapter;
- first real payment adapter;
- shared payment contract tests;
- idempotency;
- reconciliation design.
