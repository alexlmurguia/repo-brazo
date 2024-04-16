# importar librerias
from pyModbusTCP.client import ModbusClient
import time
import tkinter as tk
from tkinter import ttk
import funciones as f
from PIL import ImageTk, Image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import pandas as pd

client = ModbusClient()

# crear funciones
def energia():

    return

def paro():
    
    return

def apagar():
    
    return

def directa():
    
    th1 = float(q1.get())
    th2 = float(q2.get())
    th3 = float(q3.get())
    th4 = float(q4.get())
    th5 = float(q5.get())
    th6 = float(q6.get())
    
    sim()
    
    x, y, z, Ya, P, R = f.coordenadasDirecta(th1, th2, th3, th4, th5, th6)
    
    X.set(round(x))
    Y.set(round(y))
    Z.set(round(z))
    Yaw.set(round(Ya))
    Pitch.set(round(P))
    Roll.set(round(R))
    
    if th1 < 0:
        th1 = th1 + 360
    if th2 < 0:
        th2 = th2 + 360
    if th3 < 0:
        th3 = th3 + 360
    if th4 < 0:
        th4 = th4 + 360
    if th5 < 0:
        th5 = th5 + 360
    if th6 < 0:
        th6 = th6 + 360
    
    if modo.get() == 1:
    
        client.write_single_register(0, int(th1))
        client.write_single_register(1, int(th2))
        client.write_single_register(2, int(th3))
        client.write_single_register(3, int(th4))
        client.write_single_register(4, int(th5))
        client.write_single_register(5, int(th6))
    
        time.sleep(0.1)
    
def inversa():
    
    xf = float(X.get())
    yf = float(Y.get())
    zf = float(Z.get())
    Ya = float(Yaw.get())
    P = float(Pitch.get())
    R = float(Roll.get())
    
    ths = f.angulosInversa(xf, yf, zf, Ya, P, R)
    
    th1 = int(ths[0])
    th2 = int(ths[1])
    th3 = int(ths[2])
    th4 = int(ths[3])
    th5 = int(ths[4])
    th6 = int(ths[5])
    
    q1.set(th1)
    q2.set(th2)
    q3.set(th3)
    q4.set(th4)
    q5.set(th5)
    q6.set(th6)
    
    sim()
    
    if th1 < 0:
        th1 = th1 + 360
    if th2 < 0:
        th2 = th2 + 360
    if th3 < 0:
        th3 = th3 + 360
    if th4 < 0:
        th4 = th4 + 360
    if th5 < 0:
        th5 = th5 + 360
    if th6 < 0:
        th6 = th6 + 360
    
    if modo.get() == 1:
        
        client.write_single_register(0, th1)
        client.write_single_register(1, th2)
        client.write_single_register(2, th3)
        client.write_single_register(3, th4)
        client.write_single_register(4, th5)
        client.write_single_register(5, th6)
    
        time.sleep(0.1)

def sim():
    
    th1 = float(q1.get())
    th2 = float(q2.get())
    th3 = float(q3.get())
    th4 = float(q4.get())
    th5 = float(q5.get())
    th6 = float(q6.get())
    
    p1, p2, p3, p4, p6 = f.simulacion(th1, th2, th3, th4, th5, th6)
    
    x = [0,p1[1],p2[1],p3[1],p4[1],p6[1]]
    y = [0,p1[2],p2[2],p3[2],p4[2],p6[2]]
    z = [0,p1[0],p2[0],p3[0],p4[0],p6[0]]
    
    fig = Figure(figsize=(3,3), dpi=60)
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    ax.scatter(x,y,z, c='#969696',s=100)
    ax.plot(x,y,z, color='g')
    ax.set_xlim(400, -400)
    ax.set_ylim(300, 0)
    ax.set_zlim(-300, 300)
    ax.set_xlabel('Y (mm)')
    ax.set_ylabel('Z (mm)')
    ax.set_zlabel('X (mm)')
    
    canvas = FigureCanvasTkAgg(fig, frameSim)
    canvas.draw()
    canvas.get_tk_widget().grid(row=0, column=0)
    
    return

def internet():
    
    # variables de comunicación wifi
    server_host = ip.get()
    server_port = int(puerto.get())
    
    client.host(server_host)
    client.port(server_port)
    
    if not client.is_open():
        if not client.open():
            st.set("Sin conexión")
    
    if client.is_open():
        st.set("Conectado")

def home():
    
    th1 = q1_home.get()
    th2 = q2_home.get()
    th3 = q3_home.get()
    th4 = q4_home.get()
    th5 = q5_home.get()
    th6 = q6_home.get()
    
    q1.set(th1)
    q2.set(th2)
    q3.set(th3)
    q4.set(th4)
    q5.set(th5)
    q6.set(th6)
    
    directa()
    
    return

