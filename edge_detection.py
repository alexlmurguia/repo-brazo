import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
test_pin = 10  # Asegúrate de que este pin no está siendo utilizado por otro hardware o script

GPIO.setup(test_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
try:
    GPIO.add_event_detect(test_pin, GPIO.BOTH)
    print("Edge detection added successfully!")
    while True:
        time.sleep(1)
except Exception as e:
    print(f"Failed to add edge detection: {e}")
finally:
    GPIO.cleanup()
