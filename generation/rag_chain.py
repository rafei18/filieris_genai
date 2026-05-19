from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from retrieval.retrieval import Retriever
from utils.model_loader import ModelLoader
from prompt_library.prompt import PROMPT_TEMPLATES


class RAGChain:

    def __init__(self):

        self.retriever_obj = Retriever()

        self.model_loader = ModelLoader()

        self.retriever = self.retriever_obj.load_retriever()

        self.llm = self.model_loader.load_llm()

        self.prompt = ChatPromptTemplate.from_template(
            PROMPT_TEMPLATES["filieris_bot"]
        )

    def generate_response(self, query: str):

        docs = self.retriever.invoke(query)

        context = "\n\n".join(
            [doc.page_content for doc in docs]
        )

        chain = (
            self.prompt
            | self.llm
            | StrOutputParser()
        )

        response = chain.invoke({
            "context": context,
            "question": query
        })

        return response