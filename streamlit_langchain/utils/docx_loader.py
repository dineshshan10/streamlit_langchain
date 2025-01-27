from docx import Document

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
