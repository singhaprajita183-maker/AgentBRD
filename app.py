import os
import streamlit as st
from google import genai
from google.genai import types
from dotenv import load_dotenv

# Load Environment Variables
load_dotenv()

# Streamlit Page Config - Dark Modern UI
st.set_page_config(
    page_title="AgentBRD - Autonomous Multi-Modal Enterprise Analyst",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling (Dark Glassmorphism)
st.markdown("""
    <style>
    .main { background-color: #0d1117; color: #c9d1d9; }
    .stButton>button { background-color: #238636; color: white; border-radius: 8px; font-weight: bold; }
    .stTextArea textarea { background-color: #161b22; color: #58a6ff; border: 1px solid #30363d; }
    .agent-card { background: #161b22; padding: 20px; border-radius: 10px; border: 1px solid #30363d; margin-bottom: 15px; }
    </style>
""", unsafe_allow_html=True)

# App Header
st.title("💼 AgentBRD — Enterprise Multi-Agent Suite")
st.caption("Powered by Google Gemini 1.5 Pro Engine | 2026 Architecture")

st.divider()

# Sidebar Setup
with st.sidebar:
    st.header("⚙️ Configuration")
    api_key = st.text_input("Gemini API Key", value=os.getenv("GEMINI_API_KEY", ""), type="password")
    
    st.markdown("---")
    st.markdown("### 🤖 Active Agents")
    st.success("✅ Analysis Agent (Requirements)")
    st.success("✅ Engineering Agent (Compliance)")
    st.success("✅ Planner Agent (Traceability)")

if not api_key:
    st.warning("Please enter your Gemini API Key in the sidebar or setup .env file!")
    st.stop()

# Initialize Gemini Client
client = genai.Client(api_key=api_key)

# Input Section
st.subheader("📥 Enterprise Multi-Modal Ingestion")
raw_input = st.text_area("Paste Raw Discovery Notes, Transcripts, or Feature Requirements:", height=150, 
                         placeholder="e.g., Client wants a real-time messaging feature with ZK-privacy, auto-translation, and BigQuery analytics...")

col1, col2 = st.columns([1, 4])
with col1:
    generate_btn = st.button("🚀 Run Agentic Pipeline", use_container_width=True)

# Execution Workflow
if generate_btn and raw_input:
    status_box = st.empty()
    
    # --- Agent 1: Context & Core Extractor ---
    status_box.info("🔍 [Agent 1/3] Analysis Agent extracting core business logic...")
    prompt_1 = f"Sanitize and extract business objectives from this raw input:\n{raw_input}"
    agent1_res = client.models.generate_content(
        model='gemini-1.5-pro',
        contents=prompt_1,
        config=types.GenerateContentConfig(
            system_instruction="You are a Senior Lead Business Analyst.",
            temperature=0.2
        )
    )
    
    # --- Agent 2: Compliance & Architecture Validator ---
    status_box.info("🛡️ [Agent 2/3] Engineering Agent enforcing 2026 Tech Compliance...")
    prompt_2 = f"Based on these requirements, recommend a enterprise 2026 Tech Stack and compliance schema:\n{agent1_res.text}"
    agent2_res = client.models.generate_content(
        model='gemini-1.5-pro',
        contents=prompt_2,
        config=types.GenerateContentConfig(
            system_instruction="You are an Enterprise Solutions Architect.",
            temperature=0.3
        )
    )

    # --- Agent 3: Final BRD Synthesizer ---
    status_box.info("📑 [Agent 3/3] Planner Agent synthesizing final traceable BRD...")
    prompt_3 = f"Requirements:\n{agent1_res.text}\n\nTech Stack & Schema:\n{agent2_res.text}\n\nGenerate a complete, formal Corporate Business Requirement Document (BRD) in Markdown."
    final_brd = client.models.generate_content(
        model='gemini-1.5-pro',
        contents=prompt_3,
        config=types.GenerateContentConfig(
            system_instruction="You are an Executive Director of Product Engineering. Output full Markdown BRD.",
            temperature=0.3
        )
    )
    
    status_box.success("✅ BRD Generation Completed Successfully!")
    
    st.markdown("---")
    st.subheader("📄 Generated Corporate BRD Document")
    st.markdown(final_brd.text)
    
    # Download Button
    st.download_button(
        label="📥 Download Markdown BRD",
        data=final_brd.text,
        file_name="AgentBRD_Enterprise_Document.md",
        mime="text/markdown"
    )
