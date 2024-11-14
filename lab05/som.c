#include <stdio.h>
#include <wiringPi.h>
#include <softPwm.h>

int main(){
	int pino_PWM = 18;                         // pwm por software na GPIO18
	float PWM_freq_Hz = 261.6;
	int intervalo = 20000;
	int i;
	int range = 100;
	int notas[4] = {0, 0, 0, 0};
	 
	
	wiringPiSetupGpio();                 	     // usar a numeracao GPIO, nao WPi
	pinMode(pino_PWM,OUTPUT);	       	   	   	 // configura GPIO18 como saida
	softPwmCreate(pino_PWM, 1, range);       	 // inicializa PWM por software
	
	
	for(i = 0; i <= 10; i++)
	{
		softPwmWrite(pino_PWM, PWM_freq_Hz);
		delay(intervalo);
		printf("%d", i);
		softPwmWrite(pino_PWM, 0);
	}
}

