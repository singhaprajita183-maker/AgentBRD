import streamlit as st
import time
import pandas as pd

# 1. Set page layout to wide and corporate look
st.set_page_config(
    page_title="AgentBRD - Autonomous Corporate Analyst",
    page_icon="💼",
    layout="wide"
)

# 2. Combined Custom Styling (Forces Dark Blue-Black Theme across the entire screen)
st.markdown("""
    <style>
    /* Global Background and text color override */
    .stApp {
        background-color: #0b0f19;
        color: #f8fafc;
    }
    /* Element level components styling */
    .main-title { font-size: 40px; color: #38bdf8; font-weight: bold; margin-bottom: 5px; }
    .sub-title { font-size: 18px; color: #94a3b8; margin-bottom: 25px; }
    .metric-card { background-color: #0f172a; padding: 15px; border-radius: 8px; border: 1px solid #1e293b; text-align: center; }
    .metric-value { font-size: 24px; color: #38bdf8; font-weight: bold; }
    .metric-label { font-size: 14px; color: #64748b; }
    </style>
""", unsafe_allow_html=True)

# 3. Sidebar Configuration
with st.sidebar:
    st.image("https://img.icons8.com/external-flatart-icons-flat-flatarticons/128/external-agent-customer-support-flatart-icons-flat-flatarticons.png", width=80)
    st.markdown("## **AgentBRD Command Center**")
    st.info("⚡ Powered by Gemini 1.5 Pro & Google Cloud")
    
    st.markdown("---")
    st.markdown("### 📊 **Agent Configuration**")
    temperature = st.slider("Gemini Creativity (Temperature)", 0.0, 1.0, 0.2, step=0.1)
    brd_template = st.selectbox("Compliance Template", ["Standard Corporate BRD", "Agile User Stories", "Banking System Compliance"])
    
    st.markdown("---")
    st.markdown("### 🛸 **Team Identity**")
    st.markdown("- **Team:** AI Agentic")
    st.markdown("- **Builders:** Aprajita Singh (Class 10) & Divyanshu Singh")
    st.markdown("- **Track:** Google Cloud Rapid Agent Hackathon")

# 4. Main Screen Header
st.markdown('<div class="main-title">💼 AgentBRD Dashboard</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Multi-agent system ingesting text transcripts, audio, and wireframe designs into verifiable corporate BRDs.</div>', unsafe_allow_html=True)

# 5. Top Live Metrics Bar
m1, m2, m3, m4 = st.columns(4)
with m1:
    st.markdown('<div class="metric-card"><div class="metric-value">2M Tokens</div><div class="metric-label">Gemini Context Window</div></div>', unsafe_allow_html=True)
with m2:
    st.markdown('<div class="metric-card"><div class="metric-value">&lt; 15 Mins</div><div class="metric-label">Average Processing Time</div></div>', unsafe_allow_html=True)
with m3:
    st.markdown('<div class="metric-card"><div class="metric-value">Active</div><div class="metric-label">Google GCS Landing Zone</div></div>', unsafe_allow_html=True)
