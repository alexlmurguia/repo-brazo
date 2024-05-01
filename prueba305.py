import cv2, imutils, socket, serial
import numpy as np
import time, base64
from multiprocessing import Process

def process_commands(server_ip, command_port, arduino_mov_port, arduino_mov_baud_rate):
    arduino_mov_serial = serial.Serial(arduino_mov_port, arduino_mov_baud_rate, timeout=1)
    command_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    command_socket.bind((server_ip, command_port))
    print('Command server is up and listening...')
    
    while True:
        message, address = command_socket.recvfrom(1024)
        message = message.decode('utf-8')
        print('Message received:', message)
        print('Client address:', address[0])
        
        button_pressed_value, buttonmodalidadbrazo_pressed_value, buttongripper_pressed_value, velocidad, angulo, q1, q2, q3, q4, q5, q6, mastil, buttoncamera_pressed_value = message.split(',') 
        print(button_pressed_value)
        if button_pressed_value=="1":
            #arduino_mov_serial.write(f"{velocidad},{angulo}\n".encode('utf-8'))
            print('Message received:',f"{velocidad},{angulo}\n" )
            response_msg = "Updated successfully"
            command_socket.sendto(response_msg.encode('utf-8'), address)
        if button_pressed_value=="2":
            if buttonmodalidadbrazo_pressed_value=="1":
                #arduino_brazo_serial.write(f"{buttonmodalidadbrazo_pressed_value},{q1},{q2},{q3},{q4},{q5},{q6}\n".encode('utf-8'))
                print('Message received:',f"{buttonmodalidadbrazo_pressed_value},{q1},{q2},{q3},{q4},{q5},{q6}\n")
                response_msg = "Updated successfully"
                command_socket.sendto(response_msg.encode('utf-8'), address)
            if buttonmodalidadbrazo_pressed_value=="2":
            #FALTA AGREGAR LA LIBRERIA DE CINEMATICA INVERSA
            #YA MANDA COO SI FUERA DIRECTA
                #arduino_brazo_serial.write(f"{buttonmodalidadbrazo_pressed_value},{q1},{q2},{q3},{q4},{q5},{q6}\n".encode('utf-8'))
                response_msg = "Updated successfully"
                command_socket.sendto(response_msg.encode('utf-8'), address)
            if buttonmodalidadbrazo_pressed_value=="3":
                #arduino_brazo_serial.write(f"{buttonmodalidadbrazo_pressed_value},{buttongripper_pressed_value}\n".encode('utf-8'))
                print('Message received:',f"{buttonmodalidadbrazo_pressed_value},{buttongripper_pressed_value}\n")
                response_msg = "Updated successfully"
                command_socket.sendto(response_msg.encode('utf-8'), address)
        if button_pressed_value=="3":
            #arduino_mov_serial.write(f"{mastil}\n".encode('utf-8'))
            response_msg = "Updated successfully"
            print('Message received:',f"{mastil}\n")
            command_socket.sendto(response_msg.encode('utf-8'), address)
        if button_pressed_value=="4":
            if buttoncamera_pressed_value=="1":
                print('Message received:',f"{buttoncamera_pressed_value}\n")
                send_video(server_ip,video_port)
            if buttoncamera_pressed_value=="2":
                print('Message received:',f"{buttoncamera_pressed_value}\n")
                

def send_video(host_ip, port):
    video_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 65536)
    video_socket.bind((host_ip, port))
    print('Video server listening at:', host_ip, port)
    if button_pressed_value=="4":
        if buttoncamera_pressed_value=="1":
            print('Message received:',f"{buttoncamera_pressed_value}\n")
            vid = cv2.VideoCapture(0)
        if buttoncamera_pressed_value=="2":
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
                    if buttoncamera_pressed_value=="2":
                        print('Message received:',f"{buttoncamera_pressed_value}\n")
                        video_socket.close()
                        vid.release()
                        cv2.destroyAllWindows()
                        break

if __name__ == '__main__':
    server_ip = '192.168.0.100'
    command_port = 2222
    video_port = 9999
    arduino_mov_port = '/dev/ttyACM0'
    arduino_mov_baud_rate = 9600
    buttoncamera_pressed_value=0
    

    # Crear y empezar los procesos
    process1 = Process(target=process_commands, args=(server_ip, command_port, arduino_mov_port, arduino_mov_baud_rate))
    process2 = Process(target=send_video, args=('0.0.0.0', video_port))
    process1.start()
    process2.start()

    process1.join()
    process2.join()
