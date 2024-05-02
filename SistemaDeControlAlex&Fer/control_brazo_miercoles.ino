#include <Servo.h>
// Si desea abrir la terminal en Ubuntu correr lo siguiente en su terminal:
//
// Para verificar que el arduino se encuentra conectado: ls -l /dev/ttyACM*
//
//                                                     : sudo usermod -a -G dialout aaron
//
//                                                     : sudo chmod a+rw /dev/ttyACM0
//
const int servoPin=13; //pin del servo

Servo myServo; // creo un objeto servo


//Indicar puertos PWM
int PWM_q1_1 = 9; //right //ya
int PWM_q1_2 = 10; //ya
int PWM_q2_1 = 11; //ya
int PWM_q2_2 = 12; // ya
int PWM_q3_1 = 44; //ya 
int PWM_q3_2 = 45;// ya
int PWM_q4 = 6; //ya
int PWM_q5 = 7;//ya
int PWM_q6 = 8;//ya
int PWM_on = 0;
int PWM_off = 0;

volatile int pulse_width = 0;
//pulsos por revolucion
//int ppr_q1 = 2600;
int ppr_q1 = 4320;
int ppr_grande = 5986;
int ppr_chico = 2441;

// Indicar los puertos de entrada de las señales del encoder
int A_q1 = 4; //Encoder A va al puerto 3 fisico
int B_q1 = 5; //Encoder B va al puerto 2 fisico por algun motivo

// int A_q2 = 22; son los de antes
// int B_q2 = 23;
int A_q2 = 2; //actualizados por conveniencia
int B_q2 = 3;


// int A_q3 = 18;
// int B_q3 = 24;
// int A_q4 = 19;
// int B_q4 = 25;
// int A_q5 = 20;
// int B_q5 = 26;
// int A_q6 = 21;
// int B_q6 = 27;

int A_q3 = 18; //modificados por conveniencia
int B_q3 = 19;
int A_q4 = 20;
int B_q4 = 21;
int A_q5 = 24;
int B_q5 = 25;
int A_q6 = 26;
int B_q6 = 27;

//Indicar terminales de motores
int MOTOR_A_PIN_q4 = 28;
int MOTOR_B_PIN_q4 = 29;
int MOTOR_A_PIN_q5 = 30;
int MOTOR_B_PIN_q5 = 31;
int MOTOR_A_PIN_q6 = 32;
int MOTOR_B_PIN_q6 = 33;

// // Indicar optos
// int op1 = A0;
// int op2 = A1;
// int op3 = A2;
// int op4 = A3;
// int op5 = A4;
// int op6 = A5;

int val1 = 0;
int val2 = 0;
int val3 = 0;
int val4 = 0;
int val5 = 0;
int val6 = 0;

// Indicar en que posición comienza el encoder y su valor anterior
volatile int pulsos_q1 = 0;
volatile int pulsos_q2 = 0;
volatile int pulsos_q3 = 0;
volatile int pulsos_q4 = 0;
volatile int pulsos_q5 = 0;
volatile int pulsos_q6 = 0;

char del = ',';
const int dataL = 7;
int data[dataL];
volatile int mode=0, q1 = 0, q2 = 0, q3 = 0, q4 = 0, q5 = 0, q6 = 0, origen = 0, q = 0, dir = 0, gripper=0;
volatile int q1_en = 0, q2_en = 0, q3_en = 0, q4_en = 0, q5_en = 0, q6_en = 0;
volatile int origen_pasado = 0;
String str = "";


////---------------Variables del controlador PID
float T = 0.01;                 //Tiempo de muestreo de la posición angular del motor
int vel = 100;
int vel_small = 200;

//Constantes del Motor q1
float Kc_1 = 10;
float Taui_1 = 0.04;
float Taud_1 = 0.006;

//Constantes de motor q2 y q3
float Kc_g = 23.4;   
float Taui_g = 0.032;
float Taud_g = 0.008;

//Constantes de motor q4
float Kc_q4 = 2;                //Constante proporcional   
float Taui_q4 = 0.012;          //Constante integral
float Taud_q4 = 0.4;            //Constante derivativa

//Constantes de motor q5 y q6
float Kc_q56 = 0.79;    
float Taui_q56 = 0.008;
float Taud_q56 = 0.45;

Servo servoMotor;

volatile float E_q1 = 0, E_q2 = 0, E_q3 = 0, E_q4 = 0, E_q5 = 0, E_q6 = 0;
volatile float Mk = 0;
volatile float Mk1_q1 = 0, E1_q1 = 0, E2_q1 = 0;
volatile float Mk1_q2 = 0, E1_q2 = 0, E2_q2 = 0;
volatile float Mk1_q3 = 0, E1_q3 = 0, E2_q3 = 0;
volatile float Mk1_q4 = 0, E1_q4 = 0, E2_q4 = 0;
volatile float Mk1_q5 = 0, E1_q5 = 0, E2_q5 = 0;
volatile float Mk1_q6 = 0, E1_q6 = 0, E2_q6 = 0;
volatile int limit_Mk = 100;

