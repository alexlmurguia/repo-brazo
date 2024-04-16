%% Limpiar consola y variables
clc, clear, close

%% Crear matriz de transformación homogenea con parámetros de DH

% Matriz de transformación homogénea
syms th d alpha a
A = [cos(th) -cos(alpha)*sin(th)  sin(alpha)*sin(th) a*cos(th);
     sin(th)  cos(alpha)*cos(th) -sin(alpha)*cos(th) a*sin(th); 
     0        sin(alpha)          cos(alpha)         d; 
     0        0                   0                  1];

% Longitudes del brazo
syms L1 L2 L3 L4 L5

% Parámetros de DH
syms th1 th2 th3 th4 th5 th6
A01 = subs(A,{th,d,a,alpha},{th1,L1,0,pi/2})
A12 = subs(A,{th,d,a,alpha},{th2,0,L2,0})
A23 = subs(A,{th,d,a,alpha},{th3,-L3,0,-pi/2})
A34 = subs(A,{th,d,a,alpha},{th4,L4,0,pi/2})
A45 = subs(A,{th,d,a,alpha},{th5,0,0,-pi/2})
A56 = subs(A,{th,d,a,alpha},{th6,L5,0,0})

c = @cos
s = @sin
% Matriz de Transformación de efector final respecto origen
A06 = simplify(A01*A12*A23*A34*A45*A56)
A04 = simplify(A01*A12*A23*A34)

%% Calcular Th1

% Construir matriz de referencia
syms nx ny nz
syms sx sy sz
syms ax ay az
syms dx dy dz

A04 = [nx sx ax dx;
       ny sy ay dy;
       nz sz az dz;
       0  0  0  1];

% Despejar la primera MTH
T_a = simplify(inv(A01)*A04)
T_d = simplify(A12*A23*A34)

% Calcular th1
f0 = T_a(3,4) == T_d(3,4);
q1 = simplify(solve(f0,th1,'Real',true))

%% Calcular Th2 y Th3

% Proponer ecuaciones para Th2 y Th3
f1 = T_a(1,4) == T_d(1,4);
f2 = T_a(2,4) == T_d(2,4);

q3 = solve(f2,th3);
f1 = subs(f1,th3,q3);
q2 = solve(f1(1),th2,'IgnoreAnalyticConstraints',true);
q2 = simplify(q2)
q3_1 = simplify(subs(q3,th2,q2(1)))
q3_2 = simplify(subs(q3,th2,q2(2)))

%% Calcular Th4
 
% Proponer matrices para la muñeca
O_a = simplify(A45*A56);
O_d = simplify(inv(A01*A12*A23*A34)*A04);

% Resolver ecuación
f3 = O_a(3,3) == O_d(3,3);
q4 = solve(f3,th4);
q4 = simplify(q4)

%% Calcular Th5 y Th6

% Proponer ecuaciones
f4 = O_a(1,1) == O_d(1,1);
f5 = O_a(1,2) == O_d(1,2);

q6 = solve(f5,th6);
f4 = subs(f4,th6,q6);
q5 = simplify(solve(f4(1),th5))
q6_1 = simplify(subs(q6,th5,q5(1)))
