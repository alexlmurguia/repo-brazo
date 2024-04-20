#!/usr/bin/env python

import pigpio
import time

# Definición de pines usando la numeración BCM
PWM_q4 = 6
A_q4 = 10
B_q4 = 9
MOTOR_A_PIN_q4 = 20
MOTOR_B_PIN_q4 = 21

# Inicializar la librería pigpio
pi = pigpio.pi()

class decoder_class:
    def __init__(self, pi, gpioA, gpioB, callback):
        self.pi = pi
        self.gpioA = gpioA
        self.gpioB = gpioB
        self.callback = callback
        self.levA = 0
        self.levB = 0
        self.lastGpio = None

        self.pi.set_mode(gpioA, pigpio.INPUT)
        self.pi.set_mode(gpioB, pigpio.INPUT)
        self.pi.set_pull_up_down(gpioA, pigpio.PUD_UP)
        self.pi.set_pull_up_down(gpioB, pigpio.PUD_UP)

        self.cbA = self.pi.callback(gpioA, pigpio.EITHER_EDGE, self._pulse)
        self.cbB = self.pi.callback(gpioB, pigpio.EITHER_EDGE, self._pulse)

    def _pulse(self, gpio, level, tick):
        if gpio == self.gpioA:
            self.levA = level
        else:
            self.levB = level

        if gpio != self.lastGpio: # debounce
            self.lastGpio = gpio

            if gpio == self.gpioA and level == 1:
                if self.levB == 1:
                    self.callback(1)
            elif gpio == self.gpioB and level == 1:
                if self.levA == 1:
                    self.callback(-1)

    def cancel(self):
        self.cbA.cancel()
        self.cbB.cancel()

def callback(way):
    global pos
    pos += way
    print(f"Current angle change: {way}, New position: {pos}")

def move_motor(direction, duration):
    if direction == 'forward':
        pi.write(MOTOR_A_PIN_q4, 1)
        pi.write(MOTOR_B_PIN_q4, 0)
    elif direction == 'backward':
        pi.write(MOTOR_A_PIN_q4, 0)
        pi.write(MOTOR_B_PIN_q4, 1)

    pi.set_PWM_dutycycle(PWM_q4, 128)  # 50% Duty cycle

    start_time = time.time()
    while time.time() - start_time < duration:
        time.sleep(0.1)  # Print every 100ms

    pi.set_PWM_dutycycle(PWM_q4, 0)

if __name__ == "__main__":
    try:
        pos = 0
        decoder = decoder_class(pi, A_q4, B_q4, callback)

        # Move motor forward for 5 seconds
        move_motor('forward', 5)

        # Move motor backward for 5 seconds
        move_motor('backward', 5)

    finally:
        decoder.cancel()
        pi.stop()
