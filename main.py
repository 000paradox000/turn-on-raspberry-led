import time
import RPi.GPIO as GPIO


class LEDHandler:
    """
    A class to handle LED operations using Raspberry Pi GPIO.

    Attributes:
        _pin (int): The GPIO pin number where the LED is connected.
    """
    def __init__(self, pin: int) -> None:
        """
        Initialize the LEDHandler with a specific GPIO pin.

        Args:
            pin (int): The GPIO pin number where the LED is connected.
        """
        self._pin = pin
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


def main() -> None:
    """
    Main function to handle LED operations.

    It sets up the GPIO mode, turns the LED on for a specified duration,
    and then turns it off, followed by cleaning up the GPIO settings.
    """
    # Set up GPIO using BCM numbering
    GPIO.setmode(GPIO.BCM)

    led_handler = LEDHandler(18)

    try:
        # Turn on the LED
        led_handler.on()

        # Keep the LED on for 10 seconds and print every second
        for i in range(10):
            time.sleep(1)
            print(f"LED has been ON for {i + 1} seconds")

        # Turn off the LED
        led_handler.off()
    finally:
        # Clean up GPIO settings
        GPIO.cleanup()


if __name__ == "__main__":
    main()