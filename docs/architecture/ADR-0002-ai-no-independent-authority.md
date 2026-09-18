# ADR-0002 — AI Has No Independent Business Authority

Status: ACCEPTED — IMPLEMENTATION PENDING
Date: 2026-09-18
Owner: Jon Alicea

## Context

BodyFixOS will process untrusted client text from intake, SMS, email, files, and future web sources while also exposing sensitive business capabilities. A model that can interpret untrusted text and directly exercise consequential tools creates a prompt-injection and hallucination path.

## Decision

AI is an assistive subsystem, not an authority boundary.

AI may produce typed drafts, summaries, classifications, suggestions, and explanations. Consequential effects are committed only by deterministic policy/code or an explicitly authorized human.

Core clinic operation must remain usable with AI disabled.

## Prohibited autonomous effects

AI does not directly:
- charge/refund money;
- finalize or silently modify clinical notes;
- change consent;
- change permissions;
- delete retained records;
- approve contraindications or diagnose;
- change scheduling invariants or business policy.

## Required controls

- minimum necessary context;
- structured/schema-validated outputs;
- prompt/model/version provenance for material behavior;
- clear draft labeling;
- adversarial/prompt-injection evals before consequential integration;
- scoped credentials/capabilities;
- kill switch/cost cap;
- audit evidence for accepted AI-assisted changes.

## Consequences

This reduces autonomy but sharply limits the blast radius of prompt injection, provider errors, and hallucination.
