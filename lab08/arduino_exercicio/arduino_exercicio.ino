const int analogInPin = A0;            // o potenciômetro esta ligado ao pino A0
int iniciaColeta = 0;
int tempo_delay = 200;
char charRecebido;                     // cria uma variavel para armazenar o caractere recebido

void setup(){
   // Configura a serial: baud rate de 115200, 8-bit, sem paridade, 1 stop bit
   Serial.begin(115200, SERIAL_8N1);
}

void loop(){
   if (Serial.available()){            // verifica se recebeu algum comando
      charRecebido = Serial.read();    // le o caractere recebido
      switch ( charRecebido ){
          case 'i':                    // inicia coleta
             iniciaColeta = 1;
             break;
             
          case 'p':                    // para a coleta
             iniciaColeta = 0;
             break;
          
          case 'm':
              Serial.write(tempo_delay & 0xFF);          // envia byte menos significativo
              Serial.write(tempo_delay >> 8);            // envia byte mais significativo
              break;
          
          case 'a':
              tempo_delay = tempo_delay + 5;
              break;
          
          case 'd':
              tempo_delay = tempo_delay - 5;
              break;
          
             
          default:                     // outro comando, ignora...
             break;
      }
   }
   if ( iniciaColeta == 1 ){
       int valor = analogRead(analogInPin); // le valor no pino A0 usando conversor ADC de 10-bit
       Serial.write(valor & 0xFF);          // envia byte menos significativo
       Serial.write(valor >> 8);            // envia byte mais significativo
   }
   delay(tempo_delay);                          // aguarda 100ms
}
