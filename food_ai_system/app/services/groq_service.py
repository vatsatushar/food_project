import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

#i want to use grop api key from env


client= Groq(api_key=os.getenv("GROQ_API_KEY"))

def call_groq(prompt, temperature=0.5):
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {"role": "system", "content": "You are a professional culinary and nutrition expert."},
            {"role": "user", "content": prompt}
        ],
        temperature=temperature
    )

    return response.choices[0].message.content
