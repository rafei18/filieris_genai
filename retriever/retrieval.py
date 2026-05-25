import os
from typing import List

from dotenv import load_dotenv

from langchain_core.documents import Document
from langchain_chroma import Chroma

from utils.model_loader import ModelLoader
#from config.config_loader import load_config
from utils.config_loader import load_config


class Retriever:
    """
    Handle retrieval from Chroma Vector DB.
    """

    def __init__(self):

        print("Initializing Retriever...")
        load_dotenv()
        self.model_loader = ModelLoader()
        self.config = load_config()
        self.persist_directory = self.config["chroma"]["persist_directory"]
        self.embedding_model = self.model_loader.load_embeddings()
        self.vdb = None
        self.retriever = None

    def load_vector_store(self):

        """
        Load persisted Chroma vector database.
        """

        if self.vdb is None:

            print("Loading ChromaDB...")

            self.vdb = Chroma(
                persist_directory=self.persist_directory,
                embedding_function=self.embedding_model
            )

            print("chromaDB loaded successfully")

        return self.vdb

    def load_retriever(self):

        """
        Create retriever from vector store.
        """
        if self.retriever is None:
            vdb = self.load_vector_store()
            top_k = self.config["retriever"]["top_k"]
            self.retriever = vdb.as_retriever(
                search_kwargs={"k": top_k}
            )

            print(f"retriever loaded successfully with top_k={top_k}")

        return self.retriever

    def retrieve_documents(self, query: str) -> List[Document]:

        """
        retrieve k relevant chunks for 
        """
        retriever = self.load_retriever()
        results = retriever.invoke(query)
        return results


if __name__ == "__main__":

    retriever_obj = Retriever()
    query = "MOTIFS D'HOSPITALISATION"
    results = retriever_obj.retrieve_documents(query)
    print("\n===== RETRIEVED DOCUMENTS =====\n")

    for idx, doc in enumerate(results, 1):

        print(f"Result {idx}\n")
        print(doc.page_content)
        print("\nMetadata:")
        print(doc.metadata)
        print("\n" + "="*80 + "\n")