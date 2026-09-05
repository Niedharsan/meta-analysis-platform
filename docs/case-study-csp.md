# Case study: CSP systematic review and meta-analysis

The first production use of the platform was a systematic review and meta-analysis in conduction-system pacing (CSP) and heart-failure research.

This work originally began as a CSP-specific evidence database. As the workflow expanded, the data model and review pipeline were refactored into reusable project-level infrastructure so that later research projects would not require a separate ingestion, review and analysis application.

## What this use case exercised

- literature search/import and deduplication;
- study/report management;
- full-text/source handling;
- structured evidence extraction;
- exact source provenance;
- candidate-versus-curated evidence separation;
- human scientific review and correction;
- study-design/risk-of-bias workflow support;
- statistical analysis and research exports.

## Generalization work prompted by CSP

The original domain-specific tables and workflow were progressively supplemented by generalized concepts including:

- project configuration versions;
- project-scoped variables and synonyms;
- study groups and comparisons;
- observations and effect estimates;
- statistical tests;
- evidence provenance and controlled links;
- analysis-specific evidence sets;
- immutable review/audit history.

The existing CSP records were retained while reusable adapters and generic entities were added around them rather than replacing the research database destructively.

## Private protocol boundary

The CSP study is active/private research. This public repository therefore does **not** disclose the exact systematic-review or meta-analysis protocol.

In particular, it excludes:

- exact database search strings and search-line construction;
- inclusion/exclusion criteria and screening decision rules;
- project-specific variable/outcome definitions;
- statistical-analysis choices specific to the CSP project;
- risk-of-bias/appraisal mappings and project decisions;
- unpublished extracted evidence or study-level datasets;
- client/research deliverables.

The purpose of this case study is to show how the software was used and generalized, not to publish the underlying CSP protocol.