def reposo():
    
    th1 = q1_rep.get()
    th2 = q2_rep.get()
    th3 = q3_rep.get()
    th4 = q4_rep.get()
    th5 = q5_rep.get()
    th6 = q6_rep.get()
    
    q1.set(th1)
    q2.set(th2)
    q3.set(th3)
    q4.set(th4)
    q5.set(th5)
    q6.set(th6)
    
    directa()
    
    return

def archivo():
    
    df = pd.read_csv("datosBrazo.csv")
    
    ip.set(df["IP"][0])
    puerto.set(int(df["Puerto"][0]))
    internet()
    
    q1_home.set(df["Home"][0])
    q2_home.set(df["Home"][1])
    q3_home.set(df["Home"][2])
    q4_home.set(df["Home"][3])
    q5_home.set(df["Home"][4])
    q6_home.set(df["Home"][5])
    
    q1_rep.set(df["Reposo"][0])
    q2_rep.set(df["Reposo"][1])
    q3_rep.set(df["Reposo"][2])
    q4_rep.set(df["Reposo"][3])
    q5_rep.set(df["Reposo"][4])
    q6_rep.set(df["Reposo"][5])
    
    return

def origen():
    
    client.write_single_register(6, 1)
    time.sleep(0.1)
    
    reposo()
    
    top = tk.Toplevel()
    top.title("Buscar Origen")
    root.iconbitmap("Icono.ico")
    
    botonq1org = tk.Radiobutton(top, text="q1", variable=art, value=1)
    botonq1org.grid(row=0, column=0, padx=20, pady=5)
    botonq2org = tk.Radiobutton(top, text="q2", variable=art, value=2)
    botonq2org.grid(row=1, column=0, padx=20, pady=5)
    botonq3org = tk.Radiobutton(top, text="q3", variable=art, value=3)
    botonq3org.grid(row=2, column=0, padx=20, pady=5)
    botonq4org = tk.Radiobutton(top, text="q4", variable=art, value=4)
    botonq4org.grid(row=3, column=0, padx=20, pady=5)
    botonq5org = tk.Radiobutton(top, text="q5", variable=art, value=5)
    botonq5org.grid(row=4, column=0, padx=20, pady=5)
    botonq6org = tk.Radiobutton(top, text="q6", variable=art, value=6)
    botonq6org.grid(row=5, column=0, padx=20, pady=5)
    
    botonIzq = tk.Button(top, text="Izquierda", font=("Arial",10))
    botonIzq.grid(row=0, column=1, rowspan=3, padx=20, pady=5)
    botonIzq.bind('<ButtonPress-1>',izq)
    botonIzq.bind('<ButtonRelease-1>',paroizq)
    botonDer = tk.Button(top, text="Derecha", font=("Arial",10))
    botonDer.grid(row=3, column=1, rowspan=3, padx=20, pady=5)
    botonDer.bind('<ButtonPress-1>',der)
    botonDer.bind('<ButtonRelease-1>',paroder)
    
    def encontrado():
        
        top.destroy()
        client.write_single_register(6, 0)
        time.sleep(0.1)
        
    botonReady = tk.Button(top, text="OK", font=("Arial",10), command=encontrado)
    botonReady.grid(row=6, column=0, columnspan=2, padx=20, pady=5)
    
        
def izq(event):
    
    client.write_single_register(7, art.get())
    client.write_single_register(8, 1)
    time.sleep(0.1)

def paroizq(event):
    
    client.write_single_register(7, art.get())
    client.write_single_register(8, 0)
    time.sleep(0.1)
    

def der(event):
    
    client.write_single_register(7, art.get())
    client.write_single_register(8, 2)
    time.sleep(0.1)


def paroder(event):
    
    client.write_single_register(7, art.get())
    client.write_single_register(8, 0)
    time.sleep(0.1)


# crear la interfaz
root = tk.Tk()
notebook = ttk.Notebook(root)

tab1 = tk.Frame(notebook, bg="#969696")

notebook.add(tab1, text="Cinemática")

notebook.grid(row=0, column=0)

# crear variables dinámicas
q1 = tk.StringVar()
q2 = tk.StringVar()
q3 = tk.StringVar()
q4 = tk.StringVar()
q5 = tk.StringVar()
q6 = tk.StringVar()

q1_home = tk.StringVar()
q2_home = tk.StringVar()
q3_home = tk.StringVar()
q4_home = tk.StringVar()
q5_home = tk.StringVar()
q6_home = tk.StringVar()

