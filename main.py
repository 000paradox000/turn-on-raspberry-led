import time

import RPi.GPIO as GPIO

MAX_TIME = 10


def main():
    # Set up GPIO using BCM numbering
    GPIO.setmode(GPIO.BCM)

    # Set up GPIO pin 18 as an output
    GPIO.setup(18, GPIO.OUT)

    try:
        # Turn on the LED
        GPIO.output(18, GPIO.HIGH)
        print("LED is ON")

        # Keep the LED on for 10 seconds and print every second
        for i in range(MAX_TIME):
            time.sleep(1)
            print(f"LED has been ON for {i + 1} seconds")

        # Turn off the LED
        GPIO.output(18, GPIO.LOW)
        print("LED is OFF")

    finally:
        # Clean up GPIO settings
        GPIO.cleanup()


if __name__ == "__main__":
    main()
