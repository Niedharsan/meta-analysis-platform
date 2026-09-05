# Case study: zebrafish CRISPR meta-analysis

The zebrafish CRISPR meta-analysis became the second major scientific use of the generalized platform.

Unlike the original CSP project, this use case involved different scientific entities, outcome semantics and source structures. Reusing the same project, provenance, candidate-review and evidence infrastructure provided a practical test of whether the platform had genuinely moved beyond a single clinical-review schema.

## What changed between domains

The CRISPR project required support for domain-specific evidence such as guide-level and experiment-level records, structured supplements and distinctions between different classes of experimental outcome.

Those domain rules were implemented on top of the shared evidence infrastructure rather than by creating a second review database.

## Shared platform components reused

- project and report scoping;
- literature/source ingestion;
- retained source assets;
- source-grounded extraction packets;
- AI-generated candidate records;
- deterministic validation gates;
- independent verification;
- human review;
- provenance and audit history;
- export and downstream analysis infrastructure.

## Scientific safeguards

The CRISPR workflow includes rules intended to prevent common extraction errors, including:

- missing values are not treated as zero;
- distinct biological outcome types remain distinct;
- multiplex results are not automatically assigned to individual component guides;
- reported sequences are retained rather than silently reinterpreted;
- source attribution is required for new scientific evidence;
- model-generated evidence cannot approve itself.

## Why this case study matters

CSP and CRISPR differ substantially in scientific content. Supporting both within the same evidence platform demonstrates the intended separation between reusable evidence infrastructure and project-specific scientific logic.

This public case study describes the architecture and safeguards at a high level. It does not publish the complete production extraction configuration, prompts, source corpus or research dataset.
