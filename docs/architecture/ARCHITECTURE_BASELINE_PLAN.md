# BodyFixOS Architecture Baseline Plan

Status: **GREENFIELD ARCHITECTURE CANDIDATE — NO IMPLEMENTATION CLAIM**  
Baseline: `main` @ `25a822803ceb93f6dba9c5e6cb2bacd3b8702d39`  
Date: 2026-10-01

## 1. Evidence-backed current state

At this baseline, the public BodyFixOS repository contains product/architecture documentation but no production application source tree, database schema, deployed runtime, or production integration code.

Therefore BodyFixOS is a **greenfield software product**. Architecture decisions may exist before code, but documents must not be described as implemented or enforced unless code/tests prove that state.

Evidence labels used here:

- **DOCUMENTED** — repository text states it.
- **TESTED** — repeatable test evidence demonstrates it.
- **ENFORCED** — code or Continuous Integration automation blocks violations.
- **PROPOSED** — candidate design awaiting ratification/implementation.
- **UNKNOWN** — evidence is insufficient.

## 2. Product boundary — hard invariant

BodyFixOS is an independent software product for BodyFix Clinic operations.

It owns its own repository, local project folder, architecture, domain model, private operational data stores, credentials/secrets, tests, releases, backups, runbooks, security/privacy boundary, roadmap, and Architecture Decision Records (ADRs).

BodyFixOS is **not** a HumanOS module, subdirectory, database namespace, internal package, or private-state subtree.

A future HumanOS integration, if deliberately approved, must be an external versioned connector / Application Programming Interface (API) contract with a separate identity, narrow scope, minimal data transfer, revocable permission, audit evidence, and independent failure/recovery behavior.

There is no `HumanOSPort` placeholder inside BodyFixOS. A HumanOS connector is designed only if an approved real integration need appears.

No shared database, direct internal imports, shared private-state directory, or automatic HumanOS access to BodyFixOS records is allowed by default.

## 3. Product purpose

BodyFixOS should:

- preserve a high-touch human-centered client experience;
- standardize discovery/intake, expectations, scheduling, follow-up and service recovery;
- reduce repetitive administrative work with bounded automation;
- track operational outcomes without unsupported medical claims;
- use least-privilege access and deliberate data collection;
- support repeatable operations for future locations and teams.

Business workflow evidence drives architecture. Technology choices serve that purpose, not the reverse.

## 4. Quality attributes to make testable

### Scheduling integrity
The system must prevent or visibly detect conflicting appointments/resource assignments and expose reconciliation paths rather than silently overwriting state.

### Payment/deposit integrity
The system must never silently lose, duplicate, or misrepresent a payment/deposit event. External payment-provider facts must reconcile against BodyFixOS records.

### Privacy and data minimization
Collect and retain only information required for legitimate operations. Public code/tests use synthetic data. Private client information never belongs in the public repository.

### Human authority
Automation may recommend, prepare, classify or route work, but consequential client/business actions follow explicit authority rules enforced outside the model.

### Reliability and recoverability
Reminders, follow-up, scheduling and payment workflows need visible failures, idempotency/duplicate prevention where applicable, retry/recovery behavior, backups and tested restoration/reconciliation.

### Auditability
Important business/automation actions are attributable to a human or system identity with timestamp, requested action, authority, outcome and evidence.

### Modifiability and portability
Core business rules remain independent from one payment, scheduling, messaging, Artificial Intelligence (AI), automation, database-hosting, or cloud provider where the cost of independence is justified.

### Operational simplicity
BodyFixOS starts with the simplest architecture that safely supports current workflows. New abstractions must solve a demonstrated problem.

## 5. Domain map — target hypothesis to validate

```text
BodyFixOS
|
+-- Client Journey
|   discovery, expectations, intake workflow, follow-up, retention
|
+-- Scheduling & Capacity
|   appointments, availability, rooms/resources, rescheduling/cancellation
|
+-- Payments & Deposits
|   pricing references, deposits, payment status, refund/cancellation rules
|
+-- Service Operations
|   session workflow, operational checklists, service recovery, handoffs
|
+-- Communications
|   reminders, confirmations, follow-up messages, communication preferences
|
+-- Knowledge & Training
|   procedures, protocols, staff guidance, versioned operating knowledge
|
+-- Reporting & Metrics
|   operational metrics, reconciliation, quality indicators
|
+-- Identity / Permissions / Audit
    user identities, roles, approvals, audit events, privacy controls
```

