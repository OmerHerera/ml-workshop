# ✅ Train only if the saved model doesn’t exist
# ✅ Reuse the saved model for inference
# 🛑 Avoid retraining from scratch every time

import torch
import torch.nn as nn
import torch.optim as optim
import os
from sklearn.feature_extraction.text import CountVectorizer
import joblib

# --- Funny Dataset ---
texts = [
    "This potato changed my life",
    "I cried tears of joy eating this",
    "Tasted like sadness and cardboard",
    "My dog wouldn't eat it",
    "A spiritual experience in starch form",
    "I'd rather chew my shoe",
]
labels = [1, 1, 0, 0, 1, 0]  # 1 = Positive, 0 = Negative

# --- File paths ---
model_path = "potato_model.pth"
vectorizer_path = "potato_vectorizer.pkl"

# --- Text Vectorizer ---
if os.path.exists(vectorizer_path):
    vectorizer = joblib.load(vectorizer_path)
    X = vectorizer.transform(texts).toarray()
else:
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(texts).toarray()
    joblib.dump(vectorizer, vectorizer_path)

y = torch.tensor(labels, dtype=torch.float32)
X_tensor = torch.tensor(X, dtype=torch.float32)
input_size = X_tensor.shape[1]

# --- Model Structure ---
model = nn.Sequential(
    nn.Linear(input_size, 1),
    nn.Sigmoid()
)

# --- Load or Train ---
if os.path.exists(model_path):
    model.load_state_dict(torch.load(model_path))
    model.eval()
    print("✅ Model loaded from file — skipping training.")
else:
    print("🚀 No saved model found — training from scratch.")
    loss_fn = nn.BCELoss()
    optimizer = optim.Adam(model.parameters(), lr=0.01)
    epochs = 5

    for epoch in range(epochs):
        model.train()
        optimizer.zero_grad()
        outputs = model(X_tensor).squeeze()
        loss = loss_fn(outputs, y)
        loss.backward()
        optimizer.step()
        print(f"Epoch {epoch+1}/{epochs}, Loss: {loss.item():.4f}")

    torch.save(model.state_dict(), model_path)
    print("💾 Model saved!")

# --- Inference Function ---
def predict_sentiment(text):
    vec = vectorizer.transform([text]).toarray()
    input_tensor = torch.tensor(vec, dtype=torch.float32)
    output = model(input_tensor).item()
    return "🥰 Positive" if output > 0.5 else "😠 Negative"

# --- Try It Out ---
print(predict_sentiment("I would marry this potato"))
print(predict_sentiment("Tastes like betrayal and chalk"))
