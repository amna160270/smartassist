# 🤖 SmartAssist — Modular AI Agent

A command-line AI agent that uses LLM-powered tool routing to handle different types of queries automatically.

## 🚀 Features

- 🧮 **Calculator** — Solves math expressions
- 📝 **Summarizer** — Condenses long text using AI
- 🔍 **Search** — Answers knowledge queries

## 🏗️ Architecture

- `main.py` — CLI entry point
- `agent.py` — Agent brain (LLM-powered routing)
- `llm/client.py` — Groq API wrapper
- `tools/` — Modular tool classes

## ⚙️ Setup

```bash
pip install -r requirements.txt
```

Add your API key in `.env`: