import os
from langchain.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS


def get_vectorstore(chunks, embeddings_model="text-embedding-ada-002"):
    embeddings = OpenAIEmbeddings(model=embeddings_model)
    if os.path.exists("vectorstore"):
        print("Loading existing vectorstore...")
        vectorstore = FAISS.load_local("vectorstore", embeddings, allow_dangerous_deserialization=True)
    else:
        print("Creating new vectorstore...")
        vectorstore = FAISS.from_texts(chunks, embeddings)
        vectorstore.save_local("vectorstore")
    return vectorstore
