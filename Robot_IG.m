
function varargout = Robot_IG(varargin)
% ROBOT_IG MATLAB code for Robot_IG.fig
%      ROBOT_IG, by itself, creates a new ROBOT_IG or raises the existing
%      singleton*.
%
%      H = ROBOT_IG returns the handle to a new ROBOT_IG or the handle to
%      the existing singleton*.
%
%      ROBOT_IG('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in ROBOT_IG.M with the given input arguments.
%
%      ROBOT_IG('Property','Value',...) creates a new ROBOT_IG or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before Robot_IG_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to Robot_IG_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help Robot_IG

% Last Modified by GUIDE v2.5 03-Mar-2021 20:23:00

% Begin initialization code - DO NOT EDIT

gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @Robot_IG_OpeningFcn, ...
                   'gui_OutputFcn',  @Robot_IG_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT

% --- Executes just before Robot_IG is made visible.
function Robot_IG_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to Robot_IG (see VARARGIN)

% Choose default command line output for Robot_IG
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);

set(gcf,'Color',[1 1 0])
 
sliderVal_1 = 0;
sliderVal_2 = 0;
sliderVal_3 = 0;
sliderVal_4 = 0;
sliderVal_5 = 0;
sliderVal_6 = 0;
set(handles.q1,'string',num2str(sliderVal_1));
set(handles.q2,'string',num2str(sliderVal_2));
set(handles.q3,'string',num2str(sliderVal_3));
set(handles.q4,'string',num2str(sliderVal_4));
set(handles.q5,'string',num2str(sliderVal_5));
set(handles.q6,'string',num2str(sliderVal_6));
assignin('base','sliderVal_1',sliderVal_1);
assignin('base','sliderVal_2',sliderVal_2);
assignin('base','sliderVal_3',sliderVal_3);
assignin('base','sliderVal_4',sliderVal_4);
assignin('base','sliderVal_5',sliderVal_5);
assignin('base','sliderVal_6',sliderVal_6);
updateData();

% UIWAIT makes Robot_IG wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = Robot_IG_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;



function Th1_Callback(hObject, eventdata, handles)
% hObject    handle to Th1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of Th1 as text
%        str2double(get(hObject,'String')) returns contents of Th1 as a double
sliderVal_1 = get(hObject,'Value');
assignin('base','sliderVal_1',sliderVal_1);
set(handles.q1,'string',num2str(sliderVal_1));
updateData();

% --- Executes during object creation, after setting all properties.
function Th1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to Th1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


function Th2_Callback(hObject, eventdata, handles)
% hObject    handle to Th2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of Th2 as text
%        str2double(get(hObject,'String')) returns contents of Th2 as a double
sliderVal_2 = get(hObject,'Value');
assignin('base','sliderVal_2',sliderVal_2);
set(handles.q2,'string',num2str(sliderVal_2));
updateData();


% --- Executes during object creation, after setting all properties.
function Th2_CreateFcn(hObject, eventdata, handles)
% hObject    handle to Th2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function Th3_Callback(hObject, eventdata, handles)
% hObject    handle to Th3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of Th3 as text
%        str2double(get(hObject,'String')) returns contents of Th3 as a double
sliderVal_3 = get(hObject,'Value');
assignin('base','sliderVal_3',sliderVal_3);
set(handles.q3,'string',num2str(sliderVal_3));
updateData();


% --- Executes during object creation, after setting all properties.
function Th3_CreateFcn(hObject, eventdata, handles)
% hObject    handle to Th3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

function Th4_Callback(hObject, eventdata, handles)
% hObject    handle to Th1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of Th1 as text
%        str2double(get(hObject,'String')) returns contents of Th1 as a double
sliderVal_4 = get(hObject,'Value');
assignin('base','sliderVal_4',sliderVal_4);
set(handles.q4,'string',num2str(sliderVal_4));
updateData();

