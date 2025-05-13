from transformers import pipeline

# Load a sentiment analysis pipeline (uses a pretrained model under the hood)
classifier = pipeline("sentiment-analysis")

# Run inference
result = classifier("I love using pretrained models with Hugging Face!")
print("Sentiment Analysis Result:")
print(result)

result = classifier("I hate using pretrained models with Hugging Face!")
print("Sentiment Analysis Result:")
print(result)
