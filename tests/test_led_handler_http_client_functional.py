import time
from http import HTTPStatus

import requests


from libs import settings


def test_led_handler_http_client_on_off():
    """
    Test the LEDHandler's on and off methods with real GPIO using http client.
    """
    headers = {
        "Content-Type": "application/json",
    }

    # Turn the LED on
    body = {
        "state": True,
    }
    response = requests.post(
        url=settings.FASTAPI_URL,
        json=body,
        headers=headers,
    )
    expected_answer = True
    assert response.status_code == HTTPStatus.OK
    received_answer = response.json()["state"]
    assert received_answer is expected_answer

    time.sleep(3)  # Wait for 1 second to visually confirm the LED is on

    # Turn the LED off
    body = {
        "state": False,
    }
    response = requests.post(
        url=settings.FASTAPI_URL,
        json=body,
        headers=headers,
    )
    expected_answer = False
    assert response.status_code == HTTPStatus.OK
    received_answer = response.json()["state"]
    assert received_answer is expected_answer
