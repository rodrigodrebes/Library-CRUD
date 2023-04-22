import pandas as pd

# Leitura de arquivo CSV
pessoas = pd.read_csv('python\pandas,mat,numpy\myFile.csv')

#selecionar colunas CSV
coluna1 = pessoas['firstname']
print(coluna1)
