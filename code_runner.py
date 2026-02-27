"""
Code execution tool for AI Code Assistant Agent.
Executes Python code safely and returns output or error.
"""

import subprocess
import tempfile


def run_python_code(code: str) -> str:
    """
    Execute Python code and return output or error.

    Args:
        code (str): Python code string.

    Returns:
        str: Execution result or error message.
    """

    if not code.strip():
        return "No code provided."

    try:
        # Create temporary Python file
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".py", delete=False
        ) as temp_file:
            temp_file.write(code)
            file_name = temp_file.name

        # Run Python file
        result = subprocess.run(
            ["python", file_name],
            capture_output=True,
            text=True,
            timeout=5
        )

        if result.stdout:
            return result.stdout

        return result.stderr

    except Exception as error:
        return str(error)