volatile float posicion_q1 = 0;     //Posición angular actual del motor variable de control
volatile float posicion_q2 = 0;
volatile float posicion_q3 = 0;
volatile float posicion_q4 = 0;
volatile float posicion_q5 = 0;
volatile float posicion_q6 = 0;
float BC1_q4 = 0;
float BC2_q4 = 0;
float BC3_q4 = 0;
float BC1_q56 = 0;
float BC2_q56 = 0;
float BC3_q56 = 0;
float BC1_g = 0;
float BC2_g = 0;
float BC3_g = 0;
float BC1_1 = 0;
float BC2_1 = 0;
float BC3_1 = 0;

unsigned long tiempoAnterior = 0;

void setup() {
  
  // Comenzar la comunicación serial
  Serial.begin(115200);
  Serial3.begin(115200);

  TCCR4B = TCCR4B & B11111000 | B00000010;  // for PWM frequency of 3921.16 Hz
  
  // Indicar que A y B son entradas
  pinMode(A_q1, INPUT);
  pinMode(B_q1, INPUT);
  pinMode(A_q2, INPUT);
  pinMode(B_q2, INPUT);
  pinMode(A_q3, INPUT);
  pinMode(B_q3, INPUT);
  pinMode(A_q4, INPUT);
  pinMode(B_q4, INPUT);
  pinMode(A_q5, INPUT);
  pinMode(B_q5, INPUT);
  pinMode(A_q6, INPUT);
  pinMode(B_q6, INPUT);

  // pinMode(op1, INPUT);
  // pinMode(op2, INPUT);
  // pinMode(op3, INPUT);
  // pinMode(op4, INPUT);
  // pinMode(op5, INPUT);
  // pinMode(op6, INPUT);

  pinMode(MOTOR_A_PIN_q4, OUTPUT);
  pinMode(MOTOR_B_PIN_q4, OUTPUT);
  pinMode(MOTOR_A_PIN_q5, OUTPUT);
  pinMode(MOTOR_B_PIN_q5, OUTPUT);
  pinMode(MOTOR_A_PIN_q6, OUTPUT);
  pinMode(MOTOR_B_PIN_q6, OUTPUT);
  
  // Configuración de salidas para el encoder
  pinMode(PWM_q1_1, OUTPUT);
  pinMode(PWM_q1_2, OUTPUT);
  pinMode(PWM_q2_1, OUTPUT);
  pinMode(PWM_q2_2, OUTPUT);
  pinMode(PWM_q3_1, OUTPUT);
  pinMode(PWM_q3_2, OUTPUT);
  pinMode(PWM_q4, OUTPUT);
  pinMode(PWM_q5, OUTPUT);
  pinMode(PWM_q6, OUTPUT);

  // Crear la interrupción de flancos negativos en q1
  attachInterrupt(digitalPinToInterrupt(A_q1), contar_q1, FALLING);
  attachInterrupt(digitalPinToInterrupt(A_q2), contar_q2, FALLING);
  attachInterrupt(digitalPinToInterrupt(A_q3), contar_q3, FALLING);
  attachInterrupt(digitalPinToInterrupt(A_q4), contar_q4, FALLING);
  attachInterrupt(digitalPinToInterrupt(A_q5), contar_q5, FALLING);
  attachInterrupt(digitalPinToInterrupt(A_q6), contar_q6, FALLING);

  // Coeficientes de ecuación de diferencias de PID
  BC1_1 = Kc_1 * (1 + (T / Taui_1) + (Taud_1 / T));
  BC2_1 = Kc_1 * (-1 - (2 * Taud_1 / T));
  BC3_1 = Kc_1 * Taud_1 / T;

  BC1_g = Kc_g * (1 + (T / Taui_g) + (Taud_g / T));
  BC2_g = Kc_g * (-1 - (2 * Taud_g / T));
  BC3_g = Kc_g * Taud_g / T;
  
  BC1_q4 = Kc_q4 * (1 + (T / Taui_q4) + (Taud_q4 / T));
  BC2_q4 = Kc_q4 * (-1 - (2 * Taud_q4 / T));
  BC3_q4 = Kc_q4 * Taud_q4 / T;

  BC1_q56 = Kc_q56 * (1 + (T / Taui_q56) + (Taud_q56 / T));
  BC2_q56 = Kc_q56 * (-1 - (2 * Taud_q56 / T));
  BC3_q56 = Kc_q56 * Taud_q56 / T;

  // Iniciamos el servo para que empiece a trabajar con el pin 9
  myServo.attach(servoPin);
  myServo.write(70); //inicia en abierto
}

