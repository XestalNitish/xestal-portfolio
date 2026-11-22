"""
case_studies_view.py
Renders the Engineering Case Studies section.
Presents evidence-based technical articles explaining real debugging workflows,
empirical benchmark evaluations, failure attributions, and known limitations.
"""

import streamlit as st
from services.data_service import get_case_studies
from components.footer import render_footer


def render_case_studies() -> None:
    """Renders the detailed technical case studies."""
    studies = get_case_studies()

    header_html = """
    <div style="padding: 1rem 0 1.5rem; border-bottom: 1px solid var(--border);">
      <div class="section-marker">// ENGINEERING CASE STUDIES</div>
      <h1 class="section-title">Deep Technical Investigations &amp; Benchmarks</h1>
      <p class="section-subtitle">
        Empirical case studies detailing system failures, root-cause investigations,
        deterministic architectural solutions, and honest failure attributions.
      </p>
    </div>
    """
    st.markdown(header_html, unsafe_allow_html=True)

    for study in studies:
        metrics_block = ""
        if "benchmark_metrics" in study:
            m = study["benchmark_metrics"]
            metrics_block = f"""
            <div style="background:var(--bg-main); border:1px solid var(--border); border-radius:4px; padding:1.25rem; margin:1.25rem 0;">
              <div style="font-family:var(--font-mono); font-size:0.75rem; color:var(--accent-secondary); margin-bottom:0.75rem;">
                EMPIRICAL BENCHMARK SCORECARD (arXiv:2610.30074v1)
              </div>
              <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:1rem; margin-bottom:1rem;">
                <div>
                  <div style="font-size:0.75rem; color:var(--text-muted); font-family:var(--font-mono);">RETRIEVAL HIT RATE</div>
                  <div style="font-size:1.3rem; font-weight:700; color:#10B981; font-family:var(--font-mono);">{m.get('retrieval_hit_rate')}</div>
                  <div style="font-size:0.72rem; color:var(--text-muted);">Evidence chunk in top-k</div>
                </div>
                <div>
                  <div style="font-size:0.75rem; color:var(--text-muted); font-family:var(--font-mono);">OUT-OF-SCOPE REFUSAL</div>
                  <div style="font-size:1.3rem; font-weight:700; color:var(--accent); font-family:var(--font-mono);">{m.get('out_of_scope_handled')}</div>
                  <div style="font-size:0.72rem; color:var(--text-muted);">5/5 in this evaluation set</div>
                </div>
                <div>
                  <div style="font-size:0.75rem; color:var(--text-muted); font-family:var(--font-mono);">FAILURE CAUSES (30 ERRORS)</div>
                  <div style="font-size:1.1rem; font-weight:700; color:var(--accent-secondary); font-family:var(--font-mono);">28 Gen / 2 Retrieval</div>
                  <div style="font-size:0.72rem; color:var(--text-muted);">93.3% model reasoning limit</div>
                </div>
                <div>
                  <div style="font-size:0.75rem; color:var(--text-muted); font-family:var(--font-mono);">OVERALL PASS RATE</div>
                  <div style="font-size:1.3rem; font-weight:700; color:var(--text-primary); font-family:var(--font-mono);">{m.get('overall_pass')}</div>
                  <div style="font-size:0.72rem; color:var(--text-muted);">Keyword match evaluated</div>
                </div>
              </div>
              <div style="font-size:0.8rem; color:var(--text-muted); border-top:1px solid var(--border-subtle); padding-top:0.75rem; line-height:1.5;">
                <strong>Accuracy by Question Type:</strong> Concept: 58.3% • Factoid: 66.7% • Reasoning: 66.7% • Formula: 33.3% • Numeric: 15.8% • Table: 0.0%
              </div>
            </div>
            """

        study_html = f"""
        <div class="featured-project-card" style="margin-top:2rem; margin-bottom:2rem;">
          <div style="display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:0.5rem; margin-bottom:0.75rem;">
            <span class="category-pill">{study.get('category')}</span>
            <span style="font-family:var(--font-mono); font-size:0.75rem; color:var(--text-muted);">{study.get('date')} • {study.get('read_time')}</span>
          </div>

          <h2 style="font-family:var(--font-heading); font-size:1.45rem; color:var(--text-primary); margin-bottom:0.5rem;">
            {study.get('title')}
          </h2>
          <p style="color:var(--text-secondary); font-size:0.95rem; line-height:1.6; margin-bottom:1.5rem;">
            {study.get('subtitle')}
          </p>

          <div style="display:flex; flex-direction:column; gap:1.25rem; font-size:0.92rem; line-height:1.7; color:var(--text-secondary);">
            <div>
              <strong style="color:var(--text-primary); font-family:var(--font-mono); font-size:0.8rem; text-transform:uppercase; letter-spacing:0.05em;">
                Problem &amp; Motivation:
              </strong>
              <p style="margin-top:0.35rem; margin-bottom:0;">{study.get('problem')}</p>
            </div>

            <div>
              <strong style="color:var(--text-primary); font-family:var(--font-mono); font-size:0.8rem; text-transform:uppercase; letter-spacing:0.05em;">
                Investigation &amp; Methodology:
              </strong>
              <p style="margin-top:0.35rem; margin-bottom:0;">{study.get('investigation')}</p>
            </div>

            {metrics_block}

            <div>
              <strong style="color:var(--text-primary); font-family:var(--font-mono); font-size:0.8rem; text-transform:uppercase; letter-spacing:0.05em;">
                Engineering Solution:
              </strong>
              <pre style="white-space:pre-wrap; background:var(--bg-surface); border:1px solid var(--border-subtle); padding:1rem; border-radius:4px; font-family:var(--font-body); font-size:0.9rem; color:var(--text-secondary); margin-top:0.35rem; margin-bottom:0; line-height:1.6;">{study.get('solution_implemented')}</pre>
            </div>

            <div style="background:rgba(214, 166, 93, 0.05); border:1px solid rgba(214, 166, 93, 0.2); border-radius:4px; padding:1rem;">
              <strong style="color:var(--accent-secondary); font-family:var(--font-mono); font-size:0.75rem; text-transform:uppercase; letter-spacing:0.08em;">
                Evaluation Scope &amp; Rigorous Caveats:
              </strong>
              <p style="margin-top:0.35rem; margin-bottom:0; font-size:0.88rem; color:var(--text-secondary); line-height:1.6;">
                {study.get('evaluation_limitations')}
              </p>
            </div>
          </div>
        </div>
        """
        st.markdown(study_html, unsafe_allow_html=True)

    render_footer()
