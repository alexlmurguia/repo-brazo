import cv2
import numpy as np
import time
import base64
import socket
import tkinter as tk
from PIL import Image, ImageTk
from threading import Thread

# Parámetros del socket de video
BUFF_SIZE = 65536
video_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
video_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, BUFF_SIZE)
host_ip = '192.168.0.100'  # IP del servidor de video
video_port = 9999
fps, st, frames_to_count, cnt = (0, time.time(), 20, 0)

# Función para enviar datos a través de UDP
def send_data(data_socket, serverAddress):
    # Obtener valores de los controles
    velocidad = velocidad_entry.get()
    angulo = angulo_entry.get()
    q1 = q1_entry.get()
    q2 = q2_entry.get()
    q3 = q3_entry.get()
    q4 = q4_entry.get()
    q5 = q5_entry.get()
    q6 = q6_entry.get()

    message = f"{velocidad}, {angulo}, {q1}, {q2}, {q3}, {q4}, {q5}, {q6}"
    print("Sending:", message)
    message = message.encode('utf-8')
    data_socket.sendto(message, serverAddress)

    # Solicitar el inicio de la transmisión de vídeo
    video_socket.sendto(b'start', (host_ip, video_port))

# Función para recibir y mostrar video
def receive_video():
    global fps, st, frames_to_count, cnt
    while True:
        try:
            packet, _ = video_socket.recvfrom(BUFF_SIZE)
            data = base64.b64decode(packet)
            npdata = np.frombuffer(data, dtype=np.uint8)
            frame = cv2.imdecode(npdata, cv2.IMREAD_COLOR)
            if frame is not None:
                frame = cv2.putText(frame, 'FPS: '+str(fps), (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = Image.fromarray(frame)
                frame = ImageTk.PhotoImage(frame)
                video_label.config(image=frame)
                video_label.image = frame
                if cnt == frames_to_count:
                    fps = round(frames_to_count / (time.time() - st), 2)
                    st = time.time()
                    cnt = 0
                cnt += 1
            else:
                display_black_frame()
        except socket.timeout:
            display_black_frame()

# Función para mostrar un cuadro negro cuando no se recibe video
def display_black_frame():
    black_frame = np.zeros((480, 640, 3), dtype=np.uint8)
    black_frame = Image.fromarray(black_frame)
    black_frame = ImageTk.PhotoImage(black_frame)
    video_label.config(image=black_frame)
    video_label.image = black_frame

# Configuración de la ventana principal y controles de Tkinter
if __name__ == '__main__':
    serverAddress = ('192.168.0.100', 2222)
    data_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    root = tk.Tk()
    root.title("Control Interface")

    video_label = tk.Label(root)
    video_label.grid(row=0, column=0, columnspan=4)

    labels = ['Velocidad (0-255):', 'Ángulo (0-700):', 'q1:', 'q2:', 'q3:', 'q4:', 'q5:', 'q6:']
    entries = []
    for i, text in enumerate(labels):
        row = i // 2 + 1
        col = (i % 2) * 2
        tk.Label(root, text=text).grid(row=row, column=col)
        entry = tk.Entry(root)
        entry.grid(row=row, column=col + 1)
        entries.append(entry)

    velocidad_entry, angulo_entry, q1_entry, q2_entry, q3_entry, q4_entry, q5_entry, q6_entry = entries

    submit_button = tk.Button(root, text="Enviar y recibir video", command=lambda: send_data(data_socket, serverAddress))
    submit_button.grid(row=5, column=0, columnspan=4)

    video_thread = Thread(target=receive_video, daemon=True)
    video_thread.start()

    root.mainloop()
    video_socket.close()
