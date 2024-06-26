from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import RPi.GPIO as GPIO

from libs.models import InputMessage, OutputMessage
from libs.raspberry.led_handler import LEDHandler
from libs import settings

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    context = {
        "request": request,
        "state": False,
    }
    return templates.TemplateResponse("index.html", context)


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
        uvicorn.run(
            app="main:app",
            host="0.0.0.0",
            port=settings.FASTAPI_PORT,
            reload=True,
        )
    except KeyboardInterrupt:
        GPIO.cleanup()
