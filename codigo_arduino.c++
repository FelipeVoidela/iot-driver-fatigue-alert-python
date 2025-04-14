const int pinLEDVerde = 12;
const int pinLEDVermelho = 11;
const int pinLEDAmarelo = 9; 
const int pinBuzzer = 10;

void setup() {
  pinMode(pinLEDVerde, OUTPUT);
  pinMode(pinLEDVermelho, OUTPUT);
  pinMode(pinLEDAmarelo, OUTPUT);
  pinMode(pinBuzzer, OUTPUT);

  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char comando = Serial.read();

    if (comando == 'G') {  // LED verde
      digitalWrite(pinLEDVerde, HIGH);
      digitalWrite(pinLEDVermelho, LOW);
      digitalWrite(pinLEDAmarelo, LOW);
      digitalWrite(pinBuzzer, LOW);
    }
    else if (comando == 'Y') {  // LED amarelo
      digitalWrite(pinLEDVerde, LOW);
      digitalWrite(pinLEDVermelho, LOW);
      digitalWrite(pinLEDAmarelo, HIGH);
      digitalWrite(pinBuzzer, LOW);
    }
    else if (comando == 'R') {  // LED vermelho + buzzer
      digitalWrite(pinLEDVerde, LOW);
      digitalWrite(pinLEDVermelho, HIGH);
      digitalWrite(pinLEDAmarelo, LOW);

      digitalWrite(pinBuzzer, HIGH);
      delay(1000);  // Buzzer por 1s
      digitalWrite(pinBuzzer, LOW);
    }
  }
}
