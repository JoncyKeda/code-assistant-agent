"""
Agent controller for AI Code Assistant.
Handles LLM-based code analysis.
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def analyze_code(code: str) -> str:
    """
    Analyze Python code using LLM and return debugging feedback.

    Args:
        code (str): Python code entered by user.

    Returns:
        str: Analysis result including explanation and corrected code.
    """
    if not code.strip():
        return "No code provided."

    prompt = f"""
    You are an expert Python debugger.

    Analyze the following Python code:

    {code}

    Perform these tasks:
    1. Identify any errors.
    2. Clearly explain the issue.
    3. Provide corrected code.
    4. Suggest improvements if possible.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return response.choices[0].message.content