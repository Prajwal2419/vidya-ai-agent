import streamlit as st

from resume_parser import parse_resume
from career_engine import analyze_resume, chat_with_agent


# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------

st.set_page_config(
    page_title="Vidya AI Career Mentor",
    page_icon="🎓",
    layout="wide"
)


# ---------------------------------------------------------
# TITLE
# ---------------------------------------------------------

st.title("🎓 Vidya AI Career Guidance Platform")

st.write(
    "Upload your resume and get AI-powered career guidance, "
    "resume analysis and personalized recommendations."
)


# ---------------------------------------------------------
# RESUME UPLOAD
# ---------------------------------------------------------

uploaded_file = st.file_uploader(
    "📄 Upload Your Resume",
    type=["pdf", "docx"],
    help="Upload your resume in PDF or DOCX format."
)


# Store resume text
resume_text = ""


# ---------------------------------------------------------
# PROCESS RESUME
# ---------------------------------------------------------

if uploaded_file:

    try:

        resume_text = parse_resume(uploaded_file)

        if not resume_text.strip():

            st.error(
                "❌ No readable text was found in this resume. "
                "Please upload a text-based PDF or DOCX file."
            )

        else:

            st.success("✅ Resume uploaded successfully!")

            # Resume preview
            with st.expander("📄 Resume Preview"):

                st.text(resume_text[:3000])

            # -------------------------------------------------
            # ANALYZE RESUME BUTTON
            # -------------------------------------------------

            if st.button(
                "🚀 Analyze Resume",
                use_container_width=True
            ):

                with st.spinner(
                    "🤖 AI is analyzing your resume..."
                ):

                    try:

                        result = analyze_resume(resume_text)

                        st.success(
                            "✅ Resume analysis completed!"
                        )

                        st.subheader(
                            "📊 AI Resume Analysis"
                        )

                        st.markdown(result)

                    except Exception as e:

                        st.error(
                            "❌ Unable to analyze the resume."
                        )

                        st.code(str(e))


    except Exception as e:

        st.error(
            "❌ Unable to read the uploaded resume."
        )

        st.code(str(e))


# ---------------------------------------------------------
# DIVIDER
# ---------------------------------------------------------

st.divider()


# ---------------------------------------------------------
# AI CAREER CHATBOT
# ---------------------------------------------------------

st.subheader("🤖 Career AI Mentor")

st.write(
    "Ask questions about careers, jobs, skills, interviews, "
    "internships or your resume."
)


user_question = st.text_input(
    "💬 Ask your career question"
)


if st.button(
    "Ask AI",
    use_container_width=True
):

    if not resume_text:

        st.warning(
            "⚠️ Please upload your resume first."
        )

    elif not user_question.strip():

        st.warning(
            "⚠️ Please enter a question."
        )

    else:

        with st.spinner(
            "🤖 AI Career Mentor is thinking..."
        ):

            try:

                response = chat_with_agent(
                    user_question,
                    resume_text
                )

                st.subheader(
                    "💡 Career Mentor Response"
                )

                st.markdown(response)

            except Exception as e:

                st.error(
                    "❌ Unable to connect to the AI service."
                )

                st.code(str(e))