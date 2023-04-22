import matplotlib.pyplot as plt
import numpy as np

x = [i for i in range (10)] #cria os valores 0 a 9
print(x)

y = [2*i for i in range(10)] #cria os valores 0 a 18
print(y)


plt.xlabel('x-axis') #define o nome da label x
plt.ylabel('y-axis') #define o nome da label y
plt.title('Plot padrão') #define o título

plt.plot(x,y) #mostra a linha
plt.scatter(x,y) #mostra os pontos em vez de reta

plt.show()