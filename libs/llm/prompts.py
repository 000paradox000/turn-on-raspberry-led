# flake8: noqa: E501

system_template = """
Interpret the following user command and determine if it should turn the lights on or off.
Respond with `True` if it should turn on the lights and `False` if it should turn off the lights.

Examples:
- `Turn on the LED`: `True`
- `Turn off the LED`: `False`
- `Switch on the light`: `True`
- `Switch off the light`: `False`
- `quiero apagar el bombillo`: `False`
- `quiero prender el bombillo`: `True`
- `Switch on the lights`: `True`
- `Switch off the lights`: `False`
"""
