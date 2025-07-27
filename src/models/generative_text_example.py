from transformers import pipeline

# 🔄 Downloading the Pretrained GPT-2 Model
# The model is fetched from the Hugging Face Model Hub, specifically:
# 📦 https://huggingface.co/gpt2
# The model weights, configuration, and tokenizer are downloaded and cached locally the first time you run it.
# After that, it's loaded from your local cache (usually in ~/.cache/huggingface/transformers).
generator = pipeline("text-generation", model="gpt2")
# Here’s what happens behind the scenes:
# "Once upon a time" is passed to the tokenizer, which converts it into tokens (numbers).
# These tokens are fed into the GPT-2 neural network (which you've downloaded).
# The model predicts the next token, then the next, and so on, until it reaches the max length or an end-of-sequence token.
# Finally, the tokens are converted back into human-readable text using the tokenizer.
result = generator("Once upon a time,", max_length=50, truncation=True)
print("----------------------------------------------------------------------------------------------------------")
print(result[0]["generated_text"])
print("----------------------------------------------------------------------------------------------------------")