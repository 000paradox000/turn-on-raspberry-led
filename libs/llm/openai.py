from langchain_openai import ChatOpenAI

from .base import LLMBaseHandler


class OpenAILLMHandler(LLMBaseHandler):
    def __init__(self):
        super().__init__()
        self._llm = ChatOpenAI(model="gpt-4o")
