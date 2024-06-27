import RPi.GPIO as GPIO


class RaspberryBaseHandler:
    _instance = None

    def __new__(cls, pin):
        if cls._instance is None:
            cls._instance = super(RaspberryBaseHandler, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self) -> None:
        if self._initialized:
            return

        GPIO.setmode(GPIO.BCM)

    @staticmethod
    def cleanup():
        GPIO.cleanup()
