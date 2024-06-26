import RPi.GPIO as GPIO

from libs import settings
from .base import RaspberryBaseHandler


class LEDHandler(RaspberryBaseHandler):
    """
    A class to handle LED operations using Raspberry Pi GPIO.

    Attributes:
        _pin (int): The GPIO pin number where the LED is connected.
    """

    def __init__(self, pin: int | None = None) -> None:
        """
        Initialize the LEDHandler with a specific GPIO pin.

        Args:
            pin (int): The GPIO pin number where the LED is connected.
        """
        super().__init__()

        self._pin = pin or settings.PIN
        # Set up the specified GPIO pin as an output
        GPIO.setup(self._pin, GPIO.OUT)

    def on(self) -> None:
        """
        Turn on the LED.
        """
        GPIO.output(self._pin, GPIO.HIGH)
        print("LED is ON")

    def off(self) -> None:
        """
        Turn off the LED.
        """
        GPIO.output(self._pin, GPIO.LOW)
        print("LED is OFF")
