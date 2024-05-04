import cv2, imutils, socket
import numpy as np
import time
import base64
import tkinter as tk
from multiprocessing import Process, Queue
from PIL import Image, ImageTk

# Global variable to track the button press
button_pressed_value= 0
buttonmodalidadbrazo_pressed_value= 0
buttongripper_pressed_value=0
buttoncamara_pressed_value=0

def send_data(data_socket, serverAddress, queue):    
    # Recoger los valores de entrada
    velocidad = velocidad_entry.get()
    angulo = angulo_entry.get()
    q1 = q1_entry.get()
    q2 = q2_entry.get()
    q3 = q3_entry.get()
    q4 = q4_entry.get()
    q5 = q5_entry.get()
    q6 = q6_entry.get()
    mastil = mastil_entry.get()

    # Construir el mensaje a enviar
    message = f"{button_pressed_value},{buttonmodalidadbrazo_pressed_value},{buttongripper_pressed_value},{velocidad}, {angulo}, {q1}, {q2}, {q3}, {q4}, {q5}, {q6},{mastil},{buttoncamara_pressed_value}"
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

def on_mov_button(data_socket, serverAddress, queue):
    global button_pressed_value
    button_pressed_value = 1
    send_data(data_socket, serverAddress, queue)  

def on_directa_button():
    global buttonmodalidadbrazo_pressed_value
    buttonmodalidadbrazo_pressed_value= 1

def on_inversa_button():
    global buttonmodalidadbrazo_pressed_value
    buttonmodalidadbrazo_pressed_value = 2

def on_abierto_button(data_socket, serverAddress, queue):
    global buttonmodalidadbrazo_pressed_value
    global buttongripper_pressed_value
    global button_pressed_value
    button_pressed_value = 2
    buttonmodalidadbrazo_pressed_value = 3
    buttongripper_pressed_value=1
    send_data(data_socket, serverAddress, queue)  

def on_cerrado_button(data_socket, serverAddress, queue):
    global buttonmodalidadbrazo_pressed_value
    global buttongripper_pressed_value
    global button_pressed_value
    button_pressed_value = 2
    buttonmodalidadbrazo_pressed_value = 3
    buttongripper_pressed_value=2
    send_data(data_socket, serverAddress, queue)  

def on_brazo_button(data_socket, serverAddress, queue):
    global button_pressed_value
    button_pressed_value = 2
    send_data(data_socket, serverAddress, queue)  

def on_mastil_button(data_socket, serverAddress, queue):
    global button_pressed_value
    button_pressed_value = 3
    send_data(data_socket, serverAddress, queue)  
    queue.put('start')

def on_on_button(data_socket, serverAddress, queue):
    global button_pressed_value
    global buttoncamara_pressed_value
    button_pressed_value = 4
    buttoncamara_pressed_value=1
    send_data(data_socket, serverAddress, queue)  

def on_off_button(data_socket, serverAddress, queue):
    global button_pressed_value
    global buttoncamara_pressed_value
    button_pressed_value = 4
    buttoncamara_pressed_value=2
    send_data(data_socket, serverAddress, queue)  

def on_reposobrazo_button():
    # Define los valores de reposo para cada entrada
    valores_reposo = ["0", "0", "0", "0", "0", "0"]
    # Asigna estos valores a las entradas correspondientes
    q1_entry.delete(0, tk.END)
    q1_entry.insert(0, valores_reposo[0])
    q2_entry.delete(0, tk.END)
    q2_entry.insert(0, valores_reposo[1])
    q3_entry.delete(0, tk.END)
    q3_entry.insert(0, valores_reposo[2])
    q4_entry.delete(0, tk.END)
    q4_entry.insert(0, valores_reposo[3])
    q5_entry.delete(0, tk.END)
    q5_entry.insert(0, valores_reposo[4])
    q6_entry.delete(0, tk.END)
    q6_entry.insert(0, valores_reposo[5])

def on_iniciobrazo_button():
    # Define los valores de reposo para cada entrada
    valores_reposo = ["45", "45", "45", "45", "45", "45"]
    # Asigna estos valores a las entradas correspondientes
    q1_entry.delete(0, tk.END)
    q1_entry.insert(0, valores_reposo[0])
    q2_entry.delete(0, tk.END)
    q2_entry.insert(0, valores_reposo[1])
    q3_entry.delete(0, tk.END)
    q3_entry.insert(0, valores_reposo[2])
    q4_entry.delete(0, tk.END)
    q4_entry.insert(0, valores_reposo[3])
    q5_entry.delete(0, tk.END)
    q5_entry.insert(0, valores_reposo[4])
    q6_entry.delete(0, tk.END)
    q6_entry.insert(0, valores_reposo[5])