% --- Executes during object creation, after setting all properties.
function Th4_CreateFcn(hObject, eventdata, handles)
% hObject    handle to Th1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

function Th5_Callback(hObject, eventdata, handles)
% hObject    handle to Th1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of Th1 as text
%        str2double(get(hObject,'String')) returns contents of Th1 as a double
sliderVal_5 = get(hObject,'Value');
assignin('base','sliderVal_5',sliderVal_5);
set(handles.q5,'string',num2str(sliderVal_5));
updateData();

% --- Executes during object creation, after setting all properties.
function s_CreateFcn(hObject, eventdata, handles)
% hObject    handle to Th1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

function updateData()

sliderVal_1 = evalin('base', 'sliderVal_1');
sliderVal_2 = evalin('base', 'sliderVal_2');
sliderVal_3 = evalin('base', 'sliderVal_3');
sliderVal_4 = evalin('base', 'sliderVal_4');
sliderVal_5 = evalin('base', 'sliderVal_5');
sliderVal_6 = evalin('base', 'sliderVal_6');

L1 = 83;
L2 = 190;
L3 = 50;
L4 = 172;
L5 = 88;

an1 = sliderVal_1*pi/180;
an2 = sliderVal_2*pi/180;
an3 = sliderVal_3*pi/180;
an4 = sliderVal_4*pi/180;
an5 = sliderVal_5*pi/180;
an6 = sliderVal_6*pi/180;

At_x = L2*cos(an1).*cos(an2) - L4*sin(an2 + an3).*cos(an1) - L3*sin(an1) - L5*sin(an2 + an3).*cos(an1).*cos(an5) + L5*sin(an1).*sin(an4).*sin(an5) + L5*cos(an1).*cos(an4).*sin(an2).*sin(an3).*sin(an5) - L5*cos(an1).*cos(an2).*cos(an3).*cos(an4).*sin(an5);
At_y = L3*cos(an1) - L4*sin(an2 + an3).*sin(an1) + L2*cos(an2).*sin(an1) - L5*sin(an2 + an3).*cos(an5).*sin(an1) - L5*cos(an1).*sin(an4).*sin(an5) - L5*cos(an2).*cos(an3).*cos(an4).*sin(an1).*sin(an5) + L5*cos(an4).*sin(an1).*sin(an2).*sin(an3).*sin(an5);
At_z = L1 + L4*cos(an2 + an3) + L2*sin(an2) - (L5*sin(an2 + an3).*sin(an4 + an5))/2 + L5*cos(an2 + an3).*cos(an5) + (L5*sin(an4 - an5).*sin(an2 + an3))/2;

assignin('base','PosX',At_x);
assignin('base','PosY',At_y);
assignin('base','PosZ',At_z);

L(1) = Link([0,L1,0,pi/2]);
L(2) = Link([0,0,L2,0]);
L(3) = Link([0,-L3,0,-pi/2]);
L(4) = Link([0,L4,0,pi/2]);
L(5) = Link([0,0,0,-pi/2]);
L(6) = Link([0,L5,0,0]);

Robot = SerialLink(L);
Robot.name = 'QAVAH';
Robot.plot([an1 an2 an3 an4 an5 an6])

% --- Executes on slider movement.
function slider10_Callback(hObject, eventdata, handles)
% hObject    handle to Th5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'Value') returns position of slider
%        get(hObject,'Min') and get(hObject,'Max') to determine range of slider


% --- Executes during object creation, after setting all properties.
function Th5_CreateFcn(hObject, eventdata, handles)
% hObject    handle to Th5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: slider controls usually have a light gray background.
if isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor',[.9 .9 .9]);
end



function q1_Callback(hObject, eventdata, handles)
% hObject    handle to q1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of q1 as text
%        str2double(get(hObject,'String')) returns contents of q1 as a double

