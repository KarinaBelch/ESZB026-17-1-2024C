#!/bin/bash

ARQUIVODADOS=/home/vboxuser/Desktop/lab07/dados.txt
echo "Content-type: text/html"
echo ""
echo '<HTML><HEAD><meta charset="UTF-8">'
echo '<TITLE>OXÍMETRO DE PULSO</TITLE>'
echo '<style>'
echo '  html, body {'
echo '    font-family: Arial, sans-serif;'
echo '    margin: 0;'
echo '    padding: 0;'
echo '    height: 100%;'   # Garantir que a altura seja 100% da tela
echo '    overflow: auto;  # Permitir rolagem se necessário'
echo '    background-color: #c3c3c3;'
echo '  }'
echo '  body {'
echo '    display: flex;'
echo '    flex-direction: column;'
echo '    justify-content: flex-start;'  # O conteúdo fica no topo da página
echo '    align-items: center;'         # Centraliza horizontalmente'
echo '  }'
echo '  .container {'
echo '    text-align: center;'
echo '    background-color: #ffffff;'
echo '    padding: 20px;'
echo '    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);'
echo '    border-radius: 8px;'
echo '    width: 80%;'
echo '    max-width: 900px;'
echo '  }'
echo '  h1 {'
echo '    color: #333;'
echo '    font-size: 48px;'
echo '  }'
echo '  h2 {'
echo '    color: #404040;'
echo '    font-size: 20px;'
echo '    color: #3c3c3c;'
echo '  }'
echo '  pre {'
echo '    text-align: left;'
echo '    background-color: #c3c3c3;'
echo '    padding: 10px;'
echo '    border-radius: 5px;'
echo '  }'
echo '  p {'
echo '    color: #3c3c3c;'  # Mudando a cor do parágrafo para azul
echo '  }'
echo '  .bottom-container {'
echo '    text-align: justify;'  # Deixa o texto justificado
echo '    font-color: #3c3c3c;'
echo '    width: 80%;'
echo '    max-width: 900px;'
echo '    padding: 20px;'  # Adiciona padding na parte inferior
echo '    background-color: #ffffff;'
echo '    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);'
echo '    border-radius: 8px;'
echo '    margin-top: 20px;'  # Adiciona uma margem superior para separar do conteúdo acima'
echo '  }'
echo '</style>'
echo '</HEAD>'
echo '<BODY>'
echo '<div class="container">'
echo '<H1>Oxímetro de Pulso</H1>'
echo '<H2> Projeto desenvolvido para a disciplina Sistemas Embarcados para Engenharia Biomédica </H2>'
echo '<p> <b>Docente:</b> Erick </p>'
echo '<p> <b>Discentes:</b> Anna, Bianca, Karina </p>'
echo '</div>'

echo '<div class="bottom-container">'
echo '<p> O projeto foi desenvolvido com o objetivo de criar um oxímetro de pulso sem o uso de módulos e através das placas de Arduino e Raspberry. Estabelecendo a comunicação por meio do circuíto eletrônico e das placas. </p>'

echo '<H3><b> Informações sobre o equipamento projetado </b></H3>'

echo '<p><b> Equipamento médico: </b> Oxímetro de pulso <br><br>'

echo '<b> Sinal de entrada: </b> Luz visível e infravermelha dos LEDs que atravessam o dedo e entram em contato com o LED receptor <br><br>'

echo '<b> Sinal de saída: </b> Saturação de oxigênio no sangue (SpO2) e batimentos cardíacos por minuto (BPM). <br><br>'

echo '<b> Interfaces com o usuário: </b> Os sinais serão obtidos através do contato do usuário com o oxímetro por meio de dois LEDs - vermelho e infravermelho - e um fotodiodo. Os valores serão mostrados em um display e através do monitor do computador. <br><br>'

echo '<b> Informações que irão constar no relatório via Web:</b> O relatório vai informar os sinais de saída do oxímetro: a saturação de oxigênio no sangue e batimentos cardíacos por minuto. <br><br>'

echo '<b> Estados que levam a uma notificação: </b> Saturação abaixo de 96%. </p>'

echo '</div>'
echo '<div class="bottom-container">'
echo '<h2>Dados: </h2>'
echo '<pre>'
cat $ARQUIVODADOS
echo '</pre>'

echo '<H2> Gráficos </H2>'
echo '<img src="/cgi-bin/imagem.cgi">'
echo '</div>'

echo '</BODY>'
echo '</HTML>'

