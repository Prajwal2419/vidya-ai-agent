import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

# Get Groq API key from environment
groq_key = os.getenv("GROQ_API_KEY")

# Create Groq client
client = Groq(api_key=groq_key)


def analyze_resume(resume_text):

    prompt = f"""
    Analyze this resume and provide:

    1. Resume Score out of 100
    2. Key Skills detected
    3. Missing Skills
    4. Career roles suitable
    5. Learning roadmap

    Resume:
    {resume_text}
    """

    chat = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.3-70b-versatile"
    )
    return chat.choices[0].message.content


def chat_with_agent(message, resume_text):

    prompt = f"""
    You are an AI career mentor.

    Student Resume:
    {resume_text}

    Student Question:
    {message}
    """

    chat = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.3-70b-versatile"
    )

    return chat.choices[0].message.content