#include <Arduino.h>

#define MASTER_EN 8

int surge_count;
int tov_count;

ISR (PCINT2_vect) {
    if(PIND & bit(2)){ //if D2 was interrupted
        surge_count = surge_count + 1; //increment surge count
        delay(1000);
    } else if(PIND & bit(3)){ //if D3 was interrupted 
        tov_count = tov_count + 1; //increment tov count
        delay(1000);
    }
}

void setup(){
    pinMode(MASTER_EN, OUTPUT);
    digitalWrite(MASTER_EN, LOW);
    
    surge_count = 0; tov_count = 0;

    PCMSK2 |= bit(PCINT18);  // PCINTxx where D2 -> PCINT18
    PCMSK2 |= bit(PCINT19);  // PCINTxx where D3 -> PCINT19
    PCIFR  |= bit(PCIF2);    // clear any outstanding interrupts
    PCICR  |= bit(PCIE2);    // enable pin change interrupts for D0 to D7
    pinMode (2, INPUT_PULLUP);// set pin 2 as surge interrupt input 
    pinMode (3, INPUT_PULLUP);// set pin 3 as tov interrupt input

    for(int i = 4; i < 11; i++){  // intialize 7 modules from D4 through D10
        pinMode(i, INPUT);
    }

    Serial.begin(9600);
}

void loop() {
    digitalWrite(MASTER_EN, HIGH);

    Serial.println("S");
    Serial.println(surge_count);
    
    Serial.println("T");
    Serial.println(tov_count);

    Serial.println("C");
    Serial.println(1);

    Serial.println("M");
    for(int i = 4; i < 11; i++){
        if(digitalRead(i) == true){
            Serial.print(0);
        } else {
            Serial.print(1);
        }
    }

    Serial.println("L");
    for(int i = 11; i < 14; i++){
        if(digitalRead(i) == false){
            Serial.print(0);
        } else {
            Serial.print(1);
        }
    }
}