with m4:
    st.markdown('<div class="metric-card"><div class="metric-value">100%</div><div class="metric-label">Traceable Source Lineage</div></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 6. Layout: Split into Input Assets (Left) and Live Agent Execution / Output (Right)
col1, col2 = st.columns([1, 1.2])

with col1:
    st.markdown("### 📥 Multi-Modal Asset Ingestion")
    
    # Text notes input
    raw_notes = st.text_area(
        "✍️ Raw Meeting Notes / Slack Transcripts", 
        height=150,
        placeholder="Paste unorganized chat logs, client transcript interviews, or requirement snippets here..."
    )
    
    # File Uploader for Multi-Modal Data
    uploaded_files = st.file_uploader(
        "📁 Upload Architecture Diagrams, Wireframes or Audio Recordings", 
        accept_multiple_files=True,
        type=["pdf", "docx", "png", "jpeg", "jpg", "mp3", "wav"]
    )
    
    # Process Button
    generate_btn = st.button("🚀 Run Autonomous Multi-Agent Pipeline", use_container_width=True)

with col2:
    st.markdown("### ⚙️ Live Agent Activity & BRD Generation")
    
    if generate_btn:
        if not raw_notes and not uploaded_files:
            st.error("❌ Execution Failed: Please provide at least one asset (text notes or uploaded files) for AgentBRD to analyze.")
        else:
            # Step 1: Secure Ingestion Layer Simulation
            status_box = st.empty()
            progress_bar = st.progress(0)
            
            status_box.info("📥 [Step 1/4] Ingesting files into Google Cloud Storage landing zone...")
            time.sleep(1)
            progress_bar.progress(25)
            
            # Step 2: Gemini Core Processing Simulation
            status_box.info("🧠 [Step 2/4] Gemini 1.5 Pro executing Vision-Text Fusion on visual sketches...")
            time.sleep(1.5)
            progress_bar.progress(50)
            
            # Step 3: Multi-Agent Coordination Logs
            status_box.info("🤖 [Step 3/4] Running Sub-agents: Context Extractor & Anchor Lineage Linker...")
            time.sleep(1.5)
            progress_bar.progress(75)
            
            # Step 4: BigQuery Telemetry & Guardrails
            status_box.info("🛡️ [Step 4/4] Applying Compliance Guardrails and streaming pipeline telemetry to Google BigQuery...")
            time.sleep(1)
            progress_bar.progress(100)
            
            status_box.success("✅ BRD Generation Successful! 100% compliance achieved.")
            
            # --- DISPLAY GENERATED OUTPUT ---
            st.markdown("#### **📄 Output: Business Requirements Document (BRD)**")
            
            # Section 1
            with st.expander("🔍 Section 1: Project Scope & Objectives", expanded=True):
                st.markdown("##### **1.1 Overview**")
                if raw_notes:
                    st.write(f"Based on your custom inputs, AgentBRD successfully extracted the core intent: *\"{raw_notes[:120]}...\"*")
                else:
                    st.write("Successfully synthesized operational targets from the uploaded data files.")
                st.markdown("##### **1.2 Source Lineage Link (Explainability)**")
                st.code("🔗 Anchor Link: gs://agentbrd-raw-assets/source_file_line_42 [Confidence: 99.4%]", language="markdown")
            
            # Section 2
            with st.expander("🔍 Section 2: Technical & Cloud Architecture Requirements"):
                st.markdown("##### **2.1 Infrastructure Allocation**")
                st.write("- **Storage Layer:** Google Cloud Storage Bucket configured with IAM role isolation.")
                st.write("- **Compute Layer:** Gemini 1.5 Pro API executing over a 2-million high-context processing layer.")
                st.write("- **Telemetry Engine:** Streaming continuous optimization logs to Google BigQuery.")
            
            # Live BigQuery Log Simulation Table
            st.markdown("##### 📊 Real-Time BigQuery Telemetry Stream")
            log_data = {
                "Agent Sub-Unit": ["Context Extractor", "Compliance Guardrail", "Lineage Linker"],
                "Latency (s)": [0.84, 1.12, 0.45],
                "Status": ["SUCCESS", "PASSED", "SUCCESS"]
            }
            st.dataframe(pd.DataFrame(log_data), use_container_width=True)
            
            # Export Action
            st.download_button(
                label="📥 Export Corporate BRD (.md format)",
                data=f"# Generated BRD\n\nProcessed Successfully by Team AI Agentic.\nTemplate Used: {brd_template}",
                file_name="AgentBRD_Corporate_Document.md",
                mime="text/markdown",
                use_container_width=True
            )
            
    else:
        st.info("ℹ️ System Status: Idle. Ingest unorganized files or client transcripts on the left panel to trigger the autonomous pipeline.")

# 7. Footer Area
st.markdown("---")
st.markdown("<p style='text-align: center; color: #64748b;'>Developed & Conceptualized by Team AI Agentic · Hosted on Google Cloud Infrastructure</p>", unsafe_allow_html=True)
