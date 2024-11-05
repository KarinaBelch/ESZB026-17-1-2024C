/* Programa baseado no codigo disponibilizado em:
* Derek Molloy, Exploring Raspberry Pi: Interfacing to the Real World with Embedded Linux,
* Wiley 2016, ISBN 978-1-119-1868-1, http://www.exploringrpi.com/ */

#include<wiringPi.h>
#include<stdio.h>
#include<fcntl.h>
#include<unistd.h>
#include<termios.h>
#include<string.h>
#include<stdlib.h>
#include<softPwm.h>


int main(int argc, char *argv[]){
   int file, count, valor;

   if ((file = open("/dev/ttyACM0", O_RDWR | O_NOCTTY | O_NDELAY))<0){
      perror("Falha ao abrir o arquivo.\n");
      return -1;
   }
   
   struct termios options;
   tcgetattr(file, &options);
   options.c_cflag = B115200 | CS8 | CREAD | CLOCAL;
   options.c_iflag = IGNPAR | ICRNL;
   tcflush(file, TCIFLUSH);
   tcsetattr(file, TCSANOW, &options);
   
   
   int pino_PWM = 23; 
   int brilho;
	int range = 100;
   wiringPiSetupGpio();
   pinMode(pino_PWM,OUTPUT);
   softPwmCreate(pino_PWM, 1, range);
   
   while (1){{
      
      unsigned char receive[100];
      if ((count = read(file, (void*)receive, 100))<0){
         perror("Falha ao ler da entrada.\n");
         return -1;
      }
      if (count==0) printf("Nao havia dados para led.\n");
      else {
         receive[count]=0;  // o Arduino nao envia o caractere nulo (\0=0)
         // ler o valor de dentro do vetor de caracteres....
         int valor;
         valor = atoi(receive);
         //valor = valor/11;
         printf("Li valor %d\n",valor);
         
         // ajustar o pwm com esse valor
         
         brilho = valor *100.0 / 1023.0;
         softPwmWrite (pino_PWM, brilho);
         
         
		}
         
         
      }
      usleep(100000);
   }
   
   
   
   close(file);
   return 0;
}
