# Pharma Value Chain Model — Canonical Reference

This folder holds the **authoritative CPDSE Pharma Value Chain Model**: the linear
drug-development pipeline used to anchor every CPDSE engagement to the customer's
actual pipeline stage(s).

It is one of CPDSE's three reference models, alongside the
[PDS Competence Model](../competency-model/) and Training from the Back of the Room.

- **Canonical document:** [`Pharma_Value_Chain_Model.md`](Pharma_Value_Chain_Model.md)
- **Structure:** 2-tier and linear — 3 top-tier steps (Pre-clinical → Clinical
  development → On-market) → 13 substeps.
- **Versioning:** the `Version:` header + changelog in the canonical document is
  the model version.

The model is **service-agnostic**: prompts and engagements reference it, but it
does not reference them.
