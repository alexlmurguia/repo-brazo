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
    def __init__(self, pi, gpioA, gpioB):
        self.pi = pi
        self.gpioA = gpioA
        self.gpioB = gpioB
        self.pulsos_q4 = 0

        self.pi.set_mode(gpioA, pigpio.INPUT)
        self.pi.set_mode(gpioB, pigpio.INPUT)
        self.pi.set_pull_up_down(gpioA, pigpio.PUD_UP)
        self.pi.set_pull_up_down(gpioB, pigpio.PUD_UP)

        self.cbA = self.pi.callback(gpioA, pigpio.EITHER_EDGE, self._pulse)
        self.cbB = self.pi.callback(gpioB, pigpio.EITHER_EDGE, self._pulse)

    """
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
    """

    def _pulse(self, gpio, level, tick):
        if gpio == self.gpioA:
            a_state = level
            b_state = self.pi.read(self.gpioB)
        else:  # gpio == self.gpioB
            b_state = level
            a_state = self.pi.read(self.gpioA)

        if (gpio == self.gpioA and a_state != b_state) or (gpio == self.gpioB and a_state == b_state):
            self.pulsos_q4 += 1
        else:
            self.pulsos_q4 -= 1

    def get_pulses(self):
        return self.pulsos_q4

    def reset_pulses(self):
        self.pulsos_q4 = 0

    def cancel(self):
        self.cbA.cancel()
        self.cbB.cancel()

def move_motor(direction, duration):
    # Set direction
    if direction == 'forward':
        pi.write(MOTOR_A_PIN_q4, 1)
        pi.write(MOTOR_B_PIN_q4, 0)
    elif direction == 'backward':
        pi.write(MOTOR_A_PIN_q4, 0)
        pi.write(MOTOR_B_PIN_q4, 1)

    # Set PWM duty cycle for speed
    pi.set_PWM_dutycycle(PWM_q4, 128)  # 50% Duty cycle

    start_time = time.time()
    while time.time() - start_time < duration:
        print(f'Current pulses: {decoder.get_pulses()}')
        time.sleep(0.1)  # Print every 100ms

    # Stop the motor
    pi.set_PWM_dutycycle(PWM_q4, 0)

if __name__ == "__main__":
    try:
        decoder = decoder_class(pi, A_q4, B_q4)

        # Move motor forward for 5 seconds and count pulses
        move_motor('forward', 5)
        forward_pulses = decoder.get_pulses()
        print(f'Pulses while moving forward: {forward_pulses}')

        # Reset pulses count
        decoder.reset_pulses()

        # Move motor backward for 5 seconds and count pulses
        move_motor('backward', 5)
        backward_pulses = decoder.get_pulses()
        print(f'Pulses while moving backward: {backward_pulses}')

    finally:
        decoder.cancel()
        pi.stop()
