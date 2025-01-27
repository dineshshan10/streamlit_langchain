import streamlit as st

from streamlit_langchain.config import get_api_key
from streamlit_langchain.document_loader import load_documents, chunk_documents
from streamlit_langchain.vectorstore import get_vectorstore
from streamlit_langchain.qa_pipeline import create_qa_chain, calculate_tokens_and_cost

# Set OpenAI API Key
api_key = get_api_key()
st.title("Streamlit LangChain-Powered Chatbot")

# Load and chunk documents
st.sidebar.title("Document Upload")
directory = "./data/"
documents = load_documents(directory)
chunks = chunk_documents(documents)

# Vector store
vectorstore = get_vectorstore(chunks)

# RAG pipeline
qa_chain = create_qa_chain(vectorstore)

# User input
query = st.text_input("Ask a question:")
if query:
    try:
        response = qa_chain({"query": query})
        result = response["result"]

        # Display the answer
        st.write("### Answer:")
        st.write(result)

        # Display source documents
        st.write("### Sources:")
        for i, doc in enumerate(response["source_documents"]):
            # Display the title or first few words of the document as a link
            source_text = doc.page_content[:200]  # First 200 characters of the document
            st.markdown(f"**Source {i+1}:** {source_text}...")  # Display source with a number

        # Token usage and cost
        input_tokens, output_tokens, total_tokens, cost = calculate_tokens_and_cost(query, result)
        st.write("### Token Usage and Cost:")
        st.write(f"- **Input Tokens:** {input_tokens}")
        st.write(f"- **Output Tokens:** {output_tokens}")
        st.write(f"- **Total Tokens:** {total_tokens}")
        st.write(f"- **Estimated Cost:** ${cost:.6f}")

    except Exception as e:
        st.write(f"An error occurred: {e}")
