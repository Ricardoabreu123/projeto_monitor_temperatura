# Importa a biblioteca Pandas e a apelida de 'pd' (uma convenção universal)
import pandas as pd

print(" Iniciando Análise de Dados dos Sensores ")

# Usa a função read_csv do Pandas para carregar os dados do nosso arquivo
# O resultado é guardado em uma variável chamada 'df' (de DataFrame)
df = pd.read_csv("dados_sensores.csv")

# Análise Exploratória

# Mostra as 5 primeiras linhas da nossa tabela de dados
print("\n1. Amostra dos Dados:")
print(df.head())

# Gera um resumo estatístico completo das colunas numéricas
# (contagem, média, desvio padrão, mínimo, máximo.)
print("\n2. Resumo Estatístico Completo:")
print(df.describe())

# Extraindo Informações Específicas

# Calcula a temperatura média. Selecionamos a coluna 'temperatura_celsius'
# e usamos o método.mean() para calcular a média.
temperatura_media = df['temperatura_celsius'].mean()

# Encontra o pico de vibração. Selecionamos a coluna 'vibracao_mm_s'
# e usamos o método.max() para encontrar o valor máximo.
vibracao_maxima = df['vibracao_mm_s'].max()

print("\n3. Relatório Gerencial:")
print(f" - Temperatura Média Registrada: {temperatura_media:.2f}°C")
print(f" - Pico Máximo de Vibração: {vibracao_maxima} mm/s")

print("\nAnálise Finalizada")