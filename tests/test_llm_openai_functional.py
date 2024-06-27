from libs import settings  # noqa: F401
from libs.llm.openai import OpenAILLMHandler


def test_llm_openai_on():
    """Test the LLM with OpenAI to obtain ON."""
    handler = OpenAILLMHandler()

    user_commands = [
        ("quiero prender el bombillo", True),
        ("quiero apagar el bombillo", False),
        ("el ultimo en dormirse por favor que apague el foco", False),
        ("turn off the light", False),
        ("Please switch on the light.", True),
        ("Can you turn on the light?", True),
        ("Illuminate the room.", True),
        ("Activate the lights, please.", True),
        ("Let there be light.", True),
        ("Please switch off the light.", False),
        ("Can you turn off the light?", False),
        ("Extinguish the light.", False),
        ("Deactivate the lights, please.", False),
        ("Turn off the light, please.", False),
        ("Por favor, enciende la luz.", True),
        ("¿Puedes prender la luz?", True),
        ("Ilumina el cuarto.", True),
        ("Activa las luces, por favor.", True),
        ("Que se haga la luz.", True),
        ("Por favor, apaga la luz.", False),
        ("¿Puedes apagar la luz?", False),
        ("Extingue la luz.", False),
        ("Desactiva las luces, por favor.", False),
        ("Apaga la luz, por favor.", False),
    ]

    for user_command, expected_answer in user_commands:
        received_answer = handler.get_state(user_command)
        error_msg = f"{user_command} => {received_answer}"
        assert received_answer is expected_answer, error_msg
