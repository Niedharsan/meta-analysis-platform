from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from evidence_contracts import EvidenceCandidate, EvidencePacket, ScientificRecord
from review_gate import candidate_materialization_check, is_curated


def synthetic_packet() -> EvidencePacket:
    return EvidencePacket(
        project_id=1,
        study_id=2,
        article_id=3,
        configuration_version_id=4,
        source_location="Synthetic source location",
        source_text="Synthetic supporting text",
    )


def test_valid_candidate_can_materialize_as_draft_but_is_not_curated():
    packet = synthetic_packet()
    candidate = EvidenceCandidate(
        candidate_id="demo",
        entity_type="observation",
        payload={"value": 1.0},
        packet_hash=packet.packet_hash,
    )
    candidate.validate()

    check = candidate_materialization_check(
        source_location=packet.source_location,
        source_text=packet.source_text,
        candidate_project_id=1,
        target_project_id=1,
        candidate_study_id=2,
        target_study_id=2,
        configuration_is_frozen=True,
    )
    draft = ScientificRecord(candidate.entity_type, candidate.payload)

    assert check.allowed is True
    assert draft.review_status == "draft_ai"
    assert draft.curated is False
    assert is_curated(
        review_status=draft.review_status,
        provenance_is_attributable=True,
    ) is False


def test_human_approved_row_requires_attributable_provenance():
    assert is_curated(
        review_status="approved",
        provenance_is_attributable=False,
    ) is False
    assert is_curated(
        review_status="approved",
        provenance_is_attributable=True,
    ) is True


def test_cross_project_candidate_is_blocked():
    check = candidate_materialization_check(
        source_location="Synthetic source location",
        source_text="Synthetic supporting text",
        candidate_project_id=1,
        target_project_id=99,
        candidate_study_id=2,
        target_study_id=2,
        configuration_is_frozen=True,
    )
    assert check.allowed is False


def test_unfrozen_configuration_is_blocked():
    check = candidate_materialization_check(
        source_location="Synthetic source location",
        source_text="Synthetic supporting text",
        candidate_project_id=1,
        target_project_id=1,
        candidate_study_id=2,
        target_study_id=2,
        configuration_is_frozen=False,
    )
    assert check.allowed is False


def test_public_tree_contains_no_private_release_artifact_types():
    prohibited_suffixes = {
        ".bib",
        ".csv",
        ".db",
        ".dump",
        ".env",
        ".nbib",
        ".pdf",
        ".pem",
        ".key",
        ".ris",
        ".sql",
        ".sqlite",
        ".sqlite3",
        ".tsv",
        ".xls",
        ".xlsx",
        ".xml",
        ".zip",
    }
    files = [
        path
        for path in ROOT.rglob("*")
        if path.is_file() and ".git" not in path.parts
    ]
    assert not [path for path in files if path.suffix.lower() in prohibited_suffixes]


def test_public_text_has_no_private_host_or_project3_markers():
    markers = (
        "127.0.0.1",
        "/users/",
        "cloudflare",
        "localhost",
        "ngrok",
        "project 3",
        "project3",
    )
    text_files = [
        path
        for path in ROOT.rglob("*")
        if path.is_file()
        and ".git" not in path.parts
        and path.resolve() != Path(__file__).resolve()
        and path.suffix.lower() in {
            ".md",
            ".py",
            ".json",
            ".txt",
            ".yml",
            ".yaml",
        }
    ]
    findings = {
        str(path.relative_to(ROOT)): marker
        for path in text_files
        for marker in markers
        if marker in path.read_text(encoding="utf-8").casefold()
    }
    assert not findings
