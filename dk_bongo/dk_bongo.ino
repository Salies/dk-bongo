#define TIME 300
unsigned short timeout[2] = {TIME, TIME};
bool counting[2] = {false, false};
//String msg;
  
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
  if(analogRead(A2) > 0 && timeout[0] >= TIME) {
    Serial.print("R");
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

  if(analogRead(A4) > 300 && timeout[1] >= TIME) {
    Serial.print("L");
    timeout[1] = 0;
    counting[1] = true;
  }

  // está no timeout
  if(counting[1] && timeout[1] < TIME) {
    timeout[1]++;
  }

  // timeout deu 100, para de contar
  if(counting[1] && timeout[1] >= TIME) {
    counting[1] = false;
  }
}