"""
about_view.py
Renders the candid personal About page for Nitish Kumar (X-ESTAL Nitish).
Preserves first-person voice, personal engineering journey, project insights,
engineering principles, and career objectives without generic marketing language.
"""

from components.footer import render_footer
from components.utils import render_html


def render_about() -> None:
    """Renders the authentic personal about page."""
    about_html = """<div style="padding: 1rem 0 1.5rem; border-bottom: 1px solid var(--border);">
<div class="section-marker">// ABOUT &amp; BACKGROUND</div>
<h1 class="section-title">Nitish Kumar (X-ESTAL Nitish)</h1>
<p class="section-subtitle">
Independent developer focusing on AI engineering, agentic workflows, retrieval systems, and intelligent tools.
</p>
</div>

<div style="max-width: 860px; margin-top: 2rem; display:flex; flex-direction:column; gap: 2.25rem; font-size: 0.98rem; line-height: 1.8; color: var(--text-secondary);">

<div>
<h2 style="font-family:var(--font-heading); font-size:1.35rem; color:var(--text-primary); margin-bottom:0.75rem; letter-spacing:-0.01em;">
Who I Am
</h2>
<p style="margin-bottom: 1rem;">
I'm Nitish Kumar, an aspiring AI Engineer from India, building and experimenting with AI-powered software under the name <strong>X-ESTAL Nitish</strong>.
</p>
<p style="margin-bottom: 1rem;">
I'm at the beginning of my professional journey and currently looking for opportunities where I can contribute, learn from experienced engineers, and work on real engineering problems.
</p>
<p style="margin-bottom: 1rem;">
Most of what I've learned has come from building things myself. I've spent time writing Python applications, experimenting with machine learning models, working with LLMs, and figuring out what happens when software doesn't behave as expected.
</p>
<p style="margin-bottom: 0;">
I enjoy understanding how things work beneath the surface, not just getting a model or application to produce an output.
</p>
</div>

<div style="border-top:1px solid var(--border-subtle); padding-top:2rem;">
<h2 style="font-family:var(--font-heading); font-size:1.35rem; color:var(--text-primary); margin-bottom:0.75rem; letter-spacing:-0.01em;">
How I Got Here
</h2>
<p style="margin-bottom: 1rem;">
My journey started with basic programming and projects like a <em>Library Management System</em>, where I learned Python, database operations, and application logic.
</p>
<p style="margin-bottom: 1rem;">
Later, I explored machine learning through projects such as a <em>Brain Tumor Classifier</em> using CNNs and a <em>Bitcoin Price Predictor</em> using LSTM networks. These projects helped me understand how data, models, and evaluation come together.
</p>
<p style="margin-bottom: 1rem;">
Over time, my interest shifted towards LLMs and Agentic AI. I became curious about a bigger question: how can we build systems that don't just generate responses, but can plan tasks, use tools, manage state, and recover from failures?
</p>
<p style="margin-bottom: 1rem;">
That curiosity led me to LangGraph, hybrid retrieval systems, ChromaDB, BM25, and local model inference using <code>llama.cpp</code>.
</p>
<p style="margin-bottom: 0;">
I've been learning by building, breaking, testing, and improving my own projects.
</p>
</div>

<div style="border-top:1px solid var(--border-subtle); padding-top:2rem;">
<h2 style="font-family:var(--font-heading); font-size:1.35rem; color:var(--text-primary); margin-bottom:0.75rem; letter-spacing:-0.01em;">
What I've Been Building
</h2>
<p style="margin-bottom: 1.25rem;">
A few projects represent the direction I'm exploring:
</p>

<div style="display:flex; flex-direction:column; gap:1.25rem; margin-bottom:1.25rem;">
<div style="background:var(--bg-secondary); border:1px solid var(--border); border-radius:4px; padding:1.25rem;">
<h3 style="font-family:var(--font-heading); font-size:1.15rem; color:var(--text-primary); margin-bottom:0.4rem;">
Ultimate Coding Agent
</h3>
<p style="margin:0; font-size:0.92rem; color:var(--text-secondary); line-height:1.65;">
An autonomous coding assistant built around LangGraph. It includes specialized agents, code generation workflows, AST-based code repair, dependency ordering, and checks around execution and environment variables.
</p>
</div>

<div style="background:var(--bg-secondary); border:1px solid var(--border); border-radius:4px; padding:1.25rem;">
<h3 style="font-family:var(--font-heading); font-size:1.15rem; color:var(--text-primary); margin-bottom:0.4rem;">
X-ESTAL Enterprise Hybrid RAG
</h3>
<p style="margin:0; font-size:0.92rem; color:var(--text-secondary); line-height:1.65;">
A document retrieval and question-answering system combining ChromaDB vector search with BM25. I also built an evaluation suite to understand retrieval performance and identify whether failures came from retrieval or answer generation.
</p>
</div>

<div style="background:var(--bg-secondary); border:1px solid var(--border); border-radius:4px; padding:1.25rem;">
<h3 style="font-family:var(--font-heading); font-size:1.15rem; color:var(--text-primary); margin-bottom:0.4rem;">
Plearun Verified Findings
</h3>
<p style="margin:0; font-size:0.92rem; color:var(--text-secondary); line-height:1.65;">
A deterministic incident-verification pipeline designed to process logs from different systems. It handles mixed text encodings, timestamp normalization, clock differences, and evidence-based verification.
</p>
</div>
</div>

<p style="margin-top:0.75rem; margin-bottom:0;">
These projects have taught me that getting something to work is only one part of engineering. Understanding its limitations and making it more reliable is just as important.
</p>
</div>

<div style="border-top:1px solid var(--border-subtle); padding-top:2rem;">
<h2 style="font-family:var(--font-heading); font-size:1.35rem; color:var(--text-primary); margin-bottom:0.75rem; letter-spacing:-0.01em;">
How I Think About Engineering
</h2>
<p style="margin-bottom: 1rem;">
I don't believe every problem needs a bigger model or another layer of AI.
</p>
<p style="margin-bottom: 1rem;">
Sometimes a simple Python function is more reliable than an LLM call. Sometimes an AST parser can solve a problem that would otherwise require another generation attempt. And sometimes the most important improvement is not adding a feature, but understanding why the existing one failed.
</p>
<p style="margin-bottom: 0.75rem;">
A few principles guide the way I build:
</p>
<ul style="padding-left:1.35rem; line-height:1.8; margin-bottom:1rem;">
<li><strong>Use deterministic code</strong> wherever it makes a system more predictable.</li>
<li><strong>Evaluate retrieval and generation separately</strong> instead of assuming that a good-looking answer is a correct one.</li>
<li><strong>Keep tool execution controlled</strong> and treat credentials and environment variables carefully.</li>
<li><strong>Make failures observable</strong> so they can be understood and improved.</li>
</ul>
<p style="margin-bottom: 0;">
I'm still learning, and I see that as part of becoming a better engineer.
</p>
</div>

<div style="border-top:1px solid var(--border-subtle); padding-top:2rem;">
<h2 style="font-family:var(--font-heading); font-size:1.35rem; color:var(--text-primary); margin-bottom:0.75rem; letter-spacing:-0.01em;">
What I'm Looking For
</h2>
<p style="margin-bottom: 1rem;">
I'm currently exploring opportunities in AI Engineering, Agentic AI, LLM applications, and Python development, particularly internships and entry-level roles.
</p>
<p style="margin-bottom: 1rem;">
I'd like to work with people who build real products, care about engineering quality, and are willing to challenge how things are designed.
</p>
<p style="margin-bottom: 1rem;">
I can bring curiosity, hands-on project experience, a strong interest in Python and AI systems, and the willingness to take responsibility for learning and improving.
</p>
<p style="margin-bottom: 0;">
I'm not presenting myself as an experienced industry engineer. I'm showing what I've built, what I've learned, and the kind of engineer I'm working towards becoming.
</p>
</div>

</div>"""
    render_html(about_html)
    render_footer()
