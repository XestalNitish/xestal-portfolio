"""
project_detail_view.py
Renders the complete 15-part technical engineering presentation for projects.
Features verified architecture SVG diagrams, empirical evaluation data,
failure recovery mechanisms, and known limitations.
Handles invalid project IDs with an informative fallback.
"""

from services.data_service import get_project_by_id
from services.dossier_service import get_flagship_dossier
from components.footer import render_footer
from components.utils import render_html


def render_project_detail(project_id: str) -> None:
    """Renders the comprehensive 15-part engineering presentation."""
    project = get_project_by_id(project_id)

    # 1. Graceful fallback on invalid project ID
    if not project:
        render_html("""<div style="padding: 4rem 1rem; text-align: center;">
<div class="section-marker">// 404 NOT FOUND</div>
<h2 class="section-title">Project Not Found</h2>
<p style="color:var(--text-secondary); max-width:500px; margin: 0 auto 1.5rem;">
The requested project identifier does not exist in our verified inventory.
</p>
<a href="?tab=projects" target="_self" class="btn-primary">
← Return to Project Explorer
</a>
</div>""")
        render_footer()
        return

    # Check if a dedicated 15-part flagship dossier exists
    dossier = get_flagship_dossier(project_id)

    name = project.get("name")
    status = project.get("status")
    last_updated = project.get("last_updated")
    repo_url = project.get("repo_url")
    demo_url = project.get("live_demo_url")

    tech_pills = "".join([f'<span class="tech-tag">{t}</span>' for t in project.get("tech_stack", [])])
    category_pills = "".join([f'<span class="category-pill">{c}</span>' for c in project.get("category", [])])

    demo_btn_html = ""
    if demo_url:
        demo_btn_html = f'<a href="{demo_url}" target="_blank" rel="noopener noreferrer" class="btn-primary" style="background:#10B981; border-color:#10B981;">Launch Live App ↗</a>'

    if dossier:
        # Full 15-part flagship presentation
        design_goals_html = "".join([f'<li>{g}</li>' for g in dossier["p3_design_goals"]])
        tech_choices_html = "".join([
            f'<div style="background:var(--bg-main); border:1px solid var(--border); border-radius:4px; padding:0.85rem;">'
            f'<div style="font-family:var(--font-mono); font-size:0.82rem; font-weight:600; color:var(--accent); margin-bottom:0.25rem;">{t[0]}</div>'
            f'<div style="font-size:0.84rem; color:var(--text-secondary); line-height:1.5;">{t[1]}</div>'
            f'</div>'
            for t in dossier["p6_technology_choices"]
        ])
        challenges_html = "".join([f'<li>{c}</li>' for c in dossier["p8_engineering_challenges"]])
        results_html = "".join([f'<li>{r}</li>' for r in dossier["p11_results"]])
        limitations_html = "".join([f'<li>{l}</li>' for l in dossier["p12_limitations"]])
        improvements_html = "".join([f'<li>{imp}</li>' for imp in dossier["p13_future_improvements"]])

        detail_content_html = f"""<div style="border-bottom:1px solid var(--border-subtle); padding-bottom:1.75rem;">
<div class="section-marker">01 // OVERVIEW</div>
<h3 style="font-family:var(--font-heading); font-size:1.25rem; color:var(--text-primary); margin-bottom:0.6rem;">System Overview</h3>
<p style="color:var(--text-secondary); line-height:1.75; font-size:0.95rem; margin:0;">{dossier["p1_overview"]}</p>
</div>

<div style="border-bottom:1px solid var(--border-subtle); padding-bottom:1.75rem;">
<div class="section-marker">02 // PROBLEM STATEMENT</div>
<h3 style="font-family:var(--font-heading); font-size:1.25rem; color:var(--text-primary); margin-bottom:0.6rem;">Engineering Problem Context</h3>
<pre style="white-space:pre-wrap; background:var(--bg-surface); border:1px solid var(--border-subtle); padding:1rem; border-radius:4px; font-family:var(--font-body); font-size:0.9rem; color:var(--text-secondary); margin:0; line-height:1.65;">{dossier["p2_problem"]}</pre>
</div>

<div style="border-bottom:1px solid var(--border-subtle); padding-bottom:1.75rem;">
<div class="section-marker">03 // DESIGN GOALS</div>
<h3 style="font-family:var(--font-heading); font-size:1.25rem; color:var(--text-primary); margin-bottom:0.6rem;">Architectural Goals</h3>
<ul style="color:var(--text-secondary); line-height:1.8; font-size:0.92rem; padding-left:1.25rem; margin:0;">
{design_goals_html}
</ul>
</div>

<div style="border-bottom:1px solid var(--border-subtle); padding-bottom:1.75rem;">
<div class="section-marker">04 // ARCHITECTURAL TOPOLOGY</div>
<h3 style="font-family:var(--font-heading); font-size:1.25rem; color:var(--text-primary); margin-bottom:0.6rem;">Verified System Graph</h3>
{dossier["p4_architecture_svg"]}
</div>

<div style="border-bottom:1px solid var(--border-subtle); padding-bottom:1.75rem;">
<div class="section-marker">05 // WORKFLOW &amp; EXECUTION PHASES</div>
<h3 style="font-family:var(--font-heading); font-size:1.25rem; color:var(--text-primary); margin-bottom:0.6rem;">Step-by-Step Execution</h3>
<pre style="white-space:pre-wrap; background:var(--bg-main); border:1px solid var(--border); padding:1.25rem; border-radius:4px; font-family:var(--font-body); font-size:0.9rem; color:var(--text-secondary); margin:0; line-height:1.7;">{dossier["p5_workflow"]}</pre>
</div>

<div style="border-bottom:1px solid var(--border-subtle); padding-bottom:1.75rem;">
<div class="section-marker">06 // TECHNOLOGY CHOICES &amp; TRADEOFFS</div>
<h3 style="font-family:var(--font-heading); font-size:1.25rem; color:var(--text-primary); margin-bottom:0.6rem;">Core Technology Stack</h3>
<div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:0.75rem;">
{tech_choices_html}
</div>
</div>

<div style="border-bottom:1px solid var(--border-subtle); padding-bottom:1.75rem;">
<div class="section-marker">07 // IMPLEMENTATION DETAILS</div>
<h3 style="font-family:var(--font-heading); font-size:1.25rem; color:var(--text-primary); margin-bottom:0.6rem;">Codebase Structure</h3>
<p style="color:var(--text-secondary); line-height:1.75; font-size:0.95rem; margin:0;">{dossier["p7_implementation"]}</p>
</div>

<div style="border-bottom:1px solid var(--border-subtle); padding-bottom:1.75rem;">
<div class="section-marker">08 // ENGINEERING CHALLENGES &amp; DEBUGGING</div>
<h3 style="font-family:var(--font-heading); font-size:1.25rem; color:var(--text-primary); margin-bottom:0.6rem;">Key Technical Obstacles Overcome</h3>
<ul style="color:var(--text-secondary); line-height:1.8; font-size:0.92rem; padding-left:1.25rem; margin:0;">
{challenges_html}
</ul>
</div>

<div style="border-bottom:1px solid var(--border-subtle); padding-bottom:1.75rem;">
<div class="section-marker">09 // FAILURE HANDLING &amp; RECOVERY</div>
<h3 style="font-family:var(--font-heading); font-size:1.25rem; color:var(--text-primary); margin-bottom:0.6rem;">Resilience &amp; Error Boundaries</h3>
<pre style="white-space:pre-wrap; background:var(--bg-surface); border:1px solid var(--border-subtle); padding:1rem; border-radius:4px; font-family:var(--font-body); font-size:0.9rem; color:var(--text-secondary); margin:0; line-height:1.65;">{dossier["p9_failure_handling"]}</pre>
</div>

<div style="border-bottom:1px solid var(--border-subtle); padding-bottom:1.75rem;">
<div class="section-marker">10 // EVALUATION &amp; 11 // MEASURABLE RESULTS</div>
<h3 style="font-family:var(--font-heading); font-size:1.25rem; color:var(--text-primary); margin-bottom:0.6rem;">Empirical Evaluation</h3>
<p style="color:var(--text-secondary); line-height:1.75; font-size:0.95rem; margin-bottom:0.75rem;">{dossier["p10_evaluation"]}</p>
<ul style="color:var(--text-secondary); line-height:1.8; font-size:0.92rem; padding-left:1.25rem; margin:0;">
{results_html}
</ul>
</div>

<div style="border-bottom:1px solid var(--border-subtle); padding-bottom:1.75rem;">
<div class="section-marker">12 // LIMITATIONS &amp; 13 // ROADMAP</div>
<h3 style="font-family:var(--font-heading); font-size:1.25rem; color:var(--text-primary); margin-bottom:0.6rem;">Known Limitations &amp; Future Scope</h3>
<div style="background:rgba(214, 166, 93, 0.05); border:1px solid rgba(214, 166, 93, 0.2); border-radius:4px; padding:1rem; margin-bottom:1rem;">
<div style="font-family:var(--font-mono); font-size:0.75rem; color:var(--accent-secondary); margin-bottom:0.4rem;">KNOWN SYSTEM CONSTRAINTS</div>
<ul style="color:var(--text-secondary); font-size:0.88rem; line-height:1.6; margin:0; padding-left:1.25rem;">
{limitations_html}
</ul>
</div>
<div style="background:var(--bg-main); border:1px solid var(--border); border-radius:4px; padding:1rem;">
<div style="font-family:var(--font-mono); font-size:0.75rem; color:var(--accent); margin-bottom:0.4rem;">FUTURE ENGINEERING ROADMAP</div>
<ul style="color:var(--text-secondary); font-size:0.88rem; line-height:1.6; margin:0; padding-left:1.25rem;">
{improvements_html}
</ul>
</div>
</div>

<div style="padding-bottom:1rem;">
<div class="section-marker">14 // SOURCE CODE &amp; 15 // DEMONSTRATION</div>
<h3 style="font-family:var(--font-heading); font-size:1.25rem; color:var(--text-primary); margin-bottom:0.75rem;">Verification Links</h3>
<div style="display:flex; align-items:center; gap:1rem; flex-wrap:wrap;">
<a href="{dossier['p14_source_code']}" target="_blank" rel="noopener noreferrer" class="btn-primary">
Inspect Repository on GitHub ↗
</a>
{demo_btn_html}
</div>
</div>"""
    else:
        # Standard structured presentation for secondary projects
        features_list = "".join([f'<li>{f}</li>' for f in project.get("actual_features", [])])
        evidence_list = "".join([f'<li><code>{e}</code></li>' for e in project.get("evidence_references", [])])
        limitations_list = "".join([f'<li>{lim}</li>' for lim in project.get("known_limitations", [])])

        detail_content_html = f"""<div style="border-bottom:1px solid var(--border-subtle); padding-bottom:1.75rem;">
<div class="section-marker">01 // OVERVIEW &amp; 02 // PROBLEM STATEMENT</div>
<h3 style="font-family:var(--font-heading); font-size:1.25rem; color:var(--text-primary); margin-bottom:0.6rem;">Overview &amp; Problem Context</h3>
<p style="color:var(--text-secondary); line-height:1.75; font-size:0.95rem; margin-bottom:1rem;">{project.get('description')}</p>
<pre style="white-space:pre-wrap; background:var(--bg-surface); border:1px solid var(--border-subtle); padding:1rem; border-radius:4px; font-family:var(--font-body); font-size:0.9rem; color:var(--text-secondary); margin:0; line-height:1.65;">{project.get('problem_statement')}</pre>
</div>

<div style="border-bottom:1px solid var(--border-subtle); padding-bottom:1.75rem;">
<div class="section-marker">03 // VERIFIED CAPABILITIES &amp; 04 // EVIDENCE</div>
<h3 style="font-family:var(--font-heading); font-size:1.25rem; color:var(--text-primary); margin-bottom:0.6rem;">Implementation Highlights</h3>
<ul style="color:var(--text-secondary); line-height:1.8; font-size:0.92rem; padding-left:1.25rem; margin-bottom:1rem;">
{features_list}
</ul>
<div style="padding:1rem; background:var(--bg-surface); border:1px solid var(--border); border-radius:4px;">
<div style="font-family:var(--font-mono); font-size:0.72rem; color:var(--accent-secondary); margin-bottom:0.4rem;">VERIFIED CODE EVIDENCE</div>
<ul style="color:var(--text-muted); font-size:0.85rem; line-height:1.6; margin:0; padding-left:1.25rem;">
{evidence_list}
</ul>
</div>
</div>

<div style="border-bottom:1px solid var(--border-subtle); padding-bottom:1.75rem;">
<div class="section-marker">05 // CONSTRAINTS &amp; 06 // KNOWN LIMITATIONS</div>
<h3 style="font-family:var(--font-heading); font-size:1.25rem; color:var(--text-primary); margin-bottom:0.6rem;">System Limitations</h3>
<ul style="color:var(--text-secondary); line-height:1.8; font-size:0.92rem; padding-left:1.25rem; margin:0;">
{limitations_list}
</ul>
</div>

<div style="padding-bottom:1rem;">
<div class="section-marker">07 // SOURCE CODE &amp; DEPLOYMENT</div>
<h3 style="font-family:var(--font-heading); font-size:1.25rem; color:var(--text-primary); margin-bottom:0.75rem;">Repository Access</h3>
<div style="display:flex; align-items:center; gap:1rem; flex-wrap:wrap;">
<a href="{repo_url}" target="_blank" rel="noopener noreferrer" class="btn-primary">
View Source on GitHub ↗
</a>
{demo_btn_html}
</div>
</div>"""

    header_html = f"""<div style="padding: 1rem 0 2rem;">
<a href="?tab=projects" target="_self" class="nav-item" style="display:inline-block; margin-bottom:1.25rem;">
← Back to Project Explorer
</a>

<div style="border-bottom: 1px solid var(--border); padding-bottom: 1.5rem; margin-bottom: 2rem;">
<div style="display:flex; align-items:center; gap:0.5rem; margin-bottom:0.75rem; flex-wrap:wrap;">
{category_pills}
<span class="project-status-tag" style="margin-left:auto;">{status} • Updated {last_updated}</span>
</div>
<h1 class="section-title" style="font-size:2.2rem; margin-bottom:0.75rem;">{name}</h1>
<p class="section-subtitle" style="font-size:1.05rem;">{project.get('description')}</p>
<div style="margin-bottom:1.5rem;">
{tech_pills}
</div>
<div style="display:flex; align-items:center; gap:1rem; flex-wrap:wrap;">
<a href="{repo_url}" target="_blank" rel="noopener noreferrer" class="btn-primary">
View Source Code on GitHub ↗
</a>
{demo_btn_html}
</div>
</div>

<div style="display:flex; flex-direction:column; gap:2.5rem; max-width:880px;">
{detail_content_html}
</div>
</div>"""

    render_html(header_html)
    render_footer()
