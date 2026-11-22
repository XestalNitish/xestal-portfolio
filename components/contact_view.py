"""
contact_view.py
Renders the Contact & Communication page.
Features both verified email addresses (nkumar22573@gmail.com, estalnitish@gmail.com),
verified LinkedIn (nitish-kumar-ai), GitHub (@XestalNitish), and working resume download.
Diagnoses and repairs the two non-functional buttons with dual mailto/webmail dispatch and real PDF download.
"""

from services.data_service import get_profile
from services.resume_service import get_resume_data_url, is_resume_available
from components.footer import render_footer
from components.utils import render_html


def render_contact() -> None:
    """Renders the contact page with verified communication channels and working actions."""
    profile = get_profile()
    github_url = profile.get("github_url", "https://github.com/XestalNitish")
    linkedin_url = profile.get("linkedin_url", "https://www.linkedin.com/in/nitish-kumar-ai")
    primary_email = profile.get("email", "nkumar22573@gmail.com")
    secondary_email = profile.get("email_secondary", "estalnitish@gmail.com")

    # Mailto and webmail URLs
    subject = "AI%20Engineering%20Inquiry%20-%20Nitish%20Kumar%20(X-ESTAL)"
    mailto_primary = f"mailto:{primary_email}?subject={subject}"
    mailto_secondary = f"mailto:{secondary_email}?subject={subject}"
    gmail_web_primary = f"https://mail.google.com/mail/?view=cm&fs=1&to={primary_email}&su={subject}"

    # Resume download URL
    resume_data_url = get_resume_data_url()
    if resume_data_url:
        resume_action_btn = (
            f'<a href="{resume_data_url}" download="Nitish_Kumar_CV.pdf" class="btn-primary" '
            f'style="width:100%; justify-content:center; text-align:center;">'
            f'Download Resume (PDF) ↓</a>'
        )
    else:
        resume_action_btn = (
            f'<a href="{mailto_primary}" class="btn-secondary" style="width:100%; justify-content:center;">'
            f'Request Resume via Email ✉️</a>'
        )

    contact_html = f"""<div style="padding: 1rem 0 1.5rem; border-bottom: 1px solid var(--border);">
<div class="section-marker">// CONNECT &amp; CONTACT</div>
<h1 class="section-title">Direct Communication Channels</h1>
<p class="section-subtitle">
I am actively interviewing for AI engineering internships, Agentic AI developer positions,
and junior Python AI roles. Reach out directly through any of the verified channels below.
</p>
</div>

<div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(320px, 1fr)); gap:1.5rem; margin-top:2rem;">

<!-- Channel 1: Email (Both Verified Addresses) -->
<div class="featured-project-card" style="margin:0; display:flex; flex-direction:column; justify-content:space-between;">
<div>
<div style="font-family:var(--font-mono); font-size:0.75rem; color:var(--accent); margin-bottom:0.5rem;">DIRECT EMAIL CHANNELS</div>

<div style="margin-bottom:0.85rem;">
<div style="font-family:var(--font-mono); font-size:0.72rem; color:var(--text-muted); text-transform:uppercase;">Primary Email</div>
<a href="{mailto_primary}" target="_blank" rel="noopener noreferrer" style="font-family:var(--font-heading); font-size:1.15rem; color:var(--text-primary); text-decoration:none; font-weight:600;">
{primary_email}
</a>
</div>

<div style="margin-bottom:1.25rem;">
<div style="font-family:var(--font-mono); font-size:0.72rem; color:var(--text-muted); text-transform:uppercase;">Secondary Email</div>
<a href="{mailto_secondary}" target="_blank" rel="noopener noreferrer" style="font-family:var(--font-heading); font-size:1.05rem; color:var(--text-secondary); text-decoration:none;">
{secondary_email}
</a>
</div>

<p style="font-size:0.88rem; color:var(--text-secondary); line-height:1.6; margin-bottom:1.5rem;">
Fastest channel for technical recruiters, hiring managers, and internship inquiries.
Supports native email clients and direct browser Gmail compose.
</p>
</div>

<div style="display:flex; flex-direction:column; gap:0.6rem;">
<a href="{mailto_primary}" target="_blank" rel="noopener noreferrer" class="btn-primary" style="justify-content:center; text-align:center;">
Open Email Client ✉️
</a>
<a href="{gmail_web_primary}" target="_blank" rel="noopener noreferrer" class="btn-secondary" style="justify-content:center; text-align:center; font-size:0.78rem;">
Open in Gmail Web ↗
</a>
</div>
</div>

<!-- Channel 2: LinkedIn -->
<div class="featured-project-card" style="margin:0; display:flex; flex-direction:column; justify-content:space-between;">
<div>
<div style="font-family:var(--font-mono); font-size:0.75rem; color:var(--accent); margin-bottom:0.5rem;">PROFESSIONAL NETWORK</div>
<h3 style="font-family:var(--font-heading); font-size:1.2rem; color:var(--text-primary); margin-bottom:0.5rem;">
LinkedIn Profile
</h3>
<p style="font-size:0.88rem; color:var(--text-secondary); line-height:1.6; margin-bottom:1.25rem;">
Connect for professional updates, project discussions, and direct messaging on LinkedIn.
</p>
<div style="font-family:var(--font-mono); font-size:0.82rem; color:var(--text-muted); margin-bottom:1.5rem; word-break:break-all;">
linkedin.com/in/nitish-kumar-ai
</div>
</div>
<a href="{linkedin_url}" target="_blank" rel="noopener noreferrer" class="btn-secondary" style="justify-content:center; text-align:center;">
Visit LinkedIn Profile ↗
</a>
</div>

<!-- Channel 3: GitHub -->
<div class="featured-project-card" style="margin:0; display:flex; flex-direction:column; justify-content:space-between;">
<div>
<div style="font-family:var(--font-mono); font-size:0.75rem; color:var(--accent); margin-bottom:0.5rem;">OPEN SOURCE CODEBASE</div>
<h3 style="font-family:var(--font-heading); font-size:1.2rem; color:var(--text-primary); margin-bottom:0.5rem;">
GitHub (@XestalNitish)
</h3>
<p style="font-size:0.88rem; color:var(--text-secondary); line-height:1.6; margin-bottom:1.25rem;">
Inspect commit logs, issue discussions, and repository source code across all 10 public projects.
</p>
<div style="font-family:var(--font-mono); font-size:0.82rem; color:var(--text-muted); margin-bottom:1.5rem;">
github.com/XestalNitish
</div>
</div>
<a href="{github_url}" target="_blank" rel="noopener noreferrer" class="btn-secondary" style="justify-content:center; text-align:center;">
Inspect Repositories ↗
</a>
</div>

<!-- Channel 4: Resume Download (Repaired Functional Button) -->
<div class="featured-project-card" style="margin:0; border-color:var(--border-focus); display:flex; flex-direction:column; justify-content:space-between;">
<div>
<div style="font-family:var(--font-mono); font-size:0.75rem; color:var(--accent-secondary); margin-bottom:0.5rem;">OFFICIAL RESUME</div>
<h3 style="font-family:var(--font-heading); font-size:1.2rem; color:var(--text-primary); margin-bottom:0.5rem;">
Nitish Kumar CV (PDF)
</h3>
<p style="font-size:0.88rem; color:var(--text-secondary); line-height:1.6; margin-bottom:1.25rem;">
Official two-page technical resume covering Agentic AI, LangGraph architectures,
Hybrid RAG, FastMCP servers, and education credentials.
</p>
<div style="font-family:var(--font-mono); font-size:0.78rem; color:var(--accent-secondary); margin-bottom:1.5rem;">
✓ 2-Page Verified PDF • 177 KB
</div>
</div>
{resume_action_btn}
</div>

</div>"""

    render_html(contact_html)
    render_footer()