q1_rep = tk.StringVar()
q2_rep = tk.StringVar()
q3_rep = tk.StringVar()
q4_rep = tk.StringVar()
q5_rep = tk.StringVar()
q6_rep = tk.StringVar()

X = tk.StringVar()
Y = tk.StringVar()
Z = tk.StringVar()

Yaw = tk.StringVar()
Pitch = tk.StringVar()
Roll = tk.StringVar()

st = tk.StringVar()
st.set("Sin conexión")

ip = tk.StringVar()
puerto = tk.StringVar()
modo = tk.IntVar()
art = tk.IntVar()

# titulo de la interfáz
title = "Interfaz de usuario: Brazo manipulador QAVAH"
root.title(title)

# crear frames
frame1 = tk.LabelFrame(tab1, text="Control esencial")
frame1.grid(column=0, row=2, padx=10, pady=10, sticky="NW", ipadx=21, ipady=5)
frame2 = tk.LabelFrame(tab1, text="Conexión WiFi")
frame2.grid(column=0, row=3, padx=10, pady=5, sticky="NW")
frame3 = tk.LabelFrame(tab1, text="Posiciones predeterminadas")
frame3.grid(column=0, row=4, padx=10, pady=5, sticky="NW", ipadx=10)
frameIm = tk.LabelFrame(tab1, text="Imágen de ejemplo")
frameIm.grid(column=2, row=2, rowspan=3, padx=10, pady=10, sticky="N")
frameSim = tk.LabelFrame(tab1, text="Gráfica de posición del E.F.")
frameSim.grid(column=2, row=3, rowspan=2, padx=10, pady=10, sticky="S")
frameM = tk.LabelFrame(tab1, text="Control de cinemática")
frameM.grid(column=1, row=2, rowspan=3, padx=10, pady=10, sticky="N")

# crear imagen
#img = Image.open('Brazo2.jpg')
#img = img.resize((180,180))
#img = ImageTk.PhotoImage(img)
#imgl = tk.Label(frameIm, image=img, borderwidth = 0, highlightthickness = 0)
#imgl.grid(row=0, column=0)

# # titulo dentro de la interfaz (tab1)
labelT = tk.Label(tab1, text="Control de Cinemática del Brazo Manipulador", fg="white")
labelT.grid(row=1, column=0, columnspan=3, pady=10)
labelT.config(font=("Arial",15,'bold'), bg="#969696")
labelTIP = tk.Label(frame2, text="IP:")
labelTIP.grid(row=0, column=0, padx=5, pady=5)
labelTIP.config(font=("Arial",12))
labelTIP = tk.Label(frame2, text="Puerto:")
labelTIP.grid(row=1, column=0, padx=5, pady=5)
labelTIP.config(font=("Arial",12))
labelTStatus = tk.Label(frame2, textvariable=st)
labelTStatus.grid(row=2, column=1, padx=5, pady=5)
labelTStatus.config(font=("Arial",12), bg="yellow")
labelTD = tk.Label(frameM, text="Cinemática Directa")
labelTD.grid(row=2, column=2, padx=10, pady=5)
labelTD.config(font=("Arial",12,'underline'))
labelTI = tk.Label(frameM, text="Cinemática Inversa")
labelTI.grid(row=2, column=3, padx=10, pady=5)
labelTI.config(font=("Arial",12,'underline'))
labelq1 = tk.Label(frameM, text="q1 (°)")
labelq1.grid(row=3, column=2, pady=5)
labelq1.config(font=("Arial",12))
labelq2 = tk.Label(frameM, text="q2 (°)")
labelq2.grid(row=5, column=2, pady=5)
labelq2.config(font=("Arial",12))
labelq3 = tk.Label(frameM, text="q3 (°)")
labelq3.grid(row=7, column=2, pady=5)
labelq3.config(font=("Arial",12))
labelq4 = tk.Label(frameM, text="q4 (°)")
labelq4.grid(row=9, column=2, pady=5)
labelq4.config(font=("Arial",12))
labelq5 = tk.Label(frameM, text="q5 (°)")
labelq5.grid(row=11, column=2, pady=5)
labelq5.config(font=("Arial",12))
labelq6 = tk.Label(frameM, text="q6 (°)")
labelq6.grid(row=13, column=2, pady=5)
labelq6.config(font=("Arial",12))
labelX = tk.Label(frameM, text="X (mm)")
labelX.grid(row=3, column=3, pady=5)
labelX.config(font=("Arial",12))
labelY = tk.Label(frameM, text="Y (mm)")
labelY.grid(row=5, column=3, pady=5)
labelY.config(font=("Arial",12))
labelZ = tk.Label(frameM, text="Z (mm)")
labelZ.grid(row=7, column=3, pady=5)
labelZ.config(font=("Arial",12))
labelYaw = tk.Label(frameM, text="Yaw (°)")
labelYaw.grid(row=9, column=3, pady=5)
labelYaw.config(font=("Arial",12))
labelPitch = tk.Label(frameM, text="Pitch (°)")
labelPitch.grid(row=11, column=3, pady=5)
labelPitch.config(font=("Arial",12))
labelRoll = tk.Label(frameM, text="Roll (°)")
labelRoll.grid(row=13, column=3, pady=5)
labelRoll.config(font=("Arial",12))

