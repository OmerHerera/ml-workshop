# 🔍 Why Mistral-7B-Instruct?
# It’s trained to follow human instructions like “Summarize this…” or “Use a tool to calculate…”
# Outputs are structured, making it ideal for LangChain agents and ReAct-style chains.
# It runs well on modern machines using llama-cpp-python, especially quantized versions like Q4_K_M.

from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool
from langchain_community.llms import LlamaCpp

# Path to your quantized Mistral model
MODEL_PATH = "mistral-7b-instruct-v0.1.Q4_K_M.gguf"

# Initialize the local LLM
llm = LlamaCpp(
    model_path=MODEL_PATH,
    temperature=0.7,
    max_tokens=256,
    n_ctx=2048,
    verbose=False
)

# Simple calculator tool function
def calculator_tool(input_text: str) -> str:
    try:
        result = eval(input_text)
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"

# Tool with a very explicit description
tools = [
    Tool(
        name="Calculator",
        func=calculator_tool,
        description=(
            "Useful for evaluating math expressions. "
            "Input should be a single valid Python arithmetic expression, like '(45 + 55) * 3'."
            "Use it like: Action: Calculator\nAction Input: (2 + 2) * 5"
        )
    )
]

# Create the agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

print("\n🤖 Agent created successfully.")

# Ask a math question
response = agent.invoke({"input": "What is (45 + 55) * 3?"})
print("\n🤖 Agent response:", response["output"])
