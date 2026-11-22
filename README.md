# ⚡ X-ESTAL Nitish — Personal AI Engineering Portfolio

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io)
[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12-blue?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-purple.svg)](LICENSE)
[![GitHub](https://img.shields.io/badge/GitHub-XestalNitish-black?logo=github)](https://github.com/XestalNitish)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Nitish_Kumar-blue?logo=linkedin)](https://www.linkedin.com/in/nitish-kumar-33714642b/)

An independent personal engineering portfolio designed for **Nitish Kumar (`X-ESTAL Nitish`)**, specializing in **Agentic AI, LLM Engineering, Hybrid RAG Architectures, and Intelligent Software Systems**.

Designed with the restraint and technical clarity of a professional engineering journal, built for 100% free hosting on **Streamlit Community Cloud** with custom editorial styling, SVG architecture diagrams, and URL query-parameter routing.

---

## 🌟 Live Deployed Applications & Repositories

| Project | Domain | Architecture Highlights | Live Demo / Repository |
| :--- | :--- | :--- | :--- |
| **⚡ Ultimate Coding Agent** *(Flagship)* | Autonomous SWE Multi-Agent Studio | 10-node StateGraph flow, dual local GGUF models (`llama-server`), deterministic AST repair, environment secret scrubbing, LangSmith live tracing | [Repository](https://github.com/XestalNitish/ultimate-coding-agent) |
| **🧠 X-Estal Enterprise Hybrid RAG** *(Flagship)* | Enterprise Hybrid Retrieval | 50/50 BM25 + Chroma MMR, 95.8% retrieval hit rate on 53-question benchmark, SSRF IP defense, Hinglish query normalization | [Repository](https://github.com/XestalNitish/xestal-enterprise-rag-engine) |
| **🔬 X-Estal Research Agent** *(Flagship)* | Autonomous Deep-Web Literature Synthesis | LangGraph `WebSearchState`, recursive web/academic paper scraping, structured dossier synthesis with formal citations | [Launch App 🚀](https://xestal-research-agent-by-x-estal-nitish.streamlit.app/) |
| **💻 Code Dev Agent** | Cloud Autonomous Programming Studio | StateGraph cycle dampeners, pre-execution security audits, automated runtime traceback diagnosis and repair | [Launch App 🚀](https://code-dev-agent-by-x-estal-nitish.streamlit.app) |
| **🔍 Plearun Verified Findings** | Deterministic Incident Verification | 5-step offline forensic verification pipeline: multi-encoding defense (BOM, CP1252, Latin1), clock drift alignment, deterministic scorecard | [Repository](https://github.com/XestalNitish/plearun-verified-findings) |
| **🧠 Brain Tumor Classifier** | Medical Diagnostic Vision AI | Deep Convolutional Neural Networks (CNN) for MRI radiological scan classification across 4 classes with probability distributions | [Launch App 🚀](https://brain-tumor-classifier-by-x-estal-nitish.streamlit.app) |
| **₿ Bitcoin Price Predictor** | Quantitative Financial Forecasting | Deep recurrent LSTM neural networks, real-time indicators (RSI, MACD, moving averages), interactive forecast dashboard | [Launch App 🚀](https://x-estal-nitish-bit-coin-price-predictor.streamlit.app) |

---

## 🏛️ System Architecture & Visual Direction

This portfolio intentionally avoids generic AI template aesthetics (no neon gradients, no random glowing spheres, no fake percentage bars, no cartoon illustrations):
- **Restrained Dark Editorial Aesthetic**: Built with deep dark tones (`#0B0D12` background, `#11151D` elevation, `#171C26` surfaces, `#6D91FF` cobalt accent, `#D6A65D` metric amber).
- **Handcrafted SVG Architecture Sketch**: Real conceptual StateGraph workflow (`Objective → Planning → Tools → Retrieval → Execution → Evaluation`) embedded directly in the hero section.
- **Robust URL Query Routing**: Clean navigation across `Home`, `Projects`, `Case Studies`, `Skills`, `About`, and `Contact` powered by Streamlit's `st.query_params` with full browser back/forward and direct bookmarking support.
- **Empirical Benchmark Rigor**: Documents the real 53-question evaluation dataset from arXiv:2610.30074v1, isolating retrieval hit rate (95.8%) from generation limits (28 of 30 errors attributed to model reasoning rather than retrieval).

---

## 🛠️ Quick Local Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/XestalNitish/portfolio.git
   cd portfolio
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run automated verification tests:**
   ```bash
   python tests/test_services.py
   ```

5. **Run the Streamlit application:**
   ```bash
   streamlit run app.py
   ```

---

## ☁️ Deploy to Streamlit Community Cloud (100% Free)

1. Push this repository to your GitHub account (e.g. `https://github.com/XestalNitish/portfolio`).
2. Go to [share.streamlit.io](https://share.streamlit.io).
3. Click **"New app"**.
4. Select your repository: `XestalNitish/portfolio`, branch: `main`.
5. Set Main file path: `app.py`.
6. Click **"Deploy!"** 🎉

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

Developed by **Nitish Kumar (`X-ESTAL Nitish`)** • [GitHub](https://github.com/XestalNitish) • [LinkedIn](https://www.linkedin.com/in/nitish-kumar-33714642b/)
