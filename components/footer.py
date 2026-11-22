"""
footer.py
Renders the restrained dark editorial footer.
Displays developer brand, verified social links, direct email, and copyright.
"""

import streamlit as st
import datetime


def render_footer() -> None:
    """Renders the editorial footer."""
    year = datetime.datetime.now().year
    footer_html = f"""
    <div class="editorial-footer">
      <div class="footer-left">
        <span class="footer-brand">X-ESTAL // Nitish Kumar</span>
        <span class="footer-copy">
          Independent AI Engineer • Built with Python &amp; Streamlit • © {year}
        </span>
      </div>
      <div class="footer-links">
        <a href="https://github.com/XestalNitish" target="_blank" rel="noopener noreferrer" class="footer-link">
          GitHub ↗
        </a>
        <a href="https://www.linkedin.com/in/nitish-kumar-33714642b/" target="_blank" rel="noopener noreferrer" class="footer-link">
          LinkedIn ↗
        </a>
        <a href="mailto:nitishkumar.xestal@gmail.com" class="footer-link">
          Email ↗
        </a>
        <a href="?tab=projects" target="_self" class="footer-link">
          Projects
        </a>
      </div>
    </div>
    """
    st.markdown(footer_html, unsafe_allow_html=True)
