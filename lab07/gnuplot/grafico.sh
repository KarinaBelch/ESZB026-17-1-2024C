#!/bin/sh
ARQUIVODADOS=/home/pi/ESZB026-17-1-2024C/lab07/gnuplot/dados3.txt
ARQUIVOSAIDA=/home/pi/ESZB026-17-1-2024C/lab07/gnuplot/dados3.png

gnuplot << EOF
set title "Dados 3"
set ylabel "Eixo Y"
set xlabel "Eixo X"
set terminal png
set output "$ARQUIVOSAIDA"
plot "$ARQUIVODADOS" \
     linecolor rgb '#f1bb13'  \
     linetype 4 \
     linewidth 1 \
     pointtype 3 \
     pointsize 1.0 \
     title "meus dados 3" \
     with linespoints
EOF

