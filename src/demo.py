"""Tiny runnable demonstration of the public review boundary."""

from evidence_contracts import EvidenceCandidate, EvidencePacket
from review_gate import publication_check


packet = EvidencePacket(
    project_id=999,
    study_id=501,
    report_id=701,
    source_location="Synthetic report, Results, paragraph 2",
    source_text="Synthetic source text supporting the example observation.",
)

candidate = EvidenceCandidate(
    candidate_id="demo-001",
    entity_type="observation",
    payload={"value": 12.4, "n": 40},
    packet_hash=packet.packet_hash,
)
candidate.validate()

before_review = publication_check(
    source_location=packet.source_location,
    source_text=packet.source_text,
    candidate_project_id=999,
    target_project_id=999,
    candidate_study_id=501,
    target_study_id=501,
    human_status="not_reviewed",
)

after_review = publication_check(
    source_location=packet.source_location,
    source_text=packet.source_text,
    candidate_project_id=999,
    target_project_id=999,
    candidate_study_id=501,
    target_study_id=501,
    human_status="approved",
)

print(f"Candidate publishable before human review: {before_review.allowed}")
print(f"Candidate publishable after human review:  {after_review.allowed}")
