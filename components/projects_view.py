"""
projects_view.py
Renders the dedicated Project Explorer section.
Features dynamic category filters, project counts, verified architecture badges,
direct repository links, verified live app launches, and detail links.
"""

import html
import urllib.parse
from services.data_service import (
    get_all_projects,
    get_category_counts,
    get_projects_by_category,
)
from components.footer import render_footer
from components.utils import render_html


def render_projects_explorer(selected_category: str = "All") -> None:
    """Renders the filterable Project Explorer view."""
    counts = get_category_counts()
    categories = ["All", "Agentic AI", "RAG & Retrieval", "Developer Tools", "Machine Learning", "Computer Vision"]

    # Filter tabs as HTML links with target='_self'
    filter_links_html = ""
    norm_selected = (selected_category or "All").strip().lower()
    for cat in categories:
        count = counts.get(cat, 0)
        is_active = "active" if cat.strip().lower() == norm_selected else ""
        
        # Proper URL encoding with safe="" to ensure reserved characters like '&' are %-encoded
        encoded_cat = urllib.parse.quote(cat, safe="")
        raw_url = f"?tab=projects&cat={encoded_cat}"
        escaped_href = html.escape(raw_url)
        escaped_cat_label = html.escape(cat)

        filter_links_html += (
            f'<a href="{escaped_href}" target="_self" class="nav-item {is_active}" style="font-size:0.78rem;">'
            f'{escaped_cat_label} <span style="color:var(--text-muted); font-size:0.7rem;">({count})</span>'
            f'</a>'
        )

    header_html = f"""<div style="padding: 1rem 0 1.5rem; border-bottom: 1px solid var(--border);">
<div class="section-marker">// PROJECT EXPLORER</div>
<h1 class="section-title">Verified Technical Projects</h1>
<p class="section-subtitle">
Ten public repositories demonstrating autonomous multi-agent workflows,
hybrid retrieval systems, medical vision diagnostics, and quantitative modeling.
</p>
<div style="display:flex; align-items:center; gap:0.5rem; flex-wrap:wrap; margin-top:1.25rem;">
{filter_links_html}
</div>
</div>"""
    render_html(header_html)

    # Fetch projects matching category
    projects = get_projects_by_category(selected_category)

    if not projects:
        render_html("""<div style="padding:3rem 0; text-align:center; color:var(--text-muted);">
No projects found in this category.
</div>""")
        render_footer()
        return

    # Render Project Cards
    for proj in projects:
        cats_html = "".join([f'<span class="category-pill">{html.escape(c)}</span>' for c in proj.get("category", [])])
        tech_html = "".join([f'<span class="tech-tag">{html.escape(t)}</span>' for t in proj.get("tech_stack", [])])
        features_html = "".join([f'<li>{html.escape(f)}</li>' for f in proj.get("actual_features", [])[:3]])

        demo_btn = ""
        if proj.get("live_demo_url"):
            demo_btn = f'<a href="{html.escape(proj["live_demo_url"])}" target="_blank" rel="noopener noreferrer" class="project-link demo">Launch Live Demo ↗</a>'

        flagship_badge = ""
        if proj.get("flagship"):
            flagship_badge = '<span style="font-family:var(--font-mono); font-size:0.7rem; color:var(--accent-secondary); background:rgba(214, 166, 93, 0.1); border:1px solid rgba(214, 166, 93, 0.25); padding:0.15rem 0.45rem; border-radius:3px;">FLAGSHIP ARCHITECTURE</span>'

        encoded_proj_id = urllib.parse.quote(proj.get("id", ""), safe="")
        detail_href = html.escape(f"?tab=project_detail&id={encoded_proj_id}")
        repo_href = html.escape(proj.get("repo_url", ""))

        card_html = f"""<div class="featured-project-card" style="margin-top:1.5rem; margin-bottom:1.5rem;">
<div class="featured-project-meta-row">
<div class="project-category-pills">
{cats_html}
{flagship_badge}
</div>
<span class="project-status-tag">{html.escape(proj.get('status', ''))} • {html.escape(proj.get('last_updated', ''))}</span>
</div>

<h3 class="featured-project-title" style="font-size:1.3rem;">{html.escape(proj.get('name', ''))}</h3>
<p class="featured-project-desc" style="font-size:0.92rem;">{html.escape(proj.get('description', ''))}</p>

<div class="project-architecture-block">
<div class="architecture-block-label">Implementation Highlights</div>
<ul class="architecture-feature-list">
{features_html}
</ul>
</div>

<div class="project-tech-row">
{tech_html}
</div>

<div class="project-links-row">
<a href="{repo_href}" target="_blank" rel="noopener noreferrer" class="project-link">
GitHub Source ↗
</a>
{demo_btn}
<a href="{detail_href}" target="_self" class="project-link" style="margin-left:auto;">
Technical Dossier →
</a>
</div>
</div>"""
        render_html(card_html)

    render_footer()
