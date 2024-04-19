import lgpio
import time

# Constants for GPIO pins
PWM_q4 = 27
A_q4 = 23
B_q4 = 18
MOTOR_A_PIN_q4 = 16
MOTOR_B_PIN_q4 = 12

# Encoder resolution and motor control parameters
ppr_chico = 2441
PWM_FREQ = 1000  # 1000 Hz PWM frequency
PWM_DUTY_CYCLE = 50  # Duty cycle percentage

# GPIO setup using lgpio
lg = lgpio.gpiochip_open(0)
lgpio.gpio_claim_output(lg, PWM_q4)
lgpio.gpio_claim_input(lg, A_q4)
lgpio.gpio_claim_input(lg, B_q4)
lgpio.gpio_claim_output(lg, MOTOR_A_PIN_q4)
lgpio.gpio_claim_output(lg, MOTOR_B_PIN_q4)

# Function to start PWM on a pin
def start_pwm(pin, frequency, duty_cycle_percentage):
    # Convert duty cycle percentage to duty cycle units
    duty_cycle_units = int((duty_cycle_percentage / 100.0) * (1 << 16))  # Duty cycle as a fraction of (2^16 - 1)
    lgpio.tx_pwm(lg, pin, frequency, duty_cycle_units)

# Function to stop PWM
def stop_pwm(pin):
    lgpio.tx_pwm(lg, pin, 0, 0)

try:
    # Start PWM
    start_pwm(PWM_q4, PWM_FREQ, PWM_DUTY_CYCLE)
    time.sleep(10)  # Run PWM for 10 seconds
finally:
    # Stop PWM and clean up
    stop_pwm(PWM_q4)
    lgpio.gpiochip_close(lg)
