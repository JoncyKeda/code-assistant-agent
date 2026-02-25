"""
Streamlit UI for AI Code Assistant Agent.
"""

import streamlit as st
from agent.agent_controller import analyze_code


def main() -> None:
    """Run Streamlit application."""

    st.set_page_config(
        page_title="AI Code Assistant Agent",
        page_icon="🤖",
        layout="wide"
    )

    st.title("🤖 AI Code Assistant Agent")
    st.write("Paste your Python code below for AI-powered debugging and analysis.")

    code: str = st.text_area(
        "Enter your Python code:",
        height=250,
        placeholder="Example:\nprint('Hello world')"
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🔍 Analyze Code"):
            handle_analyze(code)

    with col2:
        if st.button("▶ Run Code"):
            st.info("Code execution feature will be added on Day 4.")

    st.divider()
    st.subheader("📄 Output")
    st.info("Results will appear here after analysis.")


def handle_analyze(code: str) -> None:
    """
    Handle code analysis request.
    """
    if not code.strip():
        st.warning("⚠ Please enter Python code first.")
        return

    with st.spinner("Analyzing code..."):
        result = analyze_code(code)

    st.success("Analysis Complete ✅")
    st.write(result)


if __name__ == "__main__":
    main()
