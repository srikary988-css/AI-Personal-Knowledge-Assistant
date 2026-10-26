from pypdf import PdfReader
from docx import Document
import requests
from bs4 import BeautifulSoup


def extract_pdf(file):
    reader = PdfReader(file)
    pages = []

    for page_number, page in enumerate(reader.pages, start=1):

        page_text = page.extract_text()

        if page_text:
            pages.append({
                "text": page_text,
                "page": page_number
            })

    return pages


def extract_docx(file):
    document = Document(file)

    text = ""

    for paragraph in document.paragraphs:

        if paragraph.text.strip():
            text += paragraph.text + "\n"

    return [{
        "text": text,
        "page": None
    }]


def extract_txt(file):
    text = file.read().decode("utf-8")

    return [{
        "text": text,
        "page": None
    }]


def extract_url(url):

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(
        url,
        headers=headers,
        timeout=10
    )

    response.raise_for_status()

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    for element in soup(
        ["script", "style", "nav", "footer", "header"]
    ):
        element.decompose()

    text = soup.get_text(
        separator=" ",
        strip=True
    )

    return [{
        "text": text,
        "page": None
    }]


def extract_text(file):

    filename = file.name.lower()

    if filename.endswith(".pdf"):
        return extract_pdf(file)

    elif filename.endswith(".docx"):
        return extract_docx(file)

    elif filename.endswith(".txt"):
        return extract_txt(file)

    else:
        raise ValueError(
            "Unsupported file type. Use PDF, DOCX or TXT."
        )