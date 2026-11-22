"""
home_view.py
Renders the complete editorial Homepage for X-ESTAL Nitish.
Includes Hero, Candid About introduction, Curated Flagship Projects showcase,
6 Engineering Principles, Current Focus, and Footer.
"""

from components.hero import render_hero
from components.footer import render_footer
from components.utils import render_html
from services.data_service import get_flagship_projects


def render_about_intro() -> None:
    """Renders the concise, honest editorial about introduction."""
    about_html = """<div style="padding: 2.5rem 0 2rem; border-bottom: 1px solid var(--border);">
<div class="section-marker">// 01. BACKGROUND &amp; APPROACH</div>
<h2 class="section-title">Engineering practical AI systems beyond standard API wrappers.</h2>
<div style="max-width: 820px; color: var(--text-secondary); font-size: 0.96rem; line-height: 1.75;">
<p style="margin-bottom: 1rem;">
I am an independent developer preparing for my first professional AI engineering role.
Rather than focusing solely on prompting cloud APIs, I spend my time building system architectures:
stateful agent workflows with LangGraph, hybrid retrieval pipelines with Chroma and BM25,
and offline inference with local GGUF models.
</p>
<p style="margin-bottom: 0;">
My engineering approach prioritizes empirical measurement over assumptions. When a multi-agent system
breaks or a RAG engine returns incorrect context, I investigate the exact failure layer — isolating
whether an error stems from retrieval hit failure, small-model reasoning capacity, or syntax generation —
and introduce deterministic guardrails (such as AST parsing and SSRF IP validation) to prevent recurrence.
</p>
</div>
</div>"""
    render_html(about_html)


def render_featured_flagships() -> None:
    """Renders the 3 curated flagship projects with editorial presentation."""
    flagships = get_flagship_projects()

    header_html = """<div style="padding: 2.5rem 0 1rem;">
<div class="section-marker">// 02. FLAGSHIP PROJECTS</div>
<h2 class="section-title">Verified systems with source code and empirical evidence.</h2>
<p class="section-subtitle">
Three distinct architectures addressing multi-file code generation, hybrid enterprise retrieval,
and autonomous deep-web research.
</p>
</div>"""
    render_html(header_html)

    for proj in flagships:
        categories_html = "".join([f'<span class="category-pill">{cat}</span>' for cat in proj.get("category", [])])
        tech_html = "".join([f'<span class="tech-tag">{t}</span>' for t in proj.get("tech_stack", [])])
        features_list_html = "".join([f'<li>{f}</li>' for f in proj.get("actual_features", [])[:4]])

        demo_link_html = ""
        if proj.get("live_demo_url"):
            demo_link_html = f'<a href="{proj["live_demo_url"]}" target="_blank" rel="noopener noreferrer" class="project-link demo">Launch Live App ↗</a>'

        card_html = f"""<div class="featured-project-card">
<div class="featured-project-meta-row">
<div class="project-category-pills">
{categories_html}
</div>
<span class="project-status-tag">{proj.get('status')} • {proj.get('last_updated')}</span>
</div>

<h3 class="featured-project-title">{proj.get('name')}</h3>
<p class="featured-project-desc">{proj.get('description')}</p>

<div class="project-architecture-block">
<div class="architecture-block-label">Verified Engineering Capabilities</div>
<ul class="architecture-feature-list">
{features_list_html}
</ul>
</div>

<div class="project-tech-row">
{tech_html}
</div>

<div class="project-links-row">
<a href="{proj.get('repo_url')}" target="_blank" rel="noopener noreferrer" class="project-link">
View Repository ↗
</a>
{demo_link_html}
<a href="?tab=project_detail&id={proj.get('id')}" target="_self" class="project-link" style="margin-left: auto;">
Full Architecture Detail →
</a>
</div>
</div>"""
        render_html(card_html)


