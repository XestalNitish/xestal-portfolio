"""
resume_service.py
Handles verified PDF resume loading, base64 data encoding, and Streamlit download button rendering.
"""

import base64
import os
from pathlib import Path
from typing import Optional
import streamlit as st

RESUME_PATH = Path("assets/Nitish_Kumar_CV.pdf")


def get_resume_path() -> Path:
    """Returns the path to the official resume PDF."""
    return RESUME_PATH


def is_resume_available() -> bool:
    """Checks whether the official resume PDF exists."""
    return RESUME_PATH.exists() and RESUME_PATH.stat().st_size > 0


def get_resume_bytes() -> Optional[bytes]:
    """Reads and returns the raw bytes of the official resume PDF."""
    if is_resume_available():
        return RESUME_PATH.read_bytes()
    return None


def get_resume_data_url() -> Optional[str]:
    """Returns a client-side downloadable data URI for the resume PDF."""
    data = get_resume_bytes()
    if data:
        b64 = base64.b64encode(data).decode("utf-8")
        return f"data:application/pdf;base64,{b64}"
    return None


def render_resume_download_button(
    label: str = "Download Resume ↓",
    key: str = "resume_download_btn",
    use_container_width: bool = False
) -> None:
    """Renders a Streamlit native download button for the official resume."""
    if is_resume_available():
        with open(RESUME_PATH, "rb") as f:
            st.download_button(
                label=label,
                data=f.read(),
                file_name="Nitish_Kumar_CV.pdf",
                mime="application/pdf",
                key=key,
                use_container_width=use_container_width
            )
    else:
        st.error("Resume is currently unavailable.")
