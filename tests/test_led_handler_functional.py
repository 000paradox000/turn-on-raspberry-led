import time
import pytest
from libs import utilities

# Ensure this test file is only run on a Raspberry Pi
if not utilities.is_raspberry():
    pytest.skip(
        "Skipping GPIO tests on non-Raspberry Pi platforms",
        allow_module_level=True,
    )

import RPi.GPIO as GPIO
from libs.raspberry.led_handler import LEDHandler


@pytest.fixture(scope="module")
def led_handler():
    """
    Fixture to initialize and clean up the LEDHandler instance.
    """
    handler = LEDHandler(18)
    yield handler
    GPIO.cleanup()


def test_led_handler_on_off(led_handler):
    """
    Test the LEDHandler's on and off methods with real GPIO.
    """
    # Turn the LED on
    led_handler.on()
    time.sleep(1)  # Wait for 1 second to visually confirm the LED is on
    assert GPIO.input(18) == GPIO.HIGH
    print("Test: LED on method executed correctly.")

    # Turn the LED off
    led_handler.off()
    time.sleep(1)  # Wait for 1 second to visually confirm the LED is off
    assert GPIO.input(18) == GPIO.LOW
    print("Test: LED off method executed correctly.")


def test_led_on_off_sequence(led_handler):
    """
    Test the sequence of turning the LED on and off with real GPIO.
    """
    # Turn the LED on and off in sequence
    led_handler.on()
    time.sleep(1)  # Wait for 1 second to visually confirm the LED is on
    assert GPIO.input(18) == GPIO.HIGH

    led_handler.off()
    time.sleep(1)  # Wait for 1 second to visually confirm the LED is off
    assert GPIO.input(18) == GPIO.LOW
    print("Test: LED on and off sequence executed correctly.")
