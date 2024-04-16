clc, clear, close

%% Masa de los Joints de PLA
% Se calculan las masas de todos los joints de PLA, los cuales se imprimen
% en 3D.

% masa de los joints 50% (g)
J1 = 80;
J2 = 65;
J3 = 72;
J4 = 66;
J5 = 67;
J6 = 34;
J7 = 37;
J8 = 20;
J9 = 9;

%% Masa de otros componentes
% Se indica la masa de diversos componentes colocados en el brazo, como
% los eslabones de PVC, los baleros, los motores y el efector final.

% masa hub (g)
H = 3.2;

% masa de motores (g)
M1 = 108 + H;
M2 = 108 + H;
M3 = 108 + H;
M4 = 47 + H;
M5 = 47 + H;
M6 = 47 + H;

% masa balero (g)
B1 = 22;
B2 = 4;
B3 = 22;
B4 = 22;
B5 = 4;

% masa pvc (g)
W1 = 21.6;
W2 = 16.7;

% masa efector final (g)
EF = 100;

% Se calcula la masa total (kg)
MasaT = M1 + M2 + M3 + M4 + M5 + M6 + B1 + B2 + B3 + B4 + B5 + W1 + W2 + EF;
MasaT = (MasaT + J1 + J2 + J3 + J4 + J5 + J6 + J7 + J8 + J9)/1000
%% Cálculo de torque en el chasis (Empotramiento)
% Se calcula la reacción de momento generado en el chasis debido al peso
% del brazo manipulador.

r = 83;

% distancias de empotramiento a fuerzas (mm)
dM1 = 30;
dM2 = 83;
dM3 = 190 + r;
dM4 = 293 + r;
dM5 = 362 + r;
dM6 = 405 + r;
dJ1 = 30;
dJ2 = 64;
dJ3 = 18 + r;
dJ4 = 174 + r;
dJ5 = 203 + r;
dJ6 = 315 + r;
dJ7 = 349 + r;
dJ8 = 381 + r;
dJ9 = 446 + r;
dW1 = 99 + r;
dW2 = 265 + r;
dB1 = 44;
dB2 = 83;
dB3 = 190 + r;
dB4 = 326 + r;
dB5 = 362 + r;
dEF = 457 + r;

% Ecuaciones de momento (g x mm)
MM = M1*dM1 + M2*dM2 + M3*dM3 + M4*dM4 + M5*dM5 + M6*dM6;
MB = B1*dB1 + B2*dB2 + B3*dB3 + B4*dB4 + B5*dB5;
MW = W1*dW1 + W2*dW2;
MJ = J1*dJ1 + J2*dJ2 + J3*dJ3 + J4*dJ4 + J5*dJ5 + J6*dJ6 + J7*dJ7 + J8*dJ8 + J9*dJ9;
MEF = EF*dEF;

% Torque de empotramiento (kg x cm)
Tb = (MM + MB + MW + MJ + MEF)/(1000*10)


%% Cálculo de torque en el joint 1 (Motor 2)
% Se calcula la reacción de momento generado en el motor debido al peso
% del brazo manipulador.

% distancias de motor a fuerzas (mm)
dM3 = 190;
dM4 = 293;
dM5 = 362;
dM6 = 405;
dJ3 = 18;
dJ4 = 174;
dJ5 = 203;
dJ6 = 315;
dJ7 = 349;
dJ8 = 381;
dJ9 = 446;
dW1 = 99;
dW2 = 265;
dB3 = 190;
dB4 = 326;
dB5 = 362;
dEF = 457;

% Ecuaciones de momento (g x mm)
MM = (M3*dM3 + M4*dM4 + M5*dM5 + M6*dM6)/(1000*10);
MB = (B3*dB3 + B4*dB4 + B5*dB5)/(1000*10);
MW = (W1*dW1 + W2*dW2)/(1000*10);
MJ = (J3*dJ3 + J4*dJ4 + J5*dJ5 + J6*dJ6 + J7*dJ7 + J8*dJ8 + J9*dJ9)/(1000*10);
MEF = EF*dEF/(1000*10);

% Torque del joint 1 (kg x cm)
Tm = (MM + MB + MW + MJ + MEF)

