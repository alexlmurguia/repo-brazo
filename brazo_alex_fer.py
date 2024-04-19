import RPi.GPIO as GPIO
import time
import threading

GPIO.setwarnings(False)


PWM_q1_1 = 3
PWM_q1_2 = 5
PWM_q2_1 = 7
PWM_q2_2 = 16 #regresar a 11, cambie a 16 para la prueba
PWM_q3_1 = 13
PWM_q3_2 = 15
PWM_q4 = 19
#PWM_q5 = 21
#PWM_q6 = 23
PWM_on = 0
PWM_off = 0

pulse_width = 0
ppr_grande = 5986
ppr_chico = 2441

A_q1 = 29
B_q1 = 31
A_q2 = 33
B_q2 = 35
A_q3 = 40
B_q3 = 38
A_q4 = 36
B_q4 = 32
A_q5 = 26
B_q5 = 24
A_q6 = 22
B_q6 = 18

MOTOR_A_PIN_q4 = 11 #cambiar a 16, cambie a 11 para la prueba
MOTOR_B_PIN_q4 = 12 
MOTOR_A_PIN_q5 = 10
MOTOR_B_PIN_q5 = 8
MOTOR_A_PIN_q6 = 22
MOTOR_B_PIN_q6 = 21

val1 = 0
val2 = 0
val3 = 0
val4 = 0
val5 = 0
val6 = 0

pulsos_q1 = 0
pulsos_q2 = 0
pulsos_q3 = 0
pulsos_q4 = 0
pulsos_q5 = 0
pulsos_q6 = 0

delim = ','
dataL = 6
data = [0] * dataL
q1, q2, q3, q4, q5, q6, origen, q, dir = 0, 0, 0, 0, 0, 0, 0, 0, 0
q1_en, q2_en, q3_en, q4_en, q5_en, q6_en = 0, 0, 0, 0, 0, 0
origen_pasado = 0
str = ""
negativo = True

Kc_q4 = 2
Taui_q4 = 0.012
Taud_q4 = 0.4
T = 0.01

Kc_q56 = 0.79
Taui_q56 = 0.008
Taud_q56 = 0.45

Kc_g = 23.4
Taui_g = 0.032
Taud_g = 0.008

E_q1, E_q2, E_q3, E_q4, E_q5, E_q6 = 0, 0, 0, 0, 0, 0
Mk = 0
Mk1_q1, E1_q1, E2_q1 = 0, 0, 0
Mk1_q2, E1_q2, E2_q2 = 0, 0, 0
Mk1_q3, E1_q3, E2_q3 = 0, 0, 0
Mk1_q4, E1_q4, E2_q4 = 0, 0, 0
Mk1_q5, E1_q5, E2_q5 = 0, 0, 0
Mk1_q6, E1_q6, E2_q6 = 0, 0, 0
limit_Mk = 100

posicion_q1, posicion_q2, posicion_q3, posicion_q4, posicion_q5, posicion_q6 = 0, 0, 0, 0, 0, 0
BC1_q4, BC2_q4, BC3_q4 = 0, 0, 0
BC1_q56, BC2_q56, BC3_q56 = 0, 0, 0
BC1_g, BC2_g, BC3_g = 0, 0, 0

tiempoAnterior = 0

# Configuración de los pines GPIO
GPIO.setmode(GPIO.BCM)

# Configuración de la comunicación serial
#serial = serial.Serial('/dev/ttyAMA0', 115200)  # Puedes cambiar '/dev/ttyS0' según el puerto serial en tu Raspberry
#serial3 = serial.Serial('/dev/ttyS2', 115200)  # Puedes cambiar '/dev/ttyS2' según el puerto serial en tu Raspberry Pi

# Configuración del PWM
GPIO.setup(PWM_q1_1 , GPIO.OUT)  # Pin del PWM_q1_1
GPIO.setup(PWM_q1_2, GPIO.OUT)  # Pin del PWM_q1_2
GPIO.setup(PWM_q2_1, GPIO.OUT)  # Pin del PWM_q2_1
GPIO.setup(PWM_q2_2, GPIO.OUT)  # Pin del PWM_q2_2
GPIO.setup(PWM_q3_1, GPIO.OUT)  # Pin del PWM_q3_1
GPIO.setup(PWM_q3_2, GPIO.OUT)  # Pin del PWM_q3_2
GPIO.setup(PWM_q4, GPIO.OUT)  # Pin del PWM_q4
#GPIO.setup(7, GPIO.OUT)  # Pin del PWM_q5
#GPIO.setup(8, GPIO.OUT)  # Pin del PWM_q6

