from langchain.agents import load_tools, initialize_agent
from langchain.llms import OpenAI

tools = load_tools(["serpapi", "llm-math"])
agent = initialize_agent(tools, OpenAI(temperature=0), agent="zero-shot-react-description")
result = agent.run("What is the square root of the result of 7*11?")
print(result)