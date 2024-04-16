# importar librerias
import time
import tkinter as tk
from tkinter import ttk
from tkinter import Listbox
import funciones as f
from PIL import ImageTk, Image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import pandas as pd
import numpy as np
import pandas as pd
from tkinter import messagebox
from tkinter.simpledialog import askstring
import serial
from tkinter import Scrollbar
ser=serial.Serial("/dev/ttyACM0",115200)
#Descripción:
#Esta es una OOP, por lo que es una sola clase que contiene métodos y atributos.
frente="./udemlogo.png"

class Brazo_qavah: #cambiar a nombre relacionado con el brazo
    def __init__(self): #Se definen los atributos de los ángulos de los joints.
        self.th1=1000 #0
        self.th2=1000 #1
        self.th3=1000 #2
        self.th4=1000 #3
        self.th5=1000 #4
        self.th6=1000 #5
        self.th7=1000 #6
        self.th8=0 #7
        self.th9=0 #8
        self.lista = tk.Listbox()
        df = pd.read_csv("datosBrazo.csv")

    def guardar(self): #guardar una posición actual en el mismo csv
        #global lista
        try:
            df = pd.read_csv("datosBrazo.csv")
            new_name=askstring("Guardar posición","Nombre de la nueva posición")
            df[new_name]=[int(self.th1),int(self.th2),int(self.th3), int(self.th4), int(self.th5), int(self.th6)]
            df.to_csv("./datosBrazo.csv", index=False)
            print(df)
            self.lista.destroy()
            self.lista = tk.Listbox()
            self.load()

        except FileNotFoundError:
            messagebox.showerror("No file", "No hay documento csv.")



    def load(self):#carga información desde el csv

        df = pd.read_csv("datosBrazo.csv")
        v=0
        #global lista
        variable=list(df)
        variable=variable[2:]

        for x in list(df)[2:]:
            self.lista.insert(v,x)
            v+=1
        self.lista.grid(row=1, column=1, columnspan=2)

    def borrar(self):
        df = pd.read_csv("datosBrazo.csv")

        x=self.selected_item()
        del df[x]
        df.to_csv("./datosBrazo.csv", index=False)
        self.lista.destroy()
        self.lista = tk.Listbox()
        self.load()
    def cargar(self):
        df = pd.read_csv("datosBrazo.csv")
        x=self.selected_item()
        q1.set(df[x][0])
        q2.set(df[x][1])
        q3.set(df[x][2])
        q4.set(df[x][3])
        q5.set(df[x][4])
        q6.set(df[x][5])
        self.directa()

    def selected_item(self):
        for i in self.lista.curselection():
            return self.lista.get(i)


    # Create a button widget and
    # map the command parameter to
    # selected_item function



    def directa(self): #mecánica directa

        self.th1 = float(q1.get())  # se obtiene lo escrito de la interfaz
        self.th2 = float(q2.get())
        self.th3 = float(q3.get())
        self.th4 = float(q4.get())
        self.th5 = float(q5.get())
        self.th6 = float(q6.get())

        self.graficar()

        x, y, z, Ya, P, R = f.coordenadasDirecta(self.th1, self.th2, self.th3, self.th4, self.th5, self.th6)
        X.set(round(x))
        Y.set(round(y))
        Z.set(round(z))
        Yaw.set(round(Ya))
        Pitch.set(round(P))
        Roll.set(round(R))

        if self.th1 < 0:
            self.th1 = self.th1 + 360
        if self.th2 < 0:
            self.th2 = self.th2 + 360
        if self.th3 < 0:
            self.th3 = self.th3 + 360
        if self.th4 < 0:
            self.th4 = self.th4 + 360
        if self.th5 < 0:
            self.th5 = self.th5 + 360
        if self.th6 < 0:
            self.th6 = self.th6 + 360

        if modo.get() == 1: #se escribirá un serial
            xd=str([int(self.th1), int(self.th2), int(self.th3),  int(self.th4),  int(self.th5),  int(self.th6), int(1000),  int(1000),int(1000)])
            xd=xd.encode(encoding='utf-8')
            ser.write(xd)
            #time.sleep(0.1)

    def inversa(self): #hace referencia al movimiento inverso del brazo.

        xf = float(X.get()) #se obtienen los datos de la interfaz, en la columna de inversa
        yf = float(Y.get())
        zf = float(Z.get())
        Ya = float(Yaw.get())
        P = float(Pitch.get())
        R = float(Roll.get())

        ths = f.angulosInversa(xf, yf, zf, Ya, P, R)

        self.th1 = int(ths[0])
        self.th2 = int(ths[1])
        self.th3 = int(ths[2])
        self.th4 = int(ths[3])
        self.th5 = int(ths[4])
        self.th6 = int(ths[5])

        q1.set(self.th1)
        q2.set(self.th2)
        q3.set(self.th3)
        q4.set(self.th4)
        q5.set(self.th5)
        q6.set(self.th6)
        #se hace la gráfica
        self.graficar()
        #se transforman los ángulos
        if self.th1 < 0:
            self.th1 = self.th1 + 360
        if self.th2 < 0:
            self.th2 = self.th2 + 360
        if self.th3 < 0:
            th3 = self.th3 + 360
        if self.th4 < 0:
            self.th4 = self.th4 + 360
        if self.th5 < 0:
            self.th5 = self.th5 + 360
        if self.th6 < 0:
            self.th6 = self.th6 + 360

        if modo.get() == 1:
            xd=str([int(self.th1), int(self.th2), int(self.th3),  int(self.th4),  int(self.th5),  int(self.th6), int(1000),  int(1000),int(1000)])
            xd=xd.encode(encoding='utf-8')
            ser.write(xd)

    def graficar(self): #simulación gráfica

        self.th1 = float(q1.get())
        self.th2 = float(q2.get())
        self.th3 = float(q3.get())
        self.th4 = float(q4.get())
        self.th5 = float(q5.get())
        self.th6 = float(q6.get())

        p1, p2, p3, p4, p6 = f.simulacion(self.th1, self.th2, self.th3, self.th4, self.th5, self.th6)
        x = [0, p1[1], p2[1], p3[1], p4[1], p6[1]]
        y = [0, p1[2], p2[2], p3[2], p4[2], p6[2]]
        z = [0, p1[0], p2[0], p3[0], p4[0], p6[0]]

        fig = Figure(figsize=(3, 3), dpi=60)
        ax = fig.add_subplot(1, 1, 1, projection='3d')
        ax.scatter(x, y, z, c='#969696', s=100)
        ax.plot(x, y, z, color='g')
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
    #def internet(self): #pendiente, quitar
     #   pass

    def home(self):
        self.th1 = q1_home.get()
        self.th2 = q2_home.get()
        self.th3 = q3_home.get()
        self.th4 = q4_home.get()
        self.th5 = q5_home.get()
        self.th6 = q6_home.get()

        q1.set(self.th1)
        q2.set(self.th2)
        q3.set(self.th3)
        q4.set(self.th4)
        q5.set(self.th5)
        q6.set(self.th6)
        self.directa()
        #return

    def reposo(self):

        self.th1 = q1_rep.get()
        self.th2 = q2_rep.get()
        self.th3 = q3_rep.get()
        self.th4 = q4_rep.get()
        self.th5 = q5_rep.get()
        self.th6 = q6_rep.get()

        q1.set(self.th1)
        q2.set(self.th2)
        q3.set(self.th3)
        q4.set(self.th4)
        q5.set(self.th5)
        q6.set(self.th6)
        self.directa()

    def archivo(self):

        df = pd.read_csv("datosBrazo.csv")
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

    def buscar_origen(self):
        #client.write_single_register(6, 1)
        time.sleep(0.1)
        self.reposo()
        top = tk.Toplevel()
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
        botonIzq = tk.Button(top, text="Izquierda", font=("Arial", 10))
        botonIzq.grid(row=0, column=1, rowspan=3, padx=20, pady=5)
        botonIzq.bind('<ButtonPress-1>', self.giro_izquierda)
        botonIzq.bind('<ButtonRelease-1>', self.paro_giro_izquierda)
        botonDer = tk.Button(top, text="Derecha", font=("Arial", 10))
        botonDer.grid(row=3, column=1, rowspan=3, padx=20, pady=5)
        botonDer.bind('<ButtonPress-1>', self.giro_derecha)
        botonDer.bind('<ButtonRelease-1>', self.paro_giro_derecha)

        def origen_encontrado():
            top.destroy()
            xd=str([int(1000), int(1000), int(1000),  int(1000),  int(1000),  int(1000), int(0),  int(1000),int(1000)])
            xd=xd.encode(encoding='utf-8')
            ser.write(xd)
        botonReady = tk.Button(top, text="OK", font=("Arial", 10), command=origen_encontrado)
        botonReady.grid(row=6, column=0, columnspan=2, padx=20, pady=5)
    def giro_izquierda(self, event):
        xd = str([int(1000), int(1000), int(1000), int(1000), int(1000), int(1000), int(1), int(art.get()), int(1)])
        xd = xd.encode(encoding='utf-8')
        ser.write(xd)
        #time.sleep(0.1)
    def paro_giro_izquierda(self, event):
        xd = str([int(1000), int(1000), int(1000), int(1000), int(1000), int(1000), int(1), int(art.get()), int(0)])
        xd = xd.encode(encoding='utf-8')
        ser.write(xd)
        #time.sleep(0.1)

    def giro_derecha(self, event):
        xd = str([int(1000), int(1000), int(1000), int(1000), int(1000), int(1000), int(1), int(art.get()), int(2)])
        xd = xd.encode(encoding='utf-8')
        ser.write(xd)
        #time.sleep(0.1)

    def paro_giro_derecha(self, event):
        xd = str([int(1000), int(1000), int(1000), int(1000), int(1000), int(1000), int(1), int(art.get()), int(0)])
        xd = xd.encode(encoding='utf-8')
        ser.write(xd)
        #time.sleep(0.1)



