import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from utils.config_loader import load_config
from langchain_groq import ChatGroq
from sentence_transformers import SentenceTransformer
from langchain_huggingface import HuggingFaceEmbeddings




from langchain_huggingface import HuggingFaceEmbeddings


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




  