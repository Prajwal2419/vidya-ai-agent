import os
from dotenv import load_dotenv
from groq import Groq


# ---------------------------------------------------------
# LOAD ENVIRONMENT VARIABLES
# ---------------------------------------------------------

load_dotenv()


# ---------------------------------------------------------
# GET GROQ API KEY
# ---------------------------------------------------------

groq_key = os.getenv("GROQ_API_KEY")


if not groq_key:
    raise ValueError(
        "GROQ_API_KEY not found. "
        "Please make sure your .env file contains "
        "GROQ_API_KEY=your_api_key"
    )


# ---------------------------------------------------------
# CREATE GROQ CLIENT
# ---------------------------------------------------------

client = Groq(api_key=groq_key)


# ---------------------------------------------------------
# RESUME ANALYSIS
# ---------------------------------------------------------

def analyze_resume(resume_text):

    prompt = f"""
You are an expert AI Career Guidance and Resume Mentor.

Analyze the student's resume carefully.

Provide the following sections:

1. Resume Score out of 100

2. Key Skills Detected

3. Strengths

4. Weaknesses

5. Missing Skills

6. ATS Compatibility

7. Suitable Career Roles

8. Recommended Industries

9. Learning Roadmap

10. Resume Improvement Suggestions

11. Overall Career Guidance

Be specific and practical.

Resume:
{resume_text}
"""

    chat = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )

    return chat.choices[0].message.content


# ---------------------------------------------------------
# CAREER AI CHATBOT
# ---------------------------------------------------------

def chat_with_agent(message, resume_text):

    prompt = f"""
You are an AI Career Mentor.

Use the student's resume as context when answering.

Student Resume:
{resume_text}

Student Question:
{message}

Give clear, practical and personalized career advice.

If the question is related to jobs, skills, interviews,
resume improvement, career paths, internships or learning,
provide actionable guidance.
"""

    chat = client.chat.completions.create(
    model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.4
    )

    return chat.choices[0].message.content