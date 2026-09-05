"""Public demonstration of materialization and curation checks.

The production system implements these boundaries with database transactions,
versioned project configuration, typed schemas, provenance and review history.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class MaterializationCheck:
    has_source_location: bool
    has_source_text: bool
    project_scope_valid: bool
    study_scope_valid: bool
    configuration_is_frozen: bool

    @property
    def allowed(self) -> bool:
        return all(
            (
                self.has_source_location,
                self.has_source_text,
                self.project_scope_valid,
                self.study_scope_valid,
                self.configuration_is_frozen,
            )
        )


def candidate_materialization_check(
    *,
    source_location: str | None,
    source_text: str | None,
    candidate_project_id: int,
    target_project_id: int,
    candidate_study_id: int,
    target_study_id: int,
    configuration_is_frozen: bool,
) -> MaterializationCheck:
    """Return a limited public form of the pre-materialization checks."""

    return MaterializationCheck(
        has_source_location=bool(source_location and source_location.strip()),
        has_source_text=bool(source_text and source_text.strip()),
        project_scope_valid=candidate_project_id == target_project_id,
        study_scope_valid=candidate_study_id == target_study_id,
        configuration_is_frozen=configuration_is_frozen,
    )


def is_curated(*, review_status: str, provenance_is_attributable: bool) -> bool:
    """A materialized row is curated only after attributable human approval."""

    return (
        review_status in {"approved", "approved_with_edits"}
        and provenance_is_attributable
    )
