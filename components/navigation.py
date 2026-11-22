"""
navigation.py
Renders the restrained dark editorial top navigation bar.
Synchronizes with Streamlit's st.query_params for robust URL routing.
Supports: browser back/forward, direct bookmarking, and page refreshes.
"""

import streamlit as st
from typing import Dict, Any


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
        links_html += f"""
        <a href="?tab={item['id']}" target="_self" class="nav-item {is_active}">
          {item['label']}
        </a>
        """

    nav_html = f"""
    <div class="nav-wrapper">
      <div class="nav-container">
        <a href="?tab=home" target="_self" class="nav-brand">
          <span class="nav-brand-title">X-ESTAL</span>
          <span class="nav-brand-sub">Nitish Kumar</span>
        </a>
        <div class="nav-links">
          {links_html}
        </div>
        <div class="nav-external">
          <a href="https://github.com/XestalNitish" target="_blank" rel="noopener noreferrer" class="nav-ext-link">
            GitHub ↗
          </a>
          <a href="https://www.linkedin.com/in/nitish-kumar-33714642b/" target="_blank" rel="noopener noreferrer" class="nav-ext-link">
            LinkedIn ↗
          </a>
        </div>
      </div>
    </div>
    """
    st.markdown(nav_html, unsafe_allow_html=True)