% --- Executes during object creation, after setting all properties.
function q1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to q1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function q2_Callback(hObject, eventdata, handles)
% hObject    handle to q2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of q2 as text
%        str2double(get(hObject,'String')) returns contents of q2 as a double


% --- Executes during object creation, after setting all properties.
function q2_CreateFcn(hObject, eventdata, handles)
% hObject    handle to q2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function q3_Callback(hObject, eventdata, handles)
% hObject    handle to q3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of q3 as text
%        str2double(get(hObject,'String')) returns contents of q3 as a double


% --- Executes during object creation, after setting all properties.
function q3_CreateFcn(hObject, eventdata, handles)
% hObject    handle to q3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function q4_Callback(hObject, eventdata, handles)
% hObject    handle to q4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of q4 as text
%        str2double(get(hObject,'String')) returns contents of q4 as a double


% --- Executes during object creation, after setting all properties.
function q4_CreateFcn(hObject, eventdata, handles)
% hObject    handle to q4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function q5_Callback(hObject, eventdata, handles)
% hObject    handle to q5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of q5 as text
%        str2double(get(hObject,'String')) returns contents of q5 as a double


% --- Executes during object creation, after setting all properties.
function q5_CreateFcn(hObject, eventdata, handles)
% hObject    handle to q5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in Fw.
function Fw_Callback(hObject, eventdata, handles)
% hObject    handle to Fw (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
val_q1 = str2double(get(handles.q1,'string'));
assignin('base','sliderVal_1',val_q1);

val_q2 = str2double(get(handles.q2,'string'));
assignin('base','sliderVal_2',val_q2);

val_q3 = str2double(get(handles.q3,'string'));
assignin('base','sliderVal_3',val_q3);

val_q4 = str2double(get(handles.q4,'string'));
assignin('base','sliderVal_4',val_q4);

val_q5 = str2double(get(handles.q5,'string'));
assignin('base','sliderVal_5',val_q5);

val_q6 = str2double(get(handles.q6,'string'));
assignin('base','sliderVal_6',val_q6);

set(handles.Th1,'value',val_q1);
set(handles.Th2,'value',val_q2);
set(handles.Th3,'value',val_q3);
set(handles.Th4,'value',val_q4);
set(handles.Th5,'value',val_q5);
set(handles.Th6,'value',val_q6);

updateData();


% --- Executes on button press in Inv.
function Inv_Callback(hObject, eventdata, handles)
% hObject    handle to Inv (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Crear matriz de transformación homogenea con parámetros de DH
syms th d alph a
A = [cos(th) -cos(alph)*sin(th)  sin(alph)*sin(th) a*cos(th);
     sin(th)  cos(alph)*cos(th) -sin(alph)*cos(th) a*sin(th); 
     0        sin(alph)          cos(alph)         d; 
     0        0                   0                  1];

L1 = 83;
L2 = 190;
L3 = 50;
L4 = 172;
L5 = 88;

syms th1 th2 th3 th4 th5 th6
A01 = subs(A,{th,d,a,alph},{th1,L1,0,pi/2});
A12 = subs(A,{th,d,a,alph},{th2,0,L2,0});
A23 = subs(A,{th,d,a,alph},{th3,-L3,0,-pi/2});
A34 = subs(A,{th,d,a,alph},{th4,L4,0,pi/2});
A45 = subs(A,{th,d,a,alph},{th5,0,0,-pi/2});
A56 = subs(A,{th,d,a,alph},{th6,L5,0,0});
A06 = simplify(A01*A12*A23*A34*A45*A56);

xe = str2double(get(handles.Xf,'string'));
ye = str2double(get(handles.Yf,'string'));
ze = str2double(get(handles.Zf,'string'));
Y = str2double(get(handles.Yaw,'string'));
P = str2double(get(handles.Pitch,'string'));
R = str2double(get(handles.Roll,'string'));
Y = Y*pi/180; P = P*pi/180; R = R*pi/180;
% Proponer matriz deseada

Rx = [1      0       0;
      0 cos(Y) -sin(Y);
      0 sin(Y)  cos(Y)]
  
Ry = [ cos(P) 0 sin(P);
           0  1      0;
      -sin(P) 0 cos(P)]
  
Rz = [cos(R) -sin(R) 0;
      sin(R)  cos(R) 0;
           0      0  1]
       
Rs = Rx*Ry*Rz

Md = [Rs(1,1)  Rs(1,2)  Rs(1,3)   xe;
      Rs(2,1)  Rs(2,2)  Rs(2,3)   ye;
      Rs(3,1)  Rs(3,2)  Rs(3,3)   ze;
            0        0        0   1.0000]

nxd = Md(1,1);
nyd = Md(2,1);
nzd = Md(3,1);
sxd = Md(1,2);
syd = Md(2,2);
szd = Md(3,2);
axd = Md(1,3);
ayd = Md(2,3);
azd = Md(3,3);
xfd = Md(1,4);
yfd = Md(2,4);
zfd = Md(3,4);

% Calcular Th1

syms nx ny nz
syms sx sy sz
syms ax ay az
syms dx dy dz

A04 = [nx sx ax dx;
       ny sy ay dy;
       nz sz az dz;
       0  0  0  1];

xm = xfd - L5*axd;
ym = yfd - L5*ayd;
zm = zfd - L5*azd;

T_a = simplify(inv(A01)*A04);
T_d = simplify(A12*A23*A34);

f0 = T_a(3,4) == T_d(3,4);
q1 = subs(f0,{dx,dy},{xm,ym});
q1 = vpa(double(solve(q1,th1)));
q1 = double(real(q1));

% Calcular Th2 y Th3

f1 = T_a(2,4) == T_d(2,4);
f2 = T_a(1,4) == T_d(1,4);

f1 = subs(f1,dz,zm);
f2_1 = subs(f2,{dx,dy,th1},{xm,ym,q1(1)});
f2_2 = subs(f2,{dx,dy,th1},{xm,ym,q1(2)});

[q2_1,q3_1] = solve(f1,f2_1,th2,th3);
[q2_2,q3_2] = solve(f1,f2_2,th2,th3);
q2_1 = double(q2_1);
q2_2 = double(q2_2);
q3_1 = double(q3_1);
q3_2 = double(q3_2);

q1 = repelem(q1,2);
q2 = [q2_1;q2_2];
q2 = real(q2);
q3 = [q3_1;q3_2];
q3 = real(q3);

% Calcular Th4

O_a = simplify(A45*A56);
O_d = simplify(inv(A01*A12*A23*A34)*A04);

f3 = O_a(3,3) == O_d(3,3);
f3 = subs(f3,{th1,th2,th3,ax,ay,az},{q1,q2,q3,axd,ayd,azd});

q4_1 = double(solve(f3(1),th4));
q4_2 = double(solve(f3(2),th4));
q4_3 = double(solve(f3(3),th4));
q4_4 = double(solve(f3(4),th4));
[r,c] = size(q4_1);

if r == 1
    q4_1 = repelem(q4_1,2)';
    q4_2 = repelem(q4_2,2)';
    q4_3 = repelem(q4_3,2)';
    q4_4 = repelem(q4_4,2)';
end

q1 = repelem(q1,2);
q2 = repelem(q2,2);
q3 = repelem(q3,2);
q4 = [q4_1;q4_2;q4_3;q4_4];
q4 = real(q4);

% Calcular Th5 y Th6

f4 = O_a(1,1) == O_d(1,1);
f5 = O_a(1,2) == O_d(1,2);

f4 = subs(f4,{th1,th2,th3,th4,nx,ny,nz},{q1,q2,q3,q4,nxd,nyd,nzd});
f5 = subs(f5,{th1,th2,th3,th4,sx,sy,sz},{q1,q2,q3,q4,sxd,syd,szd});
[q51,q61] = solve([f4(1),f5(1)],[th5,th6],'IgnoreAnalyticConstraints',true);
[q52,q62] = solve([f4(2),f5(2)],[th5,th6],'IgnoreAnalyticConstraints',true);
[q53,q63] = solve([f4(3),f5(3)],[th5,th6],'IgnoreAnalyticConstraints',true);
[q54,q64] = solve([f4(4),f5(4)],[th5,th6],'IgnoreAnalyticConstraints',true);
[q55,q65] = solve([f4(5),f5(5)],[th5,th6],'IgnoreAnalyticConstraints',true);
[q56,q66] = solve([f4(6),f5(6)],[th5,th6],'IgnoreAnalyticConstraints',true);
[q57,q67] = solve([f4(7),f5(7)],[th5,th6],'IgnoreAnalyticConstraints',true);
[q58,q68] = solve([f4(8),f5(8)],[th5,th6],'IgnoreAnalyticConstraints',true);
q5 = double([q51;q52;q53;q54;q55;q56;q57;q58]);
q6 = double([q61;q62;q63;q64;q65;q66;q67;q68]);
q1 = repelem(q1,2);
q2 = repelem(q2,2);
q3 = repelem(q3,2);
q4 = repelem(q4,2);

[r,c] = size(q5);

if r == 8
    q5 = repelem(q5,2);
end

[r,c] = size(q6);

if r == 8
    q6 = repelem(q6,2);
end

% Fórmulas de traslación

an1 = q1;
an2 = q2;
an3 = q3;
an4 = q4;
an5 = q5;
an6 = q6;
size(an1)
size(an2)
size(an3)
size(an4)
size(an5)
size(an6)
At_x = L2*cos(an1).*cos(an2) - L4*sin(an2 + an3).*cos(an1) - L3*sin(an1) - L5*sin(an2 + an3).*cos(an1).*cos(an5) + L5*sin(an1).*sin(an4).*sin(an5) + L5*cos(an1).*cos(an4).*sin(an2).*sin(an3).*sin(an5) - L5*cos(an1).*cos(an2).*cos(an3).*cos(an4).*sin(an5);
At_y = L3*cos(an1) - L4*sin(an2 + an3).*sin(an1) + L2*cos(an2).*sin(an1) - L5*sin(an2 + an3).*cos(an5).*sin(an1) - L5*cos(an1).*sin(an4).*sin(an5) - L5*cos(an2).*cos(an3).*cos(an4).*sin(an1).*sin(an5) + L5*cos(an4).*sin(an1).*sin(an2).*sin(an3).*sin(an5);
At_z = L1 + L4*cos(an2 + an3) + L2*sin(an2) - (L5*sin(an2 + an3).*sin(an4 + an5))/2 + L5*cos(an2 + an3).*cos(an5) + (L5*sin(an4 - an5).*sin(an2 + an3))/2;
eq = sqrt((xfd-At_x).^2+(yfd-At_y).^2+(zfd-At_z).^2);

% Recolectar ángulos

qT = [q1,q2,q3,q4,q5,q6];
qT = real(qT);
qTd = qT*180/pi;
[val,I] = min(eq);
qs = [qT(I,1),qT(I,2),qT(I,3),qT(I,4),qT(I,5),qT(I,6)];
qsd = [qTd(I,1),qTd(I,2),qTd(I,3),qTd(I,4),qTd(I,5),qTd(I,6)]
q1_inv = qsd(1);
q2_inv = qsd(2);
q3_inv = qsd(3);
q4_inv = qsd(4);
q5_inv = qsd(5);
q6_inv = qsd(6);

% Verificar resultado

A06_ev = subs(A06,{th1,th2,th3,th4,th5,th6},{qs(1),qs(2),qs(3),qs(4),qs(5),qs(6)});
A06_ev = vpa(simplify(A06_ev),6);
A06_ev = double(A06_ev)

assignin('base','sliderVal_1',q1_inv);
assignin('base','sliderVal_2',q2_inv);
assignin('base','sliderVal_3',q3_inv);
assignin('base','sliderVal_4',q4_inv);
assignin('base','sliderVal_5',q5_inv);
assignin('base','sliderVal_6',q6_inv);

set(handles.Th1,'value',q1_inv);
set(handles.Th2,'value',q2_inv);
set(handles.Th3,'value',q3_inv);
set(handles.Th4,'value',q4_inv);
set(handles.Th5,'value',q5_inv);
set(handles.Th6,'value',q6_inv);

set(handles.q1,'string',num2str(q1_inv));
set(handles.q2,'string',num2str(q2_inv));
set(handles.q3,'string',num2str(q3_inv));
set(handles.q4,'string',num2str(q4_inv));
set(handles.q5,'string',num2str(q5_inv));
set(handles.q6,'string',num2str(q6_inv));

updateData();

function Xf_Callback(hObject, eventdata, handles)
% hObject    handle to Xf (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of Xf as text
%        str2double(get(hObject,'String')) returns contents of Xf as a double


% --- Executes during object creation, after setting all properties.
function Xf_CreateFcn(hObject, eventdata, handles)
% hObject    handle to Xf (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function Yf_Callback(hObject, eventdata, handles)
% hObject    handle to Yf (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of Yf as text
%        str2double(get(hObject,'String')) returns contents of Yf as a double


% --- Executes during object creation, after setting all properties.
function Yf_CreateFcn(hObject, eventdata, handles)
% hObject    handle to Yf (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

function Zf_Callback(hObject, eventdata, handles)
% hObject    handle to Zf (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of Zf as text
%        str2double(get(hObject,'String')) returns contents of Zf as a double


% --- Executes during object creation, after setting all properties.
function Zf_CreateFcn(hObject, eventdata, handles)
% hObject    handle to Zf (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on slider movement.
function Th6_Callback(hObject, eventdata, handles)
% hObject    handle to Th6 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'Value') returns position of slider
%        get(hObject,'Min') and get(hObject,'Max') to determine range of slider
sliderVal_6 = get(hObject,'Value');
assignin('base','sliderVal_6',sliderVal_6);
set(handles.q6,'string',num2str(sliderVal_6));
updateData();

% --- Executes during object creation, after setting all properties.
function Th6_CreateFcn(hObject, eventdata, handles)
% hObject    handle to Th6 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: slider controls usually have a light gray background.
if isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor',[.9 .9 .9]);
end


function q6_Callback(hObject, eventdata, handles)
% hObject    handle to q6 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of q6 as text
%        str2double(get(hObject,'String')) returns contents of q6 as a double


% --- Executes during object creation, after setting all properties.
function q6_CreateFcn(hObject, eventdata, handles)
% hObject    handle to q6 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function Yaw_Callback(hObject, eventdata, handles)
% hObject    handle to Yaw (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of Yaw as text
%        str2double(get(hObject,'String')) returns contents of Yaw as a double


% --- Executes during object creation, after setting all properties.
function Yaw_CreateFcn(hObject, eventdata, handles)
% hObject    handle to Yaw (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function Pitch_Callback(hObject, eventdata, handles)
% hObject    handle to Pitch (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of Pitch as text
%        str2double(get(hObject,'String')) returns contents of Pitch as a double


% --- Executes during object creation, after setting all properties.
function Pitch_CreateFcn(hObject, eventdata, handles)
% hObject    handle to Pitch (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function Roll_Callback(hObject, eventdata, handles)
% hObject    handle to Roll (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of Roll as text
%        str2double(get(hObject,'String')) returns contents of Roll as a double


% --- Executes during object creation, after setting all properties.
function Roll_CreateFcn(hObject, eventdata, handles)
% hObject    handle to Roll (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end
