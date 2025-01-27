import os
import PyPDF2
import requests
from langchain.text_splitter import CharacterTextSplitter
from docx import Document
from bs4 import BeautifulSoup

def load_website(url):
    """
    Load text content from a website.

    Args:
        url (str): The URL of the website.

    Returns:
        str: The extracted text content.
    """
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad status codes
    soup = BeautifulSoup(response.text, "html.parser")
    paragraphs = soup.find_all("p")
    return "\n".join([para.get_text() for para in paragraphs])



def load_pdf(file_path):
    """
    Load text from a .pdf file.

    Args:
        file_path (str): Path to the .pdf file.

    Returns:
        str: The extracted text.
    """
    with open(file_path, "rb") as f:
        pdf_reader = PyPDF2.PdfReader(f)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text


def load_docx(file_path):
    """
    Load text from a .docx file.

    Args:
        file_path (str): Path to the .docx file.

    Returns:
        str: The extracted text.
    """
    document = Document(file_path)
    return "\n".join([para.text for para in document.paragraphs])


def load_documents(directory):
    docs = []
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        if file_name.endswith(".txt"):
            with open(file_path, "r", encoding="utf-8") as f:
                docs.append(f.read())
        elif file_name.endswith(".docx"):
            docs.append(load_docx(file_path))
        elif file_name.endswith(".pdf"):
            docs.append(load_pdf(file_path))
        elif file_name.endswith(".html"):
            docs.append(load_website(file_path))
    return docs

def chunk_documents(docs, chunk_size=500, chunk_overlap=50):
    text_splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return [chunk for doc in docs for chunk in text_splitter.split_text(doc)]
