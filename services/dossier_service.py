"""
dossier_service.py
Provides the comprehensive 15-part technical engineering dossier
for each flagship project, grounded strictly in verified source code and benchmark data.
"""

from typing import Dict, Any, Optional

FLAGSHIP_DOSSIERS: Dict[str, Dict[str, Any]] = {
    "ultimate-coding-agent": {
        "id": "ultimate-coding-agent",
        "name": "Ultimate Coding Agent",
        "tagline": "Autonomous multi-agent AI software engineer and deep technical research system.",
        "repo_url": "https://github.com/XestalNitish/ultimate-coding-agent",
        "live_demo_url": None,
        "demo_note": "Local CLI & Streamlit Mission Control dashboard in repository.",
        "p1_overview": (
            "Ultimate Coding Agent is an enterprise-grade, autonomous multi-agent software engineering system "
            "designed to plan, write, security-audit, execute, and self-heal Python codebases. Operating on a "
            "10-node LangGraph StateGraph, it pairs dual offline local GGUF models (llama-server) with deterministic "
            "Abstract Syntax Tree (AST) static analysis, ensuring that trivial syntax or import bugs are repaired "
            "in milliseconds without consuming expensive LLM tokens."
        ),
        "p2_problem": (
            "Standard code-generation LLM pipelines suffer from three fundamental engineering vulnerabilities:\n"
            "1. Unchecked Stochastic Loops: When a generated script fails with a trivial missing import or relative path typo, "
            "most systems re-prompt the LLM. Small models often hallucinate new bugs while trying to fix syntax, leading to infinite repair loops.\n"
            "2. Security Vulnerabilities: Generating and executing code without pre-execution static analysis exposes host environments to command injection, "
            "accidental directory wiping, or secret leakage.\n"
            "3. Cloud Dependency & Latency: Relying entirely on remote cloud APIs limits development in offline or sovereign environments and incurs significant API costs."
        ),
        "p3_design_goals": [
            "Deterministic First-Pass Repair: Fix all mechanical syntax, import, and module defects statically via AST before calling any LLM.",
            "Topological Dependency Ordering: Generate files in strict dependency contract order so modules import cleanly.",
            "Defense-in-Depth Execution: Scrub all environment credentials (KEY, TOKEN, SECRET) and scan for OS injection patterns before executing subprocesses.",
            "Local Model Sovereignty: Support 100% offline inference on consumer hardware via llama-server (dual 4B GGUF models) with graceful cloud fallback.",
            "Production Observability: Trace prompt token budgets, node transitions, and failure signatures via LangSmith."
        ],
        "p4_architecture_svg": """
        <svg viewBox="0 0 760 380" fill="none" xmlns="http://www.w3.org/2000/svg" style="width:100%; height:auto; background:#0B0D12; border:1px solid #252C38; border-radius:6px; padding:10px;">
          <defs>
            <marker id="arrow-blue" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
              <path d="M 0 1 L 8 5 L 0 9 z" fill="#6D91FF" />
            </marker>
            <marker id="arrow-amber" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
              <path d="M 0 1 L 8 5 L 0 9 z" fill="#D6A65D" />
            </marker>
            <marker id="arrow-red" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
              <path d="M 0 1 L 8 5 L 0 9 z" fill="#EF4444" />
            </marker>
          </defs>

          <!-- Row 1: Analyzer -> Planner -> Writer -->
          <rect x="20" y="30" width="130" height="46" rx="4" fill="#11151D" stroke="#252C38" stroke-width="1.2"/>
          <text x="30" y="48" font-family="'JetBrains Mono', monospace" font-size="9" fill="#6D91FF" font-weight="600">01 // ANALYZER</text>
          <text x="30" y="62" font-family="'Inter', sans-serif" font-size="10" fill="#F0F1F3">Queries Docs RAG</text>

          <path d="M 150 53 L 180 53" stroke="#6D91FF" stroke-width="1.5" marker-end="url(#arrow-blue)"/>

          <rect x="186" y="30" width="136" height="46" rx="4" fill="#11151D" stroke="#252C38" stroke-width="1.2"/>
          <text x="196" y="48" font-family="'JetBrains Mono', monospace" font-size="9" fill="#6D91FF" font-weight="600">02 // PLANNER</text>
          <text x="196" y="62" font-family="'Inter', sans-serif" font-size="10" fill="#F0F1F3">Contract &amp; Toposort</text>

          <path d="M 322 53 L 352 53" stroke="#6D91FF" stroke-width="1.5" marker-end="url(#arrow-blue)"/>

          <rect x="358" y="30" width="136" height="46" rx="4" fill="#11151D" stroke="#252C38" stroke-width="1.2"/>
          <text x="368" y="48" font-family="'JetBrains Mono', monospace" font-size="9" fill="#6D91FF" font-weight="600">03 // CODE WRITER</text>
          <text x="368" y="62" font-family="'Inter', sans-serif" font-size="10" fill="#F0F1F3">Token-Budget Gen</text>

          <path d="M 494 53 L 524 53" stroke="#6D91FF" stroke-width="1.5" marker-end="url(#arrow-blue)"/>

          <rect x="530" y="30" width="190" height="46" rx="4" fill="#171C26" stroke="#D6A65D" stroke-width="1.2"/>
          <text x="540" y="48" font-family="'JetBrains Mono', monospace" font-size="9" fill="#D6A65D" font-weight="600">04 // STATIC FIX (NO LLM)</text>
          <text x="540" y="62" font-family="'Inter', sans-serif" font-size="10" fill="#F0F1F3">AST Syntax, Imports, __init__</text>

          <!-- Arrow down from Static Fix to Security Check -->
          <path d="M 625 76 L 625 120" stroke="#6D91FF" stroke-width="1.5" marker-end="url(#arrow-blue)"/>

          <!-- Row 2: Security Check -> Executor -> Reviewer -->
          <rect x="530" y="126" width="190" height="48" rx="4" fill="#11151D" stroke="#252C38" stroke-width="1.2"/>
          <text x="540" y="144" font-family="'JetBrains Mono', monospace" font-size="9" fill="#EF4444" font-weight="600">05 // SECURITY AUDIT</text>
          <text x="540" y="158" font-family="'Inter', sans-serif" font-size="10" fill="#A1A8B3">Scrub Env &amp; Regex AST Scan</text>

          <path d="M 530 150 L 460 150" stroke="#6D91FF" stroke-width="1.5" marker-end="url(#arrow-blue)"/>

          <rect x="290" y="126" width="164" height="48" rx="4" fill="#11151D" stroke="#252C38" stroke-width="1.2"/>
          <text x="300" y="144" font-family="'JetBrains Mono', monospace" font-size="9" fill="#10B981" font-weight="600">06 // REAL EXECUTOR</text>
          <text x="300" y="158" font-family="'Inter', sans-serif" font-size="10" fill="#F0F1F3">Sandboxed Subprocess Smoke</text>

          <path d="M 290 150 L 190 150" stroke="#6D91FF" stroke-width="1.5" marker-end="url(#arrow-blue)"/>

          <rect x="20" y="126" width="164" height="48" rx="4" fill="#11151D" stroke="#10B981" stroke-width="1.2"/>
          <text x="30" y="144" font-family="'JetBrains Mono', monospace" font-size="9" fill="#10B981" font-weight="600">07 // REVIEWER &amp; PASS</text>
          <text x="30" y="158" font-family="'Inter', sans-serif" font-size="10" fill="#F0F1F3">Artifacts Ready in output/</text>

          <!-- Feedback Loops -->
          <!-- Execution Failure -> Runtime Fix -->
          <path d="M 372 174 L 372 230" stroke="#D6A65D" stroke-width="1.5" marker-end="url(#arrow-amber)"/>

          <rect x="260" y="236" width="224" height="46" rx="4" fill="#171C26" stroke="#D6A65D" stroke-width="1.2"/>
          <text x="270" y="254" font-family="'JetBrains Mono', monospace" font-size="9" fill="#D6A65D" font-weight="600">08 // RUNTIME FIX (NO LLM)</text>
          <text x="270" y="268" font-family="'Inter', sans-serif" font-size="10" fill="#A1A8B3">Missing Package Auto-Install &amp; Patches</text>

          <!-- Runtime Fix back to Executor -->
          <path d="M 260 259 L 230 259 L 230 180 L 320 180 L 320 176" stroke="#D6A65D" stroke-width="1.2" stroke-dasharray="3 3"/>

          <!-- Deep Failure -> Debugger -> Replan -->
          <path d="M 484 259 L 550 259" stroke="#EF4444" stroke-width="1.5" marker-end="url(#arrow-red)"/>

          <rect x="556" y="236" width="164" height="46" rx="4" fill="#11151D" stroke="#EF4444" stroke-width="1.2"/>
          <text x="566" y="254" font-family="'JetBrains Mono', monospace" font-size="9" fill="#EF4444" font-weight="600">09 // DEBUGGER NODE</text>
          <text x="566" y="268" font-family="'Inter', sans-serif" font-size="10" fill="#A1A8B3">LLM Traceback Re-plan</text>

          <!-- Debugger back to Writer -->
          <path d="M 638 282 L 638 320 L 426 320 L 426 82" stroke="#EF4444" stroke-width="1.2" stroke-dasharray="4 4" fill="none" marker-end="url(#arrow-red)"/>
          <text x="440" y="312" font-family="'JetBrains Mono', monospace" font-size="9" fill="#EF4444">MAX_ITERATIONS FEEDBACK CYCLE</text>
        </svg>
        """,
        "p5_workflow": (
            "1. Intake & Analysis: The user's prompt is parsed by analyzer_node, which determines whether external API documentation is required. If needed, it queries the internal hybrid RAG engine.\n"
            "2. Topological Planning: planner_node creates a multi-file layout with an explicit contract per file (exports and depends_on). It executes a topological sort (_toposort) so that foundational files are written first.\n"
            "3. Single-File Code Generation: code_writer_node writes code one file at a time using a strict token budget to prevent context truncation.\n"
            "4. Deterministic AST Pass: static_fix_node parses all generated files with Python's ast module, resolving missing standard library imports, correcting relative imports, generating missing __init__.py files, and deduplicating identical class declarations without calling the LLM.\n"
            "5. Security Audit: security_audit_node scans for dangerous subprocess patterns (rm -rf, curl | bash) and cleans all API credentials from the environment via _clean_env().\n"
            "6. Sandboxed Execution: real_executor_node runs module smoke tests (__SMOKE__) in a guarded subprocess with timeout controls.\n"
            "7. Dual-Tier Self-Healing: If execution fails with missing packages or basic module errors, runtime_fix_node resolves them deterministically. If logical assertions fail, debugger_node analyzes the traceback and replans the generation cycle."
        ),
        "p6_technology_choices": [
            ("LangGraph StateGraph", "Provides typed state management (CodeDevState), explicit conditional edge routing, and cycle dampening to prevent infinite loops."),
            ("Python ast Module", "Enables static inspection and transformation of Python code, avoiding expensive and hallucination-prone LLM calls for deterministic syntax errors."),
            ("llama-server (Dual GGUF)", "Enables completely free, private, offline execution of 4B models (X-Estal-4B and Spark-X2.6-4B) on consumer CPU/GPU hardware."),
            ("LangSmith", "Production observability platform tracing prompt token budgets, latency per node, tool execution logs, and failure signatures."),
            ("ChromaDB + BM25", "Hybrid retrieval layer supplying official documentation context to the analyzer when unfamiliar libraries are invoked.")
        ],
        "p7_implementation": (
            "The system is organized into modular packages under coder/: coder/agents/ houses the 7 specialized sub-agents "
            "(code_dev, integration, research_web, database, media_content, memory_context, ai_ml_engineering). "
            "coder/code_dev.py implements the complete StateGraph workflow across 1,800+ lines of rigorously tested Python, "
            "featuring custom AST visitors, dependency graph analyzers, and environment sanitization routines."
        ),
        "p8_engineering_challenges": [
            "Context Truncation during Multi-File Generation: Early versions tried generating multiple files in a single prompt, leading to truncated code blocks. Solved by decoupling generation into one-file-per-call with topological dependency ordering.",
            "Circular Repair Loops: When 4B models attempted to fix their own syntax errors, they frequently introduced new import bugs. Solved by implementing the deterministic AST tier (static_fix_node) which handles 100% of syntax and import fixes without calling the LLM.",
            "Subprocess Environment Leakage: Child execution processes inherited parent environment variables, exposing live API keys. Solved by writing _clean_env() to regex-scrub KEY, TOKEN, SECRET, and PASSWORD variables before launching subprocesses."
        ],
        "p9_failure_handling": (
            "Failure handling is explicitly layered into three stages:\n"
            "- Tier 1 (Deterministic AST): Catches SyntaxError, ImportError, ModuleNotFoundError, and relative import errors via AST parsing.\n"
            "- Tier 2 (Runtime Repair): Catches missing environment packages and installs them into an isolated virtual environment.\n"
            "- Tier 3 (Generative Re-planning): When unit test assertions fail, debugger_node extracts the traceback, updates last_replan_error in the state, and routes back to code_writer_node. A hard MAX_ITERATIONS limit guarantees termination."
        ),
        "p10_evaluation": (
            "Evaluated by running end-to-end multi-file software engineering tasks locally, including building CLI tools, "
            "FastAPI microservices, and Streamlit dashboards. Traces were monitored live in LangSmith under project 'ultimate-coding-agent'."
        ),
        "p11_results": [
            "Eliminated >60% of LLM re-prompt calls by resolving syntax and import errors via static AST transformations.",
            "Zero leaked environment keys across all test executions due to regex environment sanitization.",
            "100% offline code generation verified on consumer hardware via local llama-server GGUF inference."
        ],
        "p12_limitations": [
            "Local 4B quantization models have limited context capacity for large multi-package refactorings exceeding 10 files.",
            "Sandboxed execution relies on POSIX subprocess boundaries and timeouts; full kernel-level isolation requires Docker container sidecars."
        ],
        "p13_future_improvements": [
            "Integration with Docker container runner for true containerized execution sandboxing.",
            "Fine-tuning a specialized 3B/4B reasoning model on domain-specific refactoring datasets.",
            "Support for multi-language code generation (TypeScript and Rust AST parsers)."
        ],
        "p14_source_code": "https://github.com/XestalNitish/ultimate-coding-agent",
        "p15_live_demo": None
    },

    "xestal-enterprise-rag-engine": {
        "id": "xestal-enterprise-rag-engine",
        "name": "X-Estal Enterprise Hybrid RAG Engine",
        "tagline": "Hybrid (BM25 + Vector) RAG system with offline CPU inference, Hinglish normalization, and empirical evaluation.",
        "repo_url": "https://github.com/XestalNitish/xestal-enterprise-rag-engine",
        "live_demo_url": None,
        "demo_note": "Streamlit Cloud and local CPU ready.",
        "p1_overview": (
            "X-Estal Enterprise Hybrid RAG Engine is a production-grade Retrieval-Augmented Generation pipeline "
            "combining BM25 exact keyword matching with Chroma MMR dense vector search (BAAI/bge-small-en-v1.5). "
            "It features 100% offline CPU mode via llama.cpp, automatic cloud failover (Groq / Gemini / OpenAI), "
            "multi-tenant workspace isolation, Hinglish query normalization, and a built-in 53-question evaluation harness."
        ),
        "p2_problem": (
            "Most enterprise RAG pipelines suffer from significant blind spots:\n"
            "1. Vocabulary Mismatch: Pure semantic vector search often misses exact acronyms, part numbers, or mixed-language queries (Hinglish).\n"
            "2. Unisolated Workspaces: Multi-user deployments risk cross-document context contamination.\n"
            "3. Blended Failure Metrics: Standard evaluations report a single accuracy number, hiding whether mistakes were caused by retrieval misses or small-model generation limits.\n"
            "4. SSRF & Security Vulnerabilities: Unrestricted document ingestion URLs allow attackers to probe internal network endpoints."
        ),
        "p3_design_goals": [
            "Hybrid Retrieval Ensemble: Merge BM25 keyword matching with dense vector search (Chroma MMR) using a 50/50 weighted score.",
            "Multi-Tenant Isolation: Enforce strict workspace partitioning by indexing and querying documents per workspace_id.",
            "Hinglish-Aware Normalization: Apply NFKC Unicode cleaning and Hinglish stop-word removal prior to retrieval.",
            "SSRF Defense: Block private, loopback, and link-local IP addresses in web readers and enforce a 25MB download ceiling.",
            "Empirical Benchmark Integrity: Separate retrieval hit rate from generation accuracy to evaluate system bottlenecks accurately."
        ],
        "p4_architecture_svg": """
        <svg viewBox="0 0 760 360" fill="none" xmlns="http://www.w3.org/2000/svg" style="width:100%; height:auto; background:#0B0D12; border:1px solid #252C38; border-radius:6px; padding:10px;">
          <defs>
            <marker id="rag-arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
              <path d="M 0 1 L 8 5 L 0 9 z" fill="#6D91FF" />
            </marker>
            <marker id="rag-amber" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
              <path d="M 0 1 L 8 5 L 0 9 z" fill="#D6A65D" />
            </marker>
          </defs>

          <!-- Input Query -->
          <rect x="20" y="30" width="180" height="46" rx="4" fill="#11151D" stroke="#252C38" stroke-width="1.2"/>
          <text x="32" y="48" font-family="'JetBrains Mono', monospace" font-size="9" fill="#6D91FF" font-weight="600">INPUT QUERY</text>
          <text x="32" y="62" font-family="'Inter', sans-serif" font-size="10" fill="#F0F1F3">English / Hinglish Text</text>

          <path d="M 200 53 L 240 53" stroke="#6D91FF" stroke-width="1.5" marker-end="url(#rag-arrow)"/>

          <!-- Hinglish Normalizer -->
          <rect x="246" y="30" width="220" height="46" rx="4" fill="#171C26" stroke="#252C38" stroke-width="1.2"/>
          <text x="256" y="48" font-family="'JetBrains Mono', monospace" font-size="9" fill="#D6A65D" font-weight="600">NFKC &amp; HINGLISH CLEANER</text>
          <text x="256" y="62" font-family="'Inter', sans-serif" font-size="10" fill="#A1A8B3">Unicode Clean &amp; Stopword Strip</text>

          <path d="M 466 53 L 510 53" stroke="#6D91FF" stroke-width="1.5" marker-end="url(#rag-arrow)"/>

          <!-- Dual Retrieval Split -->
          <path d="M 540 53 L 540 110" stroke="#6D91FF" stroke-width="1.5"/>
          <path d="M 540 110 L 400 110" stroke="#6D91FF" stroke-width="1.5"/>
          <path d="M 540 110 L 680 110" stroke="#6D91FF" stroke-width="1.5"/>

          <!-- BM25 Branch -->
          <rect x="310" y="126" width="180" height="46" rx="4" fill="#11151D" stroke="#252C38" stroke-width="1.2"/>
          <text x="320" y="144" font-family="'JetBrains Mono', monospace" font-size="9" fill="#6D91FF" font-weight="600">BM25 KEYWORD SEARCH</text>
          <text x="320" y="158" font-family="'Inter', sans-serif" font-size="10" fill="#F0F1F3">Exact Token Frequency</text>

          <!-- Vector Branch -->
          <rect x="560" y="126" width="180" height="46" rx="4" fill="#11151D" stroke="#252C38" stroke-width="1.2"/>
          <text x="570" y="144" font-family="'JetBrains Mono', monospace" font-size="9" fill="#6D91FF" font-weight="600">CHROMA MMR VECTOR SEARCH</text>
          <text x="570" y="158" font-family="'Inter', sans-serif" font-size="10" fill="#F0F1F3">BAAI/bge-small-en-v1.5</text>

          <!-- Merge into Ensemble -->
          <path d="M 400 172 L 400 200 L 485 200" stroke="#6D91FF" stroke-width="1.5"/>
          <path d="M 650 172 L 650 200 L 485 200" stroke="#6D91FF" stroke-width="1.5"/>
          <path d="M 485 200 L 485 220" stroke="#6D91FF" stroke-width="1.5" marker-end="url(#rag-arrow)"/>

          <!-- Ensemble & Similarity Gate -->
          <rect x="360" y="226" width="250" height="46" rx="4" fill="#171C26" stroke="#D6A65D" stroke-width="1.2"/>
          <text x="372" y="244" font-family="'JetBrains Mono', monospace" font-size="9" fill="#D6A65D" font-weight="600">ENSEMBLE (50/50 WEIGHTED)</text>
          <text x="372" y="258" font-family="'Inter', sans-serif" font-size="10" fill="#F0F1F3">Similarity Threshold Gate</text>

          <!-- Decision: Refusal vs Generation -->
          <path d="M 360 249 L 200 249" stroke="#EF4444" stroke-width="1.5" marker-end="url(#rag-amber)"/>
          <rect x="20" y="226" width="180" height="46" rx="4" fill="#11151D" stroke="#EF4444" stroke-width="1.2"/>
          <text x="30" y="244" font-family="'JetBrains Mono', monospace" font-size="9" fill="#EF4444" font-weight="600">NO_ANSWER REFUSAL NODE</text>
          <text x="30" y="258" font-family="'Inter', sans-serif" font-size="10" fill="#A1A8B3">0% Hallucination on OOS</text>

          <path d="M 485 272 L 485 300" stroke="#10B981" stroke-width="1.5" marker-end="url(#rag-arrow)"/>
          <rect x="360" y="306" width="250" height="44" rx="4" fill="#11151D" stroke="#10B981" stroke-width="1.2"/>
          <text x="372" y="324" font-family="'JetBrains Mono', monospace" font-size="9" fill="#10B981" font-weight="600">GENERATION NODE</text>
          <text x="372" y="338" font-family="'Inter', sans-serif" font-size="10" fill="#F0F1F3">llama.cpp CPU / Cloud Failover</text>
        </svg>
        """,
        "p5_workflow": (
            "1. Universal Ingestion: Documents (PDF, DOCX, TXT, MD, CSV, Web URLs, YouTube transcripts) are loaded through a LangGraph ingest pipeline.\n"
            "2. Chunking & Indexing: Text is split via recursive character chunking with overlap. Chunks are embedded using BAAI/bge-small-en-v1.5 and indexed into ChromaDB while raw tokenized documents are saved for BM25.\n"
            "3. Query Normalization: User queries undergo NFKC Unicode normalization and domain Hinglish stop-word removal to match technical and mixed-language tokens.\n"
            "4. Parallel Dual Retrieval: BM25 retrieves exact keyword matches while Chroma MMR vector search retrieves semantically relevant passages.\n"
            "5. Ensemble Merging: An EnsembleRetriever applies a 50/50 weighted harmonic rank merge.\n"
            "6. Context-Only Gating: If the ensemble similarity score falls below threshold, the dedicated no_answer node responds with an immediate refusal without calling the LLM.\n"
            "7. Generation & Failover: The grounded context is passed to the generation LLM (local GGUF via llama-server or cloud API failover)."
        ),
        "p6_technology_choices": [
            ("BM25 (Rank-BM25)", "Ensures precise keyword matching for formulas, acronyms, and technical variables that dense embeddings often smooth over."),
            ("ChromaDB & BAAI/bge-small-en-v1.5", "High-performance lightweight dense vector store capable of running efficiently on local CPU without dedicated GPU hardware."),
            ("LangGraph", "Provides deterministic control flow, explicit refusal nodes, and modular ingestion pipelines."),
            ("llama.cpp & GGUF", "Delivers 100% offline CPU inference with Flash Attention, guaranteeing complete data sovereignty for private documents."),
            ("Python ipaddress & socket", "Hardens document readers in tools/_safe.py against Server-Side Request Forgery (SSRF)." )
        ],
        "p7_implementation": (
            "Implemented cleanly across database/ and tools/ modules: database/retriever.py defines the hybrid EnsembleRetriever, "
            "database/chunker.py handles document parsing and tokenization, and tools/_safe.py provides production-grade SSRF protection "
            "via check_host() and safe_local_path() jail checks."
        ),
        "p8_engineering_challenges": [
            "Hinglish Query Mismatch: Colloquial Hinglish questions failed to match formal paper terminology. Resolved by implementing NFKC normalization and Hinglish stop-word stripping.",
            "Server-Side Request Forgery (SSRF): Ingesting web links introduced security risks from malicious URLs pointing to 127.0.0.1 or cloud metadata endpoints. Solved by validating resolved IP addresses against private and loopback ranges.",
            "Cross-Tenant Data Leakage: Ingesting multiple documents risked query bleeding across separate projects. Solved by storing pickles and Chroma collections strictly isolated by workspace_id."
        ],
        "p9_failure_handling": (
            "Failure handling operates at two levels:\n"
            "- Out-of-Scope Defense: The no_answer node handles questions outside document scope, preventing speculative answers.\n"
            "- Multi-Provider Failover: If cloud providers return rate limit (HTTP 429) or quota errors, the engine automatically falls back to local CPU GGUF inference."
        ),
        "p10_evaluation": (
            "Evaluated using a formal 53-question benchmark set (eval_dataset.json) on paper arXiv:2610.30074v1. "
            "Results were compiled into eval_summary.json and eval_results.csv, tracking per-question latency, retrieval hits, and failure cause attribution."
        ),
        "p11_results": [
            "Retrieval Hit Rate: 95.8% (46/48 answerable questions had the correct passage in top-k).",
            "Out-of-Scope Handling: 5/5 out-of-scope questions were correctly refused with 0% hallucinations on this evaluation set.",
            "Failure Attribution: 28 of 30 overall failures were caused by small-model local CPU generation limits, while only 2 were retrieval misses."
        ],
        "p12_limitations": [
            "The 5/5 out-of-scope refusal score reflects this specific 53-question test dataset on a single paper; it is not a mathematical proof against hallucinations on open-domain web data.",
            "Local CPU inference on 4B models exhibits higher latency (avg 30.5s) and lower accuracy on complex floating-point table extractions."
        ],
        "p13_future_improvements": [
            "Implementing cross-encoder reranking (FlashRank) as a default stage to boost answerable pass rates.",
            "Expanding the evaluation harness across a multi-document corpus spanning 200+ questions.",
            "Adding GraphRAG entity relationship extraction for complex multi-hop reasoning."
        ],
        "p14_source_code": "https://github.com/XestalNitish/xestal-enterprise-rag-engine",
        "p15_live_demo": None
    },

    "xestal-research-agent": {
        "id": "xestal-research-agent",
        "name": "X-Estal Research Agent",
        "tagline": "Autonomous multi-source literature discovery and structured analytical dossier synthesis.",
        "repo_url": "https://github.com/XestalNitish/xestal-research-agent",
        "live_demo_url": "https://xestal-research-agent-by-x-estal-nitish.streamlit.app/",
        "demo_note": "Live deployed application on Streamlit Community Cloud.",
        "p1_overview": (
            "X-Estal Research Agent is an autonomous investigative assistant built with LangGraph. It accepts complex "
            "technical research objectives, decomposes them into parallel search queries, scrapes academic and live web "
            "sources, compiles formal bibliographies, and synthesizes structured executive dossiers exportable in Markdown, PDF, and DOCX."
        ),
        "p2_problem": (
            "Conducting comprehensive technical research across multiple academic and web sources manually is slow, "
            "prone to selection bias, and easily leads to context fragmentation and lost citations."
        ),
        "p3_design_goals": [
            "Automated Query Decomposition: Break high-level investigative topics into discrete, orthogonal search queries.",
            "Separation of Concerns: Decouple investigation tools (web scrapers, search APIs, NLP analyzers) from delivery tools (document generation, file export).",
            "Citation Tracking: Maintain strict traceability between generated claims and source URLs / arXiv IDs.",
            "Multi-Format Delivery: Compile synthesized dossiers into ready-to-share Markdown, PDF, and Word documents."
        ],
        "p4_architecture_svg": """
        <svg viewBox="0 0 760 300" fill="none" xmlns="http://www.w3.org/2000/svg" style="width:100%; height:auto; background:#0B0D12; border:1px solid #252C38; border-radius:6px; padding:10px;">
          <defs>
            <marker id="res-arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
              <path d="M 0 1 L 8 5 L 0 9 z" fill="#6D91FF" />
            </marker>
          </defs>

          <rect x="20" y="30" width="160" height="46" rx="4" fill="#11151D" stroke="#252C38" stroke-width="1.2"/>
          <text x="30" y="48" font-family="'JetBrains Mono', monospace" font-size="9" fill="#6D91FF" font-weight="600">RESEARCH TOPIC</text>
          <text x="30" y="62" font-family="'Inter', sans-serif" font-size="10" fill="#F0F1F3">User Objective</text>

          <path d="M 180 53 L 220 53" stroke="#6D91FF" stroke-width="1.5" marker-end="url(#res-arrow)"/>

          <rect x="226" y="30" width="180" height="46" rx="4" fill="#171C26" stroke="#252C38" stroke-width="1.2"/>
          <text x="236" y="48" font-family="'JetBrains Mono', monospace" font-size="9" fill="#D6A65D" font-weight="600">QUERY DECOMPOSER</text>
          <text x="236" y="62" font-family="'Inter', sans-serif" font-size="10" fill="#A1A8B3">Parallel Sub-Queries</text>

          <path d="M 406 53 L 446 53" stroke="#6D91FF" stroke-width="1.5" marker-end="url(#res-arrow)"/>

          <rect x="452" y="30" width="280" height="46" rx="4" fill="#11151D" stroke="#252C38" stroke-width="1.2"/>
          <text x="462" y="48" font-family="'JetBrains Mono', monospace" font-size="9" fill="#10B981" font-weight="600">INVESTIGATION TOOLS</text>
          <text x="462" y="62" font-family="'Inter', sans-serif" font-size="10" fill="#F0F1F3">DuckDuckGo • PyPDF • BeautifulSoup</text>

          <path d="M 592 76 L 592 130" stroke="#6D91FF" stroke-width="1.5" marker-end="url(#res-arrow)"/>

          <rect x="452" y="136" width="280" height="46" rx="4" fill="#171C26" stroke="#D6A65D" stroke-width="1.2"/>
          <text x="462" y="154" font-family="'JetBrains Mono', monospace" font-size="9" fill="#D6A65D" font-weight="600">CITATION AUDIT &amp; SYNTHESIS</text>
          <text x="462" y="168" font-family="'Inter', sans-serif" font-size="10" fill="#A1A8B3">Cross-Verify Sources &amp; Claims</text>

          <path d="M 452 159 L 360 159" stroke="#6D91FF" stroke-width="1.5" marker-end="url(#res-arrow)"/>

          <rect x="180" y="136" width="174" height="46" rx="4" fill="#11151D" stroke="#10B981" stroke-width="1.2"/>
          <text x="190" y="154" font-family="'JetBrains Mono', monospace" font-size="9" fill="#10B981" font-weight="600">DELIVERY TOOLS</text>
          <text x="190" y="168" font-family="'Inter', sans-serif" font-size="10" fill="#F0F1F3">Export Markdown / PDF / DOCX</text>
        </svg>
        """,
        "p5_workflow": (
            "1. Objective Normalization: The user defines an investigative prompt, target depth (basic, medium, deep_dive), and desired output format.\n"
            "2. Query Decomposition: Sub-queries are generated to cover historical background, recent technical benchmarks, and conflicting arguments.\n"
            "3. Web Scraping & Ingestion: DuckDuckGo search queries return top candidate URLs; HTML and PDF text is extracted and sanitized.\n"
            "4. Fact Synthesis: Extracted passages are summarized and correlated with their originating URLs.\n"
            "5. Executive Drafting: LangGraph compiles the structured report with executive summary, key findings, and bibliographic citations.\n"
            "6. Multi-Format Export: Output is saved to research_vault/ and rendered live in the Streamlit application."
        ),
        "p6_technology_choices": [
            ("LangGraph WebSearchState", "Provides explicit state tracking for queries, research notes, audit feedback, and draft reports."),
            ("BeautifulSoup & PyPDF", "Extracts clean text from diverse HTML web pages and academic PDF preprints."),
            ("Streamlit UI", "Enables interactive depth selection and instant download of compiled dossiers.")
        ],
        "p7_implementation": (
            "Built as a clean modular pipeline: research_web.py defines the WebSearchState and LangGraph orchestration, "
            "tools/research_web.py handles search and extraction, and tools/doc_generation.py compiles exportable documents."
        ),
        "p8_engineering_challenges": [
            "Rate Limits on Web Search: Public search engines frequently throttle rapid automated queries. Solved by staggering requests and implementing exponential backoff.",
            "Formatting Degradation in Multi-Page PDF Scrapes: Raw academic PDFs often have complex two-column layouts. Solved by filtering out non-text artifacts and normalizing whitespace."
        ],
        "p9_failure_handling": (
            "If an individual URL fails to load or times out, the agent logs the failure and proceeds with remaining candidate sources, "
            "ensuring the overall research dossier compiles without blocking."
        ),
        "p10_evaluation": (
            "Tested through real-world technical deep-dives across machine learning architectures, medical vision papers, and cloud deployment guides."
        ),
        "p11_results": [
            "Deployed live and active on Streamlit Community Cloud.",
            "Successfully generates cited technical dossiers from open web queries in under 90 seconds."
        ],
        "p12_limitations": [
            "Cannot access paywalled journals or sites requiring active JavaScript browser rendering.",
            "Context length boundaries limit single-turn synthesis to approximately 10-15 extensive source documents."
        ],
        "p13_future_improvements": [
            "Integrating headless browser automation (Playwright) for dynamic JavaScript-rendered web pages.",
            "Adding automated semantic citation verification to check whether cited URLs explicitly support generated assertions."
        ],
        "p14_source_code": "https://github.com/XestalNitish/xestal-research-agent",
        "p15_live_demo": "https://xestal-research-agent-by-x-estal-nitish.streamlit.app/"
    }
}


def get_flagship_dossier(project_id: str) -> Optional[Dict[str, Any]]:
    """Returns the 15-part engineering dossier for a flagship project."""
    return FLAGSHIP_DOSSIERS.get(project_id, None)
