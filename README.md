# 🤖 AI Code Assistant Agent
!
An AI-powered system that automatically analyzes, debugs, explains, and fixes Python code using Large Language Models (LLMs).

This project demonstrates an autonomous AI agent that can understand code, detect errors, execute programs, and provide intelligent debugging suggestions. It showcases real-world AI engineering concepts like LLM integration, tool usage, and agent-based architecture.

---

## 🚀 Features

✅ Code error detection  
✅ Automatic bug fixing  
✅ Code execution and output generation  
✅ Error explanation in simple language  
✅ Code quality analysis  
✅ AI-powered debugging assistant  
✅ Interactive user interface  
✅ Autonomous reasoning and action loop  

---

## 🧠 How It Works

The AI agent follows a reasoning → action → observation workflow:

1. User submits Python code
2. AI analyzes code using a Large Language Model
3. Agent detects errors and issues
4. Code execution tool runs the program
5. Agent explains problems and suggests fixes
6. Improved code is returned to the user

---

## 🏗️ System Architecture
User Interface (Streamlit)
↓
Agent Controller
├── LLM Brain (Code Understanding)
├── Code Execution Tool
├── Debug Analyzer
└── Memory System

---

## 🛠️ Tech Stack

- **Python**
- **OpenAI / LLM API**
- **Streamlit** — User Interface
- **LangChain** — Agent Framework
- **Python subprocess** — Code Execution
- **python-dotenv** — Environment Management

---

## ⚙️ Installation & Setup

```bash
git clone https://github.com/yourusername/code-assistant-agent.git
cd code-assistant-agent

pip install -r requirements.txt

OPENAI_API_KEY=your_api_key_here

streamlit run app.py



