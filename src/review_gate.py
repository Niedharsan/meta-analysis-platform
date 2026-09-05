"""Public demonstration of the candidate-to-curated review boundary.

The production platform contains database transactions, project configuration,
scientific schemas, provenance tables, version history and additional gates.
Those implementation details are deliberately not part of this public release.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PublicationCheck:
    has_source_location: bool
    has_source_text: bool
    project_scope_valid: bool
    study_scope_valid: bool
    human_approved: bool

    @property
    def allowed(self) -> bool:
        return all(
            (
                self.has_source_location,
                self.has_source_text,
                self.project_scope_valid,
                self.study_scope_valid,
                self.human_approved,
            )
        )


def publication_check(
    *,
    source_location: str | None,
    source_text: str | None,
    candidate_project_id: int,
    target_project_id: int,
    candidate_study_id: int,
    target_study_id: int,
    human_status: str,
) -> PublicationCheck:
    """Return the public, simplified form of the publication boundary."""

    return PublicationCheck(
        has_source_location=bool(source_location and source_location.strip()),
        has_source_text=bool(source_text and source_text.strip()),
        project_scope_valid=candidate_project_id == target_project_id,
        study_scope_valid=candidate_study_id == target_study_id,
        human_approved=human_status == "approved",
    )
