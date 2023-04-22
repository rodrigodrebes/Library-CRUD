import pandas as pd
import csv
import numpy as np
from collections import Counter
from matplotlib import pyplot as plt

#abre o csv com a biblioteca CSV
with open('data.csv') as arquivo_csv:
  csv_reader = csv.DictReader(arquivo_csv)
  language_counter = Counter() #cria um contador de palavras
  #for com CSV
  for row in csv_reader:
    language_counter.update(row['LanguagesWorkedWith'].split(';'))

#abre o csv com pandas 
#dados=pd.read_csv('data.csv')
#ids= dados['Responder_id']
#linguagensPandas = dados['LanguagesWorkedWith']


#for com pandas
#for linguagem in linguagensPandas:
 # language_counter.update(row['LanguagesWorkedWith'].split(';'))


linguagens = []
popularidade = []



for item in language_counter.most_common(15):
   linguagens.append(item[0]) #retorna a coluna 0, nome da linguagem
   popularidade.append(item[1]) #retorna a coluna 1, o número de usuários

print(linguagens)
print(popularidade)

#barra horizontal, para caber a descrição das linguagens
plt.barh(linguagens, popularidade)

#títulos
plt.title("Linguagens mais Populares") 
plt.ylabel("Linguagens")
plt.xlabel("Número de usuários")

#imprime
plt.show()