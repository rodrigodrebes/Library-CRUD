import matplotlib.pyplot as plt
import numpy as np


#cria variável com idades
idade = [25,26,27,28,29,30]
#cria um índice para as idades
x = np.arange(len(idade))

#separa a barra de cada variável
width = 0.25

#primeira barra
salariopython = [5000, 6000, 7000, 8000, 9000, 10000]
plt.bar(x, salariopython, color='orange', width=width , label='Python')

#segunda barra
salariojs = [2000, 5000, 6000, 8000, 12000, 15000]
plt.bar(x + width, salariojs, color='blue', width=width ,  label="Javascript")

plt.legend()
plt.xticks(x, idade)

#títulos
plt.title("Média salarial desenvolvedores") 
plt.xlabel("Idades")
plt.ylabel("Salário R$")

#imprime
plt.show()