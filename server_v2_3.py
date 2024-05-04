import cv2, imutils, socket, serial
import numpy as np
import time, base64
from multiprocessing import Process

def process_commands(server_ip, command_port, arduino_mov_port, arduino_mov_baud_rate,arduino_brazo_port, arduino_brazo_baud_rate, rasp_mastil_port, rasp_mastil_baud_rate):
    try:
        
        command_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        command_socket.bind((server_ip, command_port))
        print('Command server is up and listening...')
        while True:
            try:
                message, address = command_socket.recvfrom(1024)
                if not message:
                    continue
                message = message.decode('utf-8')
                print('Message received:', message)
                print('Client address:', address[0])
                
                # Aquí iría el procesamiento de tu mensaje
                # Por simplicidad omito la lógica detallada
                button_pressed_value, buttonmodalidadbrazo_pressed_value, buttongripper_pressed_value, velocidad, angulo, q1, q2, q3, q4, q5, q6, mastil, buttoncamera_pressed_value = message.split(',') 
                print(button_pressed_value)
                if button_pressed_value=="1":
                    send_command_mov_to_arduino(velocidad, angulo)
                    print('Message received:',f"{velocidad},{angulo}\n" )
                    response_msg = "Updated successfully"
                    command_socket.sendto(response_msg.encode('utf-8'), address)
                if button_pressed_value=="2":
                    if buttonmodalidadbrazo_pressed_value=="1":
                        send_command_brazo_to_arduino(buttonmodalidadbrazo_pressed_value,q1,q2,q3,q4,q5,q6)
                        print('Message received:',f"{buttonmodalidadbrazo_pressed_value},{q1},{q2},{q3},{q4},{q5},{q6}\n")
                        response_msg = "Updated successfully"
                        command_socket.sendto(response_msg.encode('utf-8'), address)
                    if buttonmodalidadbrazo_pressed_value=="2":
                    #FALTA AGREGAR LA LIBRERIA DE CINEMATICA INVERSA
                    #YA MANDA COO SI FUERA DIRECTA
                        send_command_brazo_to_arduino(buttonmodalidadbrazo_pressed_value==1,q1,q2,q3,q4,q5,q6)
                        response_msg = "Updated successfully"
                        command_socket.sendto(response_msg.encode('utf-8'), address)
                    if buttonmodalidadbrazo_pressed_value=="3":
                        send_command_brazo_to_arduino(buttonmodalidadbrazo_pressed_value==1,q1,q2,q3,q4,q5,q6)
                        print('Message received:',f"{buttonmodalidadbrazo_pressed_value},{buttongripper_pressed_value}\n")
                        response_msg = "Updated successfully"
                        command_socket.sendto(response_msg.encode('utf-8'), address)
                if button_pressed_value=="3":
                    send_command_mastil_to_rasp(mastil)
                    print('Message received:',f"{mastil}\n")
                    command_socket.sendto(response_msg.encode('utf-8'), address)
                if button_pressed_value=="4":
                    if buttoncamera_pressed_value=="1":
                        print('Message received:',f"{buttoncamera_pressed_value}\n")
                        #running.value = 2
                        #send_video(server_ip,video_port)
                    if buttoncamera_pressed_value=="2":
                        print('Message received:',f"{buttoncamera_pressed_value}\n")
                        #running.value = 1

                response_msg = "Updated successfully"
                #command_socket.sendto(response_msg.encode('utf-8'), address)  
            except:
                pass 
    except Exception as e:
        print("Error setting up command server:", e)
    finally:
        command_socket.close()
        arduino_mov_serial.close()
        print("Command server and serial closed")

def send_video(host_ip, port):
    video_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    video_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 65536)
    video_socket.bind((host_ip, port))
    print('Video server listening at:', host_ip, port)
    
    vid = cv2.VideoCapture(0)
    if not vid.isOpened():
        print("Error: Cannot open camera")
        return

    while True:
        msg, client_addr = video_socket.recvfrom(65536)
        print('GOT connection from ', client_addr)
        while vid.isOpened():
            _, frame = vid.read()
            frame = imutils.resize(frame, width=400)
            encoded, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 80])
            message = base64.b64encode(buffer)
            video_socket.sendto(message, client_addr)
            cv2.imshow('TRANSMITTING VIDEO', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                video_socket.close()
                vid.release()
                cv2.destroyAllWindows()
                break

def send_command_mov_to_arduino(velocidad, angulo):
    command = f"{velocidad},{angulo}"
    print('Message to send:', command)
    arduino_mov_serial.write(command.encode('utf-8'))
    time.sleep(0.1)
    response = arduino_mov_serial.readline().decode('utf-8', errors='replace').strip()

def send_command_brazo_to_arduino(buttonmodalidadbrazo_pressed_value,q1,q2,q3,q4,q5,q6):
    command = f"{buttonmodalidadbrazo_pressed_value},{q1},{q2},{q3},{q4},{q5},{q6}"
    print('Message to send:', command)
    arduino_brazo_serial.write(command.encode('utf-8'))
    time.sleep(0.1)
    response = arduino_brazo_serial.readline().decode('utf-8', errors='replace').strip()
    
# Función para enviar comandos al Raspberry Pi Pico
def send_command_mastil_to_rasp(mastil):
    try:
        with serial.Serial('/dev/rasp_mastil', 115200, timeout=1) as rasp_mastil_serial:  # Asegúrate de que el dispositivo es correcto
            command = f"{mastil}\n"
            rasp_mastil_serial.write(command.encode('utf-8'))
            print('Mastil command sent:', command)
    except Exception as e:
        print(f"Error sending mastil command: {e}")

if __name__ == '__main__':
    server_ip = '192.168.0.100'
    command_port = 2222
    video_port = 9999
    arduino_mov_port = '/dev/arduino_mov'
    arduino_brazo_port = '/dev/arduino_brazo'
    arduino_mov_baud_rate = 9600
    arduino_brazo_baud_rate = 115200
    arduino_mov_serial = serial.Serial(arduino_mov_port, arduino_mov_baud_rate, timeout=1)
    arduino_brazo_serial = serial.Serial(arduino_brazo_port, arduino_brazo_baud_rate, timeout=1)
    rasp_mastil_port = '/dev/rasp_mastil'
    rasp_mastil_baud_rate = 115200
    rasp_mastil_serial = serial.Serial(rasp_mastil_port, rasp_mastil_baud_rate, timeout=1)

    # Crear y empezar los procesos
    process1 = Process(target=process_commands, args=(server_ip, command_port, arduino_mov_port, arduino_mov_baud_rate, arduino_brazo_port, arduino_brazo_baud_rate, rasp_mastil_port, rasp_mastil_baud_rate))
    process2 = Process(target=send_video, args=('0.0.0.0', video_port))
    process1.start()
    process2.start()

    process1.join()
    process2.join()
