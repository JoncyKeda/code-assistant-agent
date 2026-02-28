"""
Pylint-based syntax and quality checker.
"""

import subprocess
import tempfile


def check_code_quality(code: str) -> str:
    """
    Run pylint on provided code and return lint report.

    Args:
        code (str): Python source code.

    Returns:
        str: Pylint output report.
    """

    if not code.strip():
        return "No code provided."

    try:
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".py", delete=False
        ) as temp_file:
            temp_file.write(code)
            file_name = temp_file.name

        result = subprocess.run(
            ["pylint", file_name, "--disable=all", "--enable=E,F,W"],
            capture_output=True,
            text=True
        )

        return result.stdout if result.stdout else "No major issues detected."

    except Exception as error:
        return str(error)