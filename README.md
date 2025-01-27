# **Streamlit LangChain Chatbot**

A LangChain-powered chatbot using OpenAI's GPT-3.5 (or other OpenAI models), built with Streamlit for a simple and interactive interface. The app leverages a Retrieval-Augmented Generation (RAG) pipeline to enhance responses using document retrieval.

---

## **Features**
- **Document Loading**: The chatbot can load content from various sources, including `.txt`, `.docx`, `.pdf`, and websites (HTML).
- **Retrieval-Augmented Generation**: The chatbot retrieves relevant documents and generates responses based on them, powered by LangChain and OpenAI's GPT models.
- **Cost Tracking**: Tracks token usage and provides an estimated cost for each query.
- **Interactive UI**: Users can input queries and receive answers through a simple and interactive interface powered by Streamlit.

---

## **Installation**

### **Clone the Repository**
To get started with this project, clone it to your local machine:
```bash
git clone https://github.com/your-username/streamit_langchain.git
cd streamit_langchain


pip install -r requirements.txt

export OPENAI_API_KEY="your-api-key"

### Usage
Run the Streamlit App
Once everything is set up, you can run the app with the following command:

streamlit run streamit_langchain/app.py