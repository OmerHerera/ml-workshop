import gradio as gr
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_digits

digits = load_digits()
model = LogisticRegression(max_iter=10000)
model.fit(digits.data, digits.target)

def predict_digit(image):
    image = np.array(image).reshape(1, -1)
    return model.predict(image)[0]

gr.Interface(fn=predict_digit, inputs="sketchpad", outputs="label").launch()