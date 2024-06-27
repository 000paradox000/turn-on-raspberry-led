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

        self._pin: int = settings.LED_PIN
        self._modified: bool = False
        GPIO.setup(self._pin, GPIO.OUT)

    def on(self) -> None:
        """Turn on the LED."""
        GPIO.output(self._pin, GPIO.HIGH)
        print("LED is ON")

    def off(self) -> None:
        """Turn off the LED."""
        GPIO.output(self._pin, GPIO.LOW)
        print("LED is OFF")

    def is_on(self) -> bool:
        return GPIO.input(self._pin) == GPIO.HIGH

    def is_off(self) -> bool:
        return GPIO.input(self._pin) == GPIO.LOW

    @property
    def state(self) -> bool:
        return self.is_on()

    @state.setter
    def state(self, value: bool):
        self._modified = False
        if value and self.is_off():
            self.on()
            self._modified = True
        elif not value and self.is_on():
            self.off()
            self._modified = True

    @property
    def modified(self):
        return self._modified
