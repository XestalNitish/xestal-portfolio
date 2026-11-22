"""
hero.py
Renders the two-column editorial hero section.
Left column: Editorial headline, professional identity, candid description, actions.
Right column: Handcrafted SVG technical architecture sketch illustrating an autonomous agent workflow.
"""

import streamlit as st


def render_hero() -> None:
    """Renders the editorial hero section."""
    svg_workflow = """
    <svg viewBox="0 0 460 380" fill="none" xmlns="http://www.w3.org/2000/svg" style="width:100%; height:auto;">
      <defs>
        <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#6D91FF" />
        </marker>
        <marker id="arrow-amber" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#D6A65D" />
        </marker>
        <pattern id="grid" width="20" height="20" patternUnits="userSpaceOnUse">
          <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#171C26" stroke-width="0.75"/>
        </pattern>
      </defs>

      <!-- Background Grid -->
      <rect width="460" height="380" fill="url(#grid)" rx="6" />

      <!-- Node 1: Task Objective -->
      <rect x="30" y="24" width="180" height="42" rx="4" fill="#11151D" stroke="#252C38" stroke-width="1.2"/>
      <text x="42" y="42" font-family="'JetBrains Mono', monospace" font-size="10" fill="#6D91FF" font-weight="600">01 // TASK OBJECTIVE</text>
      <text x="42" y="56" font-family="'Inter', sans-serif" font-size="11" fill="#F0F1F3">User Goal &amp; System State</text>

      <!-- Arrow 1 -> 2 -->
      <path d="M 120 66 L 120 90" stroke="#6D91FF" stroke-width="1.5" marker-end="url(#arrow)" />

      <!-- Node 2: State Planning -->
      <rect x="30" y="94" width="180" height="42" rx="4" fill="#11151D" stroke="#252C38" stroke-width="1.2"/>
      <text x="42" y="112" font-family="'JetBrains Mono', monospace" font-size="10" fill="#6D91FF" font-weight="600">02 // STATE PLANNING</text>
      <text x="42" y="126" font-family="'Inter', sans-serif" font-size="11" fill="#F0F1F3">LangGraph Graph Routing</text>

      <!-- Branch to Tools (Right) -->
      <path d="M 210 115 L 260 115" stroke="#6D91FF" stroke-width="1.5" marker-end="url(#arrow)" />

      <!-- Node 3: Tool Dispatch -->
      <rect x="264" y="94" width="166" height="42" rx="4" fill="#171C26" stroke="#252C38" stroke-width="1.2"/>
      <text x="276" y="112" font-family="'JetBrains Mono', monospace" font-size="10" fill="#D6A65D" font-weight="600">03 // TOOL DISPATCH</text>
      <text x="276" y="126" font-family="'Inter', sans-serif" font-size="11" fill="#A1A8B3">AST &amp; Safety Verification</text>

      <!-- Arrow 2 -> 4 -->
      <path d="M 120 136 L 120 166" stroke="#6D91FF" stroke-width="1.5" marker-end="url(#arrow)" />

      <!-- Node 4: Hybrid Retrieval -->
      <rect x="30" y="170" width="180" height="46" rx="4" fill="#11151D" stroke="#252C38" stroke-width="1.2"/>
      <text x="42" y="188" font-family="'JetBrains Mono', monospace" font-size="10" fill="#6D91FF" font-weight="600">04 // HYBRID RETRIEVAL</text>
      <text x="42" y="202" font-family="'Inter', sans-serif" font-size="11" fill="#F0F1F3">BM25 + Chroma Vector MMR</text>

      <!-- Arrow from Tools down to Node 5 -->
      <path d="M 347 136 L 347 240" stroke="#6D91FF" stroke-width="1.5" stroke-dasharray="3 3"/>

      <!-- Arrow 4 -> 5 -->
      <path d="M 120 216 L 120 242" stroke="#6D91FF" stroke-width="1.5" marker-end="url(#arrow)" />

      <!-- Node 5: Sandboxed Execution -->
      <rect x="30" y="246" width="380" height="44" rx="4" fill="#11151D" stroke="#252C38" stroke-width="1.2"/>
      <text x="42" y="264" font-family="'JetBrains Mono', monospace" font-size="10" fill="#10B981" font-weight="600">05 // CONTROLLED EXECUTION</text>
      <text x="42" y="278" font-family="'Inter', sans-serif" font-size="11" fill="#F0F1F3">Isolated Subprocess • Scrubbed Env Variables • POSIX Limits</text>

      <!-- Arrow 5 -> 6 -->
      <path d="M 220 290 L 220 312" stroke="#6D91FF" stroke-width="1.5" marker-end="url(#arrow)" />

      <!-- Node 6: Verification & Auto-Heal -->
      <rect x="30" y="316" width="380" height="44" rx="4" fill="#171C26" stroke="#3B475C" stroke-width="1.2"/>
      <text x="42" y="334" font-family="'JetBrains Mono', monospace" font-size="10" fill="#D6A65D" font-weight="600">06 // EVALUATION &amp; AUTO-HEAL</text>
      <text x="42" y="348" font-family="'Inter', sans-serif" font-size="11" fill="#A1A8B3">Deterministic AST Fix or Re-plan if Test Assertions Fail</text>

      <!-- Feedback Loop: Arrow from Node 6 back up to Planning -->
      <path d="M 410 338 L 436 338 L 436 115 L 214 115" stroke="#D6A65D" stroke-width="1.2" stroke-dasharray="4 4" fill="none" marker-end="url(#arrow-amber)" />
      <text x="360" y="228" font-family="'JetBrains Mono', monospace" font-size="9" fill="#D6A65D" transform="rotate(90 360 228)">REPAIR LOOP</text>
    </svg>
    """

    hero_html = f"""
    <div class="hero-grid">
      <div>
        <div class="status-pill">
          <span class="status-dot"></span>
          <span>Open to AI Engineer Internships &amp; Junior Roles</span>
        </div>
        <div class="hero-tag">INDEPENDENT AI ENGINEERING PORTFOLIO</div>
        <h1 class="hero-heading">Building intelligent systems with code, reasoning, and experimentation.</h1>
        <p class="hero-description">
          I'm Nitish Kumar, focused on building AI-powered applications, agentic workflows,
          retrieval systems, and intelligent developer tools.
        </p>
        <div class="hero-identity-row">
          <span class="hero-identity-badge">AI Engineering</span>
          <span>•</span>
          <span class="hero-identity-badge">Agentic AI</span>
          <span>•</span>
          <span class="hero-identity-badge">LLM Systems</span>
        </div>
        <div class="hero-actions">
          <a href="?tab=projects" target="_self" class="btn-primary">
            Explore Projects →
          </a>
          <a href="https://github.com/XestalNitish" target="_blank" rel="noopener noreferrer" class="btn-secondary">
            GitHub Profile ↗
          </a>
        </div>
      </div>
      <div>
        <div class="workflow-card">
          <div class="workflow-card-header">
            <span class="workflow-card-title">Conceptual Architecture</span>
            <span class="workflow-card-label">StateGraph Flow</span>
          </div>
          <div class="workflow-svg-container">
            {svg_workflow}
          </div>
        </div>
      </div>
    </div>
    """
    st.markdown(hero_html, unsafe_allow_html=True)
