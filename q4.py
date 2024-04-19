import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Constants
PWM_q4 = 27
A_q4 = 23
B_q4 = 18
MOTOR_A_PIN_q4 = 16
MOTOR_B_PIN_q4 = 12

ppr_chico = 2441
T = 0.01
Kc_q4 = 2
Taui_q4 = 0.012
Taud_q4 = 0.4
limit_Mk = 100

# Setup GPIO
GPIO.setup([A_q4, B_q4], GPIO.IN)
GPIO.setup([MOTOR_A_PIN_q4, MOTOR_B_PIN_q4], GPIO.OUT)

# Setup PWM - Frequency: 1000 Hz
pwm_q4 = GPIO.PWM(PWM_q4, 1000)
pwm_q4.start(0)  # Start PWM with 0% duty cycle

pulsos_q4 = 0
posicion_q4 = 0

def contar_q4(channel):
    global pulsos_q4, posicion_q4
    if GPIO.input(B_q4) == GPIO.HIGH:
        pulsos_q4 -= 1
    else:
        pulsos_q4 += 1

    pulsos_q4 = pulsos_q4 % ppr_chico  # Manage overflow
    posicion_q4 = (pulsos_q4 * 360) // ppr_chico

GPIO.add_event_detect(A_q4, GPIO.RISING, callback=contar_q4)

def PID_q4():
    global posicion_q4
    Mk1_q4, E1_q4, E2_q4 = 0, 0, 0
    E_q4 = 30 - posicion_q4  # Desired angle - Current angle

    # PID calculation
    Mk = Mk1_q4 + Kc_q4 * (E_q4 + (T / Taui_q4 + Taud_q4 / T) * E1_q4 + Taud_q4 / T * E2_q4)
    Mk = max(0, min(Mk, limit_Mk))  # Constrain Mk to 0 to limit_Mk

    # Set PWM duty cycle
    duty_cycle = (Mk / limit_Mk) * 100
    pwm_q4.ChangeDutyCycle(duty_cycle)

    # Update variables for next loop
    Mk1_q4, E1_q4, E2_q4 = Mk, E_q4, E1_q4

# Main loop
while True:
    if (time.time() * 1000 - tiempoAnterior) > (T * 1000):
        PID_q4()
        print("llamo pid")
    tiempoAnterior = time.time() * 1000
