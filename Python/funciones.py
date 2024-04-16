
# Se importan librerias bÃ¡sicas
import numpy as np
import cmath
import math
#####

# se da la precisión
np.set_printoptions(precision=4)
#####

def simulacion(th1, th2, th3, th4, th5, th6):
    
    th1 = th1*math.pi/180
    th2 = th2*math.pi/180
    th3 = th3*math.pi/180
    th4 = th4*math.pi/180
    th5 = th5*math.pi/180
    th6 = th6*math.pi/180
    
    L1 = 83
    L2 = 190
    L3 = 50
    L4 = 172
    L5 = 88
    
    x1 = 0
    y1 = 0
    z1 = L1
    p1 = np.array([x1,y1,z1])

    x2 = L2*math.cos(th1)*math.cos(th2)
    y2 = L2*math.cos(th2)*math.sin(th1)
    z2 = L1 + L2*math.sin(th2)
    p2 = np.array([x2,y2,z2])
    
    x3 = L2*math.cos(th1)*math.cos(th2) - L3*math.sin(th1)
    y3 = L3*math.cos(th1) + L2*math.cos(th2)*math.sin(th1)
    z3 = L1 + L2*math.sin(th2)
    p3 = np.array([x3,y3,z3])
    
    x4 = L2*math.cos(th1)*math.cos(th2) - L4*(math.cos(th1)*math.cos(th2)*math.sin(th3) + math.cos(th1)*math.cos(th3)*math.sin(th2)) - L3*math.sin(th1)
    y4 = L3*math.cos(th1) - L4*(math.cos(th2)*math.sin(th1)*math.sin(th3) + math.cos(th3)*math.sin(th1)*math.sin(th2)) + L2*math.cos(th2)*math.sin(th1)
    z4 = L1 + L4*math.cos(th2 + th3) + L2*math.sin(th2)
    p4 = np.array([x4,y4,z4])
    
    x6 = L2*math.cos(th1)*math.cos(th2) - L4*math.sin(th2 + th3)*math.cos(th1) - L3*math.sin(th1) - L5*math.sin(th2 + th3)*math.cos(th1)*math.cos(th5) + L5*math.sin(th1)*math.sin(th4)*math.sin(th5) + L5*math.cos(th1)*math.cos(th4)*math.sin(th2)*math.sin(th3)*math.sin(th5) - L5*math.cos(th1)*math.cos(th2)*math.cos(th3)*math.cos(th4)*math.sin(th5)
    y6 = L3*math.cos(th1) - L4*math.sin(th2 + th3)*math.sin(th1) + L2*math.cos(th2)*math.sin(th1) - L5*math.sin(th2 + th3)*math.cos(th5)*math.sin(th1) - L5*math.cos(th1)*math.sin(th4)*math.sin(th5) - L5*math.cos(th2)*math.cos(th3)*math.cos(th4)*math.sin(th1)*math.sin(th5) + L5*math.cos(th4)*math.sin(th1)*math.sin(th2)*math.sin(th3)*math.sin(th5)
    z6 = L1 + L4*math.cos(th2 + th3) + L2*math.sin(th2) - (L5*math.sin(th2 + th3)*math.sin(th4 + th5))/2 + L5*math.cos(th2 + th3)*math.cos(th5) + (L5*math.sin(th4 - th5)*math.sin(th2 + th3))/2
    p6 = np.array([x6,y6,z6])

    return p1, p2, p3, p4, p6

def coordenadasDirecta(th1, th2, th3, th4, th5, th6):
    
    th1 = th1*math.pi/180
    th2 = th2*math.pi/180
    th3 = th3*math.pi/180
    th4 = th4*math.pi/180
    th5 = th5*math.pi/180
    th6 = th6*math.pi/180
    
    L1 = 83
    L2 = 190
    L3 = 50
    L4 = 172
    L5 = 88
    
    # calcular coordenadas x, y, z con los angulos th
    x = L2*np.cos(th1)*np.cos(th2) - L4*np.sin(th2 + th3)*np.cos(th1) - L3*np.sin(th1) - L5*np.sin(th2 + th3)*np.cos(th1)*np.cos(th5) + L5*np.sin(th1)*np.sin(th4)*np.sin(th5) + L5*np.cos(th1)*np.cos(th4)*np.sin(th2)*np.sin(th3)*np.sin(th5) - L5*np.cos(th1)*np.cos(th2)*np.cos(th3)*np.cos(th4)*np.sin(th5)
    y = L3*np.cos(th1) - L4*np.sin(th2 + th3)*np.sin(th1) + L2*np.cos(th2)*np.sin(th1) - L5*np.sin(th2 + th3)*np.cos(th5)*np.sin(th1) - L5*np.cos(th1)*np.sin(th4)*np.sin(th5) - L5*np.cos(th2)*np.cos(th3)*np.cos(th4)*np.sin(th1)*np.sin(th5) + L5*np.cos(th4)*np.sin(th1)*np.sin(th2)*np.sin(th3)*np.sin(th5)
    z = L1 + L4*np.cos(th2 + th3) + L2*np.sin(th2) - (L5*np.sin(th2 + th3)*np.sin(th4 + th5))/2 + L5*np.cos(th2 + th3)*np.cos(th5) + (L5*np.sin(th4 - th5)*np.sin(th2 + th3))/2
    axc = np.sin(th5)*(np.sin(th1)*np.sin(th4) + np.cos(th4)*(np.cos(th1)*np.sin(th2)*np.sin(th3) - np.cos(th1)*np.cos(th2)*np.cos(th3))) - np.cos(th5)*(np.cos(th1)*np.cos(th2)*np.sin(th3) + np.cos(th1)*np.cos(th3)*np.sin(th2))
    P = math.asin(axc)
    nxc = -np.sin(th6)*(np.cos(th4)*np.sin(th1) - np.sin(th4)*(np.cos(th1)*np.sin(th2)*np.sin(th3) - np.cos(th1)*np.cos(th2)*np.cos(th3))) - np.cos(th6)*(np.cos(th5)*(np.sin(th1)*np.sin(th4) + np.cos(th4)*(np.cos(th1)*np.sin(th2)*np.sin(th3) - np.cos(th1)*np.cos(th2)*np.cos(th3))) + np.sin(th5)*(np.cos(th1)*np.cos(th2)*np.sin(th3) + np.cos(th1)*np.cos(th3)*np.sin(th2)))
    R = math.acos(nxc/math.cos(P))
    azc = np.cos(th2 + th3)*np.cos(th5) - np.sin(th2 + th3)*np.cos(th4)*np.sin(th5)
    Ya = math.acos(azc/math.cos(P))
    
    Ya = Ya*180/math.pi
    R = R*180/math.pi
    P = P*180/math.pi
    
    
    return x, y, z, Ya, P, R

