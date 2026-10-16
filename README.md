# 🎓 Vidya AI – Autonomous AI Career Mentorship Platform

Vidya AI is an intelligent career guidance and resume evaluation tool powered by Groq's high-speed inference engine (`llama-3.3-70b-versatile`) and Streamlit. It parses student resumes, scores strengths, detects missing technical proficiencies, outlines tailored learning roadmaps, and provides an interactive AI career mentor chat.

---

## 🌟 Key Features

- **Resume Parsing & Scoring:** Extracts text from uploaded resumes (PDF/DOCX) and delivers an objective score out of 100.
- **Skill Gap Analysis:** Pinpoints detected skills vs. critical missing competencies for target industries.
- **Targeted Roadmaps:** Suggests concrete roles and sequential learning paths tailored to the applicant's profile.
- **Interactive Career Mentor:** Live conversational AI to answer career questions based strictly on the uploaded resume context.

---

## 🚀 How to Run or Access the Project

There are two primary ways to access and use Vidya AI:

### Method 1: Live Cloud Application (Zero Setup)

If deployed on Streamlit Community Cloud, no local setup or Python installation is required:

1. Visit the deployed web application link:  
   `https://<your-app-name>.streamlit.app` *(update with your live URL once deployed)*
2. Upload your resume (`.pdf` or `.docx`).
3. View instant career insights and chat directly with the mentor.

---

### Method 2: Local Setup (For Developers & Evaluators)

To run this application locally on your machine, follow these steps:

#### 1. Prerequisites
- **Python 3.10 to 3.14** installed on your system.
- A free **Groq API Key** from [console.groq.com](https://console.groq.com).

#### 2. Clone the Repository
```bash
git clone [https://github.com/Prajwal2419/vidya-ai-agent.git](https://github.com/Prajwal2419/vidya-ai-agent.git)
cd vidya-ai-agent
