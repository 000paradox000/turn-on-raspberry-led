from fastapi import FastAPI, Request
import RPi.GPIO as GPIO

from libs.models import InputMessage, OutputMessage
from libs.raspberry.led_handler import LEDHandler

app = FastAPI()


@app.post("/state/")
def change_state(
    request: Request, input_message: InputMessage
) -> OutputMessage:
    state = input_message.state

    handler = LEDHandler()
    if state:
        handler.on()
    else:
        handler.off()

    output_message = OutputMessage(state=state)

    return output_message


if __name__ == "__main__":
    import uvicorn

    try:
        uvicorn.run(app="main:app", host="0.0.0.0", port=9600, reload=True)
    except KeyboardInterrupt:
        GPIO.cleanup()
