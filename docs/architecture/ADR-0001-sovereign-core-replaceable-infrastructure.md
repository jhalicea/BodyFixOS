# ADR-0001 — Sovereign Core / Replaceable Infrastructure

Status: ACCEPTED — IMPLEMENTATION PENDING
Date: 2026-09-18
Owner: Jon Alicea

## Context

BodyFixOS is intended to become a complete business operating platform and later seed SystemFIX. Early development should remain lean, but dependence on one booking, CRM, messaging, payment, AI, database, or hosting vendor would undermine long-term portability and product ownership.

## Decision

BodyFixOS owns all domain concepts and canonical business state.

External services are integrated only through explicit BodyFixOS ports/adapters. Provider-specific SDKs may exist inside adapter packages, but domain modules may not depend on them directly.

Examples:
- PaymentPort -> processor adapter
- SmsPort -> carrier/messaging adapter
- EmailPort -> delivery adapter
- AIModelPort -> cloud/local model adapter
- ObjectStoragePort -> storage adapter

Managed infrastructure is allowed in v1.

## Consequences

Positive:
- providers can be replaced without domain rewrites;
- self-hosting/private-cloud options remain possible;
- SystemFIX can support different customer/provider choices;
- vendor outages/pricing changes have bounded blast radius.

Costs:
- adapter interfaces require deliberate design;
- lowest-common-denominator interfaces can become weak if over-generalized;
- portability must be tested rather than assumed.

## Guardrail

No provider identifier or provider object becomes a BodyFixOS primary identity. Store internal IDs and explicit integration mappings.

## Verification

Future implementation must include at least one contract test per provider port and demonstrate that core domain tests run without a live provider.
