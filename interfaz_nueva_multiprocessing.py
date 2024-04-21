import cv2, imutils, socket
import numpy as np
import time
import base64
import tkinter as tk
from multiprocessing import Process, Queue

# Función para enviar datos a través de UDP
def send_data(data_socket, serverAddress, queue):
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

    # Enviar datos al servidor
    data_socket.sendto(message, serverAddress)

    # Enviar mensaje para iniciar/reiniciar la transmisión de video
    queue.put('start')

# Función para recibir y mostrar video
def receive_video(queue):
    global fps, st, frames_to_count, cnt

    while True:
        start_message = queue.get()  # Esperar a recibir 'start' desde la cola
        if start_message == 'start':
            video_socket.sendto(b'start', (host_ip, video_port))
            while True:
                packet, _ = video_socket.recvfrom(BUFF_SIZE)
                data = base64.b64decode(packet)
                npdata = np.frombuffer(data, dtype=np.uint8)
                frame = cv2.imdecode(npdata, cv2.IMREAD_COLOR)
                frame = cv2.putText(frame, 'FPS: '+str(fps), (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                cv2.imshow("RECEIVING VIDEO", frame)
                key = cv2.waitKey(1) & 0xFF
                if key == ord('q'):
                    video_socket.close()
                    break
                if cnt == frames_to_count:
                    try:
                        fps = round(frames_to_count / (time.time() - st))
                        st = time.time()
                        cnt = 0
                    except:
                        pass
                cnt += 1

# Parámetros del socket de video
BUFF_SIZE = 65536
video_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
video_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, BUFF_SIZE)
host_ip = '192.168.0.100'  # IP del servidor de video
video_port = 9999
fps, st, frames_to_count, cnt = (0, 0, 20, 0)

# Configuración del socket de datos

#video_socket.bind((host_ip, video_port))


# Configuración de la interfaz gráfica y proceso de video
if __name__ == '__main__':

    serverAddress = ('192.168.0.100', 2222)
    data_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    root = tk.Tk()
    root.title("Control Interface")

    labels = ['Velocidad (0-255):', 'Ángulo (0-700):', 'q1:', 'q2:', 'q3:', 'q4:', 'q5:', 'q6:']
    entries = []
    for i, text in enumerate(labels):
        row = i // 2
        col = (i % 2) * 2
        tk.Label(root, text=text).grid(row=row, column=col)
        entry = tk.Entry(root)
        entry.grid(row=row, column=col+1)
        entries.append(entry)

    velocidad_entry, angulo_entry, q1_entry, q2_entry, q3_entry, q4_entry, q5_entry, q6_entry = entries

    queue = Queue()
    video_process = Process(target=receive_video, args=(queue,))
    video_process.start()

    submit_button = tk.Button(root, text="Enviar y recibir video", command=lambda: send_data(data_socket, serverAddress, queue))
    submit_button.grid(row=5, column=0, columnspan=4)

    root.mainloop()
    video_process.terminate()  # Asegurarse de terminar el proceso al cerrar la interfaz gráfica
