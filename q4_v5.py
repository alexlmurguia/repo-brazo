#!/usr/bin/env python

import pigpio
import time
import signal
import sys

# Definición de pines usando la numeración BCM
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

# Inicializar la librería pigpio
pi = pigpio.pi()

class decoder_class:
    def __init__(self, pi, gpioA, gpioB):
        self.pi = pi
        self.gpioA = gpioA
        self.gpioB = gpioB
        self.posicion_q4 = 0.0
        self.pulsos_q4 = 0

        self.pi.set_mode(gpioA, pigpio.INPUT)
        self.pi.set_mode(gpioB, pigpio.INPUT)
        self.pi.set_pull_up_down(gpioA, pigpio.PUD_UP)
        self.pi.set_pull_up_down(gpioB, pigpio.PUD_UP)

        self.cbA = self.pi.callback(gpioA, pigpio.FALLING_EDGE, self._pulse)
        self.cbB = self.pi.callback(gpioB, pigpio.FALLING_EDGE, self._pulse)

    def _pulse(self, gpio, level, tick):
        if gpio == self.gpioA:
            if level == 0:  # Check for falling edge
                if self.pi.read(self.gpioB):
                    self.pulsos_q4 -= 1
                else:
                    self.pulsos_q4 += 1
        elif gpio == self.gpioB:
            if level == 0:  # Check for falling edge
                if self.pi.read(self.gpioA):
                    self.pulsos_q4 += 1
                else:
                    self.pulsos_q4 -= 1

        self.pulsos_q4 %= ppr_chico  # Reset pulses at one full turn
        self.posicion_q4 = (self.pulsos_q4 / ppr_chico) * 360.0

    def get_position(self):
        return self.posicion_q4

    def cancel(self):
        self.cbA.cancel()
        self.cbB.cancel()

# Coeficientes del PID
BC1_q4 = Kc_q4 * (1 + (T / Taui_q4) + (Taud_q4 / T))
BC2_q4 = Kc_q4 * (-1 - (2 * Taud_q4 / T))
BC3_q4 = Kc_q4 * Taud_q4 / T

decoder = decoder_class(pi, A_q4, B_q4)

def PID_q4():
    global Mk1_q4, E1_q4, E2_q4, E_q4
    E_q4 = q4 - decoder.get_position()
    E_q4 = (E_q4 + 180) % 360 - 180  # Normalize error between -180 and 180

    Mk = Mk1_q4 + BC1_q4 * E_q4 + BC2_q4 * E1_q4 + BC3_q4 * E2_q4
    Mk = max(min(Mk, limit_Mk), 0)

    # Determine direction and apply PWM
    pulse_width = int((Mk / limit_Mk) * 255)
    pi.set_PWM_dutycycle(PWM_q4, pulse_width)
    if E_q4 > 0:
        pi.write(MOTOR_A_PIN_q4, 1)
        pi.write(MOTOR_B_PIN_q4, 0)
    else:
        pi.write(MOTOR_A_PIN_q4, 0)
        pi.write(MOTOR_B_PIN_q4, 1)

    # Update PID states
    Mk1_q4 = Mk
    E2_q4 = E1_q4
    E1_q4 = E_q4

# Manejo de señal para limpieza
def handle_signal(sig, frame):
    print("Stopping...")
    decoder.cancel()
    pi.set_PWM_dutycycle(PWM_q4, 0)
    pi.stop()
    sys.exit(0)

signal.signal(signal.SIGINT, handle_signal)

# Bucle principal
last_time = time.time()
while True:
    current_time = time.time()
    if current_time - last_time >= T:
        PID_q4()
        last_time = current_time
