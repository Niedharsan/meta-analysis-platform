from pathlib import Path
import sys


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from evidence_contracts import EvidenceCandidate, EvidencePacket
from review_gate import publication_check


def test_candidate_requires_human_review_before_publication():
    packet = EvidencePacket(
        project_id=1,
        study_id=2,
        report_id=3,
        source_location="Synthetic source location",
        source_text="Synthetic supporting text",
    )
    candidate = EvidenceCandidate(
        candidate_id="demo",
        entity_type="observation",
        payload={"value": 1.0},
        packet_hash=packet.packet_hash,
    )
    candidate.validate()

    blocked = publication_check(
        source_location=packet.source_location,
        source_text=packet.source_text,
        candidate_project_id=1,
        target_project_id=1,
        candidate_study_id=2,
        target_study_id=2,
        human_status="not_reviewed",
    )
    assert blocked.allowed is False

    approved = publication_check(
        source_location=packet.source_location,
        source_text=packet.source_text,
        candidate_project_id=1,
        target_project_id=1,
        candidate_study_id=2,
        target_study_id=2,
        human_status="approved",
    )
    assert approved.allowed is True


def test_cross_project_candidate_is_blocked():
    check = publication_check(
        source_location="Synthetic source location",
        source_text="Synthetic supporting text",
        candidate_project_id=1,
        target_project_id=99,
        candidate_study_id=2,
        target_study_id=2,
        human_status="approved",
    )
    assert check.allowed is False
