"""
test_services.py
Automated validation of data loading, dynamic category counts,
flagship dossiers, and query parameter routing logic.
"""

import os
import sys

# Ensure workspace root is in path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.data_service import (
    get_profile,
    get_all_projects,
    get_project_by_id,
    get_flagship_projects,
    get_category_counts,
    get_projects_by_category,
    get_case_studies,
    get_case_study_by_id,
)
from services.dossier_service import get_flagship_dossier


def test_profile():
    profile = get_profile()
    assert profile["name"] == "Nitish Kumar", "Profile name mismatch"
    assert profile["github_username"] == "XestalNitish", "GitHub username mismatch"
    assert "github.com/XestalNitish" in profile["github_url"]
    print("✓ Profile data validated successfully")


def test_projects_inventory():
    projects = get_all_projects()
    assert len(projects) == 10, f"Expected 10 verified projects, got {len(projects)}"

    # Check required fields
    required_fields = [
        "id", "name", "repo_url", "description", "problem_statement",
        "actual_features", "tech_stack", "status", "category",
        "evidence_references", "known_limitations"
    ]
    for p in projects:
        for field in required_fields:
            assert field in p, f"Project {p.get('id')} missing required field: {field}"
            assert p[field] is not None, f"Project {p.get('id')} field {field} is None"

    print("✓ All 10 projects contain all 11 required schema fields")


def test_flagship_projects():
    flagships = get_flagship_projects()
    assert len(flagships) == 3, f"Expected 3 flagship projects, got {len(flagships)}"
    flagship_ids = [p["id"] for p in flagships]
    assert "ultimate-coding-agent" in flagship_ids
    assert "xestal-enterprise-rag-engine" in flagship_ids
    assert "xestal-research-agent" in flagship_ids
    print("✓ Three flagship projects identified and validated")


def test_flagship_dossiers():
    for f_id in ["ultimate-coding-agent", "xestal-enterprise-rag-engine", "xestal-research-agent"]:
        dossier = get_flagship_dossier(f_id)
        assert dossier is not None, f"Dossier missing for {f_id}"
        # Verify 15 parts
        expected_keys = [
            "p1_overview", "p2_problem", "p3_design_goals", "p4_architecture_svg",
            "p5_workflow", "p6_technology_choices", "p7_implementation",
            "p8_engineering_challenges", "p9_failure_handling", "p10_evaluation",
            "p11_results", "p12_limitations", "p13_future_improvements",
            "p14_source_code", "p15_live_demo"
        ]
        for key in expected_keys:
            assert key in dossier, f"Dossier {f_id} missing 15-part key: {key}"
    print("✓ Comprehensive 15-part engineering dossiers validated for all flagship projects")


def test_category_counts():
    counts = get_category_counts()
    print("Dynamic Category Counts:", counts)
    assert counts["All"] == 10
    assert counts.get("Agentic AI", 0) >= 3
    assert counts.get("RAG & Retrieval", 0) >= 2
    assert counts.get("Developer Tools", 0) >= 3
    print("✓ Dynamic category counting functions correctly")


def test_case_studies():
    studies = get_case_studies()
    assert len(studies) == 3, f"Expected 3 case studies, got {len(studies)}"
    rag_study = get_case_study_by_id("rag-benchmark-failure-attribution")
    assert rag_study is not None
    m = rag_study["benchmark_metrics"]
    assert m["retrieval_hit_rate"] == "46/48 (95.8%)"
    assert m["failure_causes"]["generation_failures"] == 28
    assert m["failure_causes"]["retrieval_misses"] == 2
    print("✓ Case studies and benchmark integrity data verified")


def test_invalid_project_id():
    p = get_project_by_id("non-existent-project-xyz")
    assert p is None, "Expected None for non-existent project"
    print("✓ Invalid project ID returns None gracefully")


if __name__ == "__main__":
    test_profile()
    test_projects_inventory()
    test_flagship_projects()
    test_flagship_dossiers()
    test_category_counts()
    test_case_studies()
    test_invalid_project_id()
    print("\nALL AUTOMATED TESTS PASSED SUCCESSFULLY!")
