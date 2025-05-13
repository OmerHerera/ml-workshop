from langchain_community.llms import LlamaCpp

llm = LlamaCpp(
    model_path="tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf",
    temperature=0.7,
    max_tokens=256,
    n_ctx=1024,
    verbose=False  # 🔇 suppress verbose logs
)
# prompt = "What is (100 + 23) * 2? Provide just the final number."
prompt = (
    "You are a helpful math assistant.\n"
    "Please compute the result of the following expression step-by-step:\n"
    "(100 + 23) * 2\n"
    "Answer:"
)
response = llm.invoke(prompt)
print("🧠 Model response:\n", response.strip())

# 🧠 Model response:
#  153

# ⚠️ Why This Wrong Answer Happens
# This kind of mistake is typical of:

# Small models (like TinyLLaMA)

# Non-instruction-tuned models

# Models without a calculator tool