# Configuración de los pines como entradas
pins = [A_q1, B_q1, A_q2, B_q2, A_q3, B_q3, A_q4, B_q4, A_q5, B_q5, A_q6, B_q6]
for pin in pins:
    GPIO.setup(pin, GPIO.IN)

# Configuración de los pines como salidas para los motores
motor_pins = [MOTOR_A_PIN_q4, MOTOR_B_PIN_q4, MOTOR_A_PIN_q5, MOTOR_B_PIN_q5, MOTOR_A_PIN_q6, MOTOR_B_PIN_q6] #cambie el 16 por 11
for pin in motor_pins:
    GPIO.setup(pin, GPIO.OUT)

# Coeficientes de ecuación de diferencias de PID
BC1_q4 = Kc_q4 * (1 + (T / Taui_q4) + (Taud_q4 / T))
BC2_q4 = Kc_q4 * (-1 - (2 * Taud_q4 / T))
BC3_q4 = Kc_q4 * Taud_q4 / T

BC1_q56 = Kc_q56 * (1 + (T / Taui_q56) + (Taud_q56 / T))
BC2_q56 = Kc_q56 * (-1 - (2 * Taud_q56 / T))
BC3_q56 = Kc_q56 * Taud_q56 / T

BC1_g = Kc_g * (1 + (T / Taui_g) + (Taud_g / T))
BC2_g = Kc_g * (-1 - (2 * Taud_g / T))
BC3_g = Kc_g * Taud_g / T

def contar_q1():

    global pulsos_q1, posicion_q1
    # Verificar en qué sentido gira el motor y agregar pulsos
    if GPIO.input(B_q1) == GPIO.HIGH:
        pulsos_q1 += 1
    else:
        pulsos_q1 -= 1

    # Si el pulso es igual a -ppr, el pulso se restablece como 0
    if pulsos_q1 == -ppr_grande:
        pulsos_q1 = 0

    # Si el pulso es menor a 0, el pulso se reescribe en rango de 0 a ppr
    if pulsos_q1 < 0:
        pulsos_q1 += ppr_grande

    # Si el pulso es igual a ppr, el pulso se restablece como 0
    if pulsos_q1 == ppr_grande:
        pulsos_q1 = 0

    # Convertir la cantidad de pulsos en un ángulo en el rango de 0° a 360°
    posicion_q1 = map(pulsos_q1, 0, ppr_grande, 0, 360)

def contar_q2():

    global pulsos_q2, posicion_q2
    # Verificar en qué sentido gira el motor y agregar pulsos
    if GPIO.input(B_q2) == GPIO.HIGH:
        pulsos_q2 -= 1
    else:
        pulsos_q2 += 1

    # Si el pulso es igual a -ppr, el pulso se restablece como 0
    if pulsos_q2 == -ppr_grande:
        pulsos_q2 = 0

    # Si el pulso es menor a 0, el pulso se reescribe en rango de 0 a ppr
    if pulsos_q2 < 0:
        pulsos_q2 += ppr_grande

    # Si el pulso es igual a ppr, el pulso se restablece como 0
    if pulsos_q2 == ppr_grande:
        pulsos_q2 = 0

    # Convertir la cantidad de pulsos en un ángulo en el rango de 0° a 360°
    posicion_q2 = map(pulsos_q2, 0, ppr_grande, 0, 360)

def contar_q3():

    global pulsos_q3, posicion_q3
    # Verificar en qué sentido gira el motor y agregar pulsos
    if GPIO.input(B_q3) == GPIO.HIGH:
        pulsos_q3 -= 1
    else:
        pulsos_q3 += 1

    # Si el pulso es igual a -ppr, el pulso se restablece como 0
    if pulsos_q3 == -ppr_grande:
        pulsos_q3 = 0

    # Si el pulso es menor a 0, el pulso se reescribe en rango de 0 a ppr
    if pulsos_q3 < 0:
        pulsos_q3 += ppr_grande

    # Si el pulso es igual a ppr, el pulso se restablece como 0
    if pulsos_q3 == ppr_grande:
        pulsos_q3 = 0

    # Convertir la cantidad de pulsos en un ángulo en el rango de 0° a 360°
    posicion_q3 = map(pulsos_q3, 0, ppr_grande, 0, 360)

