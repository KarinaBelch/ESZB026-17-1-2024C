#!/bin/bash

# script baseado no código disponibilizado em:
# Derek Molloy, Exploring Raspberry Pi: Interfacing to the Real World with Embedded Linux,
# Wiley 2016, ISBN 978-1-119-1868-1, http://www.exploringrpi.com/ oi

LED_AMAR=16  # Usar uma variavel facilita alteracoes futuras na porta usada
LED_VERM=20
LED_VERD=21

VALUE_VERM="/sys/class/gpio/gpio$LED_VERM/value"
VALUE_VERD="/sys/class/gpio/gpio$LED_VERD/value"
VALUE_AMAR="/sys/class/gpio/gpio$LED_AMAR/value"


# fazendo  o setup dos 3 LEDs
echo $LED_AMAR >> "/sys/class/gpio/export"
echo $LED_VERM >> "/sys/class/gpio/export"
echo $LED_VERD >> "/sys/class/gpio/export"

sleep 0.2

echo "out" >> "/sys/class/gpio/gpio$LED_AMAR/direction"
echo "out" >> "/sys/class/gpio/gpio$LED_VERM/direction"
echo "out" >> "/sys/class/gpio/gpio$LED_VERD/direction"

sleep 0.2

# acendendo o vermelho por 2 s
echo 1 >> $VALUE_VERM
sleep 2
echo 0 >> $VALUE_VERM

#acendendo o verde por 1s

echo 1 >> $VALUE_VERD
sleep 1
echo 0 >> $VALUE_VERD

#acendendo o amarelo por 1s

echo 1 >> $VALUE_AMAR
sleep 1
echo 0 >> $VALUE_AMAR



# acendendo o vermelho por 2 s
echo 1 >> $VALUE_VERM
sleep 2
echo 0 >> $VALUE_VERM

#acendendo o verde por 1s

echo 1 >> $VALUE_VERD
sleep 1
echo 0 >> $VALUE_VERD

#acendendo o amarelo por 1s

echo 1 >> $VALUE_AMAR
sleep 1
echo 0 >> $VALUE_AMAR

# acendendo o vermelho por 2 s
echo 1 >> $VALUE_VERM
sleep 2
echo 0 >> $VALUE_VERM

#acendendo o verde por 1s

echo 1 >> $VALUE_VERD
sleep 1
echo 0 >> $VALUE_VERD

#acendendo o amarelo por 1s

echo 1 >> $VALUE_AMAR
sleep 1
echo 0 >> $VALUE_AMAR

# acendendo o vermelho por 2 s
echo 1 >> $VALUE_VERM
sleep 2
echo 0 >> $VALUE_VERM

#acendendo o verde por 1s

echo 1 >> $VALUE_VERD
sleep 1
echo 0 >> $VALUE_VERD

#acendendo o amarelo por 1s

echo 1 >> $VALUE_AMAR
sleep 1
echo 0 >> $VALUE_AMAR

# acendendo o vermelho por 2 s
echo 1 >> $VALUE_VERM
sleep 2
echo 0 >> $VALUE_VERM

#acendendo o verde por 1s

echo 1 >> $VALUE_VERD
sleep 1
echo 0 >> $VALUE_VERD

#acendendo o amarelo por 1s

echo 1 >> $VALUE_AMAR
sleep 1
echo 0 >> $VALUE_AMAR

# acendendo o vermelho por 2 s
echo 1 >> $VALUE_VERM
sleep 2
echo 0 >> $VALUE_VERM

#acendendo o verde por 1s

echo 1 >> $VALUE_VERD
sleep 1
echo 0 >> $VALUE_VERD

#acendendo o amarelo por 1s

echo 1 >> $VALUE_AMAR
sleep 1
echo 0 >> $VALUE_AMAR



#FECHAR


echo $LED_VERM >> "/sys/class/gpio/unexport"
echo $LED_VERD >> "/sys/class/gpio/unexport"
echo $LED_AMAR >> "/sys/class/gpio/unexport"



