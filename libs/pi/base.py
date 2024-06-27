import RPi.GPIO as GPIO


class RaspberryBaseHandler:
    def __init__(self) -> None:
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

    @staticmethod
    def cleanup():
        GPIO.cleanup()
