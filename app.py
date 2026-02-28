"""
Streamlit UI for AI Code Assistant Agent.
Includes AI analysis and Python code execution.
"""

import streamlit as st
from agent.agent_controller import analyze_code
from tools.code_runner import run_python_code


def main() -> None:
    """Run the Streamlit application."""

    st.set_page_config(
        page_title="AI Code Assistant Agent",
        page_icon="🤖",
        layout="wide"
    )

    st.title("🤖 AI Code Assistant Agent")
    st.write(
        "Paste your Python code below to analyze errors, debug issues, "
        "or execute the program."
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

    st.divider()
    st.subheader("📄 Output")
    st.caption("Results will appear above after analysis or execution.")


def handle_analyze(code: str) -> None:
    """
    Handle AI-based code analysis with pylint integration.
    """
    if not code.strip():
        st.warning("⚠ Please enter Python code first.")
        return

    st.subheader("🔎 Static Code Analysis (Pylint)")
    lint_result = check_code_quality(code)
    st.code(lint_result)

    st.subheader("🧠 AI Debugging Analysis")

    with st.spinner("Analyzing code using AI..."):
        ai_result = analyze_code(code)

    st.success("Analysis Complete ✅")
    st.write(ai_result)


def handle_execute(code: str) -> None:
    """
    Execute Python code and display output.

    Args:
        code (str): Python code entered by user.
    """
    if not code.strip():
        st.warning("⚠ Please enter Python code first.")
        return

    with st.spinner("Running code..."):
        output = run_python_code(code)

    st.success("Execution Complete ✅")
    st.code(output, language="python")


if __name__ == "__main__":
    main()
