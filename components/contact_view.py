"""
contact_view.py
Renders the Contact & Communication page.
Features verified direct communication links (GitHub, LinkedIn, Email via mailto protocol).
Includes honest resume status (official resume available on request).
"""

import streamlit as st
from services.data_service import get_profile
from components.footer import render_footer


def render_contact() -> None:
    """Renders the contact page with verified communication channels."""
    profile = get_profile()
    github_url = profile.get("github_url", "https://github.com/XestalNitish")
    linkedin_url = profile.get("linkedin_url", "https://www.linkedin.com/in/nitish-kumar-33714642b/")
    email = profile.get("email", "nitishkumar.xestal@gmail.com")

    contact_html = f"""
    <div style="padding: 1rem 0 1.5rem; border-bottom: 1px solid var(--border);">
      <div class="section-marker">// CONNECT &amp; CONTACT</div>
      <h1 class="section-title">Direct Communication Channels</h1>
      <p class="section-subtitle">
        I am actively interviewing for AI engineering internships and entry-level positions.
        Feel free to reach out directly through any of the channels below.
      </p>
    </div>

    <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(320px, 1fr)); gap:1.5rem; margin-top:2rem;">

      <!-- Channel 1: Email -->
      <div class="featured-project-card" style="margin:0;">
        <div style="font-family:var(--font-mono); font-size:0.75rem; color:var(--accent); margin-bottom:0.5rem;">DIRECT EMAIL</div>
        <h3 style="font-family:var(--font-heading); font-size:1.2rem; color:var(--text-primary); margin-bottom:0.5rem;">
          {email}
        </h3>
        <p style="font-size:0.88rem; color:var(--text-secondary); line-height:1.6; margin-bottom:1.25rem;">
          Fastest channel for technical recruiters, hiring managers, and internship inquiries.
        </p>
        <a href="mailto:{email}?subject=AI%20Engineering%20Inquiry%20-%20X-ESTAL%20Nitish" class="btn-primary">
          Open Email Client ✉️
        </a>
      </div>

      <!-- Channel 2: LinkedIn -->
      <div class="featured-project-card" style="margin:0;">
        <div style="font-family:var(--font-mono); font-size:0.75rem; color:var(--accent); margin-bottom:0.5rem;">PROFESSIONAL NETWORK</div>
        <h3 style="font-family:var(--font-heading); font-size:1.2rem; color:var(--text-primary); margin-bottom:0.5rem;">
          LinkedIn Profile
        </h3>
        <p style="font-size:0.88rem; color:var(--text-secondary); line-height:1.6; margin-bottom:1.25rem;">
          Connect for professional updates, project discussions, and direct messaging.
        </p>
        <a href="{linkedin_url}" target="_blank" rel="noopener noreferrer" class="btn-secondary">
          Visit LinkedIn Profile ↗
        </a>
      </div>

      <!-- Channel 3: GitHub -->
      <div class="featured-project-card" style="margin:0;">
        <div style="font-family:var(--font-mono); font-size:0.75rem; color:var(--accent); margin-bottom:0.5rem;">OPEN SOURCE CODEBASE</div>
        <h3 style="font-family:var(--font-heading); font-size:1.2rem; color:var(--text-primary); margin-bottom:0.5rem;">
          GitHub (@XestalNitish)
        </h3>
        <p style="font-size:0.88rem; color:var(--text-secondary); line-height:1.6; margin-bottom:1.25rem;">
          Inspect commit logs, issue discussions, and repository source code.
        </p>
        <a href="{github_url}" target="_blank" rel="noopener noreferrer" class="btn-secondary">
          Inspect Repositories ↗
        </a>
      </div>

      <!-- Channel 4: Resume Status -->
      <div class="featured-project-card" style="margin:0; border-color:var(--border-focus);">
        <div style="font-family:var(--font-mono); font-size:0.75rem; color:var(--accent-secondary); margin-bottom:0.5rem;">CURRICULUM VITAE</div>
        <h3 style="font-family:var(--font-heading); font-size:1.2rem; color:var(--text-primary); margin-bottom:0.5rem;">
          Engineering Resume
        </h3>
        <p style="font-size:0.88rem; color:var(--text-secondary); line-height:1.6; margin-bottom:1.25rem;">
          Official ATS-formatted engineering resume tailored for AI engineering and LLM roles.
          Available immediately on request.
        </p>
        <a href="mailto:{email}?subject=Resume%20Request%20-%20Nitish%20Kumar%20(X-ESTAL)" class="btn-secondary">
          Request Resume via Email ↗
        </a>
      </div>

    </div>
    """
    st.markdown(contact_html, unsafe_allow_html=True)
    render_footer()
