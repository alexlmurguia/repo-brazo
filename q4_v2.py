import lgpio
import time

# Constants for GPIO pins
PWM_q4 = 27
A_q4 = 23
B_q4 = 18
MOTOR_A_PIN_q4 = 16
MOTOR_B_PIN_q4 = 12

# Encoder resolution
ppr_chico = 2441

# PID control parameters
Kc_q4 = 2
Taui_q4 = 0.012
Taud_q4 = 0.4
T = 0.01
limit_Mk = 100
pulse_range = 100

# GPIO setup using lgpio
lg = lgpio.gpiochip_open(0)
lgpio.gpio_claim_input(lg, A_q4)
lgpio.gpio_claim_input(lg, B_q4)
lgpio.gpio_claim_output(lg, MOTOR_A_PIN_q4)
lgpio.gpio_claim_output(lg, MOTOR_B_PIN_q4)
lgpio.gpio_claim_output(lg, PWM_q4)

# PWM setup
pwm_handle = lgpio.pwm_open(lg, PWM_q4, 1000)  # Assuming 1000 Hz PWM frequency
lgpio.pwm_set_range(lg, pwm_handle, pulse_range)

# PID control variables
pulsos_q4 = 0
posicion_q4 = 0
Mk1_q4 = 0
E1_q4 = 0
E2_q4 = 0

def contar_q4(gpio, level, tick):
    global pulsos_q4, posicion_q4
    if lgpio.gpio_read(lg, B_q4):
        pulsos_q4 -= 1
    else:
        pulsos_q4 += 1

    pulsos_q4 %= ppr_chico  # Wrap around the pulse count

    posicion_q4 = (pulsos_q4 * 360) // ppr_chico  # Convert pulses to angle

# Callbacks for encoder edges
cb1 = lgpio.callback(lg, A_q4, lgpio.EITHER_EDGE, contar_q4)
cb2 = lgpio.callback(lg, B_q4, lgpio.EITHER_EDGE, contar_q4)

def PID_q4():
    global E_q4, Mk, Mk1_q4, E1_q4, E2_q4
    E_q4 = q4 - posicion_q4  # Calculate error
    Mk = Mk1_q4 + Kc_q4 * (E_q4 + (E1_q4 - E2_q4) * Taud_q4 / T + E1_q4 * T / Taui_q4)
    Mk = max(0, min(Mk, limit_Mk))  # Constrain Mk within 0 to limit_Mk

    pulse_width = int((Mk - 0) * (255 - 40) / (limit_Mk - 0) + 40)
    lgpio.pwm_set_dutycycle(lg, pwm_handle, pulse_width)

    Mk1_q4 = Mk
    E2_q4 = E1_q4
    E1_q4 = E_q4

# Main control loop
last_time = time.time()
while True:
    q4 = 30  # Target angle
    
    if (time.time() - last_time) > T:
        PID_q4()
        print("PID updated")
        last_time = time.time()
