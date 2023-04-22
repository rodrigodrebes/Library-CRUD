import pandas as pd
import numpy as np

#cria uma variável com dados de NOME na coluna 0 e IDADE na coluna 1
dados = [['Maria', 24], ['Rodrigo', 26], ['Guilherme', 25]]

#instancia esses dados no método, atribuindo nome às colunas
df = pd.DataFrame(dados, columns =['Nome', 'Idade'])

#printa o resultado
print(df)
