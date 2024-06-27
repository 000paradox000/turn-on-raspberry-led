import time
from http import HTTPStatus

import requests
import pytest

from libs import settings
from libs import utilities

# Ensure this test file is only run on a Raspberry Pi
if not utilities.is_raspberry():
    pytest.skip(
        "Skipping GPIO tests on non-Raspberry Pi platforms",
        allow_module_level=True,
    )


def test_led_handler_http_client_on_off():
    """
    Test the LEDHandler's on and off methods with real GPIO using http client.
    """
    headers = {
        "Content-Type": "application/json",
    }

    host = settings.HTTP_SERVER_HOST
    port = settings.HTTP_SERVER_PORT
    url = f"http://{host}:{port}/state/"

    # Turn the LED on
    body = {
        "state": True,
    }

    response = requests.post(
        url=url,
        json=body,
        headers=headers,
    )

    assert response.status_code == HTTPStatus.OK

    received_json = response.json()

    expected_answer = True
    received_answer = received_json["state"]
    assert received_answer is expected_answer

    expected_answer = True
    received_answer = received_json["modified"]
    assert received_answer is expected_answer

    time.sleep(3)  # Wait for 1 second to visually confirm the LED is on

    # Turn the LED off
    body = {
        "state": False,
    }

    response = requests.post(
        url=url,
        json=body,
        headers=headers,
    )

    assert response.status_code == HTTPStatus.OK

    received_json = response.json()

    expected_answer = False
    received_answer = received_json["state"]
    assert received_answer is expected_answer

    expected_answer = True
    received_answer = received_json["modified"]
    assert received_answer is expected_answer

    # Turn the LED off when led is already off
    body = {
        "state": False,
    }

    response = requests.post(
        url=url,
        json=body,
        headers=headers,
    )

    assert response.status_code == HTTPStatus.OK

    received_json = response.json()

    expected_answer = False
    received_answer = received_json["state"]
    assert received_answer is expected_answer

    expected_answer = False
    received_answer = received_json["modified"]
    assert received_answer is expected_answer
