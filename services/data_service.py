"""
data_service.py
Provides robust access to local JSON data assets (profile, projects, case studies).
Calculates category counts dynamically without assuming mutual exclusivity.
"""

import json
import os
from typing import Dict, List, Any, Optional

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")


def load_json_file(filename: str) -> Any:
    """Loads a JSON file safely from the data directory."""
    path = os.path.join(DATA_DIR, filename)
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading {filename}: {e}")
        return [] if "projects" in filename or "case_studies" in filename else {}


def get_profile() -> Dict[str, Any]:
    """Returns developer profile information."""
    return load_json_file("profile.json")


def get_all_projects() -> List[Dict[str, Any]]:
    """Returns all verified project entries."""
    return load_json_file("projects.json")


def get_project_by_id(project_id: str) -> Optional[Dict[str, Any]]:
    """Retrieves a single project by its unique ID."""
    projects = get_all_projects()
    for proj in projects:
        if proj.get("id") == project_id:
            return proj
    return None


def get_flagship_projects() -> List[Dict[str, Any]]:
    """Retrieves projects marked as flagship."""
    return [p for p in get_all_projects() if p.get("flagship", False)]


def get_category_counts() -> Dict[str, int]:
    """
    Dynamically counts projects per category.
    Handles multi-category projects properly.
    """
    projects = get_all_projects()
    counts = {"All": len(projects)}
    for proj in projects:
        categories = proj.get("category", [])
        if isinstance(categories, str):
            categories = [categories]
        for cat in categories:
            counts[cat] = counts.get(cat, 0) + 1
    return counts


def get_projects_by_category(category: str) -> List[Dict[str, Any]]:
    """Filters projects by category (case-insensitive), or returns all if 'All'."""
    projects = get_all_projects()
    if not category or category.strip().lower() == "all":
        return projects
    norm_cat = category.strip().lower()
    filtered = []
    for proj in projects:
        categories = proj.get("category", [])
        if isinstance(categories, str):
            categories = [categories]
        if any(c.strip().lower() == norm_cat for c in categories):
            filtered.append(proj)
    return filtered


def get_case_studies() -> List[Dict[str, Any]]:
    """Returns technical engineering case studies."""
    return load_json_file("case_studies.json")


def get_case_study_by_id(case_study_id: str) -> Optional[Dict[str, Any]]:
    """Retrieves a specific case study by ID."""
    studies = get_case_studies()
    for s in studies:
        if s.get("id") == case_study_id:
            return s
    return None
