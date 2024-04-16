clc , clear, close

%% Motor pequeño

syms t w

K = 0.246; % Ganancia
th = 0.016; % Tiempo muerto
tau = 0.114; % Constante de tiempo tau

% Laplaca
s=tf('s');

% Tiempo de muestreo utilizado para la captura de datos
T = 0.008;

% Función de primer orden con tiempo muerto
% Continuo
fc = K*exp(-th*s)/(tau*s + 1)*50;
% Discreto
fd = c2d(fc,T);

% Se importa el csv con los valores de RPM tomados experimentales
filename = 'q4_datos.csv';
table = readtable(filename);
RPM = table2array(table(:,2));
x = table2array(table(:,1));

% Se general la gráfica con los datos experimentales, la entrada y la
% aproximación

figure(1)
yyaxis left
[l,tout] = step(fd)
plot(tout,l)
hold on
plot(x,RPM,'.')
title('Respuesta de lazo abierto ante entrada escalón de 50%')
xlabel('Tiempo')
ylabel('RPM')

yyaxis right
fplot(50*heaviside(w),'Color','r')
ylabel('Voltaje (%)')

xlim([0 2])
legend('RPM: FOPDT','RPM: Experimental')
grid on

%%
clc, clear

%% Motor grande

syms t w

K = 0.125; % Ganancia
th = 0.016; % Tiempo muerto
tau = 0.312; % Constante de tiempo tau

% Laplaca
s=tf('s');

% Tiempo de muestreo utilizado para la captura de datos
T = 0.008;

% Función de primer orden con tiempo muerto
% Continuo
fc = K*exp(-th*s)/(tau*s + 1)*50;
% Discreto
fd = c2d(fc,T);

% Se importa el csv con los valores de RPM tomados experimentales
filename = 'q1_datos.csv';
table = readtable(filename);
RPM = table2array(table(:,2));
x = table2array(table(:,1));

% Se general la gráfica con los datos experimentales, la entrada y la
% aproximación

figure (2)
yyaxis left
[l,tout] = step(fd)
plot(tout,l)
hold on
plot(x,RPM,'.')
title('Respuesta de lazo abierto ante entrada escalón de 50%')
xlabel('Tiempo')
ylabel('RPM')

yyaxis right
fplot(50*heaviside(w),'Color','r')
ylabel('Voltaje (%)')

xlim([0 2])
legend('RPM: FOPDT','RPM: Experimental')
grid on
