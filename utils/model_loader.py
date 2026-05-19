from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq

class ModelLoader:

    def load_embeddings(self):

        embedding_model = HuggingFaceEmbeddings(
            model_name="BAAI/bge-m3"
        )

        return embedding_model
    def load_llm(self):

        llm = ChatGroq(
            model="llama-3.3-70b-versatile",
            temperature=0
        )

        return llm