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

    # Initialize session state for code editor
    if "code_input" not in st.session_state:
        st.session_state.code_input = ""

    # Code input
    code: str = st.text_area(
        label="Enter your Python code:",
        height=250,
        key="code_input",
        placeholder="Example:\nprint('Hello world')"
    )

    # Buttons layout
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("🔍 Analyze Code"):
            handle_analyze(code)

    with col2:
        if st.button("▶ Run Code"):
            handle_execute(code)

    with col3:
        if st.button("🗑 Clear Code"):
            st.session_state.code_input = ""
            st.rerun()


def extract_corrected_code(ai_response: str) -> str | None:
    """
    Extract corrected Python code block from AI response.
    """
    if "```" in ai_response:
        parts = ai_response.split("```")
        if len(parts) >= 2:
            return parts[1].replace("python", "").strip()

    if "Corrected Code:" in ai_response:
        return ai_response.split("Corrected Code:")[-1].strip()

    return None

def format_ai_response(response: str) -> tuple[str, str]:
    """
    Extract explanation and suggestions from AI response.
    """
    explanation = ""
    suggestions = ""

    if "Explanation:" in response:
        explanation = response.split("Explanation:")[-1]

    if "Suggestion" in response:
        parts = response.split("Suggestion")
        explanation = parts[0]
        suggestions = parts[-1]

    return explanation.strip(), suggestions.strip()

def handle_analyze(code: str) -> None:
    """Perform static + AI analysis with structured output."""
    if not code.strip():
        st.warning("⚠ Please enter Python code first.")
        return

    st.divider()
    st.header("📊 Code Analysis Results")

    tab1, tab2 = st.tabs(["🔎 Static Analysis", "🧠 AI Debugging"])

    # Static Analysis
    with tab1:
        with st.spinner("Running pylint analysis..."):
            lint_result = check_code_quality(code)
        st.code(lint_result, language="text")

    # AI Debugging
    with tab2:
        with st.spinner("Analyzing code using AI..."):
            ai_result = analyze_code(code)

        explanation, suggestions = format_ai_response(ai_result)

        st.subheader("❌ Error Explanation")

        if explanation:
            st.write(explanation)
        else:
            # fallback if parsing fails
            st.write(ai_result)

        if suggestions:
            st.subheader("💡 Suggestions")
            st.write(suggestions)

        # Extract corrected code
        corrected_code = extract_corrected_code(ai_result)

        if corrected_code:
            st.divider()
            st.subheader("🛠 Corrected Code")
            st.code(corrected_code, language="python")
            
            st.download_button(
                label="⬇ Download Fixed Code",
                data=corrected_code,
                file_name="fixed_code.py",
                mime="text/x-python"
            )

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

