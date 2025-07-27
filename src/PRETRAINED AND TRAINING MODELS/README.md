# Pretrained Models and Training Models

This demo shows how to use training models and pretrained models in Python.

## How to Run

✅ Step 1: Create a Virtual Environment (recommended for macOS Homebrew)

```bash
./bootstrap.sh

```

- If you get a “permission denied” error, they can still fix it with:

```bash
chmod +x bootstrap.sh

```

or

```python
python3 -m venv venv
source venv/bin/activate
```

Then install the requirements:

```python
pip install -r requirements.txt
```

✅ Step 2: Run the code

```bash
python pre_trained_model.py
```

## Dependencies

- `transformers`
- `scikit-learn`
- `torch`
