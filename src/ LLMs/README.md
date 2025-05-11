# LLM Workshop Code Examples

This repository contains Python scripts used in the "LLMs in Practice" workshop. Each script demonstrates a specific use case for GPT, AI agents, and local LLM deployment.

## Prerequisites

- Python 3.8 or newer
- pip (Python package installer)
- Access to OpenAI API (for cloud examples)
- Local inference tools (e.g., Ollama) for local examples

Install the required libraries:

```bash
pip install -r requirements.txt
```

## Libraries Used

- `openai` – Access OpenAI's GPT models
- `langchain` – Build multi-step AI agents
- `ollama` – Run local LLMs
- `transformers` – Hugging Face's model loading and inference
- `torch` – Backend used by many LLMs

## Code Examples

| File Name                 | Type/Case Learning       | Example Task                                 | Key Library     |
|--------------------------|--------------------------|-----------------------------------------------|-----------------|
| openai_gpt_example.py    | Cloud GPT API            | Summarize historical events                   | openai          |
| prompt_engineering_example.py | Prompt Engineering   | Role-based prompt for code generation         | openai / local  |
| langchain_agent_example.py | AI Agent w/ Tools      | Use math + web tools to solve questions       | langchain       |
| ollama_example.py        | Local Model Inference     | Run llama3 locally and ask about Ollama       | ollama          |
| huggingface_example.py   | Transformers / Local      | Ask a question to a Hugging Face model        | transformers    |
| local_agent_example.py   | Local Agent               | Time tool + fallback to local LLM             | ollama + logic  |

## Running the Examples

1. **Cloud**: Ensure you have an OpenAI API key.
2. **Local**: Make sure Ollama is installed and the correct models are available.
3. **Hugging Face**: Ensure you have enough resources to load large models.

Run a script using:

```bash
python <filename>.py
```

Replace `<filename>` with any script name from the table above.
