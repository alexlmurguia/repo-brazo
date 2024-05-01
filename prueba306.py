import cv2
import imutils
import socket
import serial
import numpy as np
import base64
from multiprocessing import Process, Value
import signal
import sys
import funciones as f  


def process_commands(server_ip, command_port, arduino_mov_port, arduino_mov_baud_rate, running):
    try:
        arduino_mov_serial = serial.Serial(arduino_mov_port, arduino_mov_baud_rate, timeout=1)
        command_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        command_socket.bind((server_ip, command_port))
        print('Command server is up and listening...')
        
        while running.value:
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
                        ths = f.angulosInversa(q1, q2, q3, q4, q5, q6)
                        ths = [int(th) for th in ths]  # Ajusta ángulos
                        q1, q2, q3, q4, q5, q6 = ths
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
                
                response_msg = "Updated successfully"
                #command_socket.sendto(response_msg.encode('utf-8'), address)
            except Exception as e:
                print("Error processing command:", e)
    except Exception as e:
        print("Error setting up command server:", e)
    finally:
        command_socket.close()
        arduino_mov_serial.close()
        print("Command server and serial closed")

def send_video(host_ip, port, running):
    video_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    video_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 65536)
    video_socket.bind((host_ip, port))
    print('Video server listening at:', host_ip, port)
    vid = cv2.VideoCapture(0)
    
    try:
        while running.value:
            _, frame = vid.read()
            frame = imutils.resize(frame, width=400)
            encoded, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 80])
            message = base64.b64encode(buffer)
            video_socket.sendto(message, (host_ip, port))
            cv2.imshow('TRANSMITTING VIDEO', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    except Exception as e:
        print("Error sending video:", e)
    finally:
        video_socket.close()
        vid.release()
        cv2.destroyAllWindows()
        print("Video server closed")

def signal_handler(sig, frame, processes):
    print("Shutting down gracefully")
    for p in processes:
        p.terminate()
    sys.exit(0)

if __name__ == '__main__':
    server_ip = '192.168.0.100'
    command_port = 2222
    video_port = 9999
    arduino_mov_port = '/dev/ttyACM0'
    arduino_mov_baud_rate = 9600
    running = Value('i', 1)

    # Handle signals
    signal.signal(signal.SIGINT, lambda sig, frame: signal_handler(sig, frame, [process1, process2]))

    # Start processes
    process1 = Process(target=process_commands, args=(server_ip, command_port, arduino_mov_port, arduino_mov_baud_rate, running))
    process2 = Process(target=send_video, args=('0.0.0.0', video_port, running))
    process1.start()
    process2.start()

    process1.join()
    process2.join()
