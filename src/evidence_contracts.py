"""Simplified public contracts based on the private evidence workflow.

These examples retain the production system's scope, configuration, provenance,
candidate and review-state concepts without exposing its schemas or services.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from hashlib import sha256
import json
from typing import Any


def stable_hash(payload: Any) -> str:
    encoded = json.dumps(
        payload,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")
    return sha256(encoded).hexdigest()


@dataclass(frozen=True)
class EvidencePacket:
    project_id: int
    study_id: int
    article_id: int
    configuration_version_id: int
    source_location: str
    source_text: str

    def validate(self) -> None:
        scoped_ids = (
            self.project_id,
            self.study_id,
            self.article_id,
            self.configuration_version_id,
        )
        if min(scoped_ids) <= 0:
            raise ValueError("scope and configuration IDs must be positive")
        if not self.source_location.strip():
            raise ValueError("source location is required")
        if not self.source_text.strip():
            raise ValueError("source text is required")

    @property
    def packet_hash(self) -> str:
        self.validate()
        return stable_hash(asdict(self))


@dataclass(frozen=True)
class EvidenceCandidate:
    candidate_id: str
    entity_type: str
    payload: dict[str, Any]
    packet_hash: str
    status: str = "pending"

    def validate(self) -> None:
        if not self.candidate_id.strip():
            raise ValueError("candidate ID is required")
        if not self.entity_type.strip():
            raise ValueError("entity type is required")
        if self.status not in {
            "pending",
            "published_pending_review",
            "rejected",
            "superseded",
        }:
            raise ValueError("unsupported candidate status")
        if len(self.packet_hash) != 64:
            raise ValueError("candidate must bind to a source packet hash")


@dataclass(frozen=True)
class ScientificRecord:
    entity_type: str
    payload: dict[str, Any]
    review_status: str = "draft_ai"
    version: int = 1
    previous_version_id: int | None = None

    @property
    def curated(self) -> bool:
        return self.review_status in {"approved", "approved_with_edits"}


@dataclass(frozen=True)
class ReviewDecision:
    candidate_id: str
    reviewer: str
    action: str
    notes: str | None = None

    def validate(self) -> None:
        if self.action not in {"approve", "reject", "correct"}:
            raise ValueError("unsupported review action")
        if not self.reviewer.strip():
            raise ValueError("reviewer identity is required")
