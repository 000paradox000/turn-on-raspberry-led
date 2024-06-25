import time

import RPi.GPIO as GPIO


def main():
    # Set up GPIO using BCM numbering
    GPIO.setmode(GPIO.BCM)

    # Set up GPIO pin 18 as an output
    GPIO.setup(18, GPIO.OUT)

    try:
        # Turn on the LED
        GPIO.output(18, GPIO.HIGH)
        print("LED is ON")

        # Keep the LED on for 10 seconds
        time.sleep(10)

        # Turn off the LED
        GPIO.output(18, GPIO.LOW)
        print("LED is OFF")

    finally:
        # Clean up GPIO settings
        GPIO.cleanup()


if __name__ == "__main__":
    main()