void contar_q1() {
  // Verificar en que sentido gira el motor y agregar pulsos
  if (digitalRead(B_q1) == HIGH) {
    pulsos_q1++;
  }
  else {
    pulsos_q1--;
  }

  // Si el pulso es igual a -ppr, el pulso se reestablece como 0
  if (pulsos_q1 == -ppr_q1) {
    pulsos_q1 = 0;
  }

  // Si el pulso es menor a 0, el pulso se reescribe en rango de 0 a ppr
  if (pulsos_q1 < 0) {
    pulsos_q1 = pulsos_q1 + ppr_q1;
  }

  // Si el pulso es igual a ppr, el pulso se reestablece como 0
  if (pulsos_q1 == ppr_q1) {
    pulsos_q1 = 0;
  }
  //Serial.println(pulsos_q1);
  // Convertir la cantidad de pulsos en un ángulo en el rango de 0° a 360°
  posicion_q1 = map(pulsos_q1, 0, ppr_q1, 0, 360);
}

void contar_q2() {
  // Verificar en que sentido gira el motor y agregar pulsos
  if (digitalRead(B_q2) == HIGH) {
    pulsos_q2--;
  }
  else {
    pulsos_q2++;
  }

  // Si el pulso es igual a -ppr, el pulso se reestablece como 0
  if (pulsos_q2 == -ppr_grande) {
    pulsos_q2 = 0;
  }

  // Si el pulso es menor a 0, el pulso se reescribe en rango de 0 a ppr
  if (pulsos_q2 < 0) {
    pulsos_q2 = pulsos_q2 + ppr_grande;
  }

  // Si el pulso es igual a ppr, el pulso se reestablece como 0
  if (pulsos_q2 == ppr_grande) {
    pulsos_q2 = 0;
  }

  // Convertir la cantidad de pulsos en un ángulo en el rango de 0° a 360°
  posicion_q2 = map(pulsos_q2, 0, ppr_grande, 0, 360);
}

void contar_q3() {
  // Verificar en que sentido gira el motor y agregar pulsos
  if (digitalRead(B_q3) == HIGH) {
    pulsos_q3--;
  }
  else {
    pulsos_q3++;
  }

  // Si el pulso es igual a -ppr, el pulso se reestablece como 0
  if (pulsos_q3 == -ppr_grande) {
    pulsos_q3 = 0;
  }

  // Si el pulso es menor a 0, el pulso se reescribe en rango de 0 a ppr
  if (pulsos_q3 < 0) {
    pulsos_q3 = pulsos_q3 + ppr_grande;
  }

  // Si el pulso es igual a ppr, el pulso se reestablece como 0
  if (pulsos_q3 == ppr_grande) {
    pulsos_q3 = 0;
  }

  // Convertir la cantidad de pulsos en un ángulo en el rango de 0° a 360°
  posicion_q3 = map(pulsos_q3, 0, ppr_grande, 0, 360);
}

void contar_q4() { //regresar a ppr_chico
  // Verificar en que sentido gira el motor y agregar pulsos
  if (digitalRead(B_q4) == HIGH) {
    pulsos_q4--;
  }
  else {
    pulsos_q4++;
  }

  // Si el pulso es igual a -ppr, el pulso se reestablece como 0
  if (pulsos_q4 == -ppr_chico) {
    pulsos_q4 = 0;
  }

  // Si el pulso es menor a 0, el pulso se reescribe en rango de 0 a ppr
  if (pulsos_q4 < 0) {
    pulsos_q4 = pulsos_q4 + ppr_chico;
  }

  // Si el pulso es igual a ppr, el pulso se reestablece como 0
  if (pulsos_q4 == ppr_chico) {
    pulsos_q4 = 0;
  }

  // Convertir la cantidad de pulsos en un ángulo en el rango de 0° a 360°
  posicion_q4 = map(pulsos_q4, 0, ppr_chico, 0, 360);
  //Serial.println(pulsos_q4);
}

void contar_q5() {
  // Verificar en que sentido gira el motor y agregar pulsos
  if (digitalRead(B_q5) == HIGH) {
    pulsos_q5++;
  }
  else {
    pulsos_q5--;
  }

  // Si el pulso es igual a -ppr, el pulso se reestablece como 0
  if (pulsos_q5 == -ppr_chico) {
    pulsos_q5 = 0;
  }

  // Si el pulso es menor a 0, el pulso se reescribe en rango de 0 a ppr
  if (pulsos_q5 < 0) {
    pulsos_q5 = pulsos_q5 + ppr_chico;
  }

  // Si el pulso es igual a ppr, el pulso se reestablece como 0
  if (pulsos_q5 == ppr_chico) {
    pulsos_q5 = 0;
  }

  // Convertir la cantidad de pulsos en un ángulo en el rango de 0° a 360°
  posicion_q5 = map(pulsos_q5, 0, ppr_chico, 0, 360);
}

