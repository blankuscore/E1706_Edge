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

void setup (){ 
  PCMSK2 |= bit (PCINT18);  // PCINTxx where D2 -> PCINT18
  PCMSK2 |= bit (PCINT19)   // PCINTxx where D3 -> PCINT19
  PCIFR  |= bit (PCIF2);    // clear any outstanding interrupts
  PCICR  |= bit (PCIE2);    // enable pin change interrupts for D0 to D7
  pinMode (2, INPUT_PULLUP);
  pinMode (3, INPUT_PULLUP);
}

void loop (){
}