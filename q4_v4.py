import RPi.GPIO as GPIO
import time

# Definición de pines
PWM_q4 = 6
A_q4 = 10
B_q4 = 9
MOTOR_A_PIN_q4 = 20
MOTOR_B_PIN_q4 = 21

# Configuración de GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(A_q4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(B_q4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(PWM_q4, GPIO.OUT)
GPIO.setup(MOTOR_A_PIN_q4, GPIO.OUT)
GPIO.setup(MOTOR_B_PIN_q4, GPIO.OUT)

pwm = GPIO.PWM(PWM_q4, 1000)  # PWM a 1000 Hz
pwm.start(0)

# Constantes del PID y del motor
Kc_q4 = 2.0
Taui_q4 = 0.012
Taud_q4 = 0.4
T = 0.01  # Intervalo de tiempo (10 ms)
ppr_chico = 2441
limit_Mk = 100

# Variables del estado del motor y posición
pulsos_q4 = 0
posicion_q4 = 0.0
E_q4 = 0.0
Mk1_q4 = 0.0
E1_q4 = 0.0
E2_q4 = 0.0
q4 = 90  # Posición deseada en grados

def encoder_callback(channel):
    global pulsos_q4
    if GPIO.input(B_q4) == GPIO.input(A_q4):
        pulsos_q4 += 1
    else:
        pulsos_q4 -= 1

GPIO.add_event_detect(A_q4, GPIO.BOTH, callback=encoder_callback)

def calcular_posicion():
    global posicion_q4
    posicion_q4 = (360.0 / ppr_chico) * pulsos_q4

def pid_control():
    global E_q4, E1_q4, E2_q4, Mk1_q4
    E_q4 = q4 - posicion_q4
    Mk = Mk1_q4 + Kc_q4 * (E_q4 - E1_q4) + (Kc_q4 / Taui_q4) * T * E_q4 + (Taud_q4 / T) * (E_q4 - 2 * E1_q4 + E2_q4)
    Mk = max(min(Mk, limit_Mk), -limit_Mk)
    Mk1_q4 = Mk
    E2_q4 = E1_q4
    E1_q4 = E_q4
    return Mk

def actualizar_motor(Mk):
    duty_cycle = abs(Mk)
    pwm.ChangeDutyCycle(duty_cycle)
    if Mk > 0:
        GPIO.output(MOTOR_A_PIN_q4, GPIO.HIGH)
        GPIO.output(MOTOR_B_PIN_q4, GPIO.LOW)
    else:
        GPIO.output(MOTOR_A_PIN_q4, GPIO.LOW)
        GPIO.output(MOTOR_B_PIN_q4, GPIO.HIGH)

try:
    while True:
        calcular_posicion()
        Mk = pid_control()
        actualizar_motor(Mk)
        time.sleep(T)
finally:
    pwm.stop()
    GPIO.cleanup()
