# Scientific governance

The platform treats model output as a proposal, not as scientific truth.

The production system separates evidence extraction, validation, review and analysis so that model-generated records do not silently become approved research data.

## Core rules

### Candidate evidence is separate from curated evidence

AI-assisted extraction writes proposed scientific records into a candidate/review layer. Human-approved evidence is stored separately with explicit review state and provenance.

### Provenance is part of the evidence record

Scientific rows that require source support retain a link to the source report and supporting location/text. This allows a reviewer to inspect where a claim came from rather than relying on a model summary alone.

### Missing values remain missing

The platform does not convert unreported measurements, dispersion, event counts or other missing scientific values into zero.

### Scope is enforced

Evidence packets, candidates and reviewed scientific records are scoped to a project and study/report context. Cross-project or cross-study references are rejected by the production validation layer.

### Corrections are auditable

Review edits and status transitions are recorded rather than silently replacing the previous candidate state. Approved scientific rows can also retain version/lineage information where required.

### Independent checking is supported

The evidence-agent architecture separates the domain evidence specialist from independent verifier roles. Verification is bound to the corresponding specialist output rather than being treated as an unrelated second model response.

### AI does not approve scientific evidence

Model roles can extract, flag, check and propose corrections. Final scientific approval remains outside the model role.

### Analysis inclusion is analysis-specific

A reviewed observation or effect estimate can be eligible for one analysis and not another. Inclusion therefore belongs to an analysis evidence set rather than being treated as a permanent global truth about the scientific row.

## Project-specific rules

Scientific protocols remain project configuration, not global platform assumptions. Different reviews may define different eligible designs, target variables, screening rules, analysis plans or appraisal procedures while using the same underlying infrastructure.

The exact CSP project protocol is intentionally excluded from this public repository.
