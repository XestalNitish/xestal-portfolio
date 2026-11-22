"""
utils.py
HTML sanitization and rendering utilities for Streamlit markdown.
Prevents Streamlit from parsing 4-space indented HTML lines as raw <pre><code> blocks.
"""

import streamlit as st


def clean_html(html_str: str) -> str:
    """
    Cleans leading whitespace from HTML lines so CommonMark does not interpret
    indented HTML as markdown code blocks. Preserves whitespace only inside <pre> tags.
    """
    lines = html_str.splitlines()
    cleaned = []
    in_pre = False
    for line in lines:
        if "<pre" in line:
            in_pre = True
            cleaned.append(line.strip())
        elif "</pre>" in line:
            in_pre = False
            cleaned.append(line)
        elif in_pre:
            cleaned.append(line)
        else:
            cleaned.append(line.strip())
    return "\n".join(cleaned)


def render_html(html_str: str) -> None:
    """Safely renders HTML via st.markdown with unsafe_allow_html=True."""
    st.markdown(clean_html(html_str), unsafe_allow_html=True)
