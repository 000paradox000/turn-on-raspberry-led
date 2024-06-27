import time
import pytest

from libs.pi import LEDHandler


@pytest.fixture(scope="module")
def led_handler():
    """
    Fixture to initialize and clean up the LEDHandler instance.
    """
    handler = LEDHandler()
    yield handler
    # handler.cleanup()


def test_led_handler_on_off(led_handler):
    """
    Test the LEDHandler's on and off methods with real GPIO.
    """
    # Turn the LED on
    led_handler.on()
    time.sleep(1)  # Wait for 1 second to visually confirm the LED is on
    assert led_handler.is_on() is True

    # Turn the LED off
    led_handler.off()
    time.sleep(1)  # Wait for 1 second to visually confirm the LED is off
    assert led_handler.is_off() is True