# crear la interfaz
root = tk.Tk()
notebook = ttk.Notebook(root)
root.config(padx=10, pady=10, bg="gray")
tab1 = tk.Frame(notebook, bg="#FCE22A")
tab2 = tk.Frame(notebook, bg="#969696")
notebook.add(tab1, text="Brazo")
notebook.add(tab2,text="Robot")
notebook.grid(row=0, column=0,rowspan=4, pady=0)
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
st.set("UART")

ip = tk.StringVar()
puerto = tk.StringVar()
modo = tk.IntVar()
art = tk.IntVar()

# titulo de la interfáz
title = "ROVER HMI"
root.title(title)
#
#Crear Robot
rover=Brazo_qavah()
root.bell()
#messagebox.showerror(title="Oops", message="Please don´t leave any fields empty")
rover.archivo()
rover.load()

# crear frames
palab = tk.Label(text="Posiciones guardadas:", fg="black", bg="white")
palab.grid(row=0, column=1,  pady=0)


frame1 = tk.LabelFrame(tab1, text="Control esencial")
frame1.grid(column=0, row=2, padx=10, pady=10, sticky="NW", ipadx=21, ipady=5)
frame2 = tk.LabelFrame(tab1, text="Conexión Serial")
frame2.grid(column=0, row=3, padx=10, pady=5, sticky="NW")
frame3 = tk.LabelFrame(tab1, text="Posiciones predeterminadas")
frame3.grid(column=0, row=4, padx=10, pady=5, sticky="NW", ipadx=10)
frameIm = tk.LabelFrame(tab1, text="")
frameIm.grid(column=2, row=2, rowspan=3, padx=10, pady=10, sticky="N")
frameSim = tk.LabelFrame(tab1, text="Gráfica de posición del E.F.")
frameSim.grid(column=2, row=3, rowspan=2, padx=10, pady=10, sticky="S")
frameM = tk.LabelFrame(tab1, text="Control de cinemática")
frameM.grid(column=1, row=2, rowspan=3, padx=10, pady=10, sticky="N")


