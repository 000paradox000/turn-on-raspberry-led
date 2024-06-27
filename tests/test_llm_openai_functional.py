from libs import settings  # noqa: F401
from libs.llm.openai import OpenAILLMHandler


def test_llm_openai_on(user_commands):
    """Test the LLM with OpenAI to obtain ON."""
    handler = OpenAILLMHandler()

    for user_command, expected_answer in user_commands:
        received_answer = handler.get_state(user_command)
        error_msg = f"{user_command} => {received_answer}"
        assert received_answer is expected_answer, error_msg
