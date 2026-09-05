# Meta-analysis Platform

A reusable evidence-synthesis and meta-analysis platform for life-sciences research.

The project began as a research system for a conduction-system pacing (CSP) systematic review and meta-analysis, then evolved into a multi-project platform for literature ingestion, screening, structured evidence extraction, provenance, human review and statistical analysis. A zebrafish CRISPR meta-analysis was implemented as a second scientific use case.

## Public release

This repository is a **limited technical release**, not the complete research codebase.

It shows the architecture, evidence model, review safeguards and representative implementation patterns while keeping the full production system private. The private implementation contains the complete backend, project-specific configurations, production prompts/contracts, research data and operational workflows.

**The exact CSP review/meta-analysis protocol is not public.** Protocol-specific search strategies, eligibility criteria, outcome definitions, analysis decisions, appraisal configuration and unpublished research data are intentionally excluded from this repository.

## What the platform does

```mermaid
flowchart LR
    A[Research project] --> B[Literature search / import]
    B --> C[Deduplication and screening]
    C --> D[Full text and source assets]
    D --> E[Structured evidence candidates]
    E --> F[Provenance and validation]
    F --> G[Human review]
    G --> H[Curated evidence]
    H --> I[Analysis / meta-analysis]
    I --> J[Tables, exports and forest plots]
```

The core platform separates **AI-generated candidates** from **curated scientific evidence**. Evidence proposed by a model remains reviewable and source-linked; human approval, rejection and correction are preserved as explicit decisions rather than being hidden inside model output.

## Core capabilities

- project-scoped literature search, import and deduplication;
- screening and study/report management;
- retained source assets and exact evidence provenance;
- project-configured variables, groups, observations, comparisons and effect estimates;
- structured AI-assisted extraction with independent validation gates;
- candidate-versus-curated evidence separation;
- human review, correction and audit history;
- deterministic statistical analysis and forest-plot generation;
- reproducible exports and analysis artifacts;
- model-independent backend with a Custom GPT/OpenAPI client used as one reference integration.

## Scientific use cases

### CSP systematic review and meta-analysis

The original use case drove the first evidence database and analysis workflow. It was later migrated into the generalized evidence model without deleting the original scientific records. The public case study describes the system architecture and workflow only; the private CSP protocol and research decisions are not disclosed.

[Read the CSP case study](docs/case-study-csp.md)

### Zebrafish CRISPR meta-analysis

The second use case exercised the same platform with different scientific entities, outcome types and source structures. This demonstrated that the evidence and review infrastructure could be reused beyond the original clinical research domain.

[Read the CRISPR case study](docs/case-study-crispr.md)

## Architecture

The working system uses a PostgreSQL scientific data layer, FastAPI services, versioned database migrations, a browser interface and external AI clients through authenticated API contracts. The evidence platform itself does not require a specific model provider.

A simplified view is provided in [Architecture](docs/architecture.md).

## Evidence governance

The implementation follows several platform-level rules:

- missing values are not converted to zero;
- AI output is not equivalent to human-approved evidence;
- approved scientific evidence must retain supporting provenance;
- project and study boundaries are enforced;
- corrected evidence is versioned rather than silently overwritten;
- analysis inclusion is specific to the analysis rather than a permanent property of a row;
- multiple reports from one study are not automatically treated as independent studies.

[Read the scientific governance notes](docs/scientific-governance.md).

## Public code

The `src/` directory contains small examples of the evidence contracts and review boundary used by the full system. They are intentionally limited and use synthetic data; they are not a drop-in copy of the private production implementation.

The `examples/` directory contains synthetic records illustrating the public data model without exposing research data or copyrighted source text.

## Technology used in the full implementation

Python, FastAPI, Pydantic, SQLAlchemy, PostgreSQL, Alembic, Next.js, Docker and authenticated OpenAPI integrations.

## What is intentionally not included

- complete production backend and frontend;
- CSP protocol, exact search strategy or project-specific analysis configuration;
- production CRISPR extraction configuration;
- real paper PDFs/XML/full-text corpora;
- private databases, backups or source-asset stores;
- gold-standard/reviewer datasets;
- production prompts and complete API contracts;
- credentials, deployment URLs or local environment configuration;
- the separate published-plasmid construction corpus project.

## Status

The private system remains the active research/development implementation. This repository exists to document the engineering approach and provide a limited technical demonstration without releasing the complete research platform or private scientific workflow.