The domain map remains a target hypothesis until real workflows/documents validate it.

## 6. Architecture style and prior stack decision

The intended architecture style is a **modular monolith**: one deployable application with explicit internal module boundaries. Distributed services are not the default.

A prior owner-directed project decision selected a TypeScript-only initial application stack built around **Next.js**, **PostgreSQL**, and managed **Supabase** infrastructure to start, with Python deferred unless a demonstrated need justifies adding it. That decision is being reconstructed into a repository Architecture Decision Record for explicit ratification rather than being silently treated as either forgotten or newly invented.

Supabase is an implementation provider, not the owner of BodyFixOS business meaning. The design must preserve a practical exit path for canonical domain data and business rules.

## 7. Build-versus-buy before abstraction

Before implementing a subsystem, ask:

1. Is this capability core BodyFixOS differentiation or commodity infrastructure?
2. Does an existing product/provider already perform it safely enough?
3. What business data must BodyFixOS own versus reference/reconcile externally?
4. What would make a provider realistically replaceable?
5. What operational burden is created by building it ourselves?
6. What evidence would justify a custom implementation later?

Scheduling, payment processing, messaging delivery, identity, storage, analytics, and automation should not be rebuilt merely because BodyFixOS could build them.

## 8. Ports/adapters only when justified

Do not create one abstraction per vendor in advance.

A port/adapter boundary earns its place when at least one of these is true:

- the provider is plausibly replaceable and the seam materially reduces lock-in;
- a fake/test implementation is needed for reliable automated testing;
- provider-specific types would otherwise leak into core business rules;
- multiple providers/implementations are already required;
- security/reliability policy requires a narrow choke point.

The first implementation should introduce only the seams required by the first vertical slice. It must not pre-create `SchedulingPort`, `PaymentPort`, `MessagingPort`, `CRMPort`, `AutomationPort`, `AIServicePort`, and `HumanOSPort` merely as architecture decoration.

Provider Software Development Kit (SDK) types should stop at a justified adapter boundary rather than spreading across the domain.

## 9. Data architecture principles

Before tables/schemas are expanded, classify data by purpose and sensitivity. At minimum distinguish:

- public/business-reference data;
- operational configuration;
- client contact/appointment data;
- payment-status references/tokens, while avoiding raw payment credentials where a processor should own them;
- private service/assessment records if later required;
- audit/event records;
- analytics/derived metrics;
- synthetic test fixtures.

Each category needs an owner, source of truth, retention expectation, export/deletion expectation, access policy, backup/recovery behavior, and reconciliation rule.

BodyFixOS should not mirror all vendor data merely because an API exposes it.

## 10. Agent and automation security boundary

BodyFixOS may eventually combine:

- untrusted inbound client messages;
- private client/business data;
- Artificial Intelligence models/agents;
- outbound email/SMS;
- scheduling/payment/other actions.

That combination is high risk. Model output is never the permission system.

Required controls before such automation becomes operational:

- unique agent/system identity;
- narrowly scoped credentials/capabilities;
- explicit input trust classification;
- separation between reading content and authorization to act;
- human approval tier for sensitive or consequential outbound communication;
- action/spend/rate caps;
- idempotency and duplicate-action protection;
- durable audit trail;
- revocation/kill switch outside the model;
- deterministic policy enforcement outside prompts;
- incident/recovery procedure;
- evaluation/red-team cases for prompt injection, malicious inbound content, misrouting, privacy leakage and unsafe tool proposals.

The existing GREEN / AMBER / RED model, when used, is strictly an **authority/delegation axis**. It must not be reused to describe architecture reversibility.

## 11. Compliance/privacy review checkpoint

Before enabling workflows involving sensitive health/body information, payments, protected communications, or other legally regulated data, BodyFixOS must identify what laws/contracts/vendor agreements actually apply to the concrete workflow and jurisdiction.

The architecture does **not** declare that a specific law automatically applies. Questions such as Health Insurance Portability and Accountability Act (HIPAA) coverage, state health-privacy duties, payment-card obligations, record retention, consent and vendor agreements require verified facts and qualified legal/compliance review where appropriate.

Compliance conclusions must be recorded as evidence-backed requirements, not guessed from product labels.

