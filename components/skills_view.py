"""
skills_view.py
Renders the evidence-based Technical Skills section.
Organized into clear engineering tiers with honest classification:
- Used in projects
- Currently learning
- Explored
Zero fake percentages, zero animated skill bars.
"""

from components.footer import render_footer
from components.utils import render_html


def render_skills() -> None:
    """Renders the evidence-based technical skills inventory."""
    skills_data = [
        {
            "category": "Agentic AI & Orchestration",
            "description": "Designing stateful multi-agent systems, dependency contracts, and self-healing execution loops.",
            "skills": [
                {"name": "LangGraph", "level": "Used in projects", "evidence": "Orchestrated 10-node StateGraph in ultimate-coding-agent & WebSearchState in research-agent"},
                {"name": "Multi-Agent Systems", "level": "Used in projects", "evidence": "Specialist sub-agent delegation (code dev, researcher, database analyst)"},
                {"name": "Tool Calling & Dispatch", "level": "Used in projects", "evidence": "Custom @tool implementations with typed schemas and safety checks"},
                {"name": "State Management", "level": "Used in projects", "evidence": "TypedDict state persistence, checkpointing, and cycle dampening"},
                {"name": "Deterministic Auto-Heal", "level": "Used in projects", "evidence": "AST-based syntax, import, and module repairs without LLM re-prompting"},
                {"name": "GraphRAG & Entity Graphs", "level": "Currently learning", "evidence": "Investigating knowledge graph extraction for cross-document memory"}
            ]
        },
        {
            "category": "RAG & LLM Engineering",
            "description": "Constructing hybrid retrieval pipelines, grounding contexts, and isolating failure modes.",
            "skills": [
                {"name": "Hybrid Retrieval (BM25 + Vector)", "level": "Used in projects", "evidence": "EnsembleRetriever combining Rank-BM25 and Chroma MMR (95.8% retrieval hit rate)"},
                {"name": "Vector Databases (ChromaDB)", "level": "Used in projects", "evidence": "Workspace-isolated persistent collections with BAAI/bge-small-en-v1.5"},
                {"name": "Context Grounding & Refusal", "level": "Used in projects", "evidence": "Deterministic no_answer node handling 5/5 out-of-scope benchmark questions"},
                {"name": "Empirical Benchmarking", "level": "Used in projects", "evidence": "53-question evaluation harness isolating retrieval hits from generation errors"},
                {"name": "Prompt Engineering & Structured Outputs", "level": "Used in projects", "evidence": "Strict JSON schema enforcement, token budget management, system personas"},
                {"name": "Reranking (FlashRank)", "level": "Explored", "evidence": "Evaluated cross-encoder reranking for dense passage reordering"}
            ]
        },
        {
            "category": "Local Inference & Hardware Optimization",
            "description": "Deploying quantized models locally with zero external cloud dependencies.",
            "skills": [
                {"name": "llama.cpp & GGUF Quantization", "level": "Used in projects", "evidence": "Local 4B GGUF model execution on CPU with Flash Attention"},
                {"name": "llama-server Integration", "level": "Used in projects", "evidence": "Dual local model serving on port 8082 with automated health checks"},
                {"name": "Cloud Fallback Routing", "level": "Used in projects", "evidence": "Automated failover from local models to Groq / Gemini on quota or task limits"},
                {"name": "Model Distillation & LoRA", "level": "Currently learning", "evidence": "Studying parameter-efficient fine-tuning on domain-specific coding corpora"}
            ]
        },
        {
            "category": "Programming & System Defense",
            "description": "Core software engineering, static code analysis, and execution sandboxing.",
            "skills": [
                {"name": "Python 3.10+ (Advanced)", "level": "Used in projects", "evidence": "Primary language across all 10 repositories (async, typing, regex, OOP)"},
                {"name": "AST (Abstract Syntax Tree) Parsing", "level": "Used in projects", "evidence": "Static code inspections, topological sorting, syntax auto-repair"},
                {"name": "SSRF & Environment Defense", "level": "Used in projects", "evidence": "tools/_safe.py host checking, safe path jails, secret variable scrubbing"},
                {"name": "SQL & Relational Schemas", "level": "Used in projects", "evidence": "SQLite database operations and relational modeling in library system"},
                {"name": "HTML5, CSS3 & JavaScript", "level": "Used in projects", "evidence": "Custom editorial web interfaces, SVG architecture sketches, responsive UI"}
            ]
        },
        {
            "category": "Machine Learning & Computer Vision",
            "description": "Classical and deep neural network modeling for computer vision and time-series.",
            "skills": [
                {"name": "Convolutional Neural Networks (CNN)", "level": "Used in projects", "evidence": "Brain Tumor Classifier (MRI 4-class categorization with Keras/TensorFlow)"},
                {"name": "LSTM Recurrent Networks", "level": "Used in projects", "evidence": "Bitcoin Price Predictor (time-series sequential pattern recognition)"},
                {"name": "Scikit-Learn & Classical ML", "level": "Used in projects", "evidence": "Heart stroke risk modeling, data normalization, class balancing"},
                {"name": "PyTorch Fundamentals", "level": "Explored", "evidence": "Model architecture experimentation and tensor operations"}
            ]
        },
        {
            "category": "Development & Observability",
            "description": "Tooling, version control, and production telemetry.",
            "skills": [
                {"name": "Git & GitHub", "level": "Used in projects", "evidence": "10 public repositories, branching, multi-commit history"},
                {"name": "Streamlit Framework", "level": "Used in projects", "evidence": "Multiple deployed cloud applications with custom styling and state routing"},
                {"name": "LangSmith Telemetry", "level": "Used in projects", "evidence": "Live execution tracing under project 'ultimate-coding-agent'"},
                {"name": "Docker & Containerization", "level": "Used in projects", "evidence": "Dockerfile packaging in invoice-processing-agent"}
            ]
        }
    ]

    header_html = """<div style="padding: 1rem 0 1.5rem; border-bottom: 1px solid var(--border);">
<div class="section-marker">// TECHNICAL SKILLS</div>
<h1 class="section-title">Evidence-Based Engineering Competencies</h1>
<p class="section-subtitle">
Every skill listed below is backed by concrete implementations in public repositories,
classified honestly by practical project depth.
</p>
<div style="display:flex; align-items:center; gap:1rem; margin-top:1rem; flex-wrap:wrap; font-family:var(--font-mono); font-size:0.75rem;">
<span style="display:inline-flex; align-items:center; gap:0.35rem; color:#10B981;">
<span style="width:6px; height:6px; border-radius:50%; background:#10B981;"></span>
Used in projects
</span>
<span style="display:inline-flex; align-items:center; gap:0.35rem; color:var(--accent);">
<span style="width:6px; height:6px; border-radius:50%; background:var(--accent);"></span>
Currently learning
</span>
<span style="display:inline-flex; align-items:center; gap:0.35rem; color:var(--text-muted);">
<span style="width:6px; height:6px; border-radius:50%; background:var(--text-muted);"></span>
Explored
</span>
</div>
</div>"""
    render_html(header_html)

    for cat in skills_data:
        items_html = ""
        for s in cat["skills"]:
            badge_color = "#10B981" if s["level"] == "Used in projects" else (
                "var(--accent)" if s["level"] == "Currently learning" else "var(--text-muted)"
            )
            badge_bg = "rgba(16, 185, 129, 0.08)" if s["level"] == "Used in projects" else (
                "rgba(109, 145, 255, 0.08)" if s["level"] == "Currently learning" else "rgba(115, 125, 141, 0.08)"
            )

            items_html += f"""<div style="background:var(--bg-main); border:1px solid var(--border); border-radius:4px; padding:1rem;">
<div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:0.4rem;">
<span style="font-family:var(--font-mono); font-size:0.85rem; font-weight:600; color:var(--text-primary);">{s['name']}</span>
<span style="font-family:var(--font-mono); font-size:0.68rem; color:{badge_color}; background:{badge_bg}; padding:0.15rem 0.4rem; border-radius:2px;">
{s['level']}
</span>
</div>
<p style="font-size:0.82rem; color:var(--text-secondary); margin:0; line-height:1.5;">
{s['evidence']}
</p>
</div>"""

        cat_html = f"""<div class="featured-project-card" style="margin-top:1.75rem; margin-bottom:1.75rem;">
<h2 style="font-family:var(--font-heading); font-size:1.25rem; color:var(--text-primary); margin-bottom:0.35rem;">
{cat['category']}
</h2>
<p style="font-size:0.88rem; color:var(--text-secondary); margin-bottom:1.25rem;">
{cat['description']}
</p>
<div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:0.85rem;">
{items_html}
</div>
</div>"""
        render_html(cat_html)

    render_footer()
