import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def call_openai_api():
    client = OpenAI(
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
        api_key=GEMINI_API_KEY
    )
    response = client.chat.completions.create(
        temperature=0.1,
        model="gemini-2.0-flash",
        messages=[
            {
                "role": "system",
                "content": "You are a chat bot answer questions based on the given data."
            },
            {
                "role": "user",
                "content": "What is the capital of France?"
            }
        ]
    )
    print(response.choices[0].message.content)


call_openai_api()