def on_reposomastil_button():
    # Asigna estos valores a las entradas correspondientes
    mastil_entry.delete(0, tk.END)
    mastil_entry.insert(0, "90")

# Parámetros del socket de video
BUFF_SIZE = 65536
video_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
video_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, BUFF_SIZE)
host_ip = '192.168.0.100'  # IP del servidor de video
video_port = 9999
fps, st, frames_to_count, cnt = (0, 0, 20, 0)
video_socket.sendto(b'start', (host_ip, video_port))  # Inicia la transmisión de video

# Configuración del socket de datos

#video_socket.bind((host_ip, video_port))

def borrar_mensaje_fantasma(event):
    # Borra el mensaje "fantasma" del campo de entrada de velocidad
    if event.widget == velocidad_entry and velocidad_entry.get() == "(0-255)PWM":
        velocidad_entry.delete(0, "end")
    elif event.widget == angulo_entry and angulo_entry.get() == "(0-1000)grados":
        angulo_entry.delete(0, "end")
    elif event.widget == mastil_entry and mastil_entry.get() == "grados":
        mastil_entry.delete(0, "end")
    elif event.widget == q1_entry and q1_entry.get() == "grados":
        q1_entry.delete(0, "end")
    elif event.widget == q2_entry and q2_entry.get() == "grados":
        q2_entry.delete(0, "end")
    elif event.widget == q3_entry and q3_entry.get() == "grados":
        q3_entry.delete(0, "end")
    elif event.widget == q4_entry and q4_entry.get() == "grados":
        q4_entry.delete(0, "end")
    elif event.widget == q5_entry and q5_entry.get() == "grados":
        q5_entry.delete(0, "end")
    elif event.widget == q6_entry and q6_entry.get() == "grados":
        q6_entry.delete(0, "end")

def mostrar_mensaje_fantasma(event):
    # Si el campo de entrada de velocidad está vacío, muestra el mensaje "fantasma" nuevamente
    if event.widget == velocidad_entry and not velocidad_entry.get():
        velocidad_entry.insert(0, "(0-255)PWM")
    elif event.widget == angulo_entry and not angulo_entry.get():
        angulo_entry.insert(0, "(0-1000)grados")
    elif event.widget == mastil_entry and not mastil_entry.get():
        mastil_entry.insert(0, "grados")
    elif event.widget == q1_entry and not q1_entry.get():
        q1_entry.insert(0, "grados")
    elif event.widget == q2_entry and not q2_entry.get():
        q2_entry.insert(0, "grados")
    elif event.widget == q3_entry and not q3_entry.get():
        q3_entry.insert(0, "grados")
    elif event.widget == q4_entry and not q4_entry.get():
        q4_entry.insert(0, "grados")
    elif event.widget == q5_entry and not q5_entry.get():
        q5_entry.insert(0, "grados")
    elif event.widget == q6_entry and not q6_entry.get():
        q6_entry.insert(0, "grados")

def ocultar_mensaje_fantasma(event):
    # Borra el mensaje "fantasma" cuando el usuario empieza a escribir en el campo de entrada de velocidad
    if event.widget == velocidad_entry and velocidad_entry.get() == "(0-255)PWM":
        velocidad_entry.delete(0, "end")
    elif event.widget == angulo_entry and angulo_entry.get() == "(0-1000)grados":
        angulo_entry.delete(0, "end")
    elif event.widget == mastil_entry and mastil_entry.get() == "grados":
        mastil_entry.delete(0, "end")
    elif event.widget == q1_entry and q1_entry.get() == "grados":
        q1_entry.delete(0, "end")
    elif event.widget == q2_entry and q2_entry.get() == "grados":
        q2_entry.delete(0, "end")
    elif event.widget == q3_entry and q3_entry.get() == "grados":
        q3_entry.delete(0, "end")
    elif event.widget == q4_entry and q4_entry.get() == "grados":
        q4_entry.delete(0, "end")
    elif event.widget == q5_entry and q5_entry.get() == "grados":
        q5_entry.delete(0, "end")
    elif event.widget == q6_entry and q6_entry.get() == "grados":
        q6_entry.delete(0, "end")

