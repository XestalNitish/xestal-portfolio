"""
app.py — X-ESTAL Nitish Personal AI Engineering Portfolio
=========================================================
Production-quality personal engineering portfolio designed for Nitish Kumar.
Built for deployment on Streamlit Community Cloud with a custom restrained
dark editorial aesthetic, URL query-parameter routing, and modular components.
"""

import os
import urllib.parse
import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="X-ESTAL Nitish | AI Engineering Portfolio",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# 2. Inject Editorial CSS
def inject_custom_css():
    css_path = os.path.join(os.path.dirname(__file__), "styles", "editorial.css")
    if os.path.exists(css_path):
        with open(css_path, "r", encoding="utf-8") as f:
            css_content = f.read()
        st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)

inject_custom_css()

# 3. Import View Components & Services
from components.navigation import render_navigation
from components.home_view import render_homepage
from components.projects_view import render_projects_explorer
from components.project_detail_view import render_project_detail
from components.case_studies_view import render_case_studies
from components.skills_view import render_skills
from components.about_view import render_about
from components.contact_view import render_contact

# 4. Route Handling via st.query_params
current_tab = st.query_params.get("tab", "home")
raw_project_id = st.query_params.get("id", st.query_params.get("project", None))
project_id = urllib.parse.unquote_plus(raw_project_id) if raw_project_id else None

raw_cat = st.query_params.get("cat", "All")
selected_cat = urllib.parse.unquote_plus(raw_cat) if raw_cat else "All"

# Normalize tab if user opened detail view
nav_active_tab = "projects" if current_tab == "project_detail" else current_tab

# Render Top Navigation
render_navigation(active_tab=nav_active_tab)

# View Dispatcher
if current_tab == "home":
    render_homepage()
elif current_tab == "projects":
    render_projects_explorer(selected_category=selected_cat)
elif current_tab == "project_detail":
    render_project_detail(project_id=project_id)
elif current_tab == "case_studies":
    render_case_studies()
elif current_tab == "skills":
    render_skills()
elif current_tab == "about":
    render_about()
elif current_tab == "contact":
    render_contact()
else:
    # Graceful fallback to homepage
    render_homepage()
