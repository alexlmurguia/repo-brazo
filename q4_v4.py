import RPi.GPIO as GPIO
import time

# Configuración de los pines
A_q4 = 10  # Pin del encoder A
B_q4 = 9   # Pin del encoder B

GPIO.setmode(GPIO.BCM)
GPIO.setup(A_q4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(B_q4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def read_encoder():
    pulsos_q4 = 0
    last_state = GPIO.input(A_q4)

    try:
        while True:
            # Espera a que el pin A cambie, indicando un pulso del encoder
            GPIO.wait_for_edge(A_q4, GPIO.BOTH)
            current_state = GPIO.input(A_q4)

            # Determinar la dirección del encoder
            if current_state != last_state:
                if GPIO.input(B_q4) == current_state:
                    pulsos_q4 += 1
                else:
                    pulsos_q4 -= 1
                print("Pulsos: {}".format(pulsos_q4))

            last_state = current_state

    except KeyboardInterrupt:
        GPIO.cleanup()

if __name__ == "__main__":
    read_encoder()
