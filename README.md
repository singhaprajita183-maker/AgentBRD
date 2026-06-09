# AgentBRD
Multi-modal AI agent built with Gemini 1.5 Pro to transform unstructured business data into standard corporate BRD documents.
==================================================================================
                           AGENTBRD ARCHITECTural BLUEPRINT
==================================================================================

  [📥 INPUT SOURCE LAYER]
  ├── Unstructured Audio (Client Meetings, MP3/WAV)
  ├── Visual Assets (Whiteboard Sketches, UI Wireframes, PNG/JPEG)
  ├── Fragmented Text (Slack Export, WhatsApp Chats, Legacy PDFs)
  └── Transcripts (PO Notes, Markdown)
            │
            ▼
  [🛡️ SECURE INGESTION GATEWAY]
  └── Streamlit Web UI Platform ──► Uploads to ──► Google Cloud Storage (GCS Bucket)
                                                         │
                                                         ▼
  [🧠 CORE AI PROCESSING ENGINE (Gemini 1.5 Pro Layer)] ◄┘
  ├── Massive Context Window Parsing (Up to 2 Million Tokens)
  ├── Vision-Text Fusion Engine (Deducing Technical Logic from Visual Diagrams)
  └── Multi-Agent Framework Coordination
            │
            ├───► [🔍 SUB-AGENT 1: Context Extractor]
            ├───► [🔍 SUB-AGENT 2: Structural Compliance Checker]
            └───► [🔍 SUB-AGENT 3: Anchor Lineage Linker]
            │
            ▼
  [⚡ ENTERPRISE VALIDATION & TELEMETRY LAYER]
  ├── Guardrails Engine ──► (Eliminates Hallucinations & Structural Anomalies)
  └── Real-time Telemetry ──► Streams System Logs to ──► Google BigQuery Analytics
            │
            ▼
  [📤 OUTPUT & EXPORT LAYER]
  ├── Standardized Corporate BRD Generation (Production-Grade Markdown)
  ├── Traceability Maps (Embedded Anchor Links pointing back to GCS Source Files)
  └── Future Pipeline Integration Bridge ──► (Auto-decomposition to Jira/GitHub)

==================================================================================
       Designed & Built by Team AI Agentic · Aprajita Singh (Class 10)
==================================================================================
<img width="1024" height="559" alt="image" src="https://github.com/user-attachments/assets/227ce876-9c37-4cf9-8bf0-2bba265d312b" />

### 🦊 Partner Integration: GitLab MCP Server
AgentBRD is integrated with the **GitLab MCP Server**. Once the autonomous multi-agent pipeline finalizes the production-grade Corporate BRD, the integration bridge automatically connects to the enterprise GitLab instance. It decomposes the BRD requirements into actionable GitLab Issues and pushes the generated Markdown documentation directly into the project's GitLab repository for developer handoff.