# Configuración de la interfaz gráfica y proceso de video
if __name__ == '__main__':

    serverAddress = ('192.168.0.100', 2222)
    data_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    root = tk.Tk()
    root.title("Rover NAVT QAVAH")

    # Frame con fondo negro que cubre toda la columna 0 y 1
    frame_black = tk.Frame(root, bg="black")
    frame_black.grid(rowspan=999, column=0, sticky="nsew", columnspan=2)  # Usamos sticky="nsew" para que se expanda en todas las direcciones

    # Carga y muestra la imagen PNG
    # Carga la imagen PNG
    img = Image.open("rover2.png")  # Reemplaza "imagen.png" con el nombre de tu archivo PNG
    # Redimensiona la imagen utilizando BILINEAR
    img = img.resize((70, 70), Image.BILINEAR)
    # Convierte la imagen a un objeto PhotoImage
    photo = ImageTk.PhotoImage(img)
    label_photo = tk.Label(root, image=photo,bg="black")
    label_photo.grid(row=0, column=0, padx=5, pady=5,columnspan=2)

    # Etiqueta para clasificar MOVILIDAD
    label_camara = tk.Label(root, text="CÁMARA", font=("Helvetica", 10, "bold"),bg="black",fg="white")
    label_camara.grid(row=3, column=0, padx=5, pady=5,columnspan=2)
    on_button = tk.Button(root, text="On", bg="black",fg="green",command=lambda: on_on_button(data_socket, serverAddress, queue))
    on_button.grid(row=4, column=0, padx=5, pady=5)
    off_button = tk.Button(root, text="Off", bg="black",fg="red", command=lambda: on_off_button(data_socket, serverAddress, queue))
    off_button.grid(row=4, column=1, padx=5, pady=5)

    queue = Queue()
    video_process = Process(target=receive_video, args=(queue,))
    video_process.start()
    
    # Etiqueta para clasificar MOVILIDAD
    label_movilidad = tk.Label(root, text="Movilidad", font=("Helvetica", 10, "bold"))
    label_movilidad.grid(row=0, column=2, padx=5, pady=5,columnspan=2)

    # Etiquetas y campos de entrada para velocidad y ángulo
    label_velocidad = tk.Label(root, text="VELOCIDAD (0-255)")
    label_velocidad.grid(row=1, column=2, padx=5, pady=5,columnspan=2)
    velocidad_entry = tk.Entry(root, width=30,fg="gray")  # Ajusta el ancho del campo de entrada
    velocidad_entry.grid(row=2, column=2, padx=5, pady=5,columnspan=2)
    # Inserta el mensaje "fantasma" dentro del campo de entrada
    velocidad_entry.insert(0, "(0-255)PWM")
    # Detecta cuándo el usuario hace clic en el campo de entrada
    velocidad_entry.bind("<FocusIn>", borrar_mensaje_fantasma)
    # Detecta cuándo el usuario sale del campo de entrada
    velocidad_entry.bind("<FocusOut>", mostrar_mensaje_fantasma)
    # Detecta cuándo el usuario empieza a escribir en el campo de entrada
    velocidad_entry.bind("<Key>", ocultar_mensaje_fantasma)

    label_angulo = tk.Label(root, text="ÁNGULO (0-1000)")
    label_angulo.grid(row=3, column=2, padx=5, pady=5,columnspan=2)
    angulo_entry = tk.Entry(root, width=30,fg="gray")  # Ajusta el ancho del campo de entrada
    angulo_entry.grid(row=4, column=2, padx=5, pady=5,columnspan=2)
    # Inserta el mensaje "fantasma" dentro del campo de entrada
    angulo_entry.insert(0, "(0-1000)grados")
    # Detecta cuándo el usuario hace clic en el campo de entrada
    angulo_entry.bind("<FocusIn>", borrar_mensaje_fantasma)
    # Detecta cuándo el usuario sale del campo de entrada
    angulo_entry.bind("<FocusOut>", mostrar_mensaje_fantasma)
    # Detecta cuándo el usuario empieza a escribir en el campo de entrada
    angulo_entry.bind("<Key>", ocultar_mensaje_fantasma)

    mov_button = tk.Button(root, text="Enviar", command=lambda: on_mov_button(data_socket, serverAddress, queue))
    mov_button.grid(row=5, column=2, padx=5, pady=5)

    # Etiqueta para clasificar Grippr
    label_gripper = tk.Label(root, text="Gripper", font=("Helvetica", 10, "bold"))
    label_gripper.grid(row=8, column=2, padx=5, pady=5,columnspan=2)
    label_gripper = tk.Label(root, text="POSICIÓN")
    label_gripper.grid(row=9, column=2, padx=5, pady=5,columnspan=2)
    abierto_button = tk.Button(root, text="Abierto",bg="black",fg="white",command=lambda: on_abierto_button(data_socket, serverAddress, queue))
    abierto_button.grid(row=10, column=2, padx=5, pady=5)
    cerrado_button = tk.Button(root, text="Cerrado",bg="black",fg="white", command=lambda: on_cerrado_button(data_socket, serverAddress, queue))
    cerrado_button.grid(row=10, column=3, padx=5, pady=5)

    # Etiqueta para clasificar BRAZO
    label_brazo = tk.Label(root, text="Brazo", font=("Helvetica", 10, "bold"))
    label_brazo.grid(row=0, column=4, padx=5, pady=5,columnspan=2)

    label_cinematica = tk.Label(root, text="CINEMÁTICA",font=("Helvetica", 10))
    label_cinematica.grid(row=1, column=4, padx=5, pady=5,columnspan=2)
    directa_button = tk.Button(root, text="Directa", command=on_directa_button)
    directa_button.grid(row=2, column=4, padx=5, pady=5)
    inversa_button = tk.Button(root, text="Inversa", command=on_inversa_button)
    inversa_button.grid(row=2, column=5, padx=5, pady=5)

    # Etiquetas y campos de entrada para q1, q2, q3, q4, q5, q6
    label_q1 = tk.Label(root, text="Q1/X")
    label_q1.grid(row=3, column=4, padx=5, pady=5,columnspan=2)
    q1_entry = tk.Entry(root, width=30,fg="gray")  # Ajusta el ancho del campo de entrada
    q1_entry.grid(row=4, column=4, padx=5, pady=5,columnspan=2)
    q1_entry.insert(0, "grados")
    # Detecta cuándo el usuario hace clic en el campo de entrada
    q1_entry.bind("<FocusIn>", borrar_mensaje_fantasma)
    # Detecta cuándo el usuario sale del campo de entrada
    q1_entry.bind("<FocusOut>", mostrar_mensaje_fantasma)
    # Detecta cuándo el usuario empieza a escribir en el campo de entrada
    q1_entry.bind("<Key>", ocultar_mensaje_fantasma)
    label_q2 = tk.Label(root, text="Q2/Y")
    label_q2.grid(row=5, column=4, padx=5, pady=5,columnspan=2)
    q2_entry = tk.Entry(root, width=30,fg="gray")  # Ajusta el ancho del campo de entrada
    q2_entry.grid(row=6, column=4, padx=5, pady=5,columnspan=2)
    q2_entry.insert(0, "grados")
    # Detecta cuándo el usuario hace clic en el campo de entrada
    q2_entry.bind("<FocusIn>", borrar_mensaje_fantasma)
    # Detecta cuándo el usuario sale del campo de entrada
    q2_entry.bind("<FocusOut>", mostrar_mensaje_fantasma)
    # Detecta cuándo el usuario empieza a escribir en el campo de entrada
    q2_entry.bind("<Key>", ocultar_mensaje_fantasma)
    label_q3 = tk.Label(root, text="Q3/Z")
    label_q3.grid(row=7, column=4, padx=5, pady=5,columnspan=2)
    q3_entry = tk.Entry(root, width=30,fg="gray")  # Ajusta el ancho del campo de entrada
    q3_entry.grid(row=8, column=4, padx=5, pady=5,columnspan=2)
    q3_entry.insert(0, "grados")
    # Detecta cuándo el usuario hace clic en el campo de entrada
    q3_entry.bind("<FocusIn>", borrar_mensaje_fantasma)
    # Detecta cuándo el usuario sale del campo de entrada
    q3_entry.bind("<FocusOut>", mostrar_mensaje_fantasma)
    # Detecta cuándo el usuario empieza a escribir en el campo de entrada
    q3_entry.bind("<Key>", ocultar_mensaje_fantasma)
    label_q4 = tk.Label(root, text="Q4/YAW")
    label_q4.grid(row=9, column=4, padx=5, pady=5,columnspan=2)
    q4_entry = tk.Entry(root, width=30,fg="gray")  # Ajusta el ancho del campo de entrada
    q4_entry.grid(row=10, column=4, padx=5, pady=5,columnspan=2)
    q4_entry.insert(0, "grados")
    # Detecta cuándo el usuario hace clic en el campo de entrada
    q4_entry.bind("<FocusIn>", borrar_mensaje_fantasma)
    # Detecta cuándo el usuario sale del campo de entrada
    q4_entry.bind("<FocusOut>", mostrar_mensaje_fantasma)
    # Detecta cuándo el usuario empieza a escribir en el campo de entrada
    q4_entry.bind("<Key>", ocultar_mensaje_fantasma)
    label_q5 = tk.Label(root, text="Q5/PITCH")
    label_q5.grid(row=11, column=4, padx=5, pady=5,columnspan=2)
    q5_entry = tk.Entry(root, width=30,fg="gray")  # Ajusta el ancho del campo de entrada
    q5_entry.grid(row=12, column=4, padx=5, pady=5,columnspan=2)
    q5_entry.insert(0, "grados")
    # Detecta cuándo el usuario hace clic en el campo de entrada
    q5_entry.bind("<FocusIn>", borrar_mensaje_fantasma)
    # Detecta cuándo el usuario sale del campo de entrada
    q5_entry.bind("<FocusOut>", mostrar_mensaje_fantasma)
    # Detecta cuándo el usuario empieza a escribir en el campo de entrada
    q5_entry.bind("<Key>", ocultar_mensaje_fantasma)
    label_q6 = tk.Label(root, text="Q6/ROLL")
    label_q6.grid(row=13, column=4, padx=5, pady=5,columnspan=2)
    q6_entry = tk.Entry(root, width=30,fg="gray")  # Ajusta el ancho del campo de entrada
    q6_entry.grid(row=14, column=4, padx=5, pady=5,columnspan=2)
    q6_entry.insert(0, "grados")
    # Detecta cuándo el usuario hace clic en el campo de entrada
    q6_entry.bind("<FocusIn>", borrar_mensaje_fantasma)
    # Detecta cuándo el usuario sale del campo de entrada
    q6_entry.bind("<FocusOut>", mostrar_mensaje_fantasma)
    # Detecta cuándo el usuario empieza a escribir en el campo de entrada
    q6_entry.bind("<Key>", ocultar_mensaje_fantasma)

    brazo_button = tk.Button(root, text="Enviar",bg="black",fg="white", command=lambda: on_brazo_button(data_socket, serverAddress, queue))
    brazo_button.grid(row=15, column=4, padx=5, pady=5,columnspan=2)

    # Etiqueta para clasificar MASTIL
    label_mastil = tk.Label(root, text="Mastil", font=("Helvetica", 10, "bold"))
    label_mastil.grid(row=0, column=6, padx=5, pady=5,columnspan=2)
    label_mastil = tk.Label(root, text="POSICIÓN")
    label_mastil.grid(row=1, column=6, padx=5, pady=5,columnspan=2)
    mastil_entry = tk.Entry(root, width=30,fg="gray")  # Ajusta el ancho del campo de entrada
    mastil_entry.grid(row=2, column=6, padx=5, pady=5,columnspan=2)
    mastil_entry.insert(0, "grados")
    # Detecta cuándo el usuario hace clic en el campo de entrada
    mastil_entry.bind("<FocusIn>", borrar_mensaje_fantasma)
    # Detecta cuándo el usuario sale del campo de entrada
    mastil_entry.bind("<FocusOut>", mostrar_mensaje_fantasma)
    # Detecta cuándo el usuario empieza a escribir en el campo de entrada
    mastil_entry.bind("<Key>", ocultar_mensaje_fantasma)

    mastil_button = tk.Button(root, text="Enviar",bg="black",fg="white", command=lambda: on_mastil_button(data_socket, serverAddress, queue))
    mastil_button.grid(row=3, column=6, padx=5, pady=5,columnspan=2)

    #Etiqueta de Preset
    label_preset = tk.Label(root, text="Preset", font=("Helvetica", 10, "bold"))
    label_preset.grid(row=6, column=6, padx=5, pady=5,columnspan=2) 
    label_preset = tk.Label(root, text="BRAZO")
    label_preset.grid(row=7, column=6, padx=5, pady=5,columnspan=2)
    reposobrazo_button = tk.Button(root, text="Reposo",bg="white",fg="black", command= on_reposobrazo_button)
    reposobrazo_button.grid(row=8, column=6, padx=5, pady=5,columnspan=2)
    iniciobrazo_button = tk.Button(root, text="Inicio",bg="white",fg="black", command= on_iniciobrazo_button)
    iniciobrazo_button.grid(row=9, column=6, padx=5, pady=5,columnspan=2)
    label_preset = tk.Label(root, text="MÁSTIL")
    label_preset.grid(row=11, column=6, padx=5, pady=5,columnspan=2)
    reposomastil_button = tk.Button(root, text="Reposo",bg="white",fg="black", command= on_reposomastil_button)
    reposomastil_button.grid(row=12, column=6, padx=5, pady=5,columnspan=2)

    root.mainloop()
    video_process.terminate()  # Asegurarse de terminar el proceso al cerrar la interfaz gráfica