## 12. Engineering baseline

The first implementation baseline should deliberately record:

- TypeScript runtime/tooling choice;
- Next.js application framework choice;
- PostgreSQL data model/migration strategy;
- managed Supabase implementation role and exit path;
- local development environment;
- Integrated Development Environment (IDE) / editor-neutral tooling requirements;
- package/dependency manager;
- formatter/linter/type checking;
- unit/integration/end-to-end testing strategy;
- Continuous Integration (CI) checks;
- Continuous Delivery/Deployment (CD) strategy when deployment begins;
- configuration/secrets management;
- logging/metrics/tracing/alerting as needed;
- backup/restore/reconciliation;
- versioning/release/rollback;
- dependency/security scanning.

Python remains deferred unless evidence justifies a separate Python service/tool. No technology is adopted merely because HumanOS uses it.

## 13. Repository and document architecture

The code repository contains public/repository-safe source and durable architecture/product documentation. Private clinic manuals and operational source-of-truth documents may require a separate private local document root and must not be pushed into a public repository simply for neatness.

Repository-safe documentation categories may include:

```text
docs/
  00_governance/
  01_product/
  02_clinic_operations/
  03_client_journey/
  04_scheduling_payments/
  05_automation_integrations/
  06_security_privacy/
  07_architecture/
  08_training_manuals/
  09_brand_marketing/
  10_metrics_reporting/
  90_imports/
  99_archive/
```

This is a classification model, not permission to move every private document into Git. The actual computer cleanup must build a document register first: current path, title, type, version/date, authority/source-of-truth status, duplicate/conflict status, sensitivity, proposed destination, and confidence.

## 14. Architecture documentation set — proportional

Do not create artifacts merely to increase document count. Produce an artifact when it answers a current engineering question.

Highest-value early artifacts:

1. real business workflow map for the first slice;
2. quality-attribute scenarios;
3. system context and application/container view using the C4 model (Context, Containers, Components, Code);
4. data ownership/sensitivity map;
5. trust boundaries and threat model;
6. stack Architecture Decision Record;
7. deployment/build/test baseline when implementation starts;
8. runbook/recovery skeleton before operational dependence.

Advanced notation/pattern material remains Academy knowledge until the project needs it.

## 15. First thin vertical slice

After owner ratification of the stack and first workflow, prefer one thin end-to-end slice rather than the whole clinic operating system.

Candidate learning slice to validate against current clinic documents/workflow:

`book/hold appointment → validate availability → deposit/payment status → confirmation → audit evidence → failure/recovery`

This is a hypothesis, not a command to replace existing scheduling/payment providers. Build-versus-buy analysis comes first.

## 16. Architecture fitness rules

The first concrete product-separation fitness rule should be:

> **BodyFixOS source code must never directly import HumanOS internals.**

The reciprocal HumanOS rule should also exist. The rule is **ENFORCED** only when a repeatable test / Continuous Integration check actually blocks violating source imports; until then it is DOCUMENTED.

Additional fitness rules should arise from real failure risk rather than an arbitrary checklist.

## 17. Judgment Disclosure

This baseline contains judgment, not only facts.

Judgments include:

- retaining the independent-product boundary;
- modular-monolith direction;
- reconstructing the previously selected TypeScript / Next.js / PostgreSQL / managed Supabase stack for repository ratification;
- removing speculative ports and the `HumanOSPort` placeholder;
- adding build-versus-buy, agent-security, and compliance-review checkpoints;
- prioritizing a thin booking/deposit/confirmation learning slice subject to workflow validation.

These choices are intentionally visible so the owner can ratify, amend, or reject them. Mechanical repository edits do not substitute for ratification.

## 18. Anti-drift rules

- Every major structural/security/data decision gets an Architecture Decision Record when the decision is actually made.
- Architecture diagrams state `AS-BUILT` or `TARGET`; never blur them.
- Public documentation cannot claim a capability based only on a plan.
- Evidence states distinguish DOCUMENTED, TESTED and ENFORCED.
- Generated dependency/import maps should be re-runnable where practical.
- Each release reviews meaningful architecture drift and vendor/data-boundary changes.
- Generated evidence belongs in designated artifact locations, not repository or home-directory roots.
- BodyFixOS remains independently buildable, testable, deployable and recoverable without HumanOS.
