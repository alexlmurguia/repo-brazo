#sudo apt install pigpio
#sudo pigpiod

import pigpio
import time

# Configuración de pines
PWM_q4 = 6
A_q4 = 19
B_q4 = 25
MOTOR_A_PIN_q4 = 28
MOTOR_B_PIN_q4 = 29

# Constantes de control PID
Kc_q4 = 2.0
Taui_q4 = 0.012
Taud_q4 = 0.4
T = 0.01
ppr_chico = 2441
limit_Mk = 100

# Variables para la lógica de control
pulsos_q4 = 0
posicion_q4 = 0
E_q4 = 0
Mk1_q4 = 0
E1_q4 = 0
E2_q4 = 0

# Iniciar pigpio
pi = pigpio.pi()

# Configurar pines
pi.set_mode(PWM_q4, pigpio.OUTPUT)
pi.set_mode(MOTOR_A_PIN_q4, pigpio.OUTPUT)
pi.set_mode(MOTOR_B_PIN_q4, pigpio.OUTPUT)
pi.set_mode(A_q4, pigpio.INPUT)
pi.set_mode(B_q4, pigpio.INPUT)

# Función para manejar interrupciones
def contar_q4(gpio, level, tick):
    global pulsos_q4, posicion_q4
    if pi.read(B_q4) == 1:
        pulsos_q4 += 1
    else:
        pulsos_q4 -= 1

    if pulsos_q4 == -ppr_chico:
        pulsos_q4 = 0
    if pulsos_q4 < 0:
        pulsos_q4 += ppr_chico
    if pulsos_q4 == ppr_chico:
        pulsos_q4 = 0

    posicion_q4 = (pulsos_q4 / ppr_chico) * 360

# Configurar interrupción
pi.callback(A_q4, pigpio.FALLING_EDGE, contar_q4)

# Coeficientes de la ecuación de diferencias del PID
BC1_q4 = Kc_q4 * (1 + (T / Taui_q4) + (Taud_q4 / T))
BC2_q4 = Kc_q4 * (-1 - (2 * Taud_q4 / T))
BC3_q4 = Kc_q4 * Taud_q4 / T

def PID_q4():
    global Mk1_q4, E1_q4, E2_q4
    E_q4 = q4 - posicion_q4  # Define q4 as needed
    Mk = Mk1_q4 + BC1_q4 * E_q4 + BC2_q4 * E1_q4 + BC3_q4 * E2_q4
    Mk = max(min(Mk, limit_Mk), 0)
    pulse_width = int((Mk / limit_Mk) * 255)
    pi.set_PWM_dutycycle(PWM_q4, pulse_width)
    pi.write(MOTOR_A_PIN_q4, 1 if E_q4 > 0 else 0)
    pi.write(MOTOR_B_PIN_q4, 1 if E_q4 < 0 else 0)

    Mk1_q4 = Mk
    E2_q4 = E1_q4
    E1_q4 = E_q4

# Bucle principal
try:
    last_time = time.time()
    while True:
        if time.time() - last_time > T:
            PID_q4()
            last_time = time.time()
except KeyboardInterrupt:
    pi.set_PWM_dutycycle(PWM_q4, 0)
   