# crear imagen
img = Image.open(frente)
img = img.resize((200,120))
img = ImageTk.PhotoImage(img)
imgl = tk.Label(frameIm, image=img, borderwidth = 0, highlightthickness = 0, bg="blue")
imgl.grid(row=0, column=0)

# # titulo dentro de la interfaz (tab1)
labelT = tk.Label(tab1, text="CONTROL DE CINEMÁTICA DEL BRAZO MANIPULADOR", fg="black", bg="black")
labelT.grid(row=1, column=0, columnspan=3, pady=10)
labelT.config(font=("Arial",15,'bold'), bg="#FCE22A")

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
botonD = tk.Button(frameM, text="OK", command=rover.directa, font=("Arial",10))
botonD.grid(row=15, column=2, padx=5, pady=5)
botonI = tk.Button(frameM, text="OK", command=rover.inversa, font=("Arial",10))
botonI.grid(row=15, column=3, padx=5, pady=5)
botonHome = tk.Button(frame3, text="Home", command=rover.home, font=("Arial",10))
botonHome.grid(row=0, column=0, padx=5, pady=5)
botonReposo = tk.Button(frame3, text="Reposo", command=rover.reposo, font=("Arial",10))
botonReposo.grid(row=0, column=1, padx=5, pady=5)
#botonArch = tk.Button(frame3, text="Cargar datos", command=rover.archivo, font=("Arial",10))
#botonArch.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky='W')
botonOrig = tk.Button(frame3, text="Buscar origen", command=rover.buscar_origen, font=("Arial", 10))
botonOrig.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky='W')
botonSave=tk.Button(frame3, text="Guardar", command=rover.guardar, font =("Arial",10))
botonSave.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky='W')
botonBorrar=tk.Button(text="Borrar", command=rover.borrar, font =("Arial",14))
botonBorrar.grid(row=2, column=2, padx=5, pady=10)
botonCargar=tk.Button(text="Cargar", command=rover.cargar, font =("Arial",14))
botonCargar.grid(row=2, column=1, padx=5, pady=10)

# radio button
botonModoC = tk.Radiobutton(frame1, text="Control", variable=modo, value=1)
botonModoC.grid(row=1, column=0, columnspan=2, sticky='W')
botonModoS = tk.Radiobutton(frame1, text="Simulación", variable=modo, value=2)
botonModoS.grid(row=2, column=0, columnspan=2, sticky='W')


root.resizable(0,0)
# Abajo de todo
root.mainloop()