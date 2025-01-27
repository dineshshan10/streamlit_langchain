from setuptools import setup, find_packages

setup(
    name="streamlit_langchain",  # Name of your package
    version="1.0",            # Version of your package
    description="LangChain-powered chatbot using Streamlit",  # Short description
    author="Dinesh Shankar",       # Your name or organization
    packages=find_packages(),  # Automatically finds all Python packages
    install_requires=[        # Dependencies to be installed
        "streamlit",
        "langchain",
        "langchain-community",
        "openai",
        "tiktoken",
        "python-docx",
        "PyPDF2",
        "pdfplumber",
        "beautifulsoup4",
        "requests",
        "faiss-cpu",
    ],
)
