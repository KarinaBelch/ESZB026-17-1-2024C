#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg
import numpy as np
import serial
import atexit
import time

def obtem_bpm():
    conexaoSerial.write(b'b')
    time.sleep(0.5)
    conexaoSerial.flush()
    conexaoSerial.write(b'm')
    time.sleep(0.1)
    print(conexaoSerial.inWaiting())
    dadoInt1 = conexaoSerial.read()
    dadoInt2 = conexaoSerial.read()
    intervalo = float( (ord(dadoInt1) + ord(dadoInt2)*256.0) )

def obtem_so2():
    conexaoSerial.write(b's')
    time.sleep(0.5)
    conexaoSerial.flush()
    conexaoSerial.write(b'm')
    time.sleep(0.1)
    print(conexaoSerial.inWaiting())
    dadoInt1 = conexaoSerial.read()
    dadoInt2 = conexaoSerial.read()
    intervalo = float( (ord(dadoInt1) + ord(dadoInt2)*256.0) )

    if(intervalo <= 96):
        {
            textoi.setText("Atenção: Saturação de Oxigênio com nível abaixo de 96%")
        }

def medicao_arduino():
    conexaoSerial.write(b'p')
    time.sleep(0.5)
    conexaoSerial.flush()
    conexaoSerial.write(b'm')
    time.sleep(0.1)
    print(conexaoSerial.inWaiting())
    dadoInt1 = conexaoSerial.read()
    dadoInt2 = conexaoSerial.read()
    intervalo = float( (ord(dadoInt1) + ord(dadoInt2)*256.0) )
    textoi.setText("Intervalo: "+ str(intervalo).zfill(3)+"ms" )
    conexaoSerial.write(b'i')
        

def update():
    global data1, curve1, ptr1, conexaoSerial, x_atual, npontos, previousTime
    if conexaoSerial.inWaiting() > 1:
        dado1 = conexaoSerial.read()
        dado2 = conexaoSerial.read()
        novodado = float( (ord(dado1) + ord(dado2)*256.0)*5.0/1023.0 )
        
        data1[x_atual] = novodado
        data1[(x_atual+1)%npontos] = np.nan
        x_atual = x_atual+1
        if x_atual >= npontos:
            x_atual = 0
        
        curve1.setData(data1, connect="finite")
        actualTime = time.time()*1000
        taxa = str(round(actualTime-previousTime))
        previousTime = actualTime
        texto.setText("taxa: "+taxa.zfill(3)+"ms" )

win = pg.GraphicsWindow()
win.setWindowTitle('Coletando dados do Arduino via Porta Serial')

npontos = 800
x_atual = 0
p1 = win.addPlot()
p1.setYRange(0,5,padding=0)
data1 = np.zeros(npontos)
curve1 = p1.plot(data1)
ptr1 = 0

previousTime = time.time()*1000 # pega a hora atual, em milissegundos
texto = pg.TextItem(text="", color=(255,255,0), anchor=(0,1))
p1.addItem(texto)
texto.setPos(0,0) # adiciona o texto na posicao (0,0) do grafico
textoi = pg.TextItem(text="int:", color=(255,255,0), anchor=(0,1))
p1.addItem(textoi)
textoi.setPos(650,4) # adiciona o texto na posicao (0,0) do grafico

proxy1 = QtGui.QGraphicsProxyWidget()
botao1 = QtGui.QPushButton('Coletar BPM')
proxy1.setWidget(botao1)
botao1.clicked.connect(obtem_bpm)

proxy2 = QtGui.QGraphicsProxyWidget()
botao2 = QtGui.QPushButton('Coletar SPO2')
proxy2.setWidget(botao2)
botao2.clicked.connect(obtem_so2)

p2 = win.addLayout(row=1, col=0)
p2.addItem(proxy1,row=0,col=0)
p2.addItem(proxy2,row=1,col=0)

conexaoSerial = serial.Serial('/dev/ttyACM0',115200)
conexaoSerial.write(b'i')
        
# inicia timer rodando o mais rápido possível
timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(0)

atexit.register(saindo)

## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    QtGui.QApplication.instance().exec_()
