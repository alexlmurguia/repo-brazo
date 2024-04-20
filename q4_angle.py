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
        self.last_a_state = None
        self.last_b_state = None

        self.pi.set_mode(gpioA, pigpio.INPUT)
        self.pi.set_mode(gpioB, pigpio.INPUT)
        self.pi.set_pull_up_down(gpioA, pigpio.PUD_UP)
        self.pi.set_pull_up_down(gpioB, pigpio.PUD_UP)

        self.cbA = self.pi.callback(gpioA, pigpio.EITHER_EDGE, self._pulse)
        self.cbB = self.pi.callback(gpioB, pigpio.EITHER_EDGE, self._pulse)

    def _pulse(self, gpio, level, tick):
        if self.last_a_state is None or self.last_b_state is None:
            # Initialize the states if not already done
            self.last_a_state = self.pi.read(self.gpioA)
            self.last_b_state = self.pi.read(self.gpioB)
            return

        a_state = self.pi.read(self.gpioA)
        b_state = self.pi.read(self.gpioB)

        if gpio == self.gpioA:
            if (a_state != self.last_a_state) and (a_state == b_state):
                self.pulsos_q4 += 1 if a_state == 1 else -1
            elif (a_state != self.last_a_state) and (a_state != b_state):
                self.pulsos_q4 -= 1 if a_state == 1 else 1
        elif gpio == self.gpioB:
            if (b_state != self.last_b_state) and (a_state != b_state):
                self.pulsos_q4 += 1 if b_state == 1 else -1
            elif (b_state != self.last_b_state) and (a_state == b_state):
                self.pulsos_q4 -= 1 if b_state == 1 else 1

        self.last_a_state = a_state
        self.last_b_state = b_state

    def get_position(self):
        # Suponiendo un encoder con 2441 pulsos por revolución
        ppr = 2441
        angle = (self.pulsos_q4 / ppr) * 360.0
        return angle % 360

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
    pi.set_PWM_dutycycle(PWM_q4, 100)  # Duty cycle

    start_time = time.time()
    while time.time() - start_time < duration:
        print(f'Current angle: {decoder.get_position()} degrees')
        time.sleep(0.1)  # Print every 100ms

    # Stop the motor
    pi.set_PWM_dutycycle(PWM_q4, 0)

if __name__ == "__main__":
    try:
        decoder = decoder_class(pi, A_q4, B_q4)

        # Move motor forward for 3 seconds and print angles
        move_motor('forward', 3)
        forward_angle = decoder.get_position()
        print(f'Angle after moving forward: {forward_angle} degrees')

        # Reset pulses count
        decoder.reset_pulses()

        # Move motor backward for 3 seconds and print angles
        move_motor('backward', 3)
        backward_angle = decoder.get_position()
        print(f'Angle after moving backward: {backward_angle} degrees')

    finally:
        decoder.cancel()
        pi.stop()
