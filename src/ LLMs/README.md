# LLM Workshop Code Examples

This repository contains Python scripts used in the "LLMs in Practice" workshop. Each script demonstrates a specific use case for GPT, AI agents, and local LLM deployment.

## Prerequisites

- Python 3.8 or newer
- pip (Python package installer)
- Access to OpenAI API (for cloud examples)
- Local inference tools (e.g., Ollama) for local examples
- For LLM models:
  - 🔽 1. Download a .gguf LLM (e.g. TinyLlama)
  - Go to:
     👉 <https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF>
  - Download one of these files
  - `tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf` (for low memory usage)
  - 🔽 2. Download a `.gguf` LLM (e.g. Mistral)
  - Go to:
     👉 <https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF/blob/main/mistral-7b-instruct-v0.1.Q4_K_M.gguf>
  - Download one of these files (smallest first):
  - `mistral-7b-instruct-v0.1.Q4_K_M.gguf`
  - 📁 3. Move It to Your Project Folder
    - Place the downloaded file in the same directory as your `ai_agents_*.py` script or specify the full path.

Install the required libraries:

```bash
./bootstrap.sh
```

- If you get a “permission denied” error, they can still fix it with:

```bash
chmod +x bootstrap.sh

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