void contar_q6() {
  // Verificar en que sentido gira el motor y agregar pulsos
  if (digitalRead(B_q6) == HIGH) {
    pulsos_q6--;
  }
  else {
    pulsos_q6++;
  }

  // Si el pulso es igual a -ppr, el pulso se reestablece como 0
  if (pulsos_q6 == -ppr_chico) {
    pulsos_q6 = 0;
  }

  // Si el pulso es menor a 0, el pulso se reescribe en rango de 0 a ppr
  if (pulsos_q6 < 0) {
    pulsos_q6 = pulsos_q6 + ppr_chico;
  }

  // Si el pulso es igual a ppr, el pulso se reestablece como 0
  if (pulsos_q6 == ppr_chico) {
    pulsos_q6 = 0;
  }

  // Convertir la cantidad de pulsos en un ángulo en el rango de 0° a 360°
  posicion_q6 = map(pulsos_q6, 0, ppr_chico, 0, 360);
}

void PID_q1(){
// Verificar el error entre la referencia y valor actual de ángulo, si es positivo gira en sentido horario,
// si es negativo gira en sentido anti-horario
// Se da la manipulación por el controlador PID
  if (E_q1 > 0){
    if ((360 - E_q1) <= E_q1){
      E_q1 = 360 - E_q1;
      PWM_on = PWM_q1_1;
      PWM_off = PWM_q1_2;
    }
    else if ((360 - E_q1) > E_q1){
      PWM_off = PWM_q1_1;
      PWM_on = PWM_q1_2;         
    }
    Mk = Mk1_q1 + BC1_1 * E_q1 + BC2_1 * E1_q1 + BC3_1 * E2_q1;
    if (Mk > limit_Mk) {Mk = limit_Mk;}
    if (Mk < 0) {Mk = 0;}
    pulse_width = map(Mk, 0, limit_Mk,10,vel);
    analogWrite(PWM_on, pulse_width);
    analogWrite(PWM_off, 0);
    }
    
   else if (E_q1 < 0){
    if ((360 + E_q1) <= abs(E_q1)){
      E_q1 = abs(360 + E_q1);
      PWM_off = PWM_q1_1;
      PWM_on = PWM_q1_2;
    }
    else if ((360 + E_q1) > abs(E_q1)){
      E_q1 = abs(E_q1);
      PWM_on = PWM_q1_1;
      PWM_off = PWM_q1_2;  
    }
    Mk = Mk1_q1 + BC1_1 * E_q1 + BC2_1 * E1_q1 + BC3_1 * E2_q1;
    if (Mk > limit_Mk) {Mk = limit_Mk;}
    if (Mk < 0) {Mk = 0;}
    pulse_width = map(Mk, 0, limit_Mk,40,vel);
    analogWrite(PWM_on, pulse_width);
    analogWrite(PWM_off, 0);
    }
    
   else {
    Mk = 0;
    pulse_width = map(Mk, 0, limit_Mk,40,vel);
    analogWrite(PWM_q1_1, pulse_width);
    analogWrite(PWM_q1_2, pulse_width);
    }

   Mk1_q1 = Mk;
   E2_q1 = E1_q1;
   E1_q1 = E_q1;
}

void PID_q2(){
// Verificar el error entre la referencia y valor actual de ángulo, si es positivo gira en sentido horario,
// si es negativo gira en sentido anti-horario
// Se da la manipulación por el controlador PID
  if (E_q2 > 0){
    if ((360 - E_q2) <= E_q2){
      E_q2 = 360 - E_q2;
      PWM_on = PWM_q2_2;
      PWM_off = PWM_q2_1;
    }
    else if ((360 - E_q2) > E_q2){
      PWM_off = PWM_q2_2;
      PWM_on = PWM_q2_1;         
    }
    Mk = Mk1_q2 + BC1_g * E_q2 + BC2_g * E1_q2 + BC3_g * E2_q2;
    if (Mk > limit_Mk) {Mk = limit_Mk;}
    if (Mk < 0) {Mk = 0;}
    pulse_width = map(Mk, 0, limit_Mk,40,180);
    analogWrite(PWM_on, pulse_width);
    analogWrite(PWM_off, 0);
    }
    
   else if (E_q2 < 0){
    if ((360 + E_q2) <= abs(E_q2)){
      E_q2 = abs(360 + E_q2);
      PWM_off = PWM_q2_2;
      PWM_on = PWM_q2_1;
    }
    else if ((360 + E_q2) > abs(E_q2)){
      E_q2 = abs(E_q2);
      PWM_on = PWM_q2_2;
      PWM_off = PWM_q2_1;  
    }
    Mk = Mk1_q2 + BC1_g * E_q2 + BC2_g * E1_q2 + BC3_g * E2_q2;
    if (Mk > limit_Mk) {Mk = limit_Mk;}
    if (Mk < 0) {Mk = 0;}
    pulse_width = map(Mk, 0, limit_Mk,40,180);
    analogWrite(PWM_on, pulse_width);
    analogWrite(PWM_off, 0);
    }
    
   else {
    Mk = 0;
    pulse_width = map(Mk, 0, limit_Mk,40,180);
    analogWrite(PWM_q2_2, pulse_width);
    analogWrite(PWM_q2_1, pulse_width);
    }

   Mk1_q2 = Mk;
   E2_q2 = E1_q2;
   E1_q2 = E_q2;
}

