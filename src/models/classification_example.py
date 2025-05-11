# 🔍 Explanation:
# CountVectorizer turns each email into a bag-of-words feature vector.
# Logistic Regression uses those word frequencies to learn spam patterns.
# The model can then predict whether new, unseen emails are spam.
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

# Sample emails
emails = [
    "Congratulations, you have won a free iPhone!",  # spam
    "Reminder: Your meeting is at 10am",             # not spam
    "Claim your prize now!!!",                       # spam
    "Can we reschedule our lunch?"                   # not spam
]
labels = [1, 0, 1, 0]  # 1 = spam, 0 = not spam

# Convert text to numerical features
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(emails)

# Train the classifier
model = LogisticRegression()
model.fit(X, labels)

# Predict on a new message
new_email = ["Free vacation! Click now!"]
new_features = vectorizer.transform(new_email)
print(model.predict(new_features))  # Output: [1] → spam
