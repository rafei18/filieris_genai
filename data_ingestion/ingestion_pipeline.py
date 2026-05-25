import os
import pandas as pd
from dotenv import load_dotenv
from typing import List, Tuple
from langchain_core.documents import Document
from langchain_astradb import AstraDBVectorStore
from utils.model_loader import ModelLoader
#from config.config_loader import load_config
from utils.config_loader import load_config
from sentence_transformers import SentenceTransformer






from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from utils.model_loader import ModelLoader


class DataIngestion:
    """
    Handle PDF ingestion pipeline

    """

    def __init__(self):

        print("Initializing ingestion pipeline...")

        load_dotenv()

        self.model_loader = ModelLoader()
        self.pdf_path = self._get_pdf_path()
        self.persist_directory = "vector_store/embedding_pdf_63pages"
        self.embedding_model = self.model_loader.load_embeddings()

    def _get_pdf_path(self):

        current_dir = os.getcwd()
        pdf_path = os.path.join(
            current_dir,
            "data",
            "Paramétrage Etablissement FILIERIS.pdf"
        )
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"PDF not found: {pdf_path}")

        return pdf_path

    def load_pdf(self):

        print("Loading PDF...")
        loader = PyPDFLoader(self.pdf_path)
        documents = loader.load()
        print(f"Loaded {len(documents)} pages.")

        return documents

    def split_documents(self, documents):

        print("Splitting documents into chunks...")
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1200,
            chunk_overlap=150,
            length_function=len,
        )
        split_docs = text_splitter.split_documents(documents)

        print(f"Created {len(split_docs)} chunks.")

        return split_docs

    def store_in_vector_db(self, documents):

        print("Storing embeddings into ChromaDB...")

        vector_db = Chroma.from_documents(
            documents=documents,
            embedding=self.embedding_model,
            persist_directory=self.persist_directory
        )

        print("Embeddings stored successfully.")

        return vector_db

    def run_pipeline(self):

        documents = self.load_pdf()
        split_docs = self.split_documents(documents)
        vector_db = self.store_in_vector_db(split_docs)
        print("Ingestion pipeline completed.")

        return vector_db


if __name__ == "__main__":

    ingestion = DataIngestion()

    ingestion.run_pipeline()