def contar_q4(channel):

    global pulsos_q4, posicion_q4
    # Verificar en qué sentido gira el motor y agregar pulsos
    if GPIO.input(B_q4) == GPIO.HIGH:
        pulsos_q4 -= 1
    else:
        pulsos_q4 += 1

    # Si el pulso es igual a -ppr, el pulso se restablece como 0
    if pulsos_q4 == -ppr_chico:
        pulsos_q4 = 0

    # Si el pulso es menor a 0, el pulso se reescribe en rango de 0 a ppr
    if pulsos_q4 < 0:
        pulsos_q4 += ppr_chico

    # Si el pulso es igual a ppr, el pulso se restablece como 0
    if pulsos_q4 == ppr_chico:
        pulsos_q4 = 0

    # Convertir la cantidad de pulsos en un ángulo en el rango de 0° a 360°
    posicion_q4 = map(pulsos_q4, 0, ppr_chico, 0, 360)

def contar_q5():

    global pulsos_q5, posicion_q5
    # Verificar en qué sentido gira el motor y agregar pulsos
    if GPIO.input(B_q5) == GPIO.HIGH:
        pulsos_q5 += 1
    else:
        pulsos_q5 -= 1

    # Si el pulso es igual a -ppr, el pulso se restablece como 0
    if pulsos_q5 == -ppr_chico:
        pulsos_q5 = 0

    # Si el pulso es menor a 0, el pulso se reescribe en rango de 0 a ppr
    if pulsos_q5 < 0:
        pulsos_q5 += ppr_chico

    # Si el pulso es igual a ppr, el pulso se restablece como 0
    if pulsos_q5 == ppr_chico:
        pulsos_q5 = 0

    # Convertir la cantidad de pulsos en un ángulo en el rango de 0° a 360°
    posicion_q5 = map(pulsos_q5, 0, ppr_chico, 0, 360)

def contar_q6():

    global pulsos_q6, posicion_q6
    # Verificar en qué sentido gira el motor y agregar pulsos
    if GPIO.input(B_q6) == GPIO.HIGH:
        pulsos_q6 -= 1
    else:
        pulsos_q6 += 1

    # Si el pulso es igual a -ppr, el pulso se restablece como 0
    if pulsos_q6 == -ppr_chico:
        pulsos_q6 = 0

    # Si el pulso es menor a 0, el pulso se reescribe en rango de 0 a ppr
    if pulsos_q6 < 0:
        pulsos_q6 += ppr_chico

    # Si el pulso es igual a ppr, el pulso se restablece como 0
    if pulsos_q6 == ppr_chico:
        pulsos_q6 = 0

    # Convertir la cantidad de pulsos en un ángulo en el rango de 0° a 360°
    posicion_q6 = map(pulsos_q6, 0, ppr_chico, 0, 360)


# Crear la interrupción de flancos negativos en q1
# (Necesitarás configurar esta parte específicamente en tu entorno de Raspberry Pi con la biblioteca RPi.GPIO)
# Ejemplo de cómo podría ser en Raspberry Pi:
GPIO.add_event_detect(A_q1, GPIO.FALLING, callback=contar_q1)
GPIO.add_event_detect(A_q2, GPIO.FALLING, callback=contar_q2)
GPIO.add_event_detect(A_q3, GPIO.FALLING, callback=contar_q3)
GPIO.add_event_detect(A_q4, GPIO.FALLING, callback=lambda channel: contar_q4())
GPIO.add_event_detect(A_q5, GPIO.FALLING, callback=contar_q5)
GPIO.add_event_detect(A_q6, GPIO.FALLING, callback=contar_q6)


