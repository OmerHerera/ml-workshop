# This imports the LinearRegression model from scikit-learn, a library with many machine learning algorithms.
# LinearRegression is used to model the relationship between a dependent variable (e.g., house price) and one or more independent variables (e.g., square footage).
from sklearn.linear_model import LinearRegression
# Dummy dataset
# This is a very simple dataset:
# X represents the input features—in this case, just one feature: square footage.
# y is the target variable—house prices.
# So we’re saying:
# 1000 sqft → $200,000
# 1500 sqft → $250,000
# 2000 sqft → $300,000
X = [[1000], [1500], [2000]]
y = [200000, 250000, 300000]
# This creates a new instance of a linear regression model.
# At this point, the model has no knowledge—just an untrained shell.
model = LinearRegression()
# This trains the model using the input (X) and output (y) data.
# Under the hood, the model calculates the best-fit line (y = mx + b) through the data points.
# It learns the slope (m) and intercept (b) that minimize prediction error.
model.fit(X, y)
# This makes a prediction for a house that’s 1800 sqft.
# Based on the learned line from training, it estimates what the price should be.
# Given how linear the data is, the model will likely return something around $280,000.
print(model.predict([[1800]]))  # Predict price of 1800 sqft house