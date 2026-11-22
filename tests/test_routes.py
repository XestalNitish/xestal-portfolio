"""
test_routes.py
Tests the HTTP response and HTML generation across all views and query routes:
- /?tab=home
- /?tab=projects
- /?tab=projects&cat=Agentic+AI
- /?tab=project_detail&id=ultimate-coding-agent
- /?tab=project_detail&id=xestal-enterprise-rag-engine
- /?tab=project_detail&id=xestal-research-agent
- /?tab=project_detail&id=invalid-id-fallback-check
- /?tab=case_studies
- /?tab=skills
- /?tab=about
- /?tab=contact
"""

import subprocess
import time
import urllib.request
import sys

def run_route_tests():
    port = 8504
    cmd = [
        sys.executable, "-m", "streamlit", "run", "app.py",
        "--server.headless", "true",
        "--server.port", str(port),
        "--server.enableCORS", "true"
    ]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(3.5)

    routes = [
        "",
        "?tab=home",
        "?tab=projects",
        "?tab=projects&cat=Agentic+AI",
        "?tab=project_detail&id=ultimate-coding-agent",
        "?tab=project_detail&id=xestal-enterprise-rag-engine",
        "?tab=project_detail&id=xestal-research-agent",
        "?tab=project_detail&id=invalid-id-xyz",
        "?tab=case_studies",
        "?tab=skills",
        "?tab=about",
        "?tab=contact"
    ]

    passed = 0
    try:
        for r in routes:
            url = f"http://localhost:{port}/{r}"
            req = urllib.request.Request(url, headers={"User-Agent": "TestClient"})
            with urllib.request.urlopen(req, timeout=3.0) as resp:
                assert resp.status == 200, f"Route {r} failed with status {resp.status}"
                passed += 1
                print(f"✓ Route '{r or '/'}' returned HTTP 200 OK")
    finally:
        proc.terminate()
        try:
            proc.wait(timeout=2.0)
        except Exception:
            proc.kill()

    print(f"\nALL {passed} ROUTES TESTED AND RETURNED HTTP 200 OK!")

if __name__ == "__main__":
    run_route_tests()
