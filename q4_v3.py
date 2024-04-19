import pigpio
import time
import math

# Definición de pines (BCM)
PWM_q4 = 6
A_q4 = 10
B_q4 = 9
MOTOR_A_PIN_q4 = 20
MOTOR_B_PIN_q4 = 21

# Constantes del PID y del motor
Kc_q4 = 2.0
Taui_q4 = 0.012
Taud_q4 = 0.4
T = 0.01
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

# Instancia de pigpio
pi = pigpio.pi()

# Configuración de pines
pi.set_mode(PWM_q4, pigpio.OUTPUT)
pi.set_mode(MOTOR_A_PIN_q4, pigpio.OUTPUT)
pi.set_mode(MOTOR_B_PIN_q4, pigpio.OUTPUT)
pi.set_mode(A_q4, pigpio.INPUT)
pi.set_mode(B_q4, pigpio.INPUT)

# Interrupción para contar pulsos del encoder
def contar_q4(gpio, level, tick):
    global pulsos_q4, posicion_q4
    if pi.read(B_q4) == 1:
        pulsos_q4 -= 1
    else:
        pulsos_q4 += 1

    if pulsos_q4 <= -ppr_chico or pulsos_q4 >= ppr_chico:
        pulsos_q4 = 0

    # Reajuste dentro del rango
    pulsos_q4 %= ppr_chico

    # Convertir pulsos a ángulo
    posicion_q4 = (pulsos_q4 / ppr_chico) * 360.0

pi.callback(A_q4, pigpio.FALLING_EDGE, contar_q4)

# Coeficientes del PID
BC1_q4 = Kc_q4 * (1 + (T / Taui_q4) + (Taud_q4 / T))
BC2_q4 = Kc_q4 * (-1 - (2 * Taud_q4 / T))
BC3_q4 = Kc_q4 * Taud_q4 / T

def PID_q4():
    global Mk1_q4, E1_q4, E2_q4, E_q4
    E_q4 = q4 - posicion_q4
    E_q4 = (E_q4 + 180) % 360 - 180  # Normalizar error entre -180 y 180

    Mk = Mk1_q4 + BC1_q4 * E_q4 + BC2_q4 * E1_q4 + BC3_q4 * E2_q4
    Mk = max(min(Mk, limit_Mk), 0)

    # Determinar la dirección y aplicar PWM
    pulse_width = int((Mk / limit_Mk) * 255)
    pi.set_PWM_dutycycle(PWM_q4, pulse_width)
    if E_q4 > 0:
        pi.write(MOTOR_A_PIN_q4, 1)
        pi.write(MOTOR_B_PIN_q4, 0)
    else:
        pi.write(MOTOR_A_PIN_q4, 0)
        pi.write(MOTOR_B_PIN_q4, 1)

    # Actualizar estados del PID
    Mk1_q4 = Mk
    E2_q4 = E1_q4
    E1_q4 = E_q4

# Bucle principal
try:
    last_time = time.time()
    while True:
        current_time = time.time()
        if current_time - last_time > T:
            PID_q4()
            last_time = current_time
except KeyboardInterrupt:
    pi.set_PWM_dutycycle(PWM_q4, 0)
    pi.stop()
