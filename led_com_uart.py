# sender.py
import time
import serial

ser = serial.Serial(
    port='/dev/ttyS0',  # Cambia esto según tus métodos de conexión, e.g., /dev/ttyUSB0
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

i = 0
while True:
    i += 1
    # Encender el LED cada 4 ciclos
    if i % 4 == 0:
        ser.write('OFF\n'.encode('utf-8'))  # Enviar comando para apagar el LED
        print("Counter {} - LED OFF".format(i))
    else:
        ser.write('ON\n'.encode('utf-8'))  # Enviar comando para encender el LED
        print("Counter {} - LED ON".format(i))
    time.sleep(2)
