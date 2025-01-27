from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
import tiktoken

def create_qa_chain(vectorstore, model="gpt-3.5-turbo"):
    llm = ChatOpenAI(model=model, temperature=0)
    return RetrievalQA.from_chain_type(llm=llm, retriever=vectorstore.as_retriever(), return_source_documents=True)

def calculate_tokens_and_cost(prompt, response, model="gpt-3.5-turbo"):
    encoder = tiktoken.encoding_for_model(model)
    input_tokens = len(encoder.encode(prompt))
    output_tokens = len(encoder.encode(response))
    total_tokens = input_tokens + output_tokens

    cost_per_1k_tokens = {"gpt-3.5-turbo": 0.002, "gpt-4": 0.03}
    cost_per_token = cost_per_1k_tokens.get(model, 0.002) / 1000
    total_cost = total_tokens * cost_per_token

    return input_tokens, output_tokens, total_tokens, total_cost
