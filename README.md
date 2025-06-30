  # Projeto 1: Monitor de Alerta de Temperatura

## Objetivo do Projeto

Este script foi desenvolvido como uma solução de monitoramento para a Indústria 4.0. Ele 
simula a análise de dados coletados por um sensor de temperatura em uma máquina industrial, 
identificando e alertando sobre leituras que excedem um limite de segurança pré-definido.

##  Tecnologias Utilizadas

* Python 
* Estruturas de dados (Listas)
* Laços de repetição (`for`)
* Lógica condicional (`if/else`)

##  Como Executar

1.  Certifique-se de ter o Python instalado.
2.  Clone ou baixe os arquivos deste repositório.
3.  Abra um terminal, navegue até a pasta do projeto e execute o comando: `python monitor_temperatura.py`

##  Exemplo de Saída

O programa irá imprimir o status de cada leitura de temperatura e emitirá um alerta claro para 
qualquer valor que ultrapasse o limite:

 Iniciando verificação do sensor
Status: Temperatura de 35.5°C está dentro do limite.
Status: Temperatura de 36.2°C está dentro do limite.
Status: Temperatura de 37.0°C está dentro do limite.
ALERTA! Temperatura de 38.5°C detectada, acima do limite de 38.0°C
ALERTA! Temperatura de 39.1°C detectada, acima do limite de 38.0°C
Status: Temperatura de 37.8°C está dentro do limite.
Status: Temperatura de 36.5°C está dentro do limite.
ALERTA! Temperatura de 40.2°C detectada, acima do limite de 38.0°C
ALERTA! Temperatura de 39.9°C detectada, acima do limite de 38.0°C
 Verificação finalizada 
