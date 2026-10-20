"""
X-Estal Nitish — Personal Portfolio & AI Agentic Hub
=====================================================
A Modern Production-Ready Streamlit Application with Claymorphism UI
Designed for Seamless Deployment on Streamlit Community Cloud & GitHub.

Developer: Nitish Kumar (X-Estal Nitish)
"""

import streamlit as st
import datetime

# ─────────────────────────────────────────────────────────────
# 1. PAGE CONFIGURATION
# ─────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="X-Estal Nitish | AI Developer Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────────────────────
# 2. ADVANCED CLAYMORPHISM STYLING & ANIMATIONS
# ─────────────────────────────────────────────────────────────
CLAY_CSS = """
<style>
    /* Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;700&display=swap');

    :root {
        --clay-bg: #F4F0FF;
        --clay-card-bg: linear-gradient(145deg, #FFFFFF, #EFE8FA);
        --clay-card-alt: linear-gradient(145deg, #F8F5FF, #E7DCF8);
        --clay-shadow: 12px 12px 24px rgba(165, 145, 205, 0.4), -12px -12px 24px rgba(255, 255, 255, 0.9);
        --clay-shadow-sm: 6px 6px 14px rgba(165, 145, 205, 0.35), -6px -6px 14px rgba(255, 255, 255, 0.85);
        --clay-shadow-lg: 16px 16px 32px rgba(165, 145, 205, 0.5), -16px -16px 32px rgba(255, 255, 255, 0.95);
        --clay-inset: inset 4px 4px 8px rgba(165, 145, 205, 0.3), inset -4px -4px 8px rgba(255, 255, 255, 0.7);
        --clay-inset-sm: inset 2px 2px 4px rgba(165, 145, 205, 0.25), inset -2px -2px 4px rgba(255, 255, 255, 0.6);
        --primary: #7C3AED;
        --primary-light: #9061F9;
        --secondary: #3B82F6;
        --accent-pink: #EC4899;
        --accent-green: #10B981;
        --accent-orange: #F59E0B;
        --text-dark: #1E1B4B;
        --text-muted: #5B4E77;
    }

    /* Streamlit UI Resets */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display: none;}
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 3rem !important;
        max-width: 1240px !important;
    }

    /* Global Body */
    .stApp {
        background: linear-gradient(135deg, #F4F0FF 0%, #EAE2F8 30%, #F8F5FF 60%, #ECE4FA 100%);
        font-family: 'Plus Jakarta Sans', sans-serif;
        color: var(--text-dark);
    }

    /* ─── CLAYMORPHISM CARDS ─── */
    .clay-card {
        background: var(--clay-card-bg);
        border-radius: 28px;
        padding: 32px;
        margin-bottom: 24px;
        box-shadow: var(--clay-shadow);
        border: 2px solid rgba(255, 255, 255, 0.7);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }
    .clay-card:hover {
        transform: translateY(-5px);
        box-shadow: var(--clay-shadow-lg);
    }

    .clay-card-flat {
        background: var(--clay-card-bg);
        border-radius: 24px;
        padding: 24px;
        box-shadow: var(--clay-shadow-sm);
        border: 1.5px solid rgba(255, 255, 255, 0.7);
    }

    /* ─── HERO HEADER ─── */
    .hero-container {
        text-align: center;
        padding: 40px 20px 20px;
    }

    .avatar-wrapper {
        position: relative;
        display: inline-block;
        margin-bottom: 20px;
    }

    .clay-avatar {
        width: 130px;
        height: 130px;
        border-radius: 50%;
        background: linear-gradient(135deg, #7C3AED, #3B82F6, #EC4899);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 60px;
        box-shadow: var(--clay-shadow-lg);
        border: 5px solid #FFFFFF;
        animation: floatAnim 5s ease-in-out infinite;
        margin: 0 auto;
    }

    @keyframes floatAnim {
        0%, 100% { transform: translateY(0px) rotate(0deg); }
        50% { transform: translateY(-10px) rotate(3deg); }
    }

    .status-badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        padding: 6px 18px;
        border-radius: 30px;
        background: rgba(16, 185, 129, 0.15);
        border: 1px solid rgba(16, 185, 129, 0.3);
        box-shadow: var(--clay-inset-sm);
        color: #047857;
        font-size: 0.85rem;
        font-weight: 700;
        margin-bottom: 16px;
    }
    .status-dot {
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background-color: #10B981;
        animation: pulseDot 2s infinite;
    }
    @keyframes pulseDot {
        0%, 100% { opacity: 1; transform: scale(1); }
        50% { opacity: 0.4; transform: scale(1.3); }
    }

    .hero-name {
        font-size: 3.5rem;
        font-weight: 900;
        background: linear-gradient(135deg, #6D28D9 0%, #3B82F6 50%, #EC4899 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: -1.5px;
        line-height: 1.1;
        margin-bottom: 10px;
    }

    .hero-title {
        font-size: 1.35rem;
        font-weight: 600;
        color: var(--text-dark);
        margin-bottom: 14px;
        letter-spacing: -0.2px;
    }

    .hero-bio {
        font-size: 1.05rem;
        color: var(--text-muted);
        max-width: 680px;
        margin: 0 auto 28px;
        line-height: 1.7;
    }

    /* ─── CLAY SOCIAL BUTTONS ─── */
    .social-pills-row {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        gap: 14px;
        margin-bottom: 30px;
    }

    .clay-pill-btn {
        display: inline-flex;
        align-items: center;
        gap: 10px;
        padding: 12px 26px;
        border-radius: 40px;
        font-size: 0.95rem;
        font-weight: 700;
        text-decoration: none !important;
        box-shadow: var(--clay-shadow-sm);
        border: 2px solid rgba(255, 255, 255, 0.8);
        transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        cursor: pointer;
    }
    .clay-pill-btn:hover {
        transform: translateY(-4px) scale(1.04);
        box-shadow: var(--clay-shadow);
        text-decoration: none !important;
    }
    .clay-pill-btn:active {
        transform: translateY(1px) scale(0.98);
        box-shadow: var(--clay-inset);
    }

    .btn-github {
        background: linear-gradient(145deg, #2D3748, #1A202C);
        color: #FFFFFF !important;
    }
    .btn-linkedin {
        background: linear-gradient(145deg, #0A66C2, #004182);
        color: #FFFFFF !important;
    }
    .btn-instagram {
        background: linear-gradient(145deg, #E1306C, #C13584, #833AB4);
        color: #FFFFFF !important;
    }

    /* ─── STATS BAR ─── */
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
        gap: 16px;
        margin-bottom: 36px;
    }

    .clay-stat-box {
        background: var(--clay-card-bg);
        border-radius: 22px;
        padding: 22px 18px;
        text-align: center;
        box-shadow: var(--clay-shadow-sm);
        border: 1.5px solid rgba(255, 255, 255, 0.7);
        transition: all 0.3s ease;
    }
    .clay-stat-box:hover {
        transform: translateY(-3px);
        box-shadow: var(--clay-shadow);
    }
    .stat-val {
        font-size: 2.2rem;
        font-weight: 900;
        background: linear-gradient(135deg, #7C3AED, #3B82F6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        line-height: 1.2;
    }
    .stat-label {
        font-size: 0.85rem;
        font-weight: 600;
        color: var(--text-muted);
        margin-top: 4px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    /* ─── SECTION TITLE ─── */
    .sec-header {
        text-align: center;
        margin: 40px 0 24px;
    }
    .sec-title {
        font-size: 2rem;
        font-weight: 800;
        color: var(--text-dark);
        letter-spacing: -0.5px;
    }
    .sec-subtitle {
        font-size: 1rem;
        color: var(--text-muted);
        margin-top: 4px;
    }
    .sec-bar {
        width: 60px;
        height: 5px;
        border-radius: 10px;
        background: linear-gradient(90deg, #7C3AED, #EC4899);
        margin: 10px auto 0;
    }

    /* ─── PROJECT CLAY CARDS ─── */
    .project-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 24px;
        margin-bottom: 36px;
    }

    .clay-project-card {
        background: var(--clay-card-bg);
        border-radius: 28px;
        padding: 28px;
        box-shadow: var(--clay-shadow);
        border: 2px solid rgba(255, 255, 255, 0.8);
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        position: relative;
        overflow: hidden;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }
    .clay-project-card:hover {
        transform: translateY(-8px);
        box-shadow: var(--clay-shadow-lg);
    }

    .project-card-top-accent {
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 6px;
    }
    .accent-research { background: linear-gradient(90deg, #7C3AED, #3B82F6); }
    .accent-bitcoin { background: linear-gradient(90deg, #F59E0B, #EF4444); }
    .accent-brain { background: linear-gradient(90deg, #10B981, #06B6D4); }
    .accent-codedev { background: linear-gradient(90deg, #EC4899, #8B5CF6); }

    .project-badge {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 800;
        letter-spacing: 0.5px;
        text-transform: uppercase;
        margin-bottom: 12px;
        box-shadow: var(--clay-inset-sm);
    }
    .badge-purple { background: rgba(124, 58, 237, 0.12); color: #6D28D9; }
    .badge-orange { background: rgba(245, 158, 11, 0.15); color: #B45309; }
    .badge-green { background: rgba(16, 185, 129, 0.15); color: #047857; }
    .badge-pink { background: rgba(236, 72, 153, 0.15); color: #BE185D; }

    .project-icon-box {
        width: 58px;
        height: 58px;
        border-radius: 18px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 28px;
        margin-bottom: 16px;
        box-shadow: var(--clay-shadow-sm);
        border: 2px solid #FFFFFF;
    }

    .project-title {
        font-size: 1.35rem;
        font-weight: 800;
        color: var(--text-dark);
        margin-bottom: 8px;
        line-height: 1.3;
    }

    .project-desc {
        font-size: 0.92rem;
        color: var(--text-muted);
        line-height: 1.6;
        margin-bottom: 20px;
        flex-grow: 1;
    }

    .tech-pill-row {
        display: flex;
        flex-wrap: wrap;
        gap: 6px;
        margin-bottom: 20px;
    }

    .tech-pill {
        display: inline-block;
        padding: 4px 10px;
        border-radius: 12px;
        font-size: 0.75rem;
        font-weight: 600;
        background: rgba(255, 255, 255, 0.7);
        color: var(--text-dark);
        box-shadow: var(--clay-inset-sm);
    }

    .launch-btn {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 8px;
        width: 100%;
        padding: 12px 18px;
        border-radius: 16px;
        font-size: 0.92rem;
        font-weight: 700;
        text-decoration: none !important;
        box-shadow: var(--clay-shadow-sm);
        border: 1.5px solid rgba(255, 255, 255, 0.8);
        transition: all 0.3s ease;
        color: #FFFFFF !important;
    }
    .launch-btn:hover {
        transform: translateY(-2px);
        box-shadow: var(--clay-shadow);
        text-decoration: none !important;
        filter: brightness(1.08);
    }

    .launch-purple { background: linear-gradient(135deg, #7C3AED, #6366F1); }
    .launch-orange { background: linear-gradient(135deg, #F59E0B, #EA580C); }
    .launch-green { background: linear-gradient(135deg, #10B981, #059669); }
    .launch-pink { background: linear-gradient(135deg, #EC4899, #8B5CF6); }

    /* ─── SKILL CHIPS ─── */
    .skills-cluster {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        justify-content: center;
        padding: 10px 0;
    }

    .clay-chip {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        padding: 10px 18px;
        border-radius: 20px;
        background: var(--clay-card-bg);
        box-shadow: var(--clay-shadow-sm);
        border: 1.5px solid rgba(255, 255, 255, 0.7);
        font-size: 0.88rem;
        font-weight: 700;
        color: var(--text-dark);
        transition: all 0.25s ease;
    }
    .clay-chip:hover {
        transform: translateY(-3px) scale(1.05);
        box-shadow: var(--clay-shadow);
    }

    /* ─── FOOTER ─── */
    .clay-footer {
        text-align: center;
        padding: 40px 20px 20px;
        margin-top: 50px;
    }
    .footer-brand {
        font-weight: 800;
        font-size: 1.1rem;
        color: var(--primary);
    }
    .footer-copy {
        font-size: 0.85rem;
        color: var(--text-muted);
        margin-top: 6px;
    }

    /* Responsive */
    @media (max-width: 768px) {
        .hero-name { font-size: 2.5rem; }
        .hero-title { font-size: 1.15rem; }
        .clay-avatar { width: 100px; height: 100px; font-size: 48px; }
        .stats-grid { grid-template-columns: repeat(2, 1fr); }
        .clay-card { padding: 22px; border-radius: 22px; }
    }
</style>
"""

