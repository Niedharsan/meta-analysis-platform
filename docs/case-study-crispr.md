# Case study: zebrafish CRISPR meta-analysis

The zebrafish CRISPR meta-analysis was the second real scientific use of the platform. It tested whether infrastructure developed around a clinical evidence review could support a different research domain.

## Implementation

The CRISPR project added domain-specific records for guides, experiments, guide-to-experiment relationships and measurements. These records remained project-scoped and reused shared literature, source-asset, provenance, review-decision and audit concepts rather than creating an unrelated application.

The implemented workflow includes source acquisition and retention, structured and narrative extraction, review queues, validation cohorts, project exports and analysis-readiness checks.

## Safeguards exercised

- missing measurements are not converted to zero;
- reported zero is distinguished from missing information;
- multiplex outcomes are not assigned automatically to component guides;
- reported sequences are preserved;
- evidence remains linked to its source;
- automated specialist and verifier roles cannot approve their own output.

## Public boundary

This case study confirms the implemented architectural reuse without publishing the CRISPR extraction registry, production prompts, source corpus, validation data or research results.
