"""
Streamlit UI for AI Code Assistant Agent.
Includes AI analysis, pylint checking, and code execution with structured output.
"""

import streamlit as st
from agent.agent_controller import analyze_code
from tools.code_runner import run_python_code
from tools.syntax_checker import check_code_quality


def main() -> None:
    """Run the Streamlit application."""

    st.set_page_config(
        page_title="AI Code Assistant Agent",
        page_icon="🤖",
        layout="wide"
    )

    st.title("🤖 AI Code Assistant Agent")
    st.write(
        "Analyze, debug, and execute Python code using AI-powered assistance."
    )

    # Code input
    code: str = st.text_area(
        label="Enter your Python code:",
        height=250,
        placeholder="Example:\nprint('Hello world')"
    )

    # Buttons
    col1, col2 = st.columns(2)

    with col1:
        if st.button("🔍 Analyze Code"):
            handle_analyze(code)

    with col2:
        if st.button("▶ Run Code"):
            handle_execute(code)


def handle_analyze(code: str) -> None:
    """Perform static + AI analysis with structured output."""
    if not code.strip():
        st.warning("⚠ Please enter Python code first.")
        return

    st.divider()
    st.header("📊 Code Analysis Results")

    # Create tabs
    tab1, tab2 = st.tabs(["🔎 Static Analysis (Pylint)", "🧠 AI Debugging"])

    # Static Analysis
    with tab1:
        with st.spinner("Running pylint analysis..."):
            lint_result = check_code_quality(code)

        st.code(lint_result, language="text")

    # AI Analysis
    with tab2:
        with st.spinner("Analyzing code using AI..."):
            ai_result = analyze_code(code)

        st.write(ai_result)


def handle_execute(code: str) -> None:
    """Execute Python code and show output."""
    if not code.strip():
        st.warning("⚠ Please enter Python code first.")
        return

    st.divider()
    st.header("⚡ Execution Output")

    with st.spinner("Running code..."):
        output = run_python_code(code)

    st.code(output, language="python")


if __name__ == "__main__":
    main()
