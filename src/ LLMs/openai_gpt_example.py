import openai

client = openai.OpenAI(api_key="Your-Key")

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "user", "content": "Summarize the French Revolution"}
    ]
)

print(response.choices[0].message.content)
