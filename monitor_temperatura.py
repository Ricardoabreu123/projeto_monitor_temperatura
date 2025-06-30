# monitor de alerta de temperatura

leituras_de_temperatura = [35.5, 36.2, 37.0, 38.5, 39.1, 37.8, 36.5, 40.2, 39.9]
limite_alerta = 38.0


# Inicio do processo de verificação

print("Iniciando verificação do sensor")


# Laço que analisa cada leitura da lista

for temperatura in leituras_de_temperatura:

# Condicional que decide se emite alerta ou não

    if temperatura > limite_alerta:
        print(f"Alerta! Temperatura de {temperatura}°C detectada, acima do limite de {limite_alerta}°C")
    else:
        print(f"Status: Temperatura de {temperatura}°C está dentro do limite.")

# Fim do processo

print("Verificação finalizada")