void PID_q3(){
// Verificar el error entre la referencia y valor actual de ángulo, si es positivo gira en sentido horario,
// si es negativo gira en sentido anti-horario
// Se da la manipulación por el controlador PID
  if (E_q3 > 0){
    if ((360 - E_q3) <= E_q3){
      E_q3 = 360 - E_q3;
      PWM_on = PWM_q3_2;
      PWM_off = PWM_q3_1;
    }
    else if ((360 - E_q3) > E_q3){
      PWM_off = PWM_q3_2;
      PWM_on = PWM_q3_1;         
    }
    Mk = Mk1_q3 + BC1_g * E_q3 + BC2_g * E1_q3 + BC3_g * E2_q3;
    if (Mk > limit_Mk) {Mk = limit_Mk;}
    if (Mk < 0) {Mk = 0;}
    pulse_width = map(Mk, 0, limit_Mk,40,vel);
    analogWrite(PWM_on, pulse_width);
    analogWrite(PWM_off, 0);
    }
    
   else if (E_q3 < 0){
    if ((360 + E_q3) <= abs(E_q3)){
      E_q3 = abs(360 + E_q3);
      PWM_off = PWM_q3_2;
      PWM_on = PWM_q3_1;
    }
    else if ((360 + E_q3) > abs(E_q3)){
      E_q3 = abs(E_q3);
      PWM_on = PWM_q3_2;
      PWM_off = PWM_q3_1;  
    }
    Mk = Mk1_q3 + BC1_g * E_q3 + BC2_g * E1_q3 + BC3_g * E2_q3;
    if (Mk > limit_Mk) {Mk = limit_Mk;}
    if (Mk < 0) {Mk = 0;}
    pulse_width = map(Mk, 0, limit_Mk,40,vel);
    analogWrite(PWM_on, pulse_width);
    analogWrite(PWM_off, 0);
    }
    
   else {
    Mk = 0;
    pulse_width = map(Mk, 0, limit_Mk,40,vel);
    analogWrite(PWM_q3_2, pulse_width);
    analogWrite(PWM_q3_1, pulse_width);
    }

   Mk1_q3 = Mk;
   E2_q3 = E1_q3;
   E1_q3 = E_q3;
}

void PID_q4(){
// Verificar el error entre la referencia y valor actual de ángulo, si es positivo gira en sentido horario,
// si es negativo gira en sentido anti-horario
// Se da la manipulación por el controlador PID
  if (E_q4 > 0){
    if ((360 - E_q4) <= E_q4){
      E_q4 = 360 - E_q4;
      digitalWrite(MOTOR_A_PIN_q4, HIGH);
      digitalWrite(MOTOR_B_PIN_q4, LOW);
    }
    else if ((360 - E_q4) > E_q4){
      digitalWrite(MOTOR_A_PIN_q4, LOW);
      digitalWrite(MOTOR_B_PIN_q4, HIGH);               
    }
    Mk = Mk1_q4 + BC1_q4 * E_q4 + BC2_q4 * E1_q4 + BC3_q4 * E2_q4;
    if (Mk > limit_Mk) {Mk = limit_Mk;}
    if (Mk < 0) {Mk = 0;}
    pulse_width = map(Mk, 0, limit_Mk,40,vel_small);
    analogWrite(PWM_q4, pulse_width);
    }
    
   else if (E_q4 < 0){
    if ((360 + E_q4) <= abs(E_q4)){
      E_q4 = abs(360 + E_q4);
      digitalWrite(MOTOR_A_PIN_q4, LOW);
      digitalWrite(MOTOR_B_PIN_q4, HIGH);
    }
    else if ((360 + E_q4) > abs(E_q4)){
      digitalWrite(MOTOR_A_PIN_q4, HIGH);
      digitalWrite(MOTOR_B_PIN_q4, LOW); 
      E_q4 = abs(E_q4);             
    }
    Mk = Mk1_q4 + BC1_q4 * E_q4 + BC2_q4 * E1_q4 + BC3_q4 * E2_q4;
    if (Mk > limit_Mk) {Mk = limit_Mk;}
    if (Mk < 0) {Mk = 0;}
    pulse_width = map(Mk, 0, limit_Mk,40,vel_small);
    analogWrite(PWM_q4, pulse_width);
    }
    
   else {
    Mk = 0;
    digitalWrite(MOTOR_A_PIN_q4, LOW);
    digitalWrite(MOTOR_B_PIN_q4, LOW);
    pulse_width = map(Mk, 0, limit_Mk,40,vel_small);
    analogWrite(PWM_q4, pulse_width);
    }

    Mk1_q4 = Mk;
    E2_q4 = E1_q4;
    E1_q4 = E_q4;
    
}

