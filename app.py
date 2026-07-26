import os
import streamlit as st
from google import genai
from google.genai import types
from dotenv import load_dotenv

# Load Environment Variables
load_dotenv()

# Streamlit Page Config - Enterprise Sleek Theme
st.set_page_config(
    page_title="AgentBRD — Multi-Agent Enterprise Suite",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling - High-End Minimal SaaS Look
st.markdown("""
    <style>
    .main { background-color: #0b0f19; color: #e2e8f0; }
    .stButton>button { 
        background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%); 
        color: white; 
        border-radius: 6px; 
        border: none;
        padding: 10px 24px;
        font-weight: 600; 
    }
    .stTextArea textarea { 
        background-color: #1e293b; 
        color: #f8fafc; 
        border: 1px solid #334155; 
        border-radius: 8px;
    }
    .gateway-card {
        background-color: #1e293b;
        border: 1px solid #334155;
        border-radius: 8px;
        padding: 16px;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# App Header
st.title("💼 AgentBRD")
st.caption("Enterprise Multi-Agent Intelligence Engine • Gemini 1.5 Pro Architecture")

st.divider()

# Sidebar - Minimal Gateway Settings
with st.sidebar:
    st.markdown("### 🔐 Security & Gateway")
    api_key = st.text_input("Gemini API Key Gateway", value=os.getenv("GEMINI_API_KEY", ""), type="password", placeholder="Enter key...")
    
    st.markdown("---")
    st.markdown("### 📡 Pipeline Active Gateways")
    st.caption("• Analysis Agent Gateway: `Active`")
    st.caption("• Compliance Agent Gateway: `Active`")
    st.caption("• Traceability Agent Gateway: `Active`")

if not api_key:
    st.info("💡 Gateway Initialization: Please enter your Gemini API Key in the sidebar to activate multi-agent pipelines.")
    st.stop()

# Initialize Gemini Client
client = genai.Client(api_key=api_key)

# Main Workspace Layout
st.markdown("### 📥 Multi-Modal Requirement Ingestion")
raw_input = st.text_area(
    "Discovery Notes, System Logs, or Feature Briefs", 
    height=160, 
    placeholder="Paste raw unstructured meeting notes, project requirements, or feature specifications here..."
)

col1, col2 = st.columns([1, 3])
with col1:
    generate_btn = st.button("⚡ Execute Agent Pipeline", use_container_width=True)

# Execution Workflow
if generate_btn and raw_input:
    status_area = st.empty()
    
    # --- Gateway 1: Requirements Sanitization ---
    status_area.markdown("⏳ **[1/3] Ingestion Gateway:** Sanitizing & Extracting Core Requirements...")
    prompt_1 = f"Sanitize and extract core business objectives, functional needs, and scope from:\n{raw_input}"
    agent1_res = client.models.generate_content(
        model='gemini-1.5-pro',
        contents=prompt_1,
        config=types.GenerateContentConfig(
            system_instruction="You are a Senior Business Analyst. Extract clean structured scope.",
            temperature=0.2
        )
    )
    
    # --- Gateway 2: Tech & Compliance Validation ---
    status_area.markdown("⏳ **[2/3] Compliance Gateway:** Enforcing 2026 Tech Stack Schema & Security Controls...")
    prompt_2 = f"Based on these requirements, recommend enterprise 2026 Tech Architecture, Database schema, and Security Controls:\n{agent1_res.text}"
    agent2_res = client.models.generate_content(
        model='gemini-1.5-pro',
        contents=prompt_2,
        config=types.GenerateContentConfig(
            system_instruction="You are a Principal Solutions Architect. Specify clean enterprise stack.",
            temperature=0.3
        )
    )

    # --- Gateway 3: Synthesis & Export Gateway ---
    status_area.markdown("⏳ **[3/3] Synthesis Gateway:** Link Lineage & Generating Traceable Corporate BRD...")
    prompt_3 = f"Core Scope:\n{agent1_res.text}\n\nTech Stack:\n{agent2_res.text}\n\nSynthesize a complete formal Business Requirement Document (BRD) in Markdown format."
    final_brd = client.models.generate_content(
        model='gemini-1.5-pro',
        contents=prompt_3,
        config=types.GenerateContentConfig(
            system_instruction="You are an Executive Product Director. Produce a full, professional Markdown BRD document.",
            temperature=0.3
        )
    )
    
    status_area.empty()
    
    st.markdown("---")
    st.markdown("### 📑 Enterprise Business Requirement Document")
    st.markdown(final_brd.text)
    
    # Deployment & Export Gateway
    st.markdown("---")
    st.markdown("### 📤 Export & Integration Gateway")
    col_d1, col_d2 = st.columns(2)
    with col_d1:
        st.download_button(
            label="📥 Download Markdown BRD (.md)",
            data=final_brd.text,
            file_name="AgentBRD_Enterprise_Document.md",
            mime="text/markdown",
            use_container_width=True
        )
    with col_d2:
        st.button("🔗 Push to GitLab / GitHub Issue Tracker (MCP Integrated)", disabled=True, use_container_width=True)
