"""Run the limited public demonstration with synthetic evidence."""

from evidence_contracts import EvidenceCandidate, EvidencePacket, ScientificRecord
from review_gate import candidate_materialization_check, is_curated


packet = EvidencePacket(
    project_id=999,
    study_id=501,
    article_id=701,
    configuration_version_id=1,
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

materialization = candidate_materialization_check(
    source_location=packet.source_location,
    source_text=packet.source_text,
    candidate_project_id=packet.project_id,
    target_project_id=999,
    candidate_study_id=packet.study_id,
    target_study_id=501,
    configuration_is_frozen=True,
)

draft = ScientificRecord(candidate.entity_type, candidate.payload)
approved = ScientificRecord(
    candidate.entity_type,
    candidate.payload,
    review_status="approved",
)

print(f"Candidate passes materialization checks: {materialization.allowed}")
print(f"Materialized row review status:        {draft.review_status}")
print(
    "Row is curated before human review:    "
    f"{is_curated(review_status=draft.review_status, provenance_is_attributable=True)}"
)
print(
    "Row is curated after human review:     "
    f"{is_curated(review_status=approved.review_status, provenance_is_attributable=True)}"
)
