from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from .prompts import system_template


class LLMBaseHandler:
    def __init__(self):
        self._llm = None
        self._parser = StrOutputParser()
        self._prompt = ChatPromptTemplate.from_messages(
            [
                ("system", system_template),
                ("user", "{user_command}"),
            ]
        )

    def get_state(self, user_command: str) -> bool:
        chain = self._prompt | self._llm | self._parser
        result = chain.invoke(
            {
                "user_command": user_command,
            }
        )

        result = self._clean_result(result)
        if result == "True":
            return True
        elif result == "False":
            return False

    @staticmethod
    def _clean_result(value: str) -> str:
        value = value.strip()
        value = value.replace("'", "")
        value = value.replace('"', "")
        value = value.replace("`", "")

        return value
