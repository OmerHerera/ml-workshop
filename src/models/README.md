# ml-workshop

From Models to Magic: ML Workshop

## Prerequisites

✅ 1. Install Python
Make sure Python 3.8+ is installed.

Download Python if it’s not already installed.

Run `python --version` in your terminal to confirm.

✅ Step 2: Create a Virtual Environment (recommended for macOS Homebrew)

```bash
./bootstrap.sh

```

- If you get a “permission denied” error, they can still fix it with:

```bash
chmod +x bootstrap.sh

```

Or:

✅ 2. Set Up a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

✅ 3. Install Required Libraries
Install the libraries used in the examples using pip:

```bash
pip install -r requirements.txt
```

✅ 4. Run the Examples
You can now run the examples:

```bash
python src/models/classification_example.py
python src/models/regression_example.py
python src/models/generative_text_example.py
python src/models/gradio_app_example.py
```

### Libraries used

📘 1. scikit-learn

- What it is: A widely used Python library for classical machine learning algorithms.
- Why you're installing it:
  - Provides simple and efficient tools for regression, classification, clustering, and more.

- Used in our regression and classification examples.

- Typical Use Cases:
  - Training a logistic regression model
  - Splitting datasets, cross-validation, evaluation metrics

📙 2. transformers (by Hugging Face)

- What it is: A library for using state-of-the-art pre-trained models like GPT, BERT, etc.
- Why you're installing it:

- We use it in the generative model example with GPT-2 to generate text.

- Typical Use Cases:
  - Text generation (e.g., ChatGPT-like tools)
  - Sentiment analysis
  - Question answering

📗 3. gradio

- What it is: A library to quickly create web-based UIs for your machine learning models.
- Why you're installing it:

- Used in the interactive app example where you draw digits and get predictions from a model.

- Typical Use Cases:
  - Building interactive model demos
  - Prototyping apps without writing frontend code
  - Sharing ML models via web

Prototyping apps without writing frontend code

Sharing ML models via web

📒 4. matplotlib

- What it is: A popular plotting library for creating static, animated, and interactive visualizations.

- Why it's commonly installed (not used in examples, but useful):

- Often used in ML workflows to visualize data and model performance.

- Typical Use Cases:

  - Plotting training loss curves
  - Visualizing datasets or model predictions
  - Drawing charts and graphs

> Note: While matplotlib isn’t directly used in the examples I gave you, it's often included in ML environments because it's so essential for analysis and debugging.

### Examples

| File Name                    | Model Type      | Example Task                | Key Library               |
| ---------------------------- | --------------- | --------------------------- | ------------------------- |
| `regression_example.py`      | Regression      | Predict house price         | `scikit-learn`            |
| `classification_example.py`  | Classification  | Digit or spam detection     | `scikit-learn`            |
| `generative_text_example.py` | Generative      | Text completion             | `transformers` (GPT-2)    |
| `gradio_app_example.py`      | Generative + UI | Interactive text generation | `Gradio` + `transformers` |
