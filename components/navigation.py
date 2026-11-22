"""
navigation.py
Renders the restrained dark editorial top navigation bar.
Synchronizes with Streamlit's st.query_params for robust URL routing.
Includes verified external links and one-click resume download.
"""

from typing import Dict, Any
import streamlit as st
from components.utils import render_html
from services.resume_service import get_resume_data_url, is_resume_available


NAV_ITEMS = [
    {"id": "home", "label": "Home"},
    {"id": "projects", "label": "Projects"},
    {"id": "case_studies", "label": "Case Studies"},
    {"id": "skills", "label": "Skills"},
    {"id": "about", "label": "About"},
    {"id": "contact", "label": "Contact"},
]


def get_current_route() -> Dict[str, Any]:
    """
    Reads the current navigation state from st.query_params.
    Defaults to 'home' if missing or invalid.
    """
    valid_tabs = [item["id"] for item in NAV_ITEMS]
    current_tab = st.query_params.get("tab", "home")
    if current_tab not in valid_tabs:
        current_tab = "home"
    
    project_id = st.query_params.get("project", None)
    case_study_id = st.query_params.get("case_study", None)
    
    return {
        "tab": current_tab,
        "project_id": project_id,
        "case_study_id": case_study_id,
    }


def render_navigation(active_tab: str = "home") -> None:
    """
    Renders the compact editorial top navigation bar.
    Uses target='_self' relative links to update st.query_params cleanly.
    """
    links_html = ""
    for item in NAV_ITEMS:
        is_active = "active" if item["id"] == active_tab else ""
        links_html += f'<a href="?tab={item["id"]}" target="_self" class="nav-item {is_active}">{item["label"]}</a>'

    resume_url = get_resume_data_url()
    if resume_url:
        resume_nav_link = f'<a href="{resume_url}" download="Nitish_Kumar_CV.pdf" class="nav-ext-link" style="color:var(--accent-secondary); font-weight:600;">Resume ↓</a>'
    else:
        resume_nav_link = '<a href="?tab=contact" target="_self" class="nav-ext-link" style="color:var(--text-muted);">Resume</a>'

    nav_html = f"""<div class="nav-wrapper">
<div class="nav-container">
<a href="?tab=home" target="_self" class="nav-brand">
<span class="nav-brand-title">X-ESTAL</span>
<span class="nav-brand-sub">Nitish Kumar</span>
</a>
<div class="nav-links">
{links_html}
</div>
<div class="nav-external">
{resume_nav_link}
<a href="https://github.com/XestalNitish" target="_blank" rel="noopener noreferrer" class="nav-ext-link">
GitHub ↗
</a>
<a href="https://www.linkedin.com/in/nitish-kumar-ai" target="_blank" rel="noopener noreferrer" class="nav-ext-link">
LinkedIn ↗
</a>
</div>
</div>
</div>"""
    render_html(nav_html)
