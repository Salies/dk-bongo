#define TIME 300
unsigned short timeout[2] = {TIME, TIME};
bool counting[2] = {false, false};
  
void setup()
{
  //Define a porta do led como saida
  Serial.begin(9600);
  //pinMode(11, OUTPUT);
  //pinMode(3, INPUT);
}
  
void loop()
{
  // se o timeout já estiver esgotado, reseta e conta de novo
  if(analogRead(A2) > 400 && timeout[0] >= TIME) {
    Serial.print("A");
    timeout[0] = 0;
    counting[0] = true;
  }

  // está no timeout
  if(counting[0] && timeout[0] < TIME) {
    timeout[0]++;
  }

  // timeout deu 100, para de contar
  if(counting[0] && timeout[0] >= TIME) {
    counting[0] = false;
  }
}