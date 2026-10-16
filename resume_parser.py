import PyPDF2
import docx


# ---------------------------------------------------------
# PDF TEXT EXTRACTION
# ---------------------------------------------------------

def extract_text_from_pdf(file):

    pdf_reader = PyPDF2.PdfReader(file)

    text = ""

    for page in pdf_reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text.strip()


# ---------------------------------------------------------
# DOCX TEXT EXTRACTION
# ---------------------------------------------------------

def extract_text_from_docx(file):

    document = docx.Document(file)

    text = ""

    for paragraph in document.paragraphs:

        if paragraph.text.strip():
            text += paragraph.text + "\n"

    return text.strip()


# ---------------------------------------------------------
# GENERAL RESUME PARSER
# ---------------------------------------------------------

def parse_resume(uploaded_file):

    file_name = uploaded_file.name.lower()

    if file_name.endswith(".pdf"):

        return extract_text_from_pdf(uploaded_file)

    elif file_name.endswith(".docx"):

        return extract_text_from_docx(uploaded_file)

    else:

        return "Unsupported file format. Please upload a PDF or DOCX file."