import RPi.GPIO as GPIO

from libs import settings
from .base import RaspberryBaseHandler


class LEDHandler(RaspberryBaseHandler):
    """
    A class to handle LED operations using Raspberry Pi GPIO.

    Attributes:
        _pin (int): The GPIO pin number where the LED is connected.
    """

    def __init__(self) -> None:
        """Initialize the LEDHandler with a specific GPIO pin."""
        super().__init__()

        self._pin = settings.LED_PIN
        # Set up the specified GPIO pin as an output
        GPIO.setup(self._pin, GPIO.OUT)

    def _on(self) -> None:
        """
        Turn on the LED.
        """
        GPIO.output(self._pin, GPIO.HIGH)
        print("LED is ON")

    def _off(self) -> None:
        """
        Turn off the LED.
        """
        GPIO.output(self._pin, GPIO.LOW)
        print("LED is OFF")

    def _is_on(self) -> bool:
        return GPIO.input(self._pin) == GPIO.HIGH

    def _is_off(self) -> bool:
        return GPIO.input(self._pin) == GPIO.LOW

    @property
    def state(self) -> bool:
        return self._is_on()

    @state.setter
    def state(self, value: bool):
        if value and self._is_off():
            self._on()
        elif not value and self._is_on():
            self._off()