def PID_q1():
    global E_q1, Mk, Mk1_q1, E1_q1, E2_q1

    # Verificar el error entre la referencia y valor actual de ángulo
    # Si es positivo, girar en sentido horario; si es negativo, girar en sentido anti-horario
    # Se realiza la manipulación por el controlador PID
    if E_q1 > 0:
        if (360 - E_q1) <= E_q1:
            E_q1 = 360 - E_q1
            PWM_on = PWM_q1_1
            PWM_off = PWM_q1_2
        else:
            PWM_off = PWM_q1_1
            PWM_on = PWM_q1_2

        Mk = Mk1_q1 + BC1_g * E_q1 + BC2_g * E1_q1 + BC3_g * E2_q1
        if Mk > limit_Mk:
            Mk = limit_Mk
        if Mk < 0:
            Mk = 0
        pulse_width = map(Mk, 0, limit_Mk, 40, 180)
        GPIO.output(PWM_on, pulse_width)
        GPIO.output(PWM_off, 0)

    elif E_q1 < 0:
        if (360 + E_q1) <= abs(E_q1):
            E_q1 = abs(360 + E_q1)
            PWM_off = PWM_q1_1
            PWM_on = PWM_q1_2
        else:
            E_q1 = abs(E_q1)
            PWM_on = PWM_q1_1
            PWM_off = PWM_q1_2

        Mk = Mk1_q1 + BC1_g * E_q1 + BC2_g * E1_q1 + BC3_g * E2_q1
        if Mk > limit_Mk:
            Mk = limit_Mk
        if Mk < 0:
            Mk = 0
        pulse_width = map(Mk, 0, limit_Mk, 40, 180)
        GPIO.output(PWM_on, pulse_width)
        GPIO.output(PWM_off, 0)

    else:
        Mk = 0
        pulse_width = map(Mk, 0, limit_Mk, 40, 180)
        GPIO.output(PWM_q1_1, pulse_width)
        GPIO.output(PWM_q1_2, pulse_width)

    Mk1_q1 = Mk
    E2_q1 = E1_q1
    E1_q1 = E_q1

def PID_q2():
    global E_q2, Mk, Mk1_q2, E1_q2, E2_q2, PWM_on, PWM_off, pulse_width

    # Verificar el error entre la referencia y valor actual de ángulo
    # Si es positivo, girar en sentido horario; si es negativo, girar en sentido anti-horario
    # Se realiza la manipulación por el controlador PID
    if E_q2 > 0:
        if (360 - E_q2) <= E_q2:
            E_q2 = 360 - E_q2
            PWM_on = PWM_q2_2
            PWM_off = PWM_q2_1
        else:
            PWM_off = PWM_q2_2
            PWM_on = PWM_q2_1

        Mk = Mk1_q2 + BC1_g * E_q2 + BC2_g * E1_q2 + BC3_g * E2_q2
        if Mk > limit_Mk:
            Mk = limit_Mk
        if Mk < 0:
            Mk = 0
        pulse_width = map(Mk, 0, limit_Mk, 40, 180)
        GPIO.output(PWM_on, pulse_width)
        GPIO.output(PWM_off, 0)
    
    elif E_q2 < 0:
        if (360 + E_q2) <= abs(E_q2):
            E_q2 = abs(360 + E_q2)
            PWM_off = PWM_q2_2
            PWM_on = PWM_q2_1
        else:
            E_q2 = abs(E_q2)
            PWM_on = PWM_q2_2
            PWM_off = PWM_q2_1

        Mk = Mk1_q2 + BC1_g * E_q2 + BC2_g * E1_q2 + BC3_g * E2_q2
        if Mk > limit_Mk:
            Mk = limit_Mk
        if Mk < 0:
            Mk = 0
        pulse_width = map(Mk, 0, limit_Mk, 40, 180)
        GPIO.output(PWM_on, pulse_width)
        GPIO.output(PWM_off, 0)
    
    else:
        Mk = 0
        pulse_width = map(Mk, 0, limit_Mk, 40, 180)
        GPIO.output(PWM_q2_2, pulse_width)
        GPIO.output(PWM_q2_1, pulse_width)

    Mk1_q2 = Mk
    E2_q2 = E1_q2
    E1_q2 = E_q2