void PID_q5(){
// Verificar el error entre la referencia y valor actual de ángulo, si es positivo gira en sentido horario,
// si es negativo gira en sentido anti-horario
// Se da la manipulación por el controlador PID  
  if (E_q5 > 0){
    if ((360 - E_q5) <= E_q5){
      E_q5 = 360 - E_q5;
      digitalWrite(MOTOR_A_PIN_q5, LOW);
      digitalWrite(MOTOR_B_PIN_q5, HIGH);
    }
    else if ((360 - E_q5) > E_q5){
      digitalWrite(MOTOR_A_PIN_q5, HIGH);
      digitalWrite(MOTOR_B_PIN_q5, LOW);               
    }
    Mk = Mk1_q5 + BC1_q56 * E_q5 + BC2_q56 * E1_q5 + BC3_q56 * E2_q5;
    if (Mk > limit_Mk) {Mk = limit_Mk;}
    if (Mk < 0) {Mk = 0;}
    pulse_width = map(Mk, 0, limit_Mk,40,vel_small);
    analogWrite(PWM_q5, pulse_width);
    }
    
   else if (E_q5 < 0){
    if ((360 + E_q5) <= abs(E_q5)){
      E_q5 = abs(360 + E_q5);
      digitalWrite(MOTOR_A_PIN_q5, HIGH);
      digitalWrite(MOTOR_B_PIN_q5, LOW);
    }
    else if ((360 + E_q5) > abs(E_q5)){
      digitalWrite(MOTOR_A_PIN_q5, LOW);
      digitalWrite(MOTOR_B_PIN_q5, HIGH); 
      E_q5 = abs(E_q5);             
    }
    Mk = Mk1_q5 + BC1_q56 * E_q5 + BC2_q56 * E1_q5 + BC3_q56 * E2_q5;
    if (Mk > limit_Mk) {Mk = limit_Mk;}
    if (Mk < 0) {Mk = 0;}
    pulse_width = map(Mk, 0, limit_Mk,40,vel_small);
    analogWrite(PWM_q5, pulse_width);
    }
    
   else {
    Mk = 0;
    digitalWrite(MOTOR_A_PIN_q5, LOW);
    digitalWrite(MOTOR_B_PIN_q5, LOW);
    pulse_width = map(Mk, 0, limit_Mk,40,vel_small);
    analogWrite(PWM_q5, pulse_width);
    }

    Mk1_q5 = Mk;
    E2_q5 = E1_q5;
    E1_q5 = E_q5;
    
}

void PID_q6(){
// Verificar el error entre la referencia y valor actual de ángulo, si es positivo gira en sentido horario,
// si es negativo gira en sentido anti-horario
// Se da la manipulación por el controlador PID  
  if (E_q6 > 0){
    if ((360 - E_q6) <= E_q6){
      E_q6 = 360 - E_q6;
      digitalWrite(MOTOR_A_PIN_q6, HIGH);
      digitalWrite(MOTOR_B_PIN_q6, LOW);
    }
    else if ((360 - E_q6) > E_q6){
      digitalWrite(MOTOR_A_PIN_q6, LOW);
      digitalWrite(MOTOR_B_PIN_q6, HIGH);               
    }
    Mk = Mk1_q6 + BC1_q56 * E_q6 + BC2_q56 * E1_q6 + BC3_q56 * E2_q6;
    if (Mk > limit_Mk) {Mk = limit_Mk;}
    if (Mk < 0) {Mk = 0;}
    pulse_width = map(Mk, 0, limit_Mk,40,vel_small);
    analogWrite(PWM_q6, pulse_width);
    }
    
   else if (E_q6 < 0){
    if ((360 + E_q6) <= abs(E_q6)){
      E_q6 = abs(360 + E_q6);
      digitalWrite(MOTOR_A_PIN_q6, LOW);
      digitalWrite(MOTOR_B_PIN_q6, HIGH);
    }
    else if ((360 + E_q6) > abs(E_q6)){
      digitalWrite(MOTOR_A_PIN_q6, HIGH);
      digitalWrite(MOTOR_B_PIN_q6, LOW); 
      E_q6 = abs(E_q6);             
    }
    Mk = Mk1_q6 + BC1_q56 * E_q6 + BC2_q56 * E1_q6 + BC3_q56 * E2_q6;
    if (Mk > limit_Mk) {Mk = limit_Mk;}
    if (Mk < 0) {Mk = 0;}
    pulse_width = map(Mk, 0, limit_Mk,40,vel_small);
    analogWrite(PWM_q6, pulse_width);
    }
    
   else {
    Mk = 0;
    digitalWrite(MOTOR_A_PIN_q6, LOW);
    digitalWrite(MOTOR_B_PIN_q6, LOW);
    pulse_width = map(Mk, 0, limit_Mk,40,vel_small);
    analogWrite(PWM_q6, pulse_width);
    }

    Mk1_q6 = Mk;
    E2_q6 = E1_q6;
    E1_q6 = E_q6;
    
}