def render_engineering_principles() -> None:
    """Renders the 6 core engineering principles."""
    principles = [
        {
            "num": "01 // ROOT CAUSE",
            "title": "Understand failure before adding complexity",
            "desc": "Before introducing larger context windows or more agents, isolate the exact failure layer: retrieval miss, syntax generation, or reasoning limitation."
        },
        {
            "num": "02 // EMPIRICAL RIGOR",
            "title": "Measure retrieval quality rather than guessing",
            "desc": "Benchmark systems with test datasets (like our 53-question evaluation). Know your exact retrieval hit rate versus downstream generation limits."
        },
        {
            "num": "03 // EXPLICIT STATE",
            "title": "Design agents around explicit state and transitions",
            "desc": "Use structured StateGraphs with typed schemas and cycle dampeners. Avoid unbounded autonomous loops that degrade into unpredictable execution."
        },
        {
            "num": "04 // DEFENSIVE BOUNDARIES",
            "title": "Keep tool execution strictly controlled",
            "desc": "Scrub sensitive environment variables before subprocess runs, enforce POSIX limits, and use AST analysis to validate code before executing."
        },
        {
            "num": "05 // TELEMETRY",
            "title": "Prefer observable workflows",
            "desc": "Integrate production tracing (such as LangSmith) to inspect prompt budgets, node transitions, token usage, and latency bottlenecks."
        },
        {
            "num": "06 // INTELLECTUAL HONESTY",
            "title": "Document limitations honestly",
            "desc": "Never present a test dataset score as a universal guarantee. State known failure modes, hardware boundaries, and ongoing challenges openly."
        }
    ]

    boxes_html = ""
    for p in principles:
        boxes_html += f"""<div class="principle-box">
<div class="principle-num">{p['num']}</div>
<div class="principle-title">{p['title']}</div>
<div class="principle-desc">{p['desc']}</div>
</div>"""

    principles_html = f"""<div style="padding: 2.5rem 0 2rem; border-top: 1px solid var(--border);">
<div class="section-marker">// 03. ENGINEERING PRINCIPLES</div>
<h2 class="section-title">Core principles guiding system design.</h2>
<p class="section-subtitle">
Practical standards developed through hands-on project implementation and error analysis.
</p>
<div class="principles-grid">
{boxes_html}
</div>
</div>"""
    render_html(principles_html)


def render_current_focus() -> None:
    """Renders the current engineering focus and research roadmap."""
    focus_items = [
        {
            "label": "EVALUATION HARNESSES",
            "text": "Developing automated deterministic assertion pipelines to benchmark agentic workflows against multi-step regression suites."
        },
        {
            "label": "RETRIEVAL QUALITY",
            "text": "Experimenting with GraphRAG entity extraction and reciprocal rank fusion to improve complex cross-document reasoning."
        },
        {
            "label": "RELIABLE TOOL EXECUTION",
            "text": "Strengthening AST static parsers and containerized sandboxes to safely execute autonomous multi-file refactoring."
        },
        {
            "label": "LOCAL MODEL DEPLOYMENT",
            "text": "Optimizing GGUF quantization parameters and context memory on consumer hardware using llama.cpp and Flash Attention."
        }
    ]

    items_html = ""
    for item in focus_items:
        items_html += f"""<div class="focus-item">
<div class="focus-item-label">{item['label']}</div>
<div class="focus-item-text">{item['text']}</div>
</div>"""

    focus_html = f"""<div style="padding: 1rem 0 2.5rem; border-top: 1px solid var(--border);">
<div class="section-marker">// 04. CURRENT FOCUS</div>
<h2 class="section-title">Active engineering investigations.</h2>
<p class="section-subtitle">
Ongoing research and practical implementation areas I am actively exploring.
</p>
<div class="focus-card">
<div class="focus-list">
{items_html}
</div>
</div>
</div>"""
    render_html(focus_html)


def render_homepage() -> None:
    """Renders the complete homepage view."""
    render_hero()
    render_about_intro()
    render_featured_flagships()
    render_engineering_principles()
    render_current_focus()
    render_footer()