def PID_q3():
    global E_q3, Mk, Mk1_q3, E1_q3, E2_q3

    # Verificar el error entre la referencia y valor actual de ángulo
    # Si es positivo, girar en sentido horario; si es negativo, girar en sentido anti-horario
    # Se realiza la manipulación por el controlador PID
    if E_q3 > 0:
        if (360 - E_q3) <= E_q3:
            E_q3 = 360 - E_q3
            PWM_on = PWM_q3_2
            PWM_off = PWM_q3_1
        else:
            PWM_off = PWM_q3_2
            PWM_on = PWM_q3_1

        Mk = Mk1_q3 + BC1_g * E_q3 + BC2_g * E1_q3 + BC3_g * E2_q3
        if Mk > limit_Mk:
            Mk = limit_Mk
        if Mk < 0:
            Mk = 0
        pulse_width = map(Mk, 0, limit_Mk, 40, 200)
        GPIO.output(PWM_on, pulse_width)
        GPIO.output(PWM_off, 0)

    elif E_q3 < 0:
        if (360 + E_q3) <= abs(E_q3):
            E_q3 = abs(360 + E_q3)
            PWM_off = PWM_q3_2
            PWM_on = PWM_q3_1
        else:
            E_q3 = abs(E_q3)
            PWM_on = PWM_q3_2
            PWM_off = PWM_q3_1

        Mk = Mk1_q3 + BC1_g * E_q3 + BC2_g * E1_q3 + BC3_g * E2_q3
        if Mk > limit_Mk:
            Mk = limit_Mk
        if Mk < 0:
            Mk = 0
        pulse_width = map(Mk, 0, limit_Mk, 40, 200)
        GPIO.output(PWM_on, pulse_width)
        GPIO.output(PWM_off, 0)

    else:
        Mk = 0
        pulse_width = map(Mk, 0, limit_Mk, 40, 200)
        GPIO.output(PWM_q3_2, pulse_width)
        GPIO.output(PWM_q3_1, pulse_width)

    Mk1_q3 = Mk
    E2_q3 = E1_q3
    E1_q3 = E_q3


def PID_q4():
    global E_q4, Mk, Mk1_q4, E1_q4, E2_q4

    # Verificar el error entre la referencia y valor actual de ángulo
    # Si es positivo, girar en sentido horario; si es negativo, girar en sentido anti-horario
    # Se realiza la manipulación por el controlador PID
    if E_q4 > 0:
        if (360 - E_q4) <= E_q4:
            E_q4 = 360 - E_q4
            GPIO.output(MOTOR_A_PIN_q4, GPIO.HIGH)
            GPIO.output(MOTOR_B_PIN_q4, GPIO.LOW)
        else:
            GPIO.output(MOTOR_A_PIN_q4, GPIO.LOW)
            GPIO.output(MOTOR_B_PIN_q4, GPIO.HIGH)

        Mk = Mk1_q4 + BC1_q4 * E_q4 + BC2_q4 * E1_q4 + BC3_q4 * E2_q4
        if Mk > limit_Mk:
            Mk = limit_Mk
        if Mk < 0:
            Mk = 0
        pulse_width = 40 + (Mk * (255 - 40) / limit_Mk)
        GPIO.output(PWM_q4, pulse_width)

    elif E_q4 < 0:
        if (360 + E_q4) <= abs(E_q4):
            E_q4 = abs(360 + E_q4)
            GPIO.output(MOTOR_A_PIN_q4, GPIO.LOW)
            GPIO.output(MOTOR_B_PIN_q4, GPIO.HIGH)
        else:
            GPIO.output(MOTOR_A_PIN_q4, GPIO.HIGH)
            GPIO.output(MOTOR_B_PIN_q4, GPIO.LOW)
            E_q4 = abs(E_q4)

        Mk = Mk1_q4 + BC1_q4 * E_q4 + BC2_q4 * E1_q4 + BC3_q4 * E2_q4
        if Mk > limit_Mk:
            Mk = limit_Mk
        if Mk < 0:
            Mk = 0
        pulse_width = 40 + (Mk * (255 - 40) / limit_Mk)
        GPIO.output(PWM_q4, pulse_width)

    else:
        Mk = 0
        GPIO.output(MOTOR_A_PIN_q4, GPIO.LOW)
        GPIO.output(MOTOR_B_PIN_q4, GPIO.LOW)
        pulse_width = map(Mk, 0, limit_Mk, 40, 255)
        GPIO.output(PWM_q4, pulse_width)

    Mk1_q4 = Mk
    E2_q4 = E1_q4
    E1_q4 = E_q4