st.markdown(CLAY_CSS, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────
# 3. DATA & CONSTANTS
# ─────────────────────────────────────────────────────────────

SOCIAL_CHANNELS = [
    {
        "name": "GitHub",
        "handle": "@XestalNitish",
        "url": "https://github.com/XestalNitish",
        "icon": "🐙",
        "btn_class": "btn-github",
    },
    {
        "name": "LinkedIn",
        "handle": "Nitish Kumar",
        "url": "https://www.linkedin.com/in/nitish-kumar-33714642b/",
        "icon": "💼",
        "btn_class": "btn-linkedin",
    },
    {
        "name": "Instagram",
        "handle": "@x_estal_nitish",
        "url": "https://www.instagram.com/x_estal_nitish",
        "icon": "📸",
        "btn_class": "btn-instagram",
    },
]

ALL_PROJECTS = [
    {
        "id": "research-agent",
        "title": "Research Agent",
        "category": "Autonomous AI Agent",
        "badge_class": "badge-purple",
        "accent_class": "accent-research",
        "launch_class": "launch-purple",
        "icon": "🔬",
        "url": "https://xestal-research-agent-by-x-estal-nitish.streamlit.app/",
        "description": "An autonomous AI research assistant that scans, cross-verifies, and synthesizes technical and scientific literature from multiple web and academic sources into structured executive dossiers.",
        "tags": ["LangChain", "Vector Embeddings", "Streamlit", "Web Scraper", "NLP"],
        "highlights": [
            "Autonomous multi-step research workflow",
            "Synthesizes academic papers & live web data",
            "Generates cited, professional summary reports",
        ],
    },
    {
        "id": "bitcoin-predictor",
        "title": "Bitcoin Price Predictor",
        "category": "Machine Learning & Quant",
        "badge_class": "badge-orange",
        "accent_class": "accent-bitcoin",
        "launch_class": "launch-orange",
        "icon": "₿",
        "url": "https://x-estal-nitish-bit-coin-price-predictor.streamlit.app",
        "description": "Quantitative cryptocurrency forecasting system applying deep recurrent neural architectures and real-time market sentiment to predict Bitcoin volatility and trend directions.",
        "tags": ["Deep Learning", "LSTM", "Time-Series", "Streamlit", "Finance"],
        "highlights": [
            "Historical pattern detection with LSTM networks",
            "Real-time technical indicators (RSI, MACD, Moving Averages)",
            "Interactive prediction forecasting dashboard",
        ],
    },
    {
        "id": "brain-tumor",
        "title": "Brain Tumor Classifier",
        "category": "Computer Vision & Medical AI",
        "badge_class": "badge-green",
        "accent_class": "accent-brain",
        "launch_class": "launch-green",
        "icon": "🧠",
        "url": "https://brain-tumor-classifier-by-x-estal-nitish.streamlit.app",
        "description": "High-accuracy diagnostic computer vision application built with Convolutional Neural Networks (CNNs) for detecting and categorizing brain tumors from MRI radiological scans.",
        "tags": ["CNN", "Medical Imaging", "PyTorch/TensorFlow", "Computer Vision"],
        "highlights": [
            "Multi-class MRI scan categorization",
            "High clinical sensitivity and specificity score",
            "Instant image upload & real-time confidence scores",
        ],
    },
    {
        "id": "code-dev-agent",
        "title": "Code Dev Agent",
        "category": "Autonomous Software Engineering",
        "badge_class": "badge-pink",
        "accent_class": "accent-codedev",
        "launch_class": "launch-pink",
        "icon": "⚡",
        "url": "https://code-dev-agent-by-x-estal-nitish.streamlit.app",
        "description": "Autonomous full-lifecycle programming agent that plans software architecture, writes clean production code, enforces security guardrails, runs tests in a sandbox, and self-heals bugs.",
        "tags": ["LangGraph", "Self-Debugging", "Sandbox Execution", "Security Audit"],
        "highlights": [
            "Architecture planning with dependency checks",
            "Pre-execution security audit against command injection",
            "Automated runtime traceback analysis and self-correction",
        ],
    },
]

SKILLS_CATEGORIES = {
    "🤖 AI & Autonomous Agents": [
        ("🦜", "LangChain"),
        ("🕸️", "LangGraph"),
        ("🧠", "Agentic Orchestration"),
        ("⚡", "Local LLM Serving"),
        ("🔍", "RAG Systems"),
        ("🗃️", "ChromaDB"),
    ],
    "🔬 Machine Learning & Deep Learning": [
        ("🐍", "Python 3.11+"),
        ("🔥", "PyTorch"),
        ("🧠", "TensorFlow"),
        ("📊", "Scikit-Learn"),
        ("👁️", "Computer Vision (CNN)"),
        ("📈", "Time-Series (LSTM)"),
        ("💬", "NLP & Transformers"),
    ],
    "🌐 Web Frameworks & Deployment": [
        ("🎈", "Streamlit"),
        ("⚡", "FastAPI"),
        ("🐳", "Docker"),
        ("🐙", "Git & GitHub"),
        ("☁️", "Streamlit Cloud"),
        ("🔄", "CI/CD Workflows"),
    ],
}


# ─────────────────────────────────────────────────────────────
# 4. HERO SECTION
# ─────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-container">
    <div class="avatar-wrapper">
        <div class="clay-avatar">🚀</div>
    </div>
    <div>
        <div class="status-badge">
            <span class="status-dot"></span>
            <span>Available for AI Projects & Collaborations</span>
        </div>
    </div>
    <div class="hero-name">X-Estal Nitish</div>
    <div class="hero-title">AI Engineer • Autonomous Agents Architect • ML Developer</div>
    <div class="hero-bio">
        Crafting production-ready AI agents, medical imaging vision models, and predictive quantitative systems.
        Passionate about sovereign local models, LangGraph orchestration, and human-centric software.
    </div>
</div>
""", unsafe_allow_html=True)

# Social Buttons
social_html = '<div class="social-pills-row">'
for item in SOCIAL_CHANNELS:
    social_html += f'''
    <a href="{item['url']}" target="_blank" class="clay-pill-btn {item['btn_class']}">
        <span>{item['icon']}</span>
        <span>{item['name']}</span>
    </a>
    '''
social_html += '</div>'
st.markdown(social_html, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────
# 5. METRICS / STATS BAR
# ─────────────────────────────────────────────────────────────
st.markdown("""
<div class="stats-grid">
    <div class="clay-stat-box">
        <div class="stat-val">4+</div>
        <div class="stat-label">Live Streamlit Apps</div>
    </div>
    <div class="clay-stat-box">
        <div class="stat-val">150+</div>
        <div class="stat-label">Agent Tools Built</div>
    </div>
    <div class="clay-stat-box">
        <div class="stat-val">100%</div>
        <div class="stat-label">Open Source & Free</div>
    </div>
    <div class="clay-stat-box">
        <div class="stat-val">24/7</div>
        <div class="stat-label">Cloud Deployed</div>
    </div>
</div>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────
# 6. TAB NAVIGATION
# ─────────────────────────────────────────────────────────────
tab_projects, tab_skills, tab_about, tab_contact = st.tabs([
    "🚀 Featured Projects",
    "🛠️ Tech Stack & Skills",
    "👤 About Me",
    "📬 Connect & Contact",
])


# ─────────────────────────────────────────────────────────────
# TAB 1: FEATURED PROJECTS
# ─────────────────────────────────────────────────────────────
with tab_projects:
    st.markdown("""
    <div class="sec-header">
        <div class="sec-title">🌟 Live Production Projects</div>
        <div class="sec-subtitle">Click "Launch Live App" to test each live deployed Streamlit application</div>
        <div class="sec-bar"></div>
    </div>
    """, unsafe_allow_html=True)

    # 2x2 Grid of 4 Projects
    row1_col1, row1_col2 = st.columns(2)
    row2_col1, row2_col2 = st.columns(2)
    grid_cols = [row1_col1, row1_col2, row2_col1, row2_col2]

    for idx, proj in enumerate(ALL_PROJECTS):
        with grid_cols[idx]:
            # Tech pills
            pills_html = "".join([f'<span class="tech-pill">{t}</span>' for t in proj["tags"]])
            
            # Highlights
            hl_html = "".join([f'<li style="margin-bottom:4px;">{h}</li>' for h in proj["highlights"]])

            st.markdown(f"""
            <div class="clay-project-card">
                <div class="project-card-top-accent {proj['accent_class']}"></div>
                <div>
                    <div class="project-badge {proj['badge_class']}">{proj['category']}</div>
                    <div class="project-icon-box">{proj['icon']}</div>
                    <div class="project-title">{proj['title']}</div>
                    <div class="project-desc">{proj['description']}</div>
                    <div class="tech-pill-row">{pills_html}</div>
                    <div style="font-size:0.85rem; color:#4C1D95; margin-bottom:18px;">
                        <ul style="padding-left:18px; margin:0;">
                            {hl_html}
                        </ul>
                    </div>
                </div>
                <a href="{proj['url']}" target="_blank" class="launch-btn {proj['launch_class']}">
                    <span>Launch Live App</span>
                    <span>→</span>
                </a>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Quick Jump Links Table in Clay Card
    st.markdown("""
    <div class="clay-card">
        <h3 style="margin-top:0; color:#1E1B4B; font-weight:800;">🔗 Quick Directory of Live Endpoints</h3>
        <p style="color:#5B4E77; font-size:0.95rem;">All systems are continuously hosted on Streamlit Cloud and accessible worldwide:</p>
        <div style="display:flex; flex-direction:column; gap:12px; margin-top:16px;">
            <div style="display:flex; justify-content:space-between; align-items:center; padding:10px 16px; background:rgba(255,255,255,0.7); border-radius:14px;">
                <span><strong>🔬 Research Agent:</strong> Autonomous multi-source literature investigator</span>
                <a href="https://xestal-research-agent-by-x-estal-nitish.streamlit.app/" target="_blank" style="color:#7C3AED; font-weight:700;">Open →</a>
            </div>
            <div style="display:flex; justify-content:space-between; align-items:center; padding:10px 16px; background:rgba(255,255,255,0.7); border-radius:14px;">
                <span><strong>₿ Bitcoin Price Predictor:</strong> Real-time quantitative crypto forecaster</span>
                <a href="https://x-estal-nitish-bit-coin-price-predictor.streamlit.app" target="_blank" style="color:#F59E0B; font-weight:700;">Open →</a>
            </div>
            <div style="display:flex; justify-content:space-between; align-items:center; padding:10px 16px; background:rgba(255,255,255,0.7); border-radius:14px;">
                <span><strong>🧠 Brain Tumor Classifier:</strong> Deep CNN medical imaging diagnostics</span>
                <a href="https://brain-tumor-classifier-by-x-estal-nitish.streamlit.app" target="_blank" style="color:#10B981; font-weight:700;">Open →</a>
            </div>
            <div style="display:flex; justify-content:space-between; align-items:center; padding:10px 16px; background:rgba(255,255,255,0.7); border-radius:14px;">
                <span><strong>⚡ Code Dev Agent:</strong> Autonomous self-debugging software engineer</span>
                <a href="https://code-dev-agent-by-x-estal-nitish.streamlit.app" target="_blank" style="color:#EC4899; font-weight:700;">Open →</a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────
# TAB 2: TECH STACK & SKILLS
# ─────────────────────────────────────────────────────────────
with tab_skills:
    st.markdown("""
    <div class="sec-header">
        <div class="sec-title">🛠️ Engineering Competencies</div>
        <div class="sec-subtitle">Technologies and methodologies used across production applications</div>
        <div class="sec-bar"></div>
    </div>
    """, unsafe_allow_html=True)

    for cat_title, skill_list in SKILLS_CATEGORIES.items():
        st.markdown(f"""
        <div class="clay-card">
            <h3 style="margin-top:0; color:#1E1B4B; font-size:1.25rem; font-weight:800;">{cat_title}</h3>
            <div class="skills-cluster">
                {"".join([f'<div class="clay-chip"><span>{icon}</span><span>{name}</span></div>' for icon, name in skill_list])}
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Architectural highlights
    st.markdown("""
    <div class="clay-card">
        <h3 style="margin-top:0; color:#1E1B4B; font-size:1.25rem; font-weight:800;">🏛️ Architectural Principles</h3>
        <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap:16px; margin-top:14px;">
            <div style="background:rgba(255,255,255,0.6); padding:16px; border-radius:16px;">
                <div style="font-weight:700; color:#7C3AED; margin-bottom:4px;">🛡️ Safe Autonomous Loops</div>
                <div style="font-size:0.9rem; color:#5B4E77;">StateGraph with conditional edge guards, cycle dampeners, and pre-execution safety audits.</div>
            </div>
            <div style="background:rgba(255,255,255,0.6); padding:16px; border-radius:16px;">
                <div style="font-weight:700; color:#3B82F6; margin-bottom:4px;">⚡ Production Scalability</div>
                <div style="font-size:0.9rem; color:#5B4E77;">Streamlit Cloud-ready, fast load times, minimal memory footprint, and graceful failure fallbacks.</div>
            </div>
            <div style="background:rgba(255,255,255,0.6); padding:16px; border-radius:16px;">
                <div style="font-weight:700; color:#10B981; margin-bottom:4px;">🎨 Modern Claymorphism UI</div>
                <div style="font-size:0.9rem; color:#5B4E77;">Dual-shadow 3D soft clay aesthetics designed for delightful user experience across devices.</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────
# TAB 3: ABOUT ME
# ─────────────────────────────────────────────────────────────
with tab_about:
    st.markdown("""
    <div class="sec-header">
        <div class="sec-title">👤 About Nitish Kumar</div>
        <div class="sec-subtitle">The mind behind X-Estal AI</div>
        <div class="sec-bar"></div>
    </div>
    """, unsafe_allow_html=True)

    col_about_1, col_about_2 = st.columns([1.2, 1])

    with col_about_1:
        st.markdown("""
        <div class="clay-card" style="height:100%;">
            <h3 style="margin-top:0; color:#1E1B4B; font-weight:800;">Hey, I'm Nitish Kumar 👋</h3>
            <p style="color:#5B4E77; line-height:1.75; font-size:1rem;">
                Known online as <strong style="color:#7C3AED;">X-Estal Nitish</strong>, I am an AI Engineer,
                Machine Learning Practitioner, and Full-Stack Autonomous Systems Builder based in India.
            </p>
            <p style="color:#5B4E77; line-height:1.75; font-size:1rem;">
                My passion is taking cutting-edge AI breakthroughs — from multi-agent graph orchestration
                to deep medical imaging classifiers and financial forecasting — and turning them into
                <strong>working, deployed, production-grade applications</strong> that anyone can use directly
                in their browser.
            </p>
            <p style="color:#5B4E77; line-height:1.75; font-size:1rem;">
                Every project I build is 100% open-source, cloud-accessible, and crafted with meticulous
                attention to performance, reliability, and modern aesthetic design.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col_about_2:
        st.markdown("""
        <div class="clay-card" style="height:100%;">
            <h3 style="margin-top:0; color:#1E1B4B; font-weight:800;">Quick Highlights</h3>
            <div style="display:flex; flex-direction:column; gap:12px; margin-top:14px;">
                <div style="display:flex; gap:12px; align-items:flex-start;">
                    <span style="font-size:22px;">🎯</span>
                    <div>
                        <strong style="color:#1E1B4B;">Focus Areas:</strong>
                        <div style="color:#5B4E77; font-size:0.9rem;">Agentic AI, Computer Vision, Time-Series ML, LangGraph</div>
                    </div>
                </div>
                <div style="display:flex; gap:12px; align-items:flex-start;">
                    <span style="font-size:22px;">🚀</span>
                    <div>
                        <strong style="color:#1E1B4B;">Live Portfolio:</strong>
                        <div style="color:#5B4E77; font-size:0.9rem;">4 full-scale applications live on Streamlit Cloud</div>
                    </div>
                </div>
                <div style="display:flex; gap:12px; align-items:flex-start;">
                    <span style="font-size:22px;">🌐</span>
                    <div>
                        <strong style="color:#1E1B4B;">Social Presence:</strong>
                        <div style="color:#5B4E77; font-size:0.9rem;">Active on GitHub, LinkedIn & Instagram</div>
                    </div>
                </div>
                <div style="display:flex; gap:12px; align-items:flex-start;">
                    <span style="font-size:22px;">💡</span>
                    <div>
                        <strong style="color:#1E1B4B;">Philosophy:</strong>
                        <div style="color:#5B4E77; font-size:0.9rem;">Build software that thinks, reasons, and solves real problems.</div>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────
# TAB 4: CONTACT & CONNECT
# ─────────────────────────────────────────────────────────────
with tab_contact:
    st.markdown("""
    <div class="sec-header">
        <div class="sec-title">📬 Let's Connect</div>
        <div class="sec-subtitle">Reach out for freelance inquiries, collaborations, or tech discussions</div>
        <div class="sec-bar"></div>
    </div>
    """, unsafe_allow_html=True)

    col_c1, col_c2 = st.columns([1, 1])

    with col_c1:
        st.markdown(f"""
        <div class="clay-card">
            <h3 style="margin-top:0; color:#1E1B4B; font-weight:800;">Direct Social Channels</h3>
            <p style="color:#5B4E77; font-size:0.92rem; margin-bottom:20px;">
                Connect with me directly on any of my official handles:
            </p>
            <div style="display:flex; flex-direction:column; gap:12px;">
                <a href="{SOCIAL_CHANNELS[0]['url']}" target="_blank" style="display:flex; align-items:center; gap:12px; padding:12px 18px; background:rgba(255,255,255,0.7); border-radius:16px; text-decoration:none; color:#1E1B4B; box-shadow:var(--clay-shadow-sm);">
                    <span style="font-size:24px;">🐙</span>
                    <div>
                        <div style="font-weight:700;">GitHub</div>
                        <div style="font-size:0.85rem; color:#5B4E77;">github.com/XestalNitish</div>
                    </div>
                </a>
                <a href="{SOCIAL_CHANNELS[1]['url']}" target="_blank" style="display:flex; align-items:center; gap:12px; padding:12px 18px; background:rgba(255,255,255,0.7); border-radius:16px; text-decoration:none; color:#1E1B4B; box-shadow:var(--clay-shadow-sm);">
                    <span style="font-size:24px;">💼</span>
                    <div>
                        <div style="font-weight:700;">LinkedIn</div>
                        <div style="font-size:0.85rem; color:#5B4E77;">linkedin.com/in/nitish-kumar-33714642b/</div>
                    </div>
                </a>
                <a href="{SOCIAL_CHANNELS[2]['url']}" target="_blank" style="display:flex; align-items:center; gap:12px; padding:12px 18px; background:rgba(255,255,255,0.7); border-radius:16px; text-decoration:none; color:#1E1B4B; box-shadow:var(--clay-shadow-sm);">
                    <span style="font-size:24px;">📸</span>
                    <div>
                        <div style="font-weight:700;">Instagram</div>
                        <div style="font-size:0.85rem; color:#5B4E77;">instagram.com/x_estal_nitish</div>
                    </div>
                </a>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col_c2:
        st.markdown('<div class="clay-card"><h3 style="margin-top:0; color:#1E1B4B; font-weight:800;">Send a Quick Note</h3>', unsafe_allow_html=True)
        with st.form("contact_form", clear_on_submit=True):
            name_input = st.text_input("Your Name", placeholder="e.g. Alex Johnson")
            email_input = st.text_input("Your Email", placeholder="e.g. alex@example.com")
            subject_input = st.selectbox(
                "Inquiry Purpose",
                [
                    "🚀 Project Collaboration / Freelance",
                    "💼 Job / Internship Opportunity",
                    "🤝 Open Source Contribution",
                    "💬 General Discussion / Coffee Chat",
                ]
            )
            msg_input = st.text_area("Your Message", placeholder="Tell me about your idea or question...")
            submitted = st.form_submit_button("Send Message 🚀", use_container_width=True)

            if submitted:
                if name_input.strip() and email_input.strip() and msg_input.strip():
                    st.success(f"Thank you, {name_input}! Your note has been recorded. I'll get back to you at {email_input} soon.")
                    st.balloons()
                else:
                    st.warning("Please fill in your name, email, and message before sending.")
        st.markdown('</div>', unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────
# 7. FOOTER
# ─────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="clay-footer">
    <div class="footer-brand">X-Estal Nitish</div>
    <div class="footer-copy">
        Crafted with Claymorphism & Streamlit • © {datetime.datetime.now().year} Nitish Kumar. All rights reserved.
    </div>
</div>
""", unsafe_allow_html=True)