int angle=0;

void loop(){
  // Espera a que se introduzca la cadena desde la terminal
  // Verifica si hay datos disponibles en el puerto serial
  if (Serial.available()) {  
    str = Serial.readStringUntil(';');
    for(int i = 0; i < dataL; i++)
    {
      int index = str.indexOf(del);
      data[i] = str.substring(0, index).toInt();
      str = str.substring(index+1);
    }
    mode = data[0]; //1 - Cinemática directa, 2 - Activar Gripper
    q1 = data[1];
    q2 = data[2];
    q3 = data[3];
    q4 = data[4];
    q5 = data[5];
    q6 = data[6];
    gripper=data[7];
    origen = 1;
    q = 0;
    dir = 0;
    
    //Serial.println(q1);
  }

  if (mode == 3){ //Modo Gripper
    // Vamos a tener dos bucles uno para mover en sentido positivo y otro en sentido negativo
  // Para el sentido positivo
  Serial.println("Grippier Mode");
    if(q1==2){ //cierra
        Serial.println("Mode1");
        //angle = constrain(0,0,180);
        myServo.write(0);
        delay(10);
    }
    else if(q1==1){ //abre
        //angle = constrain(70,0,180);
        Serial.println("Mode0");
        myServo.write(70);
        delay(10);
    }
    mode=0;
  }
  else{ //Modo Cinemática

    //Verificar sub-rutina de búsqueda de origen
    if (origen == 1){

      //si se activa sub-rutina, se apagan todos los motores
      if(origen_pasado == 0){
        
        q1_en = 1;
        q2_en = 1;
        q3_en = 1;
        q4_en = 1;
        q5_en = 1;
        q6_en = 1;

      analogWrite(PWM_q1_1, 0);
      analogWrite(PWM_q1_2, 0);

      
      analogWrite(PWM_q2_1, 0);
      analogWrite(PWM_q2_2, 0);

      
      analogWrite(PWM_q3_1, 0);
      analogWrite(PWM_q3_2, 0);
      
      analogWrite(PWM_q4, 0);
      digitalWrite(MOTOR_A_PIN_q4, LOW);
      digitalWrite(MOTOR_B_PIN_q4, LOW);
      
      analogWrite(PWM_q5, 0);
      digitalWrite(MOTOR_A_PIN_q5, LOW);
      digitalWrite(MOTOR_B_PIN_q5, LOW);
    
      analogWrite(PWM_q6, 0);
      digitalWrite(MOTOR_A_PIN_q6, LOW);
      digitalWrite(MOTOR_B_PIN_q6, LOW);
        
      }

      //Verificar que articulación se intenta mover, y dentro de esta moverla en la dirección deseada.
      // Si se encuentra el origen, la posición se hace 0.
      switch(q){
        
        case 1:
        if(val1 < 1002 && q1_en == 0){
          if(dir == 1){
            analogWrite(PWM_q1_1, 100);
            analogWrite(PWM_q1_2, 0);
            }
          else if(dir == 2){
            analogWrite(PWM_q1_1, 0);
            analogWrite(PWM_q1_2, 100);
            }
          else if (dir == 0){
            analogWrite(PWM_q1_1, 0);
            analogWrite(PWM_q1_2, 0);
            }
        }
        else{
            analogWrite(PWM_q1_1, 0);
            analogWrite(PWM_q1_2, 0);
            pulsos_q1 = 0;
            posicion_q1 = 0;
            q1_en = 1;
        }
        break;
        
        case 2:
        if(val2 < 994 && q2_en == 0){
          if(dir == 1){
            analogWrite(PWM_q2_1, 120);
            analogWrite(PWM_q2_2, 0);
            }
          else if(dir == 2){
            analogWrite(PWM_q2_1, 0);
            analogWrite(PWM_q2_2, 120);
            }
          else if (dir == 0){
            analogWrite(PWM_q2_1, 0);
            analogWrite(PWM_q2_2, 0);
            }
        }
        else{
            analogWrite(PWM_q2_1, 0);
            analogWrite(PWM_q2_2, 0);
            pulsos_q2 = 0;
            posicion_q2 = 0;
            q2_en = 1;
        }
        break;
        
        case 3:
        if(val3 < 998 && q3_en == 0){
          if(dir == 1){
            analogWrite(PWM_q3_1, 100);
            analogWrite(PWM_q3_2, 0);
            }
          else if(dir == 2){
            analogWrite(PWM_q3_1, 0);
            analogWrite(PWM_q3_2, 100);
            }
          else if (dir == 0){
            analogWrite(PWM_q3_1, 0);
            analogWrite(PWM_q3_2, 0);
            }
        }
        else{
            analogWrite(PWM_q3_1, 0);
            analogWrite(PWM_q3_2, 0);
            pulsos_q3 = 0;
            posicion_q3 = 0;
            q3_en = 1;
        }
        break;

        case 4:
        if(val4 < 998 && q4_en == 0){
          if(dir == 1){
            analogWrite(PWM_q4, 200);
            digitalWrite(MOTOR_A_PIN_q4, HIGH);
            digitalWrite(MOTOR_B_PIN_q4, LOW);
            }
          else if(dir == 2){
            analogWrite(PWM_q4, 200);
            digitalWrite(MOTOR_A_PIN_q4, LOW);
            digitalWrite(MOTOR_B_PIN_q4, HIGH);
            }
          else if(dir == 0){
            analogWrite(PWM_q4, 0);
            digitalWrite(MOTOR_A_PIN_q4, LOW);
            digitalWrite(MOTOR_B_PIN_q4, LOW);
            }
        }
        else{
            analogWrite(PWM_q4, 0);
            digitalWrite(MOTOR_A_PIN_q4, LOW);
            digitalWrite(MOTOR_B_PIN_q4, LOW);
            pulsos_q4 = 0;
            posicion_q4 = 0;
            q4_en = 1; 
        }
        break;
        
        case 5:
        if(val5 < 995 && q5_en == 0){
            if(dir == 1){
            analogWrite(PWM_q5, 140);
            digitalWrite(MOTOR_A_PIN_q5, HIGH);
            digitalWrite(MOTOR_B_PIN_q5, LOW);
            }
          else if(dir == 2){
            analogWrite(PWM_q5, 140);
            digitalWrite(MOTOR_A_PIN_q5, LOW);
            digitalWrite(MOTOR_B_PIN_q5, HIGH);
            }
          else if(dir == 0){
            analogWrite(PWM_q5, 0);
            digitalWrite(MOTOR_A_PIN_q5, LOW);
            digitalWrite(MOTOR_B_PIN_q5, LOW);
            }
        }
        else{
            analogWrite(PWM_q5, 0);
            digitalWrite(MOTOR_A_PIN_q5, LOW);
            digitalWrite(MOTOR_B_PIN_q5, LOW);
            pulsos_q5 = 0;
            posicion_q5 = 0;
            q5_en = 1; 
        }
        break;
        
        case 6:
        if(val6 < 996 && q6_en == 0){
            if(dir == 1){
            analogWrite(PWM_q6, 140);
            digitalWrite(MOTOR_A_PIN_q6, HIGH);
            digitalWrite(MOTOR_B_PIN_q6, LOW);
            }
          else if(dir == 2){
            analogWrite(PWM_q6, 140);
            digitalWrite(MOTOR_A_PIN_q6, LOW);
            digitalWrite(MOTOR_B_PIN_q6, HIGH);
            }
          else if(dir == 0){
            analogWrite(PWM_q6, 0);
            digitalWrite(MOTOR_A_PIN_q6, LOW);
            digitalWrite(MOTOR_B_PIN_q6, LOW);
            }
        }
        else{
            analogWrite(PWM_q6, 0);
            digitalWrite(MOTOR_A_PIN_q6, LOW);
            digitalWrite(MOTOR_B_PIN_q6, LOW);
            pulsos_q6 = 0;
            posicion_q6 = 0;
            q6_en = 1;         
        }
        break;
      
      }
      
    }

    origen_pasado = origen;
    // Cada tiempo de muestreo, se repite el ciclo de control PID.
    if (millis() - tiempoAnterior > (T * 1000)){

      if(q1_en == 1){
        if(q1<0){
          q1 = ( 360 + q1 );
        }
        E_q1 = q1 - posicion_q1; 
        PID_q1();
        //Serial.println(E_q1);        
      }

      if(q2_en == 1){
        if(q2<0){
          q2 = ( 360 + q2 );
        }
        E_q2 = q2 - posicion_q2;
        PID_q2();
      }

      if(q3_en == 1){
        if(q3<0){
          q3 = ( 360 + q3 );
        }
        E_q3 = q3 - posicion_q3;
        PID_q3();  
      }

      if(q4_en == 1){ 
        if(q4<0){
            q4 = ( 360 + q4 );
        }  
        E_q4 = q4 - posicion_q4;
        //Serial.println(E_q4);
        PID_q4();
      }

      if(q5_en == 1){
        if(q5<0){
          q5 = ( 360 + q5 );
        }  
        E_q5 = q5 - posicion_q5;
        PID_q5();
      }

      if(q6_en == 1){
        if(q6<0){
          q6 = ( 360 + q6 );
        }
        E_q6 = q6 - posicion_q6;
        PID_q6();
      }

      tiempoAnterior = millis();
      
    }
  }
}
