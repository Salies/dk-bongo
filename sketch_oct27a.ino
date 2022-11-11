// Programa : Pisque um LED
// Autor : FILIPEFLOP
  
void setup()
{
  //Define a porta do led como saida
  Serial.begin(9600);
  //pinMode(11, OUTPUT);
  //pinMode(3, INPUT);
}
  
void loop()
{
  if(analogRead(A2) > 400)
    Serial.print("A");

  //Acende o led
    
  /*if(analogRead(A2) == HIGH){
    digitalWrite(11, HIGH);
    Serial.print("A");
  }
  else{
    digitalWrite(11, LOW);
  }*/
}