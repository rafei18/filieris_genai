from langchain_huggingface import HuggingFaceEmbeddings


class ModelLoader:

    def load_embeddings(self):

        embedding_model = HuggingFaceEmbeddings(
            model_name="BAAI/bge-m3"
        )

        return embedding_model