def angulosInversa(xf, yf, zf , Y, P, R):
    
    # Se da la longitud de los eslabones
    Y = Y*math.pi/180
    P = P*math.pi/180
    R = R*math.pi/180
    
    L1 = 83
    L2 = 190
    L3 = 50
    L4 = 172
    L5 = 88
    #####
    
    # Se construyen las matrices de rotacion
    Rx = np.array([[1,0,0],[0,math.cos(Y),-math.sin(Y)],[0,math.sin(Y),math.cos(Y)]])
    Ry = np.array([[math.cos(P),0,math.sin(P)],[0,1,0],[-math.sin(P),0,math.cos(P)]])
    Rz = np.array([[math.cos(R),-math.sin(R),0],[math.sin(R),math.cos(R),0],[0,0,1]])
    
    R = np.matmul(Rx,Ry)
    R = np.matmul(R,Rz)
    
    nx = R[0,0]
    ny = R[1,0]
    nz = R[2,0]
    sx = R[0,1]
    sy = R[1,1]
    sz = R[2,1]
    ax = R[0,2]
    ay = R[1,2]
    az = R[2,2]
    #####
    
    # distancia de origen a centro de muñeca
    dx = xf - L5*ax;
    dy = yf - L5*ay;
    dz = zf - L5*az;
    #####
    try:
        # Se calcula th1
        q1_1 = -2*cmath.atan((dx - (- L3**2 + dx**2 + dy**2)**(1/2))/(L3 + dy))
        q1_2 = -2*cmath.atan((dx + (- L3**2 + dx**2 + dy**2)**(1/2))/(L3 + dy))
        # q1_1 = -cmath.log(-(L3*1j - (L3**2 - dx**2 - dy**2)**(1/2)*1j)/(dx - dy*1j))*1j
        # q1_2 = -cmath.log(-(L3*1j + (L3**2 - dx**2 - dy**2)**(1/2)*1j)/(dx - dy*1j))*1j
        q1_1 = q1_1.real
        q1_2 = q1_2.real
        th1 = np.array([[q1_1],[q1_2]])
        #####
        
        # Se calculan th2
        r = th1.size
        th2 = list()
        for i in range(r):
            q1 = th1[i]
            q2_1 = -cmath.log((cmath.exp(-q1*1j)*(dx*dy*2j + 4*L1**2*cmath.exp(q1*2j) + 4*L2**2*cmath.exp(q1*2j) - 4*L4**2*cmath.exp(q1*2j) + 2*dx**2*cmath.exp(q1*2j) + dx**2*cmath.exp(q1*4j) + 2*dy**2*cmath.exp(q1*2j) - dy**2*cmath.exp(q1*4j) + 4*dz**2*cmath.exp(q1*2j) + dx**2 - dy**2 + ((dx*dy*2j + 4*L1**2*cmath.exp(q1*2j) + 4*L2**2*cmath.exp(q1*2j) - 4*L4**2*cmath.exp(q1*2j) + 2*dx**2*cmath.exp(q1*2j) + dx**2*cmath.exp(q1*4j) + 2*dy**2*cmath.exp(q1*2j) - dy**2*cmath.exp(q1*4j) + 4*dz**2*cmath.exp(q1*2j) + dx**2 - dy**2 - 8*L1*dz*cmath.exp(q1*2j) - dx*dy*cmath.exp(q1*4j)*2j)**2 - 16*L2**2*cmath.exp(q1*2j)*(dx + dy*1j - L1*cmath.exp(q1*1j)*2j + dx*cmath.exp(q1*2j) - dy*cmath.exp(q1*2j)*1j + dz*cmath.exp(q1*1j)*2j)*(dx + dy*1j + L1*cmath.exp(q1*1j)*2j + dx*cmath.exp(q1*2j) - dy*cmath.exp(q1*2j)*1j - dz*cmath.exp(q1*1j)*2j))**(1/2) - 8*L1*dz*cmath.exp(q1*2j) - dx*dy*cmath.exp(q1*4j)*2j))/(4*L2*(dx + dy*1j + L1*cmath.exp(q1*1j)*2j + dx*cmath.exp(q1*2j) - dy*cmath.exp(q1*2j)*1j - dz*cmath.exp(q1*1j)*2j)))*1j
            q2_2 = -cmath.log((cmath.exp(-q1*1j)*(dx*dy*2j + 4*L1**2*cmath.exp(q1*2j) + 4*L2**2*cmath.exp(q1*2j) - 4*L4**2*cmath.exp(q1*2j) + 2*dx**2*cmath.exp(q1*2j) + dx**2*cmath.exp(q1*4j) + 2*dy**2*cmath.exp(q1*2j) - dy**2*cmath.exp(q1*4j) + 4*dz**2*cmath.exp(q1*2j) + dx**2 - dy**2 - ((dx*dy*2j + 4*L1**2*cmath.exp(q1*2j) + 4*L2**2*cmath.exp(q1*2j) - 4*L4**2*cmath.exp(q1*2j) + 2*dx**2*cmath.exp(q1*2j) + dx**2*cmath.exp(q1*4j) + 2*dy**2*cmath.exp(q1*2j) - dy**2*cmath.exp(q1*4j) + 4*dz**2*cmath.exp(q1*2j) + dx**2 - dy**2 - 8*L1*dz*cmath.exp(q1*2j) - dx*dy*cmath.exp(q1*4j)*2j)**2 - 16*L2**2*cmath.exp(q1*2j)*(dx + dy*1j - L1*cmath.exp(q1*1j)*2j + dx*cmath.exp(q1*2j) - dy*cmath.exp(q1*2j)*1j + dz*cmath.exp(q1*1j)*2j)*(dx + dy*1j + L1*cmath.exp(q1*1j)*2j + dx*cmath.exp(q1*2j) - dy*cmath.exp(q1*2j)*1j - dz*cmath.exp(q1*1j)*2j))**(1/2) - 8*L1*dz*cmath.exp(q1*2j) - dx*dy*cmath.exp(q1*4j)*2j))/(4*L2*(dx + dy*1j + L1*cmath.exp(q1*1j)*2j + dx*cmath.exp(q1*2j) - dy*cmath.exp(q1*2j)*1j - dz*cmath.exp(q1*1j)*2j)))*1j
            q2_1 = q2_1.real
            q2_2 = q2_2.real
            th2.append(q2_1)
            th2.append(q2_2)
        th2 = np.array([th2]).T
        #####
        
        # Se calculan th3
        r = th1.size
        th3 = list()
        for i in range(r):
            q1 = th1[i]
            q3_1 = 2*math.pi + cmath.log((cmath.exp(-q1*1j)*(dx*dy*2j + 4*L1**2*cmath.exp(q1*2j) + 4*L2**2*cmath.exp(q1*2j) - 4*L4**2*cmath.exp(q1*2j) + 2*dx**2*cmath.exp(q1*2j) + dx**2*cmath.exp(q1*4j) + 2*dy**2*cmath.exp(q1*2j) - dy**2*cmath.exp(q1*4j) + 4*dz**2*cmath.exp(q1*2j) + dx**2 - dy**2 + ((dx*dy*2j + 4*L1**2*cmath.exp(q1*2j) + 4*L2**2*cmath.exp(q1*2j) - 4*L4**2*cmath.exp(q1*2j) + 2*dx**2*cmath.exp(q1*2j) + dx**2*cmath.exp(q1*4j) + 2*dy**2*cmath.exp(q1*2j) - dy**2*cmath.exp(q1*4j) + 4*dz**2*cmath.exp(q1*2j) + dx**2 - dy**2 - 8*L1*dz*cmath.exp(q1*2j) - dx*dy*cmath.exp(q1*4j)*2j)**2 - 16*L2**2*cmath.exp(q1*2j)*(dx + dy*1j - L1*cmath.exp(q1*1j)*2j + dx*cmath.exp(q1*2j) - dy*cmath.exp(q1*2j)*1j + dz*cmath.exp(q1*1j)*2j)*(dx + dy*1j + L1*cmath.exp(q1*1j)*2j + dx*cmath.exp(q1*2j) - dy*cmath.exp(q1*2j)*1j - dz*cmath.exp(q1*1j)*2j))**(1/2) - 8*L1*dz*cmath.exp(q1*2j) - dx*dy*cmath.exp(q1*4j)*2j))/(4*L2*(dx + dy*1j + L1*cmath.exp(q1*1j)*2j + dx*cmath.exp(q1*2j) - dy*cmath.exp(q1*2j)*1j - dz*cmath.exp(q1*1j)*2j)))*1j - cmath.acos((dz - L1 + L2*cmath.sin(cmath.log((cmath.exp(-q1*1j)*(dx*dy*2j + 4*L1**2*cmath.exp(q1*2j) + 4*L2**2*cmath.exp(q1*2j) - 4*L4**2*cmath.exp(q1*2j) + 2*dx**2*cmath.exp(q1*2j) + dx**2*cmath.exp(q1*4j) + 2*dy**2*cmath.exp(q1*2j) - dy**2*cmath.exp(q1*4j) + 4*dz**2*cmath.exp(q1*2j) + dx**2 - dy**2 + ((dx*dy*2j + 4*L1**2*cmath.exp(q1*2j) + 4*L2**2*cmath.exp(q1*2j) - 4*L4**2*cmath.exp(q1*2j) + 2*dx**2*cmath.exp(q1*2j) + dx**2*cmath.exp(q1*4j) + 2*dy**2*cmath.exp(q1*2j) - dy**2*cmath.exp(q1*4j) + 4*dz**2*cmath.exp(q1*2j) + dx**2 - dy**2 - 8*L1*dz*cmath.exp(q1*2j) - dx*dy*cmath.exp(q1*4j)*2j)**2 - 16*L2**2*cmath.exp(q1*2j)*(dx + dy*1j - L1*cmath.exp(q1*1j)*2j + dx*cmath.exp(q1*2j) - dy*cmath.exp(q1*2j)*1j + dz*cmath.exp(q1*1j)*2j)*(dx + dy*1j + L1*cmath.exp(q1*1j)*2j + dx*cmath.exp(q1*2j) - dy*cmath.exp(q1*2j)*1j - dz*cmath.exp(q1*1j)*2j))**(1/2) - 8*L1*dz*cmath.exp(q1*2j) - dx*dy*cmath.exp(q1*4j)*2j))/(4*L2*(dx + dy*1j + L1*cmath.exp(q1*1j)*2j + dx*cmath.exp(q1*2j) - dy*cmath.exp(q1*2j)*1j - dz*cmath.exp(q1*1j)*2j)))*1j))/L4)
            q3_2 = cmath.log((cmath.exp(-q1*1j)*(dx*dy*2j + 4*L1**2*cmath.exp(q1*2j) + 4*L2**2*cmath.exp(q1*2j) - 4*L4**2*cmath.exp(q1*2j) + 2*dx**2*cmath.exp(q1*2j) + dx**2*cmath.exp(q1*4j) + 2*dy**2*cmath.exp(q1*2j) - dy**2*cmath.exp(q1*4j) + 4*dz**2*cmath.exp(q1*2j) + dx**2 - dy**2 + ((dx*dy*2j + 4*L1**2*cmath.exp(q1*2j) + 4*L2**2*cmath.exp(q1*2j) - 4*L4**2*cmath.exp(q1*2j) + 2*dx**2*cmath.exp(q1*2j) + dx**2*cmath.exp(q1*4j) + 2*dy**2*cmath.exp(q1*2j) - dy**2*cmath.exp(q1*4j) + 4*dz**2*cmath.exp(q1*2j) + dx**2 - dy**2 - 8*L1*dz*cmath.exp(q1*2j) - dx*dy*cmath.exp(q1*4j)*2j)**2 - 16*L2**2*cmath.exp(q1*2j)*(dx + dy*1j - L1*cmath.exp(q1*1j)*2j + dx*cmath.exp(q1*2j) - dy*cmath.exp(q1*2j)*1j + dz*cmath.exp(q1*1j)*2j)*(dx + dy*1j + L1*cmath.exp(q1*1j)*2j + dx*cmath.exp(q1*2j) - dy*cmath.exp(q1*2j)*1j - dz*cmath.exp(q1*1j)*2j))**(1/2) - 8*L1*dz*cmath.exp(q1*2j) - dx*dy*cmath.exp(q1*4j)*2j))/(4*L2*(dx + dy*1j + L1*cmath.exp(q1*1j)*2j + dx*cmath.exp(q1*2j) - dy*cmath.exp(q1*2j)*1j - dz*cmath.exp(q1*1j)*2j)))*1j + cmath.acos((dz - L1 + L2*cmath.sin(cmath.log((cmath.exp(-q1*1j)*(dx*dy*2j + 4*L1**2*cmath.exp(q1*2j) + 4*L2**2*cmath.exp(q1*2j) - 4*L4**2*cmath.exp(q1*2j) + 2*dx**2*cmath.exp(q1*2j) + dx**2*cmath.exp(q1*4j) + 2*dy**2*cmath.exp(q1*2j) - dy**2*cmath.exp(q1*4j) + 4*dz**2*cmath.exp(q1*2j) + dx**2 - dy**2 + ((dx*dy*2j + 4*L1**2*cmath.exp(q1*2j) + 4*L2**2*cmath.exp(q1*2j) - 4*L4**2*cmath.exp(q1*2j) + 2*dx**2*cmath.exp(q1*2j) + dx**2*cmath.exp(q1*4j) + 2*dy**2*cmath.exp(q1*2j) - dy**2*cmath.exp(q1*4j) + 4*dz**2*cmath.exp(q1*2j) + dx**2 - dy**2 - 8*L1*dz*cmath.exp(q1*2j) - dx*dy*cmath.exp(q1*4j)*2j)**2 - 16*L2**2*cmath.exp(q1*2j)*(dx + dy*1j - L1*cmath.exp(q1*1j)*2j + dx*cmath.exp(q1*2j) - dy*cmath.exp(q1*2j)*1j + dz*cmath.exp(q1*1j)*2j)*(dx + dy*1j + L1*cmath.exp(q1*1j)*2j + dx*cmath.exp(q1*2j) - dy*cmath.exp(q1*2j)*1j - dz*cmath.exp(q1*1j)*2j))**(1/2) - 8*L1*dz*cmath.exp(q1*2j) - dx*dy*cmath.exp(q1*4j)*2j))/(4*L2*(dx + dy*1j + L1*cmath.exp(q1*1j)*2j + dx*cmath.exp(q1*2j) - dy*cmath.exp(q1*2j)*1j - dz*cmath.exp(q1*1j)*2j)))*1j))/L4)
            q3_3 = 2*math.pi + cmath.log((cmath.exp(-q1*1j)*(dx*dy*2j + 4*L1**2*cmath.exp(q1*2j) + 4*L2**2*cmath.exp(q1*2j) - 4*L4**2*cmath.exp(q1*2j) + 2*dx**2*cmath.exp(q1*2j) + dx**2*cmath.exp(q1*4j) + 2*dy**2*cmath.exp(q1*2j) - dy**2*cmath.exp(q1*4j) + 4*dz**2*cmath.exp(q1*2j) + dx**2 - dy**2 - ((dx*dy*2j + 4*L1**2*cmath.exp(q1*2j) + 4*L2**2*cmath.exp(q1*2j) - 4*L4**2*cmath.exp(q1*2j) + 2*dx**2*cmath.exp(q1*2j) + dx**2*cmath.exp(q1*4j) + 2*dy**2*cmath.exp(q1*2j) - dy**2*cmath.exp(q1*4j) + 4*dz**2*cmath.exp(q1*2j) + dx**2 - dy**2 - 8*L1*dz*cmath.exp(q1*2j) - dx*dy*cmath.exp(q1*4j)*2j)**2 - 16*L2**2*cmath.exp(q1*2j)*(dx + dy*1j - L1*cmath.exp(q1*1j)*2j + dx*cmath.exp(q1*2j) - dy*cmath.exp(q1*2j)*1j + dz*cmath.exp(q1*1j)*2j)*(dx + dy*1j + L1*cmath.exp(q1*1j)*2j + dx*cmath.exp(q1*2j) - dy*cmath.exp(q1*2j)*1j - dz*cmath.exp(q1*1j)*2j))**(1/2) - 8*L1*dz*cmath.exp(q1*2j) - dx*dy*cmath.exp(q1*4j)*2j))/(4*L2*(dx + dy*1j + L1*cmath.exp(q1*1j)*2j + dx*cmath.exp(q1*2j) - dy*cmath.exp(q1*2j)*1j - dz*cmath.exp(q1*1j)*2j)))*1j - cmath.acos((dz - L1 + L2*cmath.sin(cmath.log((cmath.exp(-q1*1j)*(dx*dy*2j + 4*L1**2*cmath.exp(q1*2j) + 4*L2**2*cmath.exp(q1*2j) - 4*L4**2*cmath.exp(q1*2j) + 2*dx**2*cmath.exp(q1*2j) + dx**2*cmath.exp(q1*4j) + 2*dy**2*cmath.exp(q1*2j) - dy**2*cmath.exp(q1*4j) + 4*dz**2*cmath.exp(q1*2j) + dx**2 - dy**2 - ((dx*dy*2j + 4*L1**2*cmath.exp(q1*2j) + 4*L2**2*cmath.exp(q1*2j) - 4*L4**2*cmath.exp(q1*2j) + 2*dx**2*cmath.exp(q1*2j) + dx**2*cmath.exp(q1*4j) + 2*dy**2*cmath.exp(q1*2j) - dy**2*cmath.exp(q1*4j) + 4*dz**2*cmath.exp(q1*2j) + dx**2 - dy**2 - 8*L1*dz*cmath.exp(q1*2j) - dx*dy*cmath.exp(q1*4j)*2j)**2 - 16*L2**2*cmath.exp(q1*2j)*(dx + dy*1j - L1*cmath.exp(q1*1j)*2j + dx*cmath.exp(q1*2j) - dy*cmath.exp(q1*2j)*1j + dz*cmath.exp(q1*1j)*2j)*(dx + dy*1j + L1*cmath.exp(q1*1j)*2j + dx*cmath.exp(q1*2j) - dy*cmath.exp(q1*2j)*1j - dz*cmath.exp(q1*1j)*2j))**(1/2) - 8*L1*dz*cmath.exp(q1*2j) - dx*dy*cmath.exp(q1*4j)*2j))/(4*L2*(dx + dy*1j + L1*cmath.exp(q1*1j)*2j + dx*cmath.exp(q1*2j) - dy*cmath.exp(q1*2j)*1j - dz*cmath.exp(q1*1j)*2j)))*1j))/L4)
            q3_4 = cmath.log((cmath.exp(-q1*1j)*(dx*dy*2j + 4*L1**2*cmath.exp(q1*2j) + 4*L2**2*cmath.exp(q1*2j) - 4*L4**2*cmath.exp(q1*2j) + 2*dx**2*cmath.exp(q1*2j) + dx**2*cmath.exp(q1*4j) + 2*dy**2*cmath.exp(q1*2j) - dy**2*cmath.exp(q1*4j) + 4*dz**2*cmath.exp(q1*2j) + dx**2 - dy**2 - ((dx*dy*2j + 4*L1**2*cmath.exp(q1*2j) + 4*L2**2*cmath.exp(q1*2j) - 4*L4**2*cmath.exp(q1*2j) + 2*dx**2*cmath.exp(q1*2j) + dx**2*cmath.exp(q1*4j) + 2*dy**2*cmath.exp(q1*2j) - dy**2*cmath.exp(q1*4j) + 4*dz**2*cmath.exp(q1*2j) + dx**2 - dy**2 - 8*L1*dz*cmath.exp(q1*2j) - dx*dy*cmath.exp(q1*4j)*2j)**2 - 16*L2**2*cmath.exp(q1*2j)*(dx + dy*1j - L1*cmath.exp(q1*1j)*2j + dx*cmath.exp(q1*2j) - dy*cmath.exp(q1*2j)*1j + dz*cmath.exp(q1*1j)*2j)*(dx + dy*1j + L1*cmath.exp(q1*1j)*2j + dx*cmath.exp(q1*2j) - dy*cmath.exp(q1*2j)*1j - dz*cmath.exp(q1*1j)*2j))**(1/2) - 8*L1*dz*cmath.exp(q1*2j) - dx*dy*cmath.exp(q1*4j)*2j))/(4*L2*(dx + dy*1j + L1*cmath.exp(q1*1j)*2j + dx*cmath.exp(q1*2j) - dy*cmath.exp(q1*2j)*1j - dz*cmath.exp(q1*1j)*2j)))*1j + cmath.acos((dz - L1 + L2*cmath.sin(cmath.log((cmath.exp(-q1*1j)*(dx*dy*2j + 4*L1**2*cmath.exp(q1*2j) + 4*L2**2*cmath.exp(q1*2j) - 4*L4**2*cmath.exp(q1*2j) + 2*dx**2*cmath.exp(q1*2j) + dx**2*cmath.exp(q1*4j) + 2*dy**2*cmath.exp(q1*2j) - dy**2*cmath.exp(q1*4j) + 4*dz**2*cmath.exp(q1*2j) + dx**2 - dy**2 - ((dx*dy*2j + 4*L1**2*cmath.exp(q1*2j) + 4*L2**2*cmath.exp(q1*2j) - 4*L4**2*cmath.exp(q1*2j) + 2*dx**2*cmath.exp(q1*2j) + dx**2*cmath.exp(q1*4j) + 2*dy**2*cmath.exp(q1*2j) - dy**2*cmath.exp(q1*4j) + 4*dz**2*cmath.exp(q1*2j) + dx**2 - dy**2 - 8*L1*dz*cmath.exp(q1*2j) - dx*dy*cmath.exp(q1*4j)*2j)**2 - 16*L2**2*cmath.exp(q1*2j)*(dx + dy*1j - L1*cmath.exp(q1*1j)*2j + dx*cmath.exp(q1*2j) - dy*cmath.exp(q1*2j)*1j + dz*cmath.exp(q1*1j)*2j)*(dx + dy*1j + L1*cmath.exp(q1*1j)*2j + dx*cmath.exp(q1*2j) - dy*cmath.exp(q1*2j)*1j - dz*cmath.exp(q1*1j)*2j))**(1/2) - 8*L1*dz*cmath.exp(q1*2j) - dx*dy*cmath.exp(q1*4j)*2j))/(4*L2*(dx + dy*1j + L1*cmath.exp(q1*1j)*2j + dx*cmath.exp(q1*2j) - dy*cmath.exp(q1*2j)*1j - dz*cmath.exp(q1*1j)*2j)))*1j))/L4)
            q3_1 = q3_1.real
            q3_2 = q3_2.real
            q3_3 = q3_3.real
            q3_4 = q3_4.real
            th3.append(q3_1)
            th3.append(q3_2)
            th3.append(q3_3)
            th3.append(q3_4)
        th3 = np.array([th3]).T
        #####
        
        # Se construye la matriz de combinaciones de th1 th2 y th3
        th1 = np.repeat(th1,4,axis=0)
        th2 = np.repeat(th2,2,axis=0)
        
        q = np.append(th1,th2,axis=1)
        q = np.append(q,th3,axis=1)
        #####
        
        # Se calcula th4
        r = q.shape[0]
        th4 = list()
        for i in range(r):
            q1 = th1[i]
            q2 = th2[i]
            q3 = th3[i]
            q4_1 = -cmath.log((ax*ay*2j + 2*ax**2*cmath.exp(q1*2j) + ax**2*cmath.exp(q1*4j) + 2*ay**2*cmath.exp(q1*2j) - ay**2*cmath.exp(q1*4j) - 4*az**2*cmath.exp(q1*2j) + ax**2 - ay**2 - ax*ay*cmath.exp(q1*4j)*2j + ax*az*cmath.exp(q1*1j)*4j + ax*az*cmath.exp(q1*3j)*4j - 4*ay*az*cmath.exp(q1*1j) + 4*ay*az*cmath.exp(q1*3j) - 2*ax**2*cmath.exp(q2*2j)*cmath.exp(q3*2j) + ax**2*cmath.exp(q2*4j)*cmath.exp(q3*4j) + 2*ay**2*cmath.exp(q2*2j)*cmath.exp(q3*2j) - ay**2*cmath.exp(q2*4j)*cmath.exp(q3*4j) - ax*ay*cmath.exp(q2*2j)*cmath.exp(q3*2j)*4j + ax*ay*cmath.exp(q2*4j)*cmath.exp(q3*4j)*2j + 12*ax**2*cmath.exp(q1*2j)*cmath.exp(q2*2j)*cmath.exp(q3*2j) - 2*ax**2*cmath.exp(q2*2j)*cmath.exp(q1*4j)*cmath.exp(q3*2j) + 2*ax**2*cmath.exp(q1*2j)*cmath.exp(q2*4j)*cmath.exp(q3*4j) + ax**2*cmath.exp(q1*4j)*cmath.exp(q2*4j)*cmath.exp(q3*4j) + 12*ay**2*cmath.exp(q1*2j)*cmath.exp(q2*2j)*cmath.exp(q3*2j) + 2*ay**2*cmath.exp(q2*2j)*cmath.exp(q1*4j)*cmath.exp(q3*2j) + 2*ay**2*cmath.exp(q1*2j)*cmath.exp(q2*4j)*cmath.exp(q3*4j) - ay**2*cmath.exp(q1*4j)*cmath.exp(q2*4j)*cmath.exp(q3*4j) + 8*az**2*cmath.exp(q1*2j)*cmath.exp(q2*2j)*cmath.exp(q3*2j) - 4*az**2*cmath.exp(q1*2j)*cmath.exp(q2*4j)*cmath.exp(q3*4j) + ax*ay*cmath.exp(q2*2j)*cmath.exp(q1*4j)*cmath.exp(q3*2j)*4j - ax*ay*cmath.exp(q1*4j)*cmath.exp(q2*4j)*cmath.exp(q3*4j)*2j - ax*az*cmath.exp(q1*1j)*cmath.exp(q2*4j)*cmath.exp(q3*4j)*4j - ax*az*cmath.exp(q1*3j)*cmath.exp(q2*4j)*cmath.exp(q3*4j)*4j + 4*ay*az*cmath.exp(q1*1j)*cmath.exp(q2*4j)*cmath.exp(q3*4j) - 4*ay*az*cmath.exp(q1*3j)*cmath.exp(q2*4j)*cmath.exp(q3*4j))**(1/2)/(ax + ay*1j + ax*cmath.exp(q1*2j) - ay*cmath.exp(q1*2j)*1j + az*cmath.exp(q1*1j)*2j - 2*ax*cmath.exp(q2*1j)*cmath.exp(q3*1j) + ax*cmath.exp(q2*2j)*cmath.exp(q3*2j) - ay*cmath.exp(q2*1j)*cmath.exp(q3*1j)*2j + ay*cmath.exp(q2*2j)*cmath.exp(q3*2j)*1j + 2*ax*cmath.exp(q1*2j)*cmath.exp(q2*1j)*cmath.exp(q3*1j) + ax*cmath.exp(q1*2j)*cmath.exp(q2*2j)*cmath.exp(q3*2j) - ay*cmath.exp(q1*2j)*cmath.exp(q2*1j)*cmath.exp(q3*1j)*2j - ay*cmath.exp(q1*2j)*cmath.exp(q2*2j)*cmath.exp(q3*2j)*1j - az*cmath.exp(q1*1j)*cmath.exp(q2*2j)*cmath.exp(q3*2j)*2j))*1j
            q4_2 = -cmath.log(-(ax*ay*2j + 2*ax**2*cmath.exp(q1*2j) + ax**2*cmath.exp(q1*4j) + 2*ay**2*cmath.exp(q1*2j) - ay**2*cmath.exp(q1*4j) - 4*az**2*cmath.exp(q1*2j) + ax**2 - ay**2 - ax*ay*cmath.exp(q1*4j)*2j + ax*az*cmath.exp(q1*1j)*4j + ax*az*cmath.exp(q1*3j)*4j - 4*ay*az*cmath.exp(q1*1j) + 4*ay*az*cmath.exp(q1*3j) - 2*ax**2*cmath.exp(q2*2j)*cmath.exp(q3*2j) + ax**2*cmath.exp(q2*4j)*cmath.exp(q3*4j) + 2*ay**2*cmath.exp(q2*2j)*cmath.exp(q3*2j) - ay**2*cmath.exp(q2*4j)*cmath.exp(q3*4j) - ax*ay*cmath.exp(q2*2j)*cmath.exp(q3*2j)*4j + ax*ay*cmath.exp(q2*4j)*cmath.exp(q3*4j)*2j + 12*ax**2*cmath.exp(q1*2j)*cmath.exp(q2*2j)*cmath.exp(q3*2j) - 2*ax**2*cmath.exp(q2*2j)*cmath.exp(q1*4j)*cmath.exp(q3*2j) + 2*ax**2*cmath.exp(q1*2j)*cmath.exp(q2*4j)*cmath.exp(q3*4j) + ax**2*cmath.exp(q1*4j)*cmath.exp(q2*4j)*cmath.exp(q3*4j) + 12*ay**2*cmath.exp(q1*2j)*cmath.exp(q2*2j)*cmath.exp(q3*2j) + 2*ay**2*cmath.exp(q2*2j)*cmath.exp(q1*4j)*cmath.exp(q3*2j) + 2*ay**2*cmath.exp(q1*2j)*cmath.exp(q2*4j)*cmath.exp(q3*4j) - ay**2*cmath.exp(q1*4j)*cmath.exp(q2*4j)*cmath.exp(q3*4j) + 8*az**2*cmath.exp(q1*2j)*cmath.exp(q2*2j)*cmath.exp(q3*2j) - 4*az**2*cmath.exp(q1*2j)*cmath.exp(q2*4j)*cmath.exp(q3*4j) + ax*ay*cmath.exp(q2*2j)*cmath.exp(q1*4j)*cmath.exp(q3*2j)*4j - ax*ay*cmath.exp(q1*4j)*cmath.exp(q2*4j)*cmath.exp(q3*4j)*2j - ax*az*cmath.exp(q1*1j)*cmath.exp(q2*4j)*cmath.exp(q3*4j)*4j - ax*az*cmath.exp(q1*3j)*cmath.exp(q2*4j)*cmath.exp(q3*4j)*4j + 4*ay*az*cmath.exp(q1*1j)*cmath.exp(q2*4j)*cmath.exp(q3*4j) - 4*ay*az*cmath.exp(q1*3j)*cmath.exp(q2*4j)*cmath.exp(q3*4j))**(1/2)/(ax + ay*1j + ax*cmath.exp(q1*2j) - ay*cmath.exp(q1*2j)*1j + az*cmath.exp(q1*1j)*2j - 2*ax*cmath.exp(q2*1j)*cmath.exp(q3*1j) + ax*cmath.exp(q2*2j)*cmath.exp(q3*2j) - ay*cmath.exp(q2*1j)*cmath.exp(q3*1j)*2j + ay*cmath.exp(q2*2j)*cmath.exp(q3*2j)*1j + 2*ax*cmath.exp(q1*2j)*cmath.exp(q2*1j)*cmath.exp(q3*1j) + ax*cmath.exp(q1*2j)*cmath.exp(q2*2j)*cmath.exp(q3*2j) - ay*cmath.exp(q1*2j)*cmath.exp(q2*1j)*cmath.exp(q3*1j)*2j - ay*cmath.exp(q1*2j)*cmath.exp(q2*2j)*cmath.exp(q3*2j)*1j - az*cmath.exp(q1*1j)*cmath.exp(q2*2j)*cmath.exp(q3*2j)*2j))*1j
            q4_1 = q4_1.real
            q4_2 = q4_2.real
            th4.append(q4_1)
            th4.append(q4_2)
        th4 = np.array([th4]).T
        #####
        
        # Se construye la matriz de combinaciones de th1 th2 y th3
        q = np.repeat(q,2,axis=0)
        
        q = np.append(q,th4,axis=1)
        #####
        
        # Se calcula th5
        r = q.shape[0]
        th5 = list()
        for i in range(r):
            q1 = q[i,0]
            q2 = q[i,1]
            q3 = q[i,2]
            q4 = q[i,3]
            q5_1 = cmath.acos((ny**2*cmath.cos(q1)**2*cmath.sin(q4)**2 + sy**2*cmath.cos(q1)**2*cmath.sin(q4)**2 + nx**2*cmath.sin(q1)**2*cmath.sin(q4)**2 + sx**2*cmath.sin(q1)**2*cmath.sin(q4)**2 + nz**2*cmath.cos(q2)**2*cmath.cos(q4)**2*cmath.sin(q3)**2 + nz**2*cmath.cos(q3)**2*cmath.cos(q4)**2*cmath.sin(q2)**2 + sz**2*cmath.cos(q2)**2*cmath.cos(q4)**2*cmath.sin(q3)**2 + sz**2*cmath.cos(q3)**2*cmath.cos(q4)**2*cmath.sin(q2)**2 + nx**2*cmath.cos(q1)**2*cmath.cos(q2)**2*cmath.cos(q3)**2*cmath.cos(q4)**2 + sx**2*cmath.cos(q1)**2*cmath.cos(q2)**2*cmath.cos(q3)**2*cmath.cos(q4)**2 + ny**2*cmath.cos(q2)**2*cmath.cos(q3)**2*cmath.cos(q4)**2*cmath.sin(q1)**2 + sy**2*cmath.cos(q2)**2*cmath.cos(q3)**2*cmath.cos(q4)**2*cmath.sin(q1)**2 + nx**2*cmath.cos(q1)**2*cmath.cos(q4)**2*cmath.sin(q2)**2*cmath.sin(q3)**2 + sx**2*cmath.cos(q1)**2*cmath.cos(q4)**2*cmath.sin(q2)**2*cmath.sin(q3)**2 + ny**2*cmath.cos(q4)**2*cmath.sin(q1)**2*cmath.sin(q2)**2*cmath.sin(q3)**2 + sy**2*cmath.cos(q4)**2*cmath.sin(q1)**2*cmath.sin(q2)**2*cmath.sin(q3)**2 - 2*nx*ny*cmath.cos(q1)*cmath.sin(q1)*cmath.sin(q4)**2 - 2*sx*sy*cmath.cos(q1)*cmath.sin(q1)*cmath.sin(q4)**2 + 2*nz**2*cmath.cos(q2)*cmath.cos(q3)*cmath.cos(q4)**2*cmath.sin(q2)*cmath.sin(q3) + 2*sz**2*cmath.cos(q2)*cmath.cos(q3)*cmath.cos(q4)**2*cmath.sin(q2)*cmath.sin(q3) - 2*nx*ny*cmath.cos(q1)**2*cmath.cos(q4)*cmath.sin(q2)*cmath.sin(q3)*cmath.sin(q4) - 2*sx*sy*cmath.cos(q1)**2*cmath.cos(q4)*cmath.sin(q2)*cmath.sin(q3)*cmath.sin(q4) + 2*nx*ny*cmath.cos(q4)*cmath.sin(q1)**2*cmath.sin(q2)*cmath.sin(q3)*cmath.sin(q4) - 2*nx**2*cmath.cos(q1)**2*cmath.cos(q2)*cmath.cos(q3)*cmath.cos(q4)**2*cmath.sin(q2)*cmath.sin(q3) + 2*sx*sy*cmath.cos(q4)*cmath.sin(q1)**2*cmath.sin(q2)*cmath.sin(q3)*cmath.sin(q4) - 2*sx**2*cmath.cos(q1)**2*cmath.cos(q2)*cmath.cos(q3)*cmath.cos(q4)**2*cmath.sin(q2)*cmath.sin(q3) - 2*ny**2*cmath.cos(q2)*cmath.cos(q3)*cmath.cos(q4)**2*cmath.sin(q1)**2*cmath.sin(q2)*cmath.sin(q3) - 2*sy**2*cmath.cos(q2)*cmath.cos(q3)*cmath.cos(q4)**2*cmath.sin(q1)**2*cmath.sin(q2)*cmath.sin(q3) + 2*nx*nz*cmath.cos(q1)*cmath.cos(q2)*cmath.cos(q3)**2*cmath.cos(q4)**2*cmath.sin(q2) + 2*nx*nz*cmath.cos(q1)*cmath.cos(q2)**2*cmath.cos(q3)*cmath.cos(q4)**2*cmath.sin(q3) + 2*sx*sz*cmath.cos(q1)*cmath.cos(q2)*cmath.cos(q3)**2*cmath.cos(q4)**2*cmath.sin(q2) + 2*sx*sz*cmath.cos(q1)*cmath.cos(q2)**2*cmath.cos(q3)*cmath.cos(q4)**2*cmath.sin(q3) - 2*nx*nz*cmath.cos(q1)*cmath.cos(q2)*cmath.cos(q4)**2*cmath.sin(q2)*cmath.sin(q3)**2 - 2*nx*nz*cmath.cos(q1)*cmath.cos(q3)*cmath.cos(q4)**2*cmath.sin(q2)**2*cmath.sin(q3) + 2*ny*nz*cmath.cos(q2)*cmath.cos(q3)**2*cmath.cos(q4)**2*cmath.sin(q1)*cmath.sin(q2) + 2*ny*nz*cmath.cos(q2)**2*cmath.cos(q3)*cmath.cos(q4)**2*cmath.sin(q1)*cmath.sin(q3) - 2*nx**2*cmath.cos(q1)*cmath.cos(q2)*cmath.cos(q3)*cmath.cos(q4)*cmath.sin(q1)*cmath.sin(q4) + 2*ny**2*cmath.cos(q1)*cmath.cos(q2)*cmath.cos(q3)*cmath.cos(q4)*cmath.sin(q1)*cmath.sin(q4) - 2*sx*sz*cmath.cos(q1)*cmath.cos(q2)*cmath.cos(q4)**2*cmath.sin(q2)*cmath.sin(q3)**2 - 2*sx*sz*cmath.cos(q1)*cmath.cos(q3)*cmath.cos(q4)**2*cmath.sin(q2)**2*cmath.sin(q3) + 2*sy*sz*cmath.cos(q2)*cmath.cos(q3)**2*cmath.cos(q4)**2*cmath.sin(q1)*cmath.sin(q2) + 2*sy*sz*cmath.cos(q2)**2*cmath.cos(q3)*cmath.cos(q4)**2*cmath.sin(q1)*cmath.sin(q3) - 2*sx**2*cmath.cos(q1)*cmath.cos(q2)*cmath.cos(q3)*cmath.cos(q4)*cmath.sin(q1)*cmath.sin(q4) + 2*sy**2*cmath.cos(q1)*cmath.cos(q2)*cmath.cos(q3)*cmath.cos(q4)*cmath.sin(q1)*cmath.sin(q4) - 2*ny*nz*cmath.cos(q2)*cmath.cos(q4)**2*cmath.sin(q1)*cmath.sin(q2)*cmath.sin(q3)**2 - 2*ny*nz*cmath.cos(q3)*cmath.cos(q4)**2*cmath.sin(q1)*cmath.sin(q2)**2*cmath.sin(q3) - 2*sy*sz*cmath.cos(q2)*cmath.cos(q4)**2*cmath.sin(q1)*cmath.sin(q2)*cmath.sin(q3)**2 - 2*sy*sz*cmath.cos(q3)*cmath.cos(q4)**2*cmath.sin(q1)*cmath.sin(q2)**2*cmath.sin(q3) + 2*nx**2*cmath.cos(q1)*cmath.cos(q4)*cmath.sin(q1)*cmath.sin(q2)*cmath.sin(q3)*cmath.sin(q4) - 2*ny**2*cmath.cos(q1)*cmath.cos(q4)*cmath.sin(q1)*cmath.sin(q2)*cmath.sin(q3)*cmath.sin(q4) + 2*sx**2*cmath.cos(q1)*cmath.cos(q4)*cmath.sin(q1)*cmath.sin(q2)*cmath.sin(q3)*cmath.sin(q4) - 2*sy**2*cmath.cos(q1)*cmath.cos(q4)*cmath.sin(q1)*cmath.sin(q2)*cmath.sin(q3)*cmath.sin(q4) + 2*ny*nz*cmath.cos(q1)*cmath.cos(q2)*cmath.cos(q4)*cmath.sin(q3)*cmath.sin(q4) + 2*ny*nz*cmath.cos(q1)*cmath.cos(q3)*cmath.cos(q4)*cmath.sin(q2)*cmath.sin(q4) + 2*sy*sz*cmath.cos(q1)*cmath.cos(q2)*cmath.cos(q4)*cmath.sin(q3)*cmath.sin(q4) + 2*sy*sz*cmath.cos(q1)*cmath.cos(q3)*cmath.cos(q4)*cmath.sin(q2)*cmath.sin(q4) + 2*nx*ny*cmath.cos(q1)*cmath.cos(q2)**2*cmath.cos(q3)**2*cmath.cos(q4)**2*cmath.sin(q1) - 2*nx*nz*cmath.cos(q2)*cmath.cos(q4)*cmath.sin(q1)*cmath.sin(q3)*cmath.sin(q4) - 2*nx*nz*cmath.cos(q3)*cmath.cos(q4)*cmath.sin(q1)*cmath.sin(q2)*cmath.sin(q4) + 2*sx*sy*cmath.cos(q1)*cmath.cos(q2)**2*cmath.cos(q3)**2*cmath.cos(q4)**2*cmath.sin(q1) - 2*sx*sz*cmath.cos(q2)*cmath.cos(q4)*cmath.sin(q1)*cmath.sin(q3)*cmath.sin(q4) - 2*sx*sz*cmath.cos(q3)*cmath.cos(q4)*cmath.sin(q1)*cmath.sin(q2)*cmath.sin(q4) + 2*nx*ny*cmath.cos(q1)*cmath.cos(q4)**2*cmath.sin(q1)*cmath.sin(q2)**2*cmath.sin(q3)**2 + 2*sx*sy*cmath.cos(q1)*cmath.cos(q4)**2*cmath.sin(q1)*cmath.sin(q2)**2*cmath.sin(q3)**2 + 2*nx*ny*cmath.cos(q1)**2*cmath.cos(q2)*cmath.cos(q3)*cmath.cos(q4)*cmath.sin(q4) + 2*sx*sy*cmath.cos(q1)**2*cmath.cos(q2)*cmath.cos(q3)*cmath.cos(q4)*cmath.sin(q4) - 2*nx*ny*cmath.cos(q2)*cmath.cos(q3)*cmath.cos(q4)*cmath.sin(q1)**2*cmath.sin(q4) - 2*sx*sy*cmath.cos(q2)*cmath.cos(q3)*cmath.cos(q4)*cmath.sin(q1)**2*cmath.sin(q4) - 4*nx*ny*cmath.cos(q1)*cmath.cos(q2)*cmath.cos(q3)*cmath.cos(q4)**2*cmath.sin(q1)*cmath.sin(q2)*cmath.sin(q3) - 4*sx*sy*cmath.cos(q1)*cmath.cos(q2)*cmath.cos(q3)*cmath.cos(q4)**2*cmath.sin(q1)*cmath.sin(q2)*cmath.sin(q3))**(1/2))
            q5_2 = -cmath.acos((ny**2*cmath.cos(q1)**2*cmath.sin(q4)**2 + sy**2*cmath.cos(q1)**2*cmath.sin(q4)**2 + nx**2*cmath.sin(q1)**2*cmath.sin(q4)**2 + sx**2*cmath.sin(q1)**2*cmath.sin(q4)**2 + nz**2*cmath.cos(q2)**2*cmath.cos(q4)**2*cmath.sin(q3)**2 + nz**2*cmath.cos(q3)**2*cmath.cos(q4)**2*cmath.sin(q2)**2 + sz**2*cmath.cos(q2)**2*cmath.cos(q4)**2*cmath.sin(q3)**2 + sz**2*cmath.cos(q3)**2*cmath.cos(q4)**2*cmath.sin(q2)**2 + nx**2*cmath.cos(q1)**2*cmath.cos(q2)**2*cmath.cos(q3)**2*cmath.cos(q4)**2 + sx**2*cmath.cos(q1)**2*cmath.cos(q2)**2*cmath.cos(q3)**2*cmath.cos(q4)**2 + ny**2*cmath.cos(q2)**2*cmath.cos(q3)**2*cmath.cos(q4)**2*cmath.sin(q1)**2 + sy**2*cmath.cos(q2)**2*cmath.cos(q3)**2*cmath.cos(q4)**2*cmath.sin(q1)**2 + nx**2*cmath.cos(q1)**2*cmath.cos(q4)**2*cmath.sin(q2)**2*cmath.sin(q3)**2 + sx**2*cmath.cos(q1)**2*cmath.cos(q4)**2*cmath.sin(q2)**2*cmath.sin(q3)**2 + ny**2*cmath.cos(q4)**2*cmath.sin(q1)**2*cmath.sin(q2)**2*cmath.sin(q3)**2 + sy**2*cmath.cos(q4)**2*cmath.sin(q1)**2*cmath.sin(q2)**2*cmath.sin(q3)**2 - 2*nx*ny*cmath.cos(q1)*cmath.sin(q1)*cmath.sin(q4)**2 - 2*sx*sy*cmath.cos(q1)*cmath.sin(q1)*cmath.sin(q4)**2 + 2*nz**2*cmath.cos(q2)*cmath.cos(q3)*cmath.cos(q4)**2*cmath.sin(q2)*cmath.sin(q3) + 2*sz**2*cmath.cos(q2)*cmath.cos(q3)*cmath.cos(q4)**2*cmath.sin(q2)*cmath.sin(q3) - 2*nx*ny*cmath.cos(q1)**2*cmath.cos(q4)*cmath.sin(q2)*cmath.sin(q3)*cmath.sin(q4) - 2*sx*sy*cmath.cos(q1)**2*cmath.cos(q4)*cmath.sin(q2)*cmath.sin(q3)*cmath.sin(q4) + 2*nx*ny*cmath.cos(q4)*cmath.sin(q1)**2*cmath.sin(q2)*cmath.sin(q3)*cmath.sin(q4) - 2*nx**2*cmath.cos(q1)**2*cmath.cos(q2)*cmath.cos(q3)*cmath.cos(q4)**2*cmath.sin(q2)*cmath.sin(q3) + 2*sx*sy*cmath.cos(q4)*cmath.sin(q1)**2*cmath.sin(q2)*cmath.sin(q3)*cmath.sin(q4) - 2*sx**2*cmath.cos(q1)**2*cmath.cos(q2)*cmath.cos(q3)*cmath.cos(q4)**2*cmath.sin(q2)*cmath.sin(q3) - 2*ny**2*cmath.cos(q2)*cmath.cos(q3)*cmath.cos(q4)**2*cmath.sin(q1)**2*cmath.sin(q2)*cmath.sin(q3) - 2*sy**2*cmath.cos(q2)*cmath.cos(q3)*cmath.cos(q4)**2*cmath.sin(q1)**2*cmath.sin(q2)*cmath.sin(q3) + 2*nx*nz*cmath.cos(q1)*cmath.cos(q2)*cmath.cos(q3)**2*cmath.cos(q4)**2*cmath.sin(q2) + 2*nx*nz*cmath.cos(q1)*cmath.cos(q2)**2*cmath.cos(q3)*cmath.cos(q4)**2*cmath.sin(q3) + 2*sx*sz*cmath.cos(q1)*cmath.cos(q2)*cmath.cos(q3)**2*cmath.cos(q4)**2*cmath.sin(q2) + 2*sx*sz*cmath.cos(q1)*cmath.cos(q2)**2*cmath.cos(q3)*cmath.cos(q4)**2*cmath.sin(q3) - 2*nx*nz*cmath.cos(q1)*cmath.cos(q2)*cmath.cos(q4)**2*cmath.sin(q2)*cmath.sin(q3)**2 - 2*nx*nz*cmath.cos(q1)*cmath.cos(q3)*cmath.cos(q4)**2*cmath.sin(q2)**2*cmath.sin(q3) + 2*ny*nz*cmath.cos(q2)*cmath.cos(q3)**2*cmath.cos(q4)**2*cmath.sin(q1)*cmath.sin(q2) + 2*ny*nz*cmath.cos(q2)**2*cmath.cos(q3)*cmath.cos(q4)**2*cmath.sin(q1)*cmath.sin(q3) - 2*nx**2*cmath.cos(q1)*cmath.cos(q2)*cmath.cos(q3)*cmath.cos(q4)*cmath.sin(q1)*cmath.sin(q4) + 2*ny**2*cmath.cos(q1)*cmath.cos(q2)*cmath.cos(q3)*cmath.cos(q4)*cmath.sin(q1)*cmath.sin(q4) - 2*sx*sz*cmath.cos(q1)*cmath.cos(q2)*cmath.cos(q4)**2*cmath.sin(q2)*cmath.sin(q3)**2 - 2*sx*sz*cmath.cos(q1)*cmath.cos(q3)*cmath.cos(q4)**2*cmath.sin(q2)**2*cmath.sin(q3) + 2*sy*sz*cmath.cos(q2)*cmath.cos(q3)**2*cmath.cos(q4)**2*cmath.sin(q1)*cmath.sin(q2) + 2*sy*sz*cmath.cos(q2)**2*cmath.cos(q3)*cmath.cos(q4)**2*cmath.sin(q1)*cmath.sin(q3) - 2*sx**2*cmath.cos(q1)*cmath.cos(q2)*cmath.cos(q3)*cmath.cos(q4)*cmath.sin(q1)*cmath.sin(q4) + 2*sy**2*cmath.cos(q1)*cmath.cos(q2)*cmath.cos(q3)*cmath.cos(q4)*cmath.sin(q1)*cmath.sin(q4) - 2*ny*nz*cmath.cos(q2)*cmath.cos(q4)**2*cmath.sin(q1)*cmath.sin(q2)*cmath.sin(q3)**2 - 2*ny*nz*cmath.cos(q3)*cmath.cos(q4)**2*cmath.sin(q1)*cmath.sin(q2)**2*cmath.sin(q3) - 2*sy*sz*cmath.cos(q2)*cmath.cos(q4)**2*cmath.sin(q1)*cmath.sin(q2)*cmath.sin(q3)**2 - 2*sy*sz*cmath.cos(q3)*cmath.cos(q4)**2*cmath.sin(q1)*cmath.sin(q2)**2*cmath.sin(q3) + 2*nx**2*cmath.cos(q1)*cmath.cos(q4)*cmath.sin(q1)*cmath.sin(q2)*cmath.sin(q3)*cmath.sin(q4) - 2*ny**2*cmath.cos(q1)*cmath.cos(q4)*cmath.sin(q1)*cmath.sin(q2)*cmath.sin(q3)*cmath.sin(q4) + 2*sx**2*cmath.cos(q1)*cmath.cos(q4)*cmath.sin(q1)*cmath.sin(q2)*cmath.sin(q3)*cmath.sin(q4) - 2*sy**2*cmath.cos(q1)*cmath.cos(q4)*cmath.sin(q1)*cmath.sin(q2)*cmath.sin(q3)*cmath.sin(q4) + 2*ny*nz*cmath.cos(q1)*cmath.cos(q2)*cmath.cos(q4)*cmath.sin(q3)*cmath.sin(q4) + 2*ny*nz*cmath.cos(q1)*cmath.cos(q3)*cmath.cos(q4)*cmath.sin(q2)*cmath.sin(q4) + 2*sy*sz*cmath.cos(q1)*cmath.cos(q2)*cmath.cos(q4)*cmath.sin(q3)*cmath.sin(q4) + 2*sy*sz*cmath.cos(q1)*cmath.cos(q3)*cmath.cos(q4)*cmath.sin(q2)*cmath.sin(q4) + 2*nx*ny*cmath.cos(q1)*cmath.cos(q2)**2*cmath.cos(q3)**2*cmath.cos(q4)**2*cmath.sin(q1) - 2*nx*nz*cmath.cos(q2)*cmath.cos(q4)*cmath.sin(q1)*cmath.sin(q3)*cmath.sin(q4) - 2*nx*nz*cmath.cos(q3)*cmath.cos(q4)*cmath.sin(q1)*cmath.sin(q2)*cmath.sin(q4) + 2*sx*sy*cmath.cos(q1)*cmath.cos(q2)**2*cmath.cos(q3)**2*cmath.cos(q4)**2*cmath.sin(q1) - 2*sx*sz*cmath.cos(q2)*cmath.cos(q4)*cmath.sin(q1)*cmath.sin(q3)*cmath.sin(q4) - 2*sx*sz*cmath.cos(q3)*cmath.cos(q4)*cmath.sin(q1)*cmath.sin(q2)*cmath.sin(q4) + 2*nx*ny*cmath.cos(q1)*cmath.cos(q4)**2*cmath.sin(q1)*cmath.sin(q2)**2*cmath.sin(q3)**2 + 2*sx*sy*cmath.cos(q1)*cmath.cos(q4)**2*cmath.sin(q1)*cmath.sin(q2)**2*cmath.sin(q3)**2 + 2*nx*ny*cmath.cos(q1)**2*cmath.cos(q2)*cmath.cos(q3)*cmath.cos(q4)*cmath.sin(q4) + 2*sx*sy*cmath.cos(q1)**2*cmath.cos(q2)*cmath.cos(q3)*cmath.cos(q4)*cmath.sin(q4) - 2*nx*ny*cmath.cos(q2)*cmath.cos(q3)*cmath.cos(q4)*cmath.sin(q1)**2*cmath.sin(q4) - 2*sx*sy*cmath.cos(q2)*cmath.cos(q3)*cmath.cos(q4)*cmath.sin(q1)**2*cmath.sin(q4) - 4*nx*ny*cmath.cos(q1)*cmath.cos(q2)*cmath.cos(q3)*cmath.cos(q4)**2*cmath.sin(q1)*cmath.sin(q2)*cmath.sin(q3) - 4*sx*sy*cmath.cos(q1)*cmath.cos(q2)*cmath.cos(q3)*cmath.cos(q4)**2*cmath.sin(q1)*cmath.sin(q2)*cmath.sin(q3))**(1/2))
            q5_1 = q5_1.real
            q5_2 = q5_2.real
            th5.append(q5_1)
            th5.append(q5_2)
        th5 = np.array([th5]).T
        #####
        
        # Se construye la matriz de combinaciones de th1 th2 y th3
        q = np.repeat(q,2,axis=0)
        
        q = np.append(q,th5,axis=1)
        #####
        
        # Se calcula th6
        r = q.shape[0]
        th6 = list()
        for i in range(r):
            q1 = q[i,0]
            q2 = q[i,1]
            q3 = q[i,2]
            q4 = q[i,3]
            q6_1 = -cmath.asin((sy*cmath.cos(q1)*cmath.sin(q4) - sx*cmath.sin(q1)*cmath.sin(q4) + sz*cmath.cos(q2)*cmath.cos(q4)*cmath.sin(q3) + sz*cmath.cos(q3)*cmath.cos(q4)*cmath.sin(q2) + sx*cmath.cos(q1)*cmath.cos(q2)*cmath.cos(q3)*cmath.cos(q4) + sy*cmath.cos(q2)*cmath.cos(q3)*cmath.cos(q4)*cmath.sin(q1) - sx*cmath.cos(q1)*cmath.cos(q4)*cmath.sin(q2)*cmath.sin(q3) - sy*cmath.cos(q4)*cmath.sin(q1)*cmath.sin(q2)*cmath.sin(q3))/(nx**2*cmath.cos(q1)**2*cmath.cos(q2)**2*cmath.cos(q3)**2*cmath.cos(q4)**2 - 2*nx**2*cmath.cos(q1)**2*cmath.cos(q2)*cmath.cos(q3)*cmath.cos(q4)**2*cmath.sin(q2)*cmath.sin(q3) + nx**2*cmath.cos(q1)**2*cmath.cos(q4)**2*cmath.sin(q2)**2*cmath.sin(q3)**2 - 2*nx**2*cmath.cos(q1)*cmath.cos(q2)*cmath.cos(q3)*cmath.cos(q4)*cmath.sin(q1)*cmath.sin(q4) + 2*nx**2*cmath.cos(q1)*cmath.cos(q4)*cmath.sin(q1)*cmath.sin(q2)*cmath.sin(q3)*cmath.sin(q4) + nx**2*cmath.sin(q1)**2*cmath.sin(q4)**2 + 2*nx*ny*cmath.cos(q1)**2*cmath.cos(q2)*cmath.cos(q3)*cmath.cos(q4)*cmath.sin(q4) - 2*nx*ny*cmath.cos(q1)**2*cmath.cos(q4)*cmath.sin(q2)*cmath.sin(q3)*cmath.sin(q4) + 2*nx*ny*cmath.cos(q1)*cmath.cos(q2)**2*cmath.cos(q3)**2*cmath.cos(q4)**2*cmath.sin(q1) - 4*nx*ny*cmath.cos(q1)*cmath.cos(q2)*cmath.cos(q3)*cmath.cos(q4)**2*cmath.sin(q1)*cmath.sin(q2)*cmath.sin(q3) + 2*nx*ny*cmath.cos(q1)*cmath.cos(q4)**2*cmath.sin(q1)*cmath.sin(q2)**2*cmath.sin(q3)**2 - 2*nx*ny*cmath.cos(q1)*cmath.sin(q1)*cmath.sin(q4)**2 - 2*nx*ny*cmath.cos(q2)*cmath.cos(q3)*cmath.cos(q4)*cmath.sin(q1)**2*cmath.sin(q4) + 2*nx*ny*cmath.cos(q4)*cmath.sin(q1)**2*cmath.sin(q2)*cmath.sin(q3)*cmath.sin(q4) + 2*nx*nz*cmath.cos(q1)*cmath.cos(q2)**2*cmath.cos(q3)*cmath.cos(q4)**2*cmath.sin(q3) + 2*nx*nz*cmath.cos(q1)*cmath.cos(q2)*cmath.cos(q3)**2*cmath.cos(q4)**2*cmath.sin(q2) - 2*nx*nz*cmath.cos(q1)*cmath.cos(q2)*cmath.cos(q4)**2*cmath.sin(q2)*cmath.sin(q3)**2 - 2*nx*nz*cmath.cos(q1)*cmath.cos(q3)*cmath.cos(q4)**2*cmath.sin(q2)**2*cmath.sin(q3) - 2*nx*nz*cmath.cos(q2)*cmath.cos(q4)*cmath.sin(q1)*cmath.sin(q3)*cmath.sin(q4) - 2*nx*nz*cmath.cos(q3)*cmath.cos(q4)*cmath.sin(q1)*cmath.sin(q2)*cmath.sin(q4) + ny**2*cmath.cos(q1)**2*cmath.sin(q4)**2 + 2*ny**2*cmath.cos(q1)*cmath.cos(q2)*cmath.cos(q3)*cmath.cos(q4)*cmath.sin(q1)*cmath.sin(q4) - 2*ny**2*cmath.cos(q1)*cmath.cos(q4)*cmath.sin(q1)*cmath.sin(q2)*cmath.sin(q3)*cmath.sin(q4) + ny**2*cmath.cos(q2)**2*cmath.cos(q3)**2*cmath.cos(q4)**2*cmath.sin(q1)**2 - 2*ny**2*cmath.cos(q2)*cmath.cos(q3)*cmath.cos(q4)**2*cmath.sin(q1)**2*cmath.sin(q2)*cmath.sin(q3) + ny**2*cmath.cos(q4)**2*cmath.sin(q1)**2*cmath.sin(q2)**2*cmath.sin(q3)**2 + 2*ny*nz*cmath.cos(q1)*cmath.cos(q2)*cmath.cos(q4)*cmath.sin(q3)*cmath.sin(q4) + 2*ny*nz*cmath.cos(q1)*cmath.cos(q3)*cmath.cos(q4)*cmath.sin(q2)*cmath.sin(q4) + 2*ny*nz*cmath.cos(q2)**2*cmath.cos(q3)*cmath.cos(q4)**2*cmath.sin(q1)*cmath.sin(q3) + 2*ny*nz*cmath.cos(q2)*cmath.cos(q3)**2*cmath.cos(q4)**2*cmath.sin(q1)*cmath.sin(q2) - 2*ny*nz*cmath.cos(q2)*cmath.cos(q4)**2*cmath.sin(q1)*cmath.sin(q2)*cmath.sin(q3)**2 - 2*ny*nz*cmath.cos(q3)*cmath.cos(q4)**2*cmath.sin(q1)*cmath.sin(q2)**2*cmath.sin(q3) + nz**2*cmath.cos(q2)**2*cmath.cos(q4)**2*cmath.sin(q3)**2 + 2*nz**2*cmath.cos(q2)*cmath.cos(q3)*cmath.cos(q4)**2*cmath.sin(q2)*cmath.sin(q3) + nz**2*cmath.cos(q3)**2*cmath.cos(q4)**2*cmath.sin(q2)**2 + sx**2*cmath.cos(q1)**2*cmath.cos(q2)**2*cmath.cos(q3)**2*cmath.cos(q4)**2 - 2*sx**2*cmath.cos(q1)**2*cmath.cos(q2)*cmath.cos(q3)*cmath.cos(q4)**2*cmath.sin(q2)*cmath.sin(q3) + sx**2*cmath.cos(q1)**2*cmath.cos(q4)**2*cmath.sin(q2)**2*cmath.sin(q3)**2 - 2*sx**2*cmath.cos(q1)*cmath.cos(q2)*cmath.cos(q3)*cmath.cos(q4)*cmath.sin(q1)*cmath.sin(q4) + 2*sx**2*cmath.cos(q1)*cmath.cos(q4)*cmath.sin(q1)*cmath.sin(q2)*cmath.sin(q3)*cmath.sin(q4) + sx**2*cmath.sin(q1)**2*cmath.sin(q4)**2 + 2*sx*sy*cmath.cos(q1)**2*cmath.cos(q2)*cmath.cos(q3)*cmath.cos(q4)*cmath.sin(q4) - 2*sx*sy*cmath.cos(q1)**2*cmath.cos(q4)*cmath.sin(q2)*cmath.sin(q3)*cmath.sin(q4) + 2*sx*sy*cmath.cos(q1)*cmath.cos(q2)**2*cmath.cos(q3)**2*cmath.cos(q4)**2*cmath.sin(q1) - 4*sx*sy*cmath.cos(q1)*cmath.cos(q2)*cmath.cos(q3)*cmath.cos(q4)**2*cmath.sin(q1)*cmath.sin(q2)*cmath.sin(q3) + 2*sx*sy*cmath.cos(q1)*cmath.cos(q4)**2*cmath.sin(q1)*cmath.sin(q2)**2*cmath.sin(q3)**2 - 2*sx*sy*cmath.cos(q1)*cmath.sin(q1)*cmath.sin(q4)**2 - 2*sx*sy*cmath.cos(q2)*cmath.cos(q3)*cmath.cos(q4)*cmath.sin(q1)**2*cmath.sin(q4) + 2*sx*sy*cmath.cos(q4)*cmath.sin(q1)**2*cmath.sin(q2)*cmath.sin(q3)*cmath.sin(q4) + 2*sx*sz*cmath.cos(q1)*cmath.cos(q2)**2*cmath.cos(q3)*cmath.cos(q4)**2*cmath.sin(q3) + 2*sx*sz*cmath.cos(q1)*cmath.cos(q2)*cmath.cos(q3)**2*cmath.cos(q4)**2*cmath.sin(q2) - 2*sx*sz*cmath.cos(q1)*cmath.cos(q2)*cmath.cos(q4)**2*cmath.sin(q2)*cmath.sin(q3)**2 - 2*sx*sz*cmath.cos(q1)*cmath.cos(q3)*cmath.cos(q4)**2*cmath.sin(q2)**2*cmath.sin(q3) - 2*sx*sz*cmath.cos(q2)*cmath.cos(q4)*cmath.sin(q1)*cmath.sin(q3)*cmath.sin(q4) - 2*sx*sz*cmath.cos(q3)*cmath.cos(q4)*cmath.sin(q1)*cmath.sin(q2)*cmath.sin(q4) + sy**2*cmath.cos(q1)**2*cmath.sin(q4)**2 + 2*sy**2*cmath.cos(q1)*cmath.cos(q2)*cmath.cos(q3)*cmath.cos(q4)*cmath.sin(q1)*cmath.sin(q4) - 2*sy**2*cmath.cos(q1)*cmath.cos(q4)*cmath.sin(q1)*cmath.sin(q2)*cmath.sin(q3)*cmath.sin(q4) + sy**2*cmath.cos(q2)**2*cmath.cos(q3)**2*cmath.cos(q4)**2*cmath.sin(q1)**2 - 2*sy**2*cmath.cos(q2)*cmath.cos(q3)*cmath.cos(q4)**2*cmath.sin(q1)**2*cmath.sin(q2)*cmath.sin(q3) + sy**2*cmath.cos(q4)**2*cmath.sin(q1)**2*cmath.sin(q2)**2*cmath.sin(q3)**2 + 2*sy*sz*cmath.cos(q1)*cmath.cos(q2)*cmath.cos(q4)*cmath.sin(q3)*cmath.sin(q4) + 2*sy*sz*cmath.cos(q1)*cmath.cos(q3)*cmath.cos(q4)*cmath.sin(q2)*cmath.sin(q4) + 2*sy*sz*cmath.cos(q2)**2*cmath.cos(q3)*cmath.cos(q4)**2*cmath.sin(q1)*cmath.sin(q3) + 2*sy*sz*cmath.cos(q2)*cmath.cos(q3)**2*cmath.cos(q4)**2*cmath.sin(q1)*cmath.sin(q2) - 2*sy*sz*cmath.cos(q2)*cmath.cos(q4)**2*cmath.sin(q1)*cmath.sin(q2)*cmath.sin(q3)**2 - 2*sy*sz*cmath.cos(q3)*cmath.cos(q4)**2*cmath.sin(q1)*cmath.sin(q2)**2*cmath.sin(q3) + sz**2*cmath.cos(q2)**2*cmath.cos(q4)**2*cmath.sin(q3)**2 + 2*sz**2*cmath.cos(q2)*cmath.cos(q3)*cmath.cos(q4)**2*cmath.sin(q2)*cmath.sin(q3) + sz**2*cmath.cos(q3)**2*cmath.cos(q4)**2*cmath.sin(q2)**2)**(1/2))
            q6_2 = math.pi + cmath.asin((sy*cmath.cos(q1)*cmath.sin(q4) - sx*cmath.sin(q1)*cmath.sin(q4) + sz*cmath.cos(q2)*cmath.cos(q4)*cmath.sin(q3) + sz*cmath.cos(q3)*cmath.cos(q4)*cmath.sin(q2) + sx*cmath.cos(q1)*cmath.cos(q2)*cmath.cos(q3)*cmath.cos(q4) + sy*cmath.cos(q2)*cmath.cos(q3)*cmath.cos(q4)*cmath.sin(q1) - sx*cmath.cos(q1)*cmath.cos(q4)*cmath.sin(q2)*cmath.sin(q3) - sy*cmath.cos(q4)*cmath.sin(q1)*cmath.sin(q2)*cmath.sin(q3))/(nx**2*cmath.cos(q1)**2*cmath.cos(q2)**2*cmath.cos(q3)**2*cmath.cos(q4)**2 - 2*nx**2*cmath.cos(q1)**2*cmath.cos(q2)*cmath.cos(q3)*cmath.cos(q4)**2*cmath.sin(q2)*cmath.sin(q3) + nx**2*cmath.cos(q1)**2*cmath.cos(q4)**2*cmath.sin(q2)**2*cmath.sin(q3)**2 - 2*nx**2*cmath.cos(q1)*cmath.cos(q2)*cmath.cos(q3)*cmath.cos(q4)*cmath.sin(q1)*cmath.sin(q4) + 2*nx**2*cmath.cos(q1)*cmath.cos(q4)*cmath.sin(q1)*cmath.sin(q2)*cmath.sin(q3)*cmath.sin(q4) + nx**2*cmath.sin(q1)**2*cmath.sin(q4)**2 + 2*nx*ny*cmath.cos(q1)**2*cmath.cos(q2)*cmath.cos(q3)*cmath.cos(q4)*cmath.sin(q4) - 2*nx*ny*cmath.cos(q1)**2*cmath.cos(q4)*cmath.sin(q2)*cmath.sin(q3)*cmath.sin(q4) + 2*nx*ny*cmath.cos(q1)*cmath.cos(q2)**2*cmath.cos(q3)**2*cmath.cos(q4)**2*cmath.sin(q1) - 4*nx*ny*cmath.cos(q1)*cmath.cos(q2)*cmath.cos(q3)*cmath.cos(q4)**2*cmath.sin(q1)*cmath.sin(q2)*cmath.sin(q3) + 2*nx*ny*cmath.cos(q1)*cmath.cos(q4)**2*cmath.sin(q1)*cmath.sin(q2)**2*cmath.sin(q3)**2 - 2*nx*ny*cmath.cos(q1)*cmath.sin(q1)*cmath.sin(q4)**2 - 2*nx*ny*cmath.cos(q2)*cmath.cos(q3)*cmath.cos(q4)*cmath.sin(q1)**2*cmath.sin(q4) + 2*nx*ny*cmath.cos(q4)*cmath.sin(q1)**2*cmath.sin(q2)*cmath.sin(q3)*cmath.sin(q4) + 2*nx*nz*cmath.cos(q1)*cmath.cos(q2)**2*cmath.cos(q3)*cmath.cos(q4)**2*cmath.sin(q3) + 2*nx*nz*cmath.cos(q1)*cmath.cos(q2)*cmath.cos(q3)**2*cmath.cos(q4)**2*cmath.sin(q2) - 2*nx*nz*cmath.cos(q1)*cmath.cos(q2)*cmath.cos(q4)**2*cmath.sin(q2)*cmath.sin(q3)**2 - 2*nx*nz*cmath.cos(q1)*cmath.cos(q3)*cmath.cos(q4)**2*cmath.sin(q2)**2*cmath.sin(q3) - 2*nx*nz*cmath.cos(q2)*cmath.cos(q4)*cmath.sin(q1)*cmath.sin(q3)*cmath.sin(q4) - 2*nx*nz*cmath.cos(q3)*cmath.cos(q4)*cmath.sin(q1)*cmath.sin(q2)*cmath.sin(q4) + ny**2*cmath.cos(q1)**2*cmath.sin(q4)**2 + 2*ny**2*cmath.cos(q1)*cmath.cos(q2)*cmath.cos(q3)*cmath.cos(q4)*cmath.sin(q1)*cmath.sin(q4) - 2*ny**2*cmath.cos(q1)*cmath.cos(q4)*cmath.sin(q1)*cmath.sin(q2)*cmath.sin(q3)*cmath.sin(q4) + ny**2*cmath.cos(q2)**2*cmath.cos(q3)**2*cmath.cos(q4)**2*cmath.sin(q1)**2 - 2*ny**2*cmath.cos(q2)*cmath.cos(q3)*cmath.cos(q4)**2*cmath.sin(q1)**2*cmath.sin(q2)*cmath.sin(q3) + ny**2*cmath.cos(q4)**2*cmath.sin(q1)**2*cmath.sin(q2)**2*cmath.sin(q3)**2 + 2*ny*nz*cmath.cos(q1)*cmath.cos(q2)*cmath.cos(q4)*cmath.sin(q3)*cmath.sin(q4) + 2*ny*nz*cmath.cos(q1)*cmath.cos(q3)*cmath.cos(q4)*cmath.sin(q2)*cmath.sin(q4) + 2*ny*nz*cmath.cos(q2)**2*cmath.cos(q3)*cmath.cos(q4)**2*cmath.sin(q1)*cmath.sin(q3) + 2*ny*nz*cmath.cos(q2)*cmath.cos(q3)**2*cmath.cos(q4)**2*cmath.sin(q1)*cmath.sin(q2) - 2*ny*nz*cmath.cos(q2)*cmath.cos(q4)**2*cmath.sin(q1)*cmath.sin(q2)*cmath.sin(q3)**2 - 2*ny*nz*cmath.cos(q3)*cmath.cos(q4)**2*cmath.sin(q1)*cmath.sin(q2)**2*cmath.sin(q3) + nz**2*cmath.cos(q2)**2*cmath.cos(q4)**2*cmath.sin(q3)**2 + 2*nz**2*cmath.cos(q2)*cmath.cos(q3)*cmath.cos(q4)**2*cmath.sin(q2)*cmath.sin(q3) + nz**2*cmath.cos(q3)**2*cmath.cos(q4)**2*cmath.sin(q2)**2 + sx**2*cmath.cos(q1)**2*cmath.cos(q2)**2*cmath.cos(q3)**2*cmath.cos(q4)**2 - 2*sx**2*cmath.cos(q1)**2*cmath.cos(q2)*cmath.cos(q3)*cmath.cos(q4)**2*cmath.sin(q2)*cmath.sin(q3) + sx**2*cmath.cos(q1)**2*cmath.cos(q4)**2*cmath.sin(q2)**2*cmath.sin(q3)**2 - 2*sx**2*cmath.cos(q1)*cmath.cos(q2)*cmath.cos(q3)*cmath.cos(q4)*cmath.sin(q1)*cmath.sin(q4) + 2*sx**2*cmath.cos(q1)*cmath.cos(q4)*cmath.sin(q1)*cmath.sin(q2)*cmath.sin(q3)*cmath.sin(q4) + sx**2*cmath.sin(q1)**2*cmath.sin(q4)**2 + 2*sx*sy*cmath.cos(q1)**2*cmath.cos(q2)*cmath.cos(q3)*cmath.cos(q4)*cmath.sin(q4) - 2*sx*sy*cmath.cos(q1)**2*cmath.cos(q4)*cmath.sin(q2)*cmath.sin(q3)*cmath.sin(q4) + 2*sx*sy*cmath.cos(q1)*cmath.cos(q2)**2*cmath.cos(q3)**2*cmath.cos(q4)**2*cmath.sin(q1) - 4*sx*sy*cmath.cos(q1)*cmath.cos(q2)*cmath.cos(q3)*cmath.cos(q4)**2*cmath.sin(q1)*cmath.sin(q2)*cmath.sin(q3) + 2*sx*sy*cmath.cos(q1)*cmath.cos(q4)**2*cmath.sin(q1)*cmath.sin(q2)**2*cmath.sin(q3)**2 - 2*sx*sy*cmath.cos(q1)*cmath.sin(q1)*cmath.sin(q4)**2 - 2*sx*sy*cmath.cos(q2)*cmath.cos(q3)*cmath.cos(q4)*cmath.sin(q1)**2*cmath.sin(q4) + 2*sx*sy*cmath.cos(q4)*cmath.sin(q1)**2*cmath.sin(q2)*cmath.sin(q3)*cmath.sin(q4) + 2*sx*sz*cmath.cos(q1)*cmath.cos(q2)**2*cmath.cos(q3)*cmath.cos(q4)**2*cmath.sin(q3) + 2*sx*sz*cmath.cos(q1)*cmath.cos(q2)*cmath.cos(q3)**2*cmath.cos(q4)**2*cmath.sin(q2) - 2*sx*sz*cmath.cos(q1)*cmath.cos(q2)*cmath.cos(q4)**2*cmath.sin(q2)*cmath.sin(q3)**2 - 2*sx*sz*cmath.cos(q1)*cmath.cos(q3)*cmath.cos(q4)**2*cmath.sin(q2)**2*cmath.sin(q3) - 2*sx*sz*cmath.cos(q2)*cmath.cos(q4)*cmath.sin(q1)*cmath.sin(q3)*cmath.sin(q4) - 2*sx*sz*cmath.cos(q3)*cmath.cos(q4)*cmath.sin(q1)*cmath.sin(q2)*cmath.sin(q4) + sy**2*cmath.cos(q1)**2*cmath.sin(q4)**2 + 2*sy**2*cmath.cos(q1)*cmath.cos(q2)*cmath.cos(q3)*cmath.cos(q4)*cmath.sin(q1)*cmath.sin(q4) - 2*sy**2*cmath.cos(q1)*cmath.cos(q4)*cmath.sin(q1)*cmath.sin(q2)*cmath.sin(q3)*cmath.sin(q4) + sy**2*cmath.cos(q2)**2*cmath.cos(q3)**2*cmath.cos(q4)**2*cmath.sin(q1)**2 - 2*sy**2*cmath.cos(q2)*cmath.cos(q3)*cmath.cos(q4)**2*cmath.sin(q1)**2*cmath.sin(q2)*cmath.sin(q3) + sy**2*cmath.cos(q4)**2*cmath.sin(q1)**2*cmath.sin(q2)**2*cmath.sin(q3)**2 + 2*sy*sz*cmath.cos(q1)*cmath.cos(q2)*cmath.cos(q4)*cmath.sin(q3)*cmath.sin(q4) + 2*sy*sz*cmath.cos(q1)*cmath.cos(q3)*cmath.cos(q4)*cmath.sin(q2)*cmath.sin(q4) + 2*sy*sz*cmath.cos(q2)**2*cmath.cos(q3)*cmath.cos(q4)**2*cmath.sin(q1)*cmath.sin(q3) + 2*sy*sz*cmath.cos(q2)*cmath.cos(q3)**2*cmath.cos(q4)**2*cmath.sin(q1)*cmath.sin(q2) - 2*sy*sz*cmath.cos(q2)*cmath.cos(q4)**2*cmath.sin(q1)*cmath.sin(q2)*cmath.sin(q3)**2 - 2*sy*sz*cmath.cos(q3)*cmath.cos(q4)**2*cmath.sin(q1)*cmath.sin(q2)**2*cmath.sin(q3) + sz**2*cmath.cos(q2)**2*cmath.cos(q4)**2*cmath.sin(q3)**2 + 2*sz**2*cmath.cos(q2)*cmath.cos(q3)*cmath.cos(q4)**2*cmath.sin(q2)*cmath.sin(q3) + sz**2*cmath.cos(q3)**2*cmath.cos(q4)**2*cmath.sin(q2)**2)**(1/2))
            q6_1 = q6_1.real
            q6_2 = q6_2.real
            th6.append(q6_1)
            th6.append(q6_2)
        th6 = np.array([th6]).T
        #####
        
        # Se construye la matriz de combinaciones de th1 th2 th3 th4 th5 y th6
        q = np.repeat(q,2,axis=0)
        
        q = np.append(q,th6,axis=1)
        #####
        
        # Evaluar ecuaciones de traslaciÃ³n y rotaciÃ³n con todos los Ã¡ngulos
        th1 = q[:,0]
        th2 = q[:,1]
        th3 = q[:,2]
        th4 = q[:,3]
        th5 = q[:,4]
        th6 = q[:,5]
        
        x = L2*np.cos(th1)*np.cos(th2) - L4*np.sin(th2 + th3)*np.cos(th1) - L3*np.sin(th1) - L5*np.sin(th2 + th3)*np.cos(th1)*np.cos(th5) + L5*np.sin(th1)*np.sin(th4)*np.sin(th5) + L5*np.cos(th1)*np.cos(th4)*np.sin(th2)*np.sin(th3)*np.sin(th5) - L5*np.cos(th1)*np.cos(th2)*np.cos(th3)*np.cos(th4)*np.sin(th5)
        y = L3*np.cos(th1) - L4*np.sin(th2 + th3)*np.sin(th1) + L2*np.cos(th2)*np.sin(th1) - L5*np.sin(th2 + th3)*np.cos(th5)*np.sin(th1) - L5*np.cos(th1)*np.sin(th4)*np.sin(th5) - L5*np.cos(th2)*np.cos(th3)*np.cos(th4)*np.sin(th1)*np.sin(th5) + L5*np.cos(th4)*np.sin(th1)*np.sin(th2)*np.sin(th3)*np.sin(th5)
        z = L1 + L4*np.cos(th2 + th3) + L2*np.sin(th2) - (L5*np.sin(th2 + th3)*np.sin(th4 + th5))/2 + L5*np.cos(th2 + th3)*np.cos(th5) + (L5*np.sin(th4 - th5)*np.sin(th2 + th3))/2
        nxc = -np.sin(th6)*(np.cos(th4)*np.sin(th1) - np.sin(th4)*(np.cos(th1)*np.sin(th2)*np.sin(th3) - np.cos(th1)*np.cos(th2)*np.cos(th3))) - np.cos(th6)*(np.cos(th5)*(np.sin(th1)*np.sin(th4) + np.cos(th4)*(np.cos(th1)*np.sin(th2)*np.sin(th3) - np.cos(th1)*np.cos(th2)*np.cos(th3))) + np.sin(th5)*(np.cos(th1)*np.cos(th2)*np.sin(th3) + np.cos(th1)*np.cos(th3)*np.sin(th2)))
        nyc = np.sin(th6)*(np.cos(th1)*np.cos(th4) + np.sin(th4)*(np.sin(th1)*np.sin(th2)*np.sin(th3) - np.cos(th2)*np.cos(th3)*np.sin(th1))) + np.cos(th6)*(np.cos(th5)*(np.cos(th1)*np.sin(th4) - np.cos(th4)*(np.sin(th1)*np.sin(th2)*np.sin(th3) - np.cos(th2)*np.cos(th3)*np.sin(th1))) - np.sin(th5)*(np.cos(th2)*np.sin(th1)*np.sin(th3) + np.cos(th3)*np.sin(th1)*np.sin(th2)))
        nzc = np.cos(th6)*(np.cos(th2 + th3)*np.sin(th5) + np.sin(th2 + th3)*np.cos(th4)*np.cos(th5)) - np.sin(th2 + th3)*np.sin(th4)*np.sin(th6)
        sxc = np.sin(th6)*(np.cos(th5)*(np.sin(th1)*np.sin(th4) + np.cos(th4)*(np.cos(th1)*np.sin(th2)*np.sin(th3) - np.cos(th1)*np.cos(th2)*np.cos(th3))) + np.sin(th5)*(np.cos(th1)*np.cos(th2)*np.sin(th3) + np.cos(th1)*np.cos(th3)*np.sin(th2))) - np.cos(th6)*(np.cos(th4)*np.sin(th1) - np.sin(th4)*(np.cos(th1)*np.sin(th2)*np.sin(th3) - np.cos(th1)*np.cos(th2)*np.cos(th3)))
        syc = np.cos(th6)*(np.cos(th1)*np.cos(th4) + np.sin(th4)*(np.sin(th1)*np.sin(th2)*np.sin(th3) - np.cos(th2)*np.cos(th3)*np.sin(th1))) - np.sin(th6)*(np.cos(th5)*(np.cos(th1)*np.sin(th4) - np.cos(th4)*(np.sin(th1)*np.sin(th2)*np.sin(th3) - np.cos(th2)*np.cos(th3)*np.sin(th1))) - np.sin(th5)*(np.cos(th2)*np.sin(th1)*np.sin(th3) + np.cos(th3)*np.sin(th1)*np.sin(th2)))
        szc = -np.sin(th6)*(np.cos(th2 + th3)*np.sin(th5) + np.sin(th2 + th3)*np.cos(th4)*np.cos(th5)) - np.sin(th2 + th3)*np.cos(th6)*np.sin(th4)
        axc = np.sin(th5)*(np.sin(th1)*np.sin(th4) + np.cos(th4)*(np.cos(th1)*np.sin(th2)*np.sin(th3) - np.cos(th1)*np.cos(th2)*np.cos(th3))) - np.cos(th5)*(np.cos(th1)*np.cos(th2)*np.sin(th3) + np.cos(th1)*np.cos(th3)*np.sin(th2))
        ayc = -np.sin(th5)*(np.cos(th1)*np.sin(th4) - np.cos(th4)*(np.sin(th1)*np.sin(th2)*np.sin(th3) - np.cos(th2)*np.cos(th3)*np.sin(th1))) - np.cos(th5)*(np.cos(th2)*np.sin(th1)*np.sin(th3) + np.cos(th3)*np.sin(th1)*np.sin(th2))
        azc = np.cos(th2 + th3)*np.cos(th5) - np.sin(th2 + th3)*np.cos(th4)*np.sin(th5)
        #####
        
        # Observar que combinaciones entregan el menor error
        r = x.size
        xf = np.repeat(xf,r)
        yf = np.repeat(yf,r)
        zf = np.repeat(zf,r)
        nx = np.repeat(nx,r)
        ny = np.repeat(ny,r)
        nz = np.repeat(nz,r)
        sx = np.repeat(sx,r)
        sy = np.repeat(sy,r)
        sz = np.repeat(sz,r)
        ax = np.repeat(ax,r)
        ay = np.repeat(ay,r)
        az = np.repeat(az,r)
        error = np.sqrt((xf-x)**2+(yf-y)**2+(zf-z)**2+(nx-nxc)**2+(ny-nyc)**2+(nz-nzc)**2+(sx-sxc)**2+(sy-syc)**2+(sz-szc)**2+(ax-axc)**2+(ay-ayc)**2+(az-azc)**2)
        #####
        
        # Se agregan condiciones de ángulos
        I = list()
        for i in range(r):
            if q[i,1] >= 0 and q[i,1] <= math.pi:
                I.append(i)
        #####
        
        # Se toman en cuenta los nuevos indices
        # Se calcula el mínimo error y se toma el indice para seleccionar la combinación de ángulos
        q = q[I,:]
        error = error[I]
        ind = np.where(error == np.amin(error))
        ind = ind[0][0]
        qs = q[ind]
        qsd = np.degrees(qs)
        #####
    
    except:
        
        print("Esa configuracion es imposible")

    return qsd