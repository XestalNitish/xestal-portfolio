"""
test_services.py
Automated validation of data loading, dynamic category counts,
flagship dossiers, query parameter routing logic, and category filter URL encoding.
"""

import os
import sys
import urllib.parse
import html

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
    assert counts.get("Agentic AI", 0) == 5
    assert counts.get("RAG & Retrieval", 0) == 2
    assert counts.get("Developer Tools", 0) == 6
    assert counts.get("Machine Learning", 0) == 3
    assert counts.get("Computer Vision", 0) == 1
    print("✓ Dynamic category counting functions correctly")


def test_category_filtering_and_encoding():
    # 1. Test source of truth filtering
    rag_projects = get_projects_by_category("RAG & Retrieval")
    assert len(rag_projects) == 2, f"Expected 2 RAG projects, got {len(rag_projects)}"
    rag_names = [p["name"] for p in rag_projects]
    assert "Ultimate Coding Agent" in rag_names
    assert "X-Estal Enterprise Hybrid RAG Engine" in rag_names

    agentic_projects = get_projects_by_category("Agentic AI")
    assert len(agentic_projects) == 5, f"Expected 5 Agentic AI projects, got {len(agentic_projects)}"

    all_projects = get_projects_by_category("All")
    assert len(all_projects) == 10, f"Expected 10 projects for All, got {len(all_projects)}"

    # 2. Test URL encoding of category with '&'
    cat_name = "RAG & Retrieval"
    encoded_cat = urllib.parse.quote(cat_name, safe="")
    assert encoded_cat == "RAG%20%26%20Retrieval", f"Unexpected encoding: {encoded_cat}"

    # 3. Test HTML escaping of anchor href
    raw_query = f"?tab=projects&cat={encoded_cat}"
    escaped_href = html.escape(raw_query)
    assert escaped_href == "?tab=projects&amp;cat=RAG%20%26%20Retrieval"

    # 4. Verify query parser decodes RAG%20%26%20Retrieval cleanly without truncation
    parsed = urllib.parse.parse_qs(raw_query.lstrip("?"))
    decoded_val = parsed["cat"][0]
    assert decoded_val == "RAG & Retrieval", f"Parsed value truncated or corrupted: {decoded_val}"

    # 5. Contrast against bad unencoded URL to document root cause
    bad_query = f"?tab=projects&cat={cat_name}"
    bad_parsed = urllib.parse.parse_qs(bad_query.lstrip("?"))
    assert bad_parsed["cat"][0] == "RAG ", "Demonstrating root cause: unencoded & truncates cat to 'RAG '"

    # 6. Verify case-insensitivity in filtering
    assert len(get_projects_by_category("rag & retrieval")) == 2
    assert len(get_projects_by_category("agentic ai")) == 5

    print("✓ Category URL encoding, HTML attribute escaping, and filtering verified successfully")


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
    test_category_filtering_and_encoding()
    test_case_studies()
    test_invalid_project_id()
    print("\nALL AUTOMATED TESTS PASSED SUCCESSFULLY!")
