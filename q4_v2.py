import lgpio
import time


PWM_q4 = 27
PWM_on = 0
PWM_off = 0

pulse_width = 0
ppr_grande = 5986
ppr_chico = 2441

A_q4 = 23
B_q4 = 18

MOTOR_A_PIN_q4 = 16 
MOTOR_B_PIN_q4 = 12 

val1 = 0
val2 = 0
val3 = 0
val4 = 0
val5 = 0
val6 = 0

pulsos_q4 = 0

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

Kc_g = 23.4
Taui_g = 0.032
Taud_g = 0.008

E_q1, E_q2, E_q3, E_q4, E_q5, E_q6 = 0, 0, 0, 0, 0, 0
Mk = 0
Mk1_q4, E1_q4, E2_q4 = 0, 0, 0
limit_Mk = 100
posicion_q4 = 0
BC1_q4, BC2_q4, BC3_q4 = 0, 0, 0
BC1_g, BC2_g, BC3_g = 0, 0, 0

tiempoAnterior = 0

# Configuración de los pines GPIO
lg = lgpio.gpiochip_open(0)
lgpio.gpio_claim_input(lg, A_q4)
lgpio.gpio_claim_input(lg, B_q4)
lgpio.gpio_claim_output(lg, MOTOR_A_PIN_q4)
lgpio.gpio_claim_output(lg, MOTOR_B_PIN_q4)
lgpio.gpio_claim_output(lg, PWM_q4)

GPIO.setup(PWM_q4, GPIO.OUT)  # Pin del PWM_q4


BC1_q4 = Kc_q4 * (1 + (T / Taui_q4) + (Taud_q4 / T))
BC2_q4 = Kc_q4 * (-1 - (2 * Taud_q4 / T))
BC3_q4 = Kc_q4 * Taud_q4 / T

BC1_g = Kc_g * (1 + (T / Taui_g) + (Taud_g / T))
BC2_g = Kc_g * (-1 - (2 * Taud_g / T))
BC3_g = Kc_g * Taud_g / T


def contar_q4(gpio, level, tick):
    print("contar")
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
    posicion_q4 = int((pulsos_q4 - 0) * (360 - 0) / (ppr_chico-0) + 0)
   
cb1= lgpio.callback(lg, A_q4, lgpio.EITHER_EDGE, contar_q4)
cb2= lgpio.callback(lg, B_q4, lgpio.EITHER_EDGE, contar_q4)
PWM_FREC = 1000
PWM_RANGE = 100

pwm = lgpio_open(lg, PWM_PIN, PWM_FREQ)
lgpio.pwm_set_range(pwm, PWM_RANGE)

def PID_q4():
    global E_q4, Mk, Mk1_q4, E1_q4, E2_q4

    # Verificar el error entre la referencia y valor actual de ángulo
    # Si es positivo, girar en sentido horario; si es negativo, girar en sentido anti-horario
    # Se realiza la manipulación por el controlador PID
    if E_q4 > 0:
        if (360 - E_q4) <= E_q4:
            E_q4 = 360 - E_q4
            
            lgpio.gpio_write(lg, MOTOR_A_PIN_q4, 1)
            lgpio.gpio_write(lg, MOTOR_B_PIN_q4, 0)
            
        else:
        
            lgpio.gpio_write(lg, MOTOR_A_PIN_q4, 0)
            lgpio.gpio_write(lg, MOTOR_B_PIN_q4, 1)
            Mk = Mk1_q4 + BC1_q4 * E_q4 + BC2_q4 * E1_q4 + BC3_q4 * E2_q4
        if Mk > limit_Mk:
            Mk = limit_Mk
        if Mk < 0:
            Mk = 0
        pulse_width = int((Mk-0)*(255-40)/(limit_Mk - 0) + 40)
        lgpio.tx_pwm(lg,PWM_q4, PWM_FREC, pulse_width)
        
        
    elif E_q4 < 0:
        if (360 + E_q4) <= abs(E_q4):
            E_q4 = abs(360 + E_q4)
            lgpio.gpio_write(lg, MOTOR_A_PIN_q4, 0)
            lgpio.gpio_write(lg, MOTOR_B_PIN_q4, 1)
        else:
            lgpio.gpio_write(lg, MOTOR_A_PIN_q4, 1)
            lgpio.gpio_write(lg, MOTOR_B_PIN_q4, 0)
            E_q4 = abs(E_q4)

        Mk = Mk1_q4 + BC1_q4 * E_q4 + BC2_q4 * E1_q4 + BC3_q4 * E2_q4
        if Mk > limit_Mk:
            Mk = limit_Mk
        if Mk < 0:
            Mk = 0
        pulse_width = int((Mk-0)*(255-40)/(limit_Mk - 0) + 40)        
        lgpio.tx_pwm(lg,PWM_q4, PWM_FREC, pulse_width)

    else:
        Mk = 0
        lgpio.gpio_write(lg, MOTOR_A_PIN_q4, 0)
        lgpio.gpio_write(lg, MOTOR_B_PIN_q4, 0)
        pulse_width = int((Mk-0)*(255-40)/(limit_Mk - 0) + 40)
        lgpio.tx_pwm(lg,PWM_q4, PWM_FREC, pulse_width)


    Mk1_q4 = Mk
    E2_q4 = E1_q4
    E1_q4 = E_q4

while True:
    q4 = 30
    
    q4_en = 1
    
    if ( time.time() * 1000 - tiempoAnterior)>(T*1000):
        if q4_en == 1:
            E_q4 = q4 - posicion_q4
            PID_q4()
            print("llamo pid")
    tiempoAnterior = time.time()*1000
