def get_time():
    import datetime
    return str(datetime.datetime.now())

def call_model(prompt):
    import ollama
    return ollama.chat(model="mistral", messages=[{"role": "user", "content": prompt}])['message']['content']

user_query = "What's the current time?"
if "time" in user_query:
    response = get_time()
else:
    response = call_model(user_query)

print("Agent Response:", response)