"""
about_view.py
Renders the candid About page.
Covers technical interests, learning progression, systems approach, and career goals.
Strictly avoids inflated motivational fluff or fabricated employment history.
"""

from components.footer import render_footer
from components.utils import render_html


def render_about() -> None:
    """Renders the honest personal about page."""
    about_html = """<div style="padding: 1rem 0 1.5rem; border-bottom: 1px solid var(--border);">
<div class="section-marker">// ABOUT &amp; BACKGROUND</div>
<h1 class="section-title">Nitish Kumar (X-ESTAL Nitish)</h1>
<p class="section-subtitle">
Independent developer focusing on AI engineering, agentic systems, and retrieval architectures.
</p>
</div>

<div style="max-width: 840px; margin-top: 2rem; display:flex; flex-direction:column; gap: 2rem; font-size: 0.96rem; line-height: 1.8; color: var(--text-secondary);">

<div>
<h3 style="font-family:var(--font-heading); font-size:1.25rem; color:var(--text-primary); margin-bottom:0.6rem;">
Who I Am
</h3>
<p>
I am an aspiring AI Engineer based in India, known across my open-source projects as <strong>X-ESTAL Nitish</strong>.
I am currently conducting my first professional job search, actively seeking <strong>AI Engineer internships</strong>,
<strong>Agentic AI developer roles</strong>, or <strong>entry-level Python AI positions</strong>.
</p>
<p>
I do not come with years of corporate senior titles or imaginary agency credentials. What I do possess is a disciplined,
hands-on commitment to building software from scratch: writing Python systems, testing them under failure conditions,
and measuring their real behavior rather than treating machine learning as magic.
</p>
</div>

<div>
<h3 style="font-family:var(--font-heading); font-size:1.25rem; color:var(--text-primary); margin-bottom:0.6rem;">
Learning Progression &amp; Technical Evolution
</h3>
<p>
My journey in software engineering began with foundational programming logic and relational database operations
(such as my early <em>Library Management System</em>). As I deepened my focus into machine learning, I trained
convolutional neural networks for medical imaging (<em>Brain Tumor Classifier</em>) and recurrent LSTM networks
for quantitative time-series forecasting (<em>Bitcoin Price Predictor</em>).
</p>
<p>
While training classical models provided essential mathematical grounding, I became fascinated by the emerging paradigm
of <strong>Agentic AI and LLM orchestration</strong>. Over the past year, I dedicated myself to engineering stateful
multi-agent systems using LangGraph, building hybrid RAG engines with Chroma and BM25, and running quantized models
locally on CPU using <code>llama.cpp</code>.
</p>
</div>

<div>
<h3 style="font-family:var(--font-heading); font-size:1.25rem; color:var(--text-primary); margin-bottom:0.6rem;">
What I Build &amp; Why It Matters
</h3>
<p>
My projects reflect real architectural challenges encountered when deploying AI:
</p>
<ul style="padding-left:1.25rem; margin-top:0.5rem; line-height:1.75;">
<li>
<strong>Autonomous Multi-Agent Coding:</strong> Built <em>Ultimate Coding Agent</em>, featuring a 10-node StateGraph flow,
deterministic AST syntax repair without LLM re-prompting, topological dependency ordering, and environment secret scrubbing.
</li>
<li>
<strong>Hybrid Retrieval &amp; Benchmarking:</strong> Engineered <em>X-Estal Enterprise Hybrid RAG</em> with an empirical
53-question benchmark suite (arXiv:2610.30074v1) demonstrating a 95.8% retrieval hit rate and zero out-of-scope hallucinations.
</li>
<li>
<strong>Deterministic Incident Auditing:</strong> Developed <em>Plearun Verified Findings</em>, a 5-step forensic verification
pipeline handling mixed encodings (BOM, CP1252, Latin1) and clock drift across heterogeneous machine logs.
</li>
</ul>
</div>

<div>
<h3 style="font-family:var(--font-heading); font-size:1.25rem; color:var(--text-primary); margin-bottom:0.6rem;">
Engineering Approach &amp; Core Philosophy
</h3>
<p>
I believe that the mark of a solid engineer is not how quickly they can generate code, but how thoroughly they understand
why systems fail. In AI engineering, stochastic models must be bounded by deterministic guardrails:
</p>
<ul style="padding-left:1.25rem; margin-top:0.5rem; line-height:1.75;">
<li><strong>Never waste an LLM call</strong> on something a compiler, regex, or AST parser can fix in two milliseconds.</li>
<li><strong>Never assume zero hallucinations</strong> without measuring out-of-scope refusal rates on rigorous test sets.</li>
<li><strong>Never grant uncontrolled tool access</strong> without scrubbing credentials and enforcing subprocess sandboxing.</li>
</ul>
</div>

<div>
<h3 style="font-family:var(--font-heading); font-size:1.25rem; color:var(--text-primary); margin-bottom:0.6rem;">
What I Am Looking For
</h3>
<p>
I am eager to join an engineering team building intelligent applications, autonomous agent workflows, or retrieval systems.
I bring strong Python programming, deep familiarity with the LangGraph/Chroma/llama.cpp ecosystem, rigorous testing habits,
and a relentless drive to learn from senior engineers.
</p>
</div>

</div>"""
    render_html(about_html)
    render_footer()
