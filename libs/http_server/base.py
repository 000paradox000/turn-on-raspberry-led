from typing import Literal, Optional

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn

from libs import settings
from .models import InputMessage, OutputMessage
from libs.pi import LEDHandler

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

led_handler = LEDHandler()


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return RedirectResponse(url="/static/favicon/favicon.ico")


@app.get("/{page}", response_class=HTMLResponse)
@app.get("/", response_class=HTMLResponse)
async def index(
    request: Request,
    page: Optional[Literal["button", "text", "sign"]] = None,
):
    actions = {
        "button": "/button/",
        "text": "/text/",
        "sign": "/sign/",
    }
    page = page or "button"
    state = led_handler.state
    button_css_class = "huge-button-off" if state else "huge-button-on"
    button_label = "OFF" if state else "ON"
    action = actions[page]
    context = {
        "request": request,
        "page": page,
        "state": state,
        "button_css_class": button_css_class,
        "button_label": button_label,
        "action": action,
    }
    return templates.TemplateResponse("index.html", context)


@app.post("/state/")
def change_state(
    request: Request,
    input_message: InputMessage,
) -> OutputMessage:
    led_handler.state = input_message.state

    return OutputMessage(
        state=led_handler.state,
        modified=led_handler.modified,
    )


def start():
    uvicorn.run(
        app="libs.http_server.base:app",
        host=settings.HTTP_SERVER_HOST,
        port=settings.HTTP_SERVER_PORT,
        reload=True,
    )