def PID_q5():
    global E_q5, Mk, Mk1_q5, E1_q5, E2_q5

    # Verificar el error entre la referencia y valor actual de ángulo
    # Si es positivo, girar en sentido horario; si es negativo, girar en sentido anti-horario
    # Se realiza la manipulación por el controlador PID
    if E_q5 > 0:
        if (360 - E_q5) <= E_q5:
            E_q5 = 360 - E_q5
            GPIO.output(MOTOR_A_PIN_q5, GPIO.LOW)
            GPIO.output(MOTOR_B_PIN_q5, GPIO.HIGH)
        else:
            GPIO.output(MOTOR_A_PIN_q5, GPIO.HIGH)
            GPIO.output(MOTOR_B_PIN_q5, GPIO.LOW)

        Mk = Mk1_q5 + BC1_q56 * E_q5 + BC2_q56 * E1_q5 + BC3_q56 * E2_q5
        if Mk > limit_Mk:
            Mk = limit_Mk
        if Mk < 0:
            Mk = 0
        pulse_width = map(Mk, 0, limit_Mk, 40, 255)
        GPIO.output(PWM_q5, pulse_width)

    elif E_q5 < 0:
        if (360 + E_q5) <= abs(E_q5):
            E_q5 = abs(360 + E_q5)
            GPIO.output(MOTOR_A_PIN_q5, GPIO.HIGH)
            GPIO.output(MOTOR_B_PIN_q5, GPIO.LOW)
        else:
            GPIO.output(MOTOR_A_PIN_q5, GPIO.LOW)
            GPIO.output(MOTOR_B_PIN_q5, GPIO.HIGH)
            E_q5 = abs(E_q5)

        Mk = Mk1_q5 + BC1_q56 * E_q5 + BC2_q56 * E1_q5 + BC3_q56 * E2_q5
        if Mk > limit_Mk:
            Mk = limit_Mk
        if Mk < 0:
            Mk = 0
        pulse_width = map(Mk, 0, limit_Mk, 40, 255)
        GPIO.output(PWM_q5, pulse_width)

    else:
        Mk = 0
        GPIO.output(MOTOR_A_PIN_q5, GPIO.LOW)
        GPIO.output(MOTOR_B_PIN_q5, GPIO.LOW)
        pulse_width = map(Mk, 0, limit_Mk, 40, 255)
        GPIO.output(PWM_q5, pulse_width)

    Mk1_q5 = Mk
    E2_q5 = E1_q5
    E1_q5 = E_q5


def PID_q6():
    global E_q6, Mk, Mk1_q6, E1_q6, E2_q6

    # Verificar el error entre la referencia y valor actual de ángulo
    # Si es positivo, girar en sentido horario; si es negativo, girar en sentido anti-horario
    # Se realiza la manipulación por el controlador PID
    if E_q6 > 0:
        if (360 - E_q6) <= E_q6:
            E_q6 = 360 - E_q6
            GPIO.output(MOTOR_A_PIN_q6, GPIO.HIGH)
            GPIO.output(MOTOR_B_PIN_q6, GPIO.LOW)
        else:
            GPIO.output(MOTOR_A_PIN_q6, GPIO.LOW)
            GPIO.output(MOTOR_B_PIN_q6, GPIO.HIGH)

        Mk = Mk1_q6 + BC1_q56 * E_q6 + BC2_q56 * E1_q6 + BC3_q56 * E2_q6
        if Mk > limit_Mk:
            Mk = limit_Mk
        if Mk < 0:
            Mk = 0
        pulse_width = map(Mk, 0, limit_Mk, 40, 255)
        GPIO.output(PWM_q6, pulse_width)

    elif E_q6 < 0:
        if (360 + E_q6) <= abs(E_q6):
            E_q6 = abs(360 + E_q6)
            GPIO.output(MOTOR_A_PIN_q6, GPIO.LOW)
            GPIO.output(MOTOR_B_PIN_q6, GPIO.HIGH)
        else:
            GPIO.output(MOTOR_A_PIN_q6, GPIO.HIGH)
            GPIO.output(MOTOR_B_PIN_q6, GPIO.LOW)
            E_q6 = abs(E_q6)

        Mk = Mk1_q6 + BC1_q56 * E_q6 + BC2_q56 * E1_q6 + BC3_q56 * E2_q6
        if Mk > limit_Mk:
            Mk = limit_Mk
        if Mk < 0:
            Mk = 0
        pulse_width = map(Mk, 0, limit_Mk, 40, 255)
        GPIO.output(PWM_q6, pulse_width)

    else:
        Mk = 0
        GPIO.output(MOTOR_A_PIN_q6, GPIO.LOW)
        GPIO.output(MOTOR_B_PIN_q6, GPIO.LOW)
        pulse_width = map(Mk, 0, limit_Mk, 40, 255)
        GPIO.output(PWM_q6, pulse_width)

    Mk1_q6 = Mk
    E2_q6 = E1_q6
    E1_q6 = E_q6

while True:
    q4 = 90
    
    q4_en = 1
    
    if ( time.time() * 1000 - tiempoAnterior)>(T*1000):
        if q4_en == 1:
            E_q4 = q4 - posicion_q4
            PID_q4()
            
    tiempoAnterior = time.time()*1000