# entradas de texto
entryIP = tk.Entry(frame2, textvariable=ip, justify="center", width=12)
entryIP.grid(row=0, column=1, padx=5, pady=5)
entryPuerto = tk.Entry(frame2, textvariable=puerto, justify="center", width=12)
entryPuerto.grid(row=1, column=1, padx=5, pady=5)
entryq1 = tk.Entry(frameM, textvariable=q1, justify="center", width=12)
entryq1.grid(row=4, column=2, padx=5)
entryq2 = tk.Entry(frameM, textvariable=q2, justify="center", width=12)
entryq2.grid(row=6, column=2, padx=5)
entryq3 = tk.Entry(frameM, textvariable=q3, justify="center", width=12)
entryq3.grid(row=8, column=2, padx=5)
entryq4 = tk.Entry(frameM, textvariable=q4, justify="center", width=12)
entryq4.grid(row=10, column=2, padx=5)
entryq5 = tk.Entry(frameM, textvariable=q5, justify="center", width=12)
entryq5.grid(row=12, column=2, padx=5)
entryq6 = tk.Entry(frameM, textvariable=q6, justify="center", width=12)
entryq6.grid(row=14, column=2, padx=5)
entryX = tk.Entry(frameM, textvariable=X, justify="center", width=12)
entryX.grid(row=4, column=3, padx=5)
entryY = tk.Entry(frameM, textvariable=Y, justify="center", width=12)
entryY.grid(row=6, column=3, padx=5)
entryZ = tk.Entry(frameM, textvariable=Z, justify="center", width=12)
entryZ.grid(row=8, column=3, padx=5)
entryYaw = tk.Entry(frameM, textvariable=Yaw, justify="center", width=12)
entryYaw.grid(row=10, column=3, padx=5)
entryPitch = tk.Entry(frameM, textvariable=Pitch, justify="center", width=12)
entryPitch.grid(row=12, column=3, padx=5)
entryRoll = tk.Entry(frameM, textvariable=Roll, justify="center", width=12)
entryRoll.grid(row=14, column=3, padx=5)

# botones de la interfáz
botonD = tk.Button(frameM, text="OK", command=directa, font=("Arial",10))
botonD.grid(row=15, column=2, padx=5, pady=5)
botonI = tk.Button(frameM, text="OK", command=inversa, font=("Arial",10))
botonI.grid(row=15, column=3, padx=5, pady=5)
botonON = tk.Button(frame1, text="ON", command=energia, font=("Arial",10))
botonON.grid(row=0, column=0, padx=5, pady=5)
botonOFF = tk.Button(frame1, text="OFF", command=apagar, font=("Arial",10))
botonOFF.grid(row=0, column=1, padx=5, pady=5)
botonParo = tk.Button(frame1, text="Paro", command=paro, bg='red', font=("Arial",10))
botonParo.grid(row=0, column=2, padx=5, pady=5)
botonWifi = tk.Button(frame2, text="Conectar", command=internet, font=("Arial",10))
botonWifi.grid(row=2, column=0, padx=5, pady=5)
botonHome = tk.Button(frame3, text="Home", command=home, font=("Arial",10))
botonHome.grid(row=0, column=0, padx=5, pady=5)
botonReposo = tk.Button(frame3, text="Reposo", command=reposo, font=("Arial",10))
botonReposo.grid(row=0, column=1, padx=5, pady=5)
botonArch = tk.Button(frame3, text="Cargar datos", command=archivo, font=("Arial",10))
botonArch.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky='W')
botonOrig = tk.Button(frame3, text="Buscar origen", command=origen, font=("Arial",10))
botonOrig.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky='W')


# radio button
botonModoC = tk.Radiobutton(frame1, text="Control", variable=modo, value=1)
botonModoC.grid(row=1, column=0, columnspan=2, sticky='W')
botonModoS = tk.Radiobutton(frame1, text="Simulación", variable=modo, value=2)
botonModoS.grid(row=2, column=0, columnspan=2, sticky='W')

# icono de la interfáz
#icon = "Icono.ico"
#root.iconbitmap(icon)

# no modificable
root.resizable(0,0)

# Abajo de todo
root.mainloop()

