import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(override=False)

LED_PIN = os.environ["LED_PIN"]

BASE_DIR = Path(__file__).resolve().parent.parent
HTTP_SERVER_PORT = int(os.environ["HTTP_SERVER_PORT"])
HTTP_SERVER_HOST = os.environ["HTTP_SERVER_HOST"]
HTTP_SERVER_URL = os.environ["HTTP_SERVER_URL"]
