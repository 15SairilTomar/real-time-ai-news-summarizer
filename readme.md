# Real-Time AI News Summarizer

A beginner-friendly GenAI project that fetches real-time news from the internet using Tavily Search and summarizes it into concise bullet points using Mistral AI and LangChain.

---

## Features

- Real-time web search
- AI-powered news summarization
- Bullet-point summaries
- LangChain runnable pipeline
- Tavily Search integration
- Mistral AI integration
- Beginner-friendly GenAI project

---

## Technologies Used

- Python
- LangChain
- Mistral AI
- Tavily Search API

---

## Project Structure

```text
ToolsLLM/
│
├── tools.py
├── requirements.txt
├── README.md
├── .env
└── .venv/
```

---

## Installation

### 1. Clone the repository

```bash
git clone <your-github-repository-link>
```

---

### 2. Open project folder

```bash
cd ToolsLLM
```

---

### 3. Create virtual environment

```bash
python -m venv .venv
```

---

### 4. Activate virtual environment

#### Windows PowerShell

```bash
.\.venv\Scripts\Activate.ps1
```

---

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Setup API Keys

Create a `.env` file and add your API keys:

```env
MISTRAL_API_KEY=your_mistral_api_key
TAVILY_API_KEY=your_tavily_api_key
```

---

## Run the Project

```bash
python tools.py
```

---

## Example Query

```text
What is the latest news about AI?
```

---

## Example Output

```text
- OpenAI released new updates for ChatGPT
- Companies are rapidly investing in Generative AI
- AI regulations are increasing globally
```

---

## Learning Concepts

This project demonstrates:

- LLM integration
- Prompt Templates
- LangChain chains
- Output Parsers
- Real-time web search
- AI-powered summarization

---

## Future Improvements

- Streamlit UI
- Conversational chatbot
- Multiple news categories
- RAG integration
- Source citations
- AI agents

---

## Author

Sairil Tomar