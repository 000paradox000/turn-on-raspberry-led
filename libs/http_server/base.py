from typing import Literal, Optional

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# import RPi.GPIO as GPIO
import uvicorn

# from libs.models import InputMessage, OutputMessage
# from libs.raspberry.led_handler import LEDHandler
from libs import settings

PROJECT_DIR = settings.BASE_DIR / "libs" / "http_server"
TEMPLATES_DIR = PROJECT_DIR / "templates"
STATIC_DIR = PROJECT_DIR / "static"

app = FastAPI()

templates = Jinja2Templates(directory=TEMPLATES_DIR.as_posix())

app.mount(
    "/static",
    StaticFiles(directory=STATIC_DIR.as_posix()),
    name="static",
)


@app.get("/{page}", response_class=HTMLResponse)
@app.get("/", response_class=HTMLResponse)
async def index(
    request: Request,
    page: Optional[Literal["button", "text", "sign"]] = None,
):
    page = page or "button"

    context = {
        "request": request,
        "page": page,
    }
    return templates.TemplateResponse("index.html", context)


# @app.get("/text/", response_class=HTMLResponse)
# async def index_text(request: Request):
#     history = []
#
#     context = {
#         "request": request,
#         "state": False,
#         "history": history,
#     }
#     return templates.TemplateResponse("index_text.html", context)
#
#
# @app.post("/state/")
# def change_state(
#     request: Request, input_message: InputMessage
# ) -> OutputMessage:
#     state = input_message.state
#
#     handler = LEDHandler()
#     if state:
#         handler.on()
#     else:
#         handler.off()
#
#     output_message = OutputMessage(state=state)
#
#     return output_message


def start():
    uvicorn.run(
        app="libs.http_server.base:app",
        host=settings.HTTP_SERVER_HOST,
        port=settings.HTTP_SERVER_PORT,
        reload=True,
    )