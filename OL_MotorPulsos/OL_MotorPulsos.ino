// Si desea abrir la terminal en Ubuntu correr lo siguiente en su terminal:
//
// Para verificar que el arduino se encuentra conectado: ls -l /dev/ttyACM*
//
//                                                     : sudo usermod -a -G dialout aaron
//
//                                                     : sudo chmod a+rw /dev/ttyACM0
//

// Puente H
#define PWM 5

// Terminales digitales del encoder
int MOTOR_A_PIN = 6;
int MOTOR_B_PIN = 7;

// Variable donde se gurada el PWM
volatile int pulse_width = 0;

// Variable que se utiliza para indicar cuando se da la entrada escalón
int escalon = 0;

// Indicar los puertos de entrada de las señales del encoder
int A = 2;
int B = 3;
const int potenciometro = A1; // Referencia

// Inicializar variables
volatile long pulsos = 0; // Cantidad de pulsos del encoder dados
unsigned long cM = 0; // Tiempo actual transcurrido
unsigned long lM = 0; // Tiempo anterior transcurrido
double T = 0.008; // Tiempo de muestreo
int ang_pos = 0; // Entrada analógica del potenciometro
volatile float ang_ref1 = 0; // Referencia de ángulo

void setup() {

  // Comenzar la comunicación serial
  Serial.begin(115200);

  // Indicar la entrada del potenciometro
  pinMode(potenciometro, INPUT);
  
  // Indicar que A y B son entradas
  pinMode(A, INPUT);
  pinMode(B, INPUT);


  // Configuración de salidas para el motor
  pinMode(PWM, OUTPUT);
  pinMode(MOTOR_A_PIN, OUTPUT);
  pinMode(MOTOR_B_PIN, OUTPUT);
  pinMode(LED_BUILTIN, OUTPUT);

  // Crear la interrupción que se genera cuando hay un pulso en el encoder
  attachInterrupt(digitalPinToInterrupt(A), contar, FALLING);

}

void contar() {
  // Esta función permite incrementar el pulso en 1 cuando se detecta
  // un flanco descendente en la salida A del encoder

  // Incrementar el pulso en 1
  pulsos++;
}

void loop() {
  // Se lee el valor de voltaje proveniente del potenciómetro y se guarda en la variable ang_pos
  ang_pos = analogRead(potenciometro);
  // Se mapea el valor del potenciometro a ángulo (0° a 360°)
  ang_ref1 = map(ang_pos, 0, 1023, 0, 359);

  // Si el potenciometro esta en un rango el PWM es 0, si no es 50%
  // El escalón cambia dependiendo en que valor de PWM se encuentre
  if (ang_ref1 >= 0 && ang_ref1 < 180) {
    pulse_width = 0;
    escalon = 1;
    pulsos = 0;
  }
  if (ang_ref1 >= 180 && ang_ref1 < 359) {
    pulse_width = 128;
    escalon = 0;
  }

  // Se indica la dirección y el PWM con el que el motor se mueve
  digitalWrite(MOTOR_A_PIN, LOW);
  digitalWrite(MOTOR_B_PIN, HIGH);
  digitalWrite(LED_BUILTIN, LOW);
  analogWrite(PWM, pulse_width);

  // Se calcula el tiempo transcurrido
  cM = millis();

  // Si el tiempo transcurrido es mayor al tiempo de muestreo
  if (cM - lM >= (T * 1000)) {
    lM = cM;
  // Se imprimen los pulsos dados en cierto tiempo (T)
    Serial.print(pulsos);
    Serial.println(escalon);
    pulsos = 0;
  }

}
