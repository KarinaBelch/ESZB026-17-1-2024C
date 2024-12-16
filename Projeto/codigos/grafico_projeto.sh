#!/bin/sh

ARQUIVODADOS="/home/vboxuser/Desktop/lab07/dados.txt"
ARQUIVOSAIDA="/home/vboxuser/Desktop/lab07/dados.png"

gnuplot << EOF
set title "Gráfico de SO2 por segundo"
set ylabel "SO2 (em %)"
set xlabel "Tempo (em segundos)"
set terminal png
set output "$ARQUIVOSAIDA"
plot "$ARQUIVODADOS" \
	linecolor rgb '#0060ad' \
	linetype 1 \
	linewidth 1 \
	pointtype 2 \
	pointsize 1.0 \
	title "meus dados" \
	with linespoints
EOF


