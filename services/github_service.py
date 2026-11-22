"""
github_service.py
Fetches public repository metadata from GitHub API with caching and error handling.
Always falls back gracefully to local metadata on rate limit, error, or network timeout.
"""

import json
import urllib.request
import urllib.error
from typing import Dict, Any, Optional

try:
    import streamlit as st
    cache_decorator = st.cache_data(ttl=3600)
except Exception:
    def cache_decorator(func):
        return func


@cache_decorator
def fetch_github_user_profile(username: str = "XestalNitish") -> Optional[Dict[str, Any]]:
    """
    Fetches basic public profile stats for username.
    Returns None on rate limits or network issues.
    """
    url = f"https://api.github.com/users/{username}"
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "X-Estal-Portfolio-Engine/2.0"}
    )
    try:
        with urllib.request.urlopen(req, timeout=3.5) as response:
            if response.status == 200:
                return json.loads(response.read().decode("utf-8"))
    except Exception:
        # Graceful fallback: return None so caller uses local data
        pass
    return None


@cache_decorator
def fetch_repo_meta(repo_name: str, username: str = "XestalNitish") -> Optional[Dict[str, Any]]:
    """
    Fetches repository metadata (stars, forks, pushed_at).
    Returns None on rate limit or error.
    """
    url = f"https://api.github.com/repos/{username}/{repo_name}"
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "X-Estal-Portfolio-Engine/2.0"}
    )
    try:
        with urllib.request.urlopen(req, timeout=3.0) as response:
            if response.status == 200:
                data = json.loads(response.read().decode("utf-8"))
                return {
                    "stars": data.get("stargazers_count", 0),
                    "forks": data.get("forks_count", 0),
                    "updated_at": data.get("updated_at", ""),
                    "open_issues": data.get("open_issues_count", 0)
                }
    except Exception:
        pass
    return None
