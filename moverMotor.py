import RPi.GPIO as GPIO
import time
import threading

IN1= 23
IN2 = 18
ENA = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(ENA, GPIO.OUT)

pwm=GPIO.PWM(ENA,100)

pwm.start(0)

while(1):
	
	GPIO.output(IN1,GPIO.HIGH)
	GPIO.output(IN2,GPIO.LOW)
	pwm.ChangeDutyCycle(90)
	time.sleep(4)
	
	GPIO.output(IN1,GPIO.LOW)
	GPIO.output(IN2,GPIO.HIGH)
	pwm.ChangeDutyCycle(10)
	time.sleep(4)
	
	pwm.ChangeDutyCycle(0)
	time.sleep(3)
	

