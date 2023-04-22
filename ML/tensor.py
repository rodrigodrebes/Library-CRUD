import torch

# tensores são estruturas multidimensionais
# Criando um tensor 2x3
tensor = torch.tensor([[1, 2, 3],
                       [4, 5, 6]])

print(tensor)

# Verificando o número de dimensões
num_dimensions = tensor.dim()

print(f"O número de dimensões é {num_dimensions}")

# Verificando o tamanho do tensor
tensor_size = tensor.size()
print(f'Tamanho do tensor: {tensor_size}')





import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt

# Dados de treinamento (x, y)
x_train = torch.tensor([[1.0], [2.0], [3.0], [4.0], [5.0]])
y_train = torch.tensor([[2.0], [4.0], [6.0], [8.0], [10.0]])

# Definir o modelo de regressão linear

# LinearRegression que herda de nn.Module, que é a classe base para todos os modelos de redes neurais no PyTorch.
class LinearRegression(nn.Module):
    
    #construtor da classe LinearRegression. Esse método é chamado quando criamos uma instância da classe.
    def __init__(self):
        
        #Chamamos o construtor da classe base (nn.Module). Isso garante que todas as funcionalidades necessárias para a classe base sejam inicializadas corretamente.
        super(LinearRegression, self).__init__()

        #Criamos uma camada linear (também chamada de camada totalmente conectada) com uma entrada e uma saída. Isso define a relação linear entre a entrada e a saída.
        self.linear = nn.Linear(1, 1)
        
    # Definimos o método forward, que é responsável pela passagem direta (forward pass) no modelo. Ele recebe o tensor de entrada x e retorna a saída do modelo.
    def forward(self, x):
        return self.linear(x)

# Criar uma instância do modelo
model = LinearRegression()

# Definir função de perda e otimizador
# ajustar os parâmetros do modelo durante o treinamento
loss_function = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)



# Treinar o modelo

#Uma época (epoch) é uma iteração completa do conjunto de treinamento através do algoritmo de aprendizado.
num_epochs = 1000
for epoch in range(num_epochs):
    
    # Forward pass = É a etapa em que o modelo recebe os dados de entrada e os processa para gerar uma previsão. Ele passa os dados através das camadas e funções definidas no modelo. Processamento dos dados de entrada pelo modelo para gerar previsões.
    y_pred = model(x_train)

    # Calcular a perda = A função de perda (loss function) mede a diferença entre a previsão gerada pelo modelo e o valor real (rótulo/label). Essa função nos ajuda a entender o quão bem o modelo está performando e nos fornece uma métrica para melhorá-lo. Medida da diferença entre as previsões do modelo e os valores reais.
    loss = loss_function(y_pred, y_train)

    # Zerar os gradientes = O otimizador é responsável por ajustar os parâmetros do modelo (pesos e bias) com base no gradiente da função de perda, de modo a minimizar a perda e melhorar a precisão do modelo. Algoritmo para atualizar os parâmetros do modelo com base no gradiente da função de perda.
    optimizer.zero_grad()

    # Backward pass = Esta etapa é onde ocorre a retropropagação (backpropagation). A função de perda calcula o gradiente para cada parâmetro do modelo e, em seguida, atualiza esses parâmetros com base nos gradientes, usando o otimizador. Isso ajuda o modelo a aprender e melhorar suas previsões. Cálculo dos gradientes e atualização dos parâmetros do modelo usando retropropagação.
    loss.backward()

    # Atualizar os parâmetros
    optimizer.step()



# Testar o modelo treinado
#OBS = quando testamos o modelo usando apenas um único ponto de teste (x_test = torch.tensor([[6.0]])), a linha "x_range = torch.arange(0, 7, 0.1).unsqueeze(1)" não é necessária.
x_test = torch.tensor([[6.0]])
y_test = model(x_test)
print(f"Resultado da previsão para x = {x_test.item()}: y = {y_test.item()}")


#PLOTANDO TUDO ISSO


# Plotar os dados de treinamento
plt.scatter(x_train, y_train, color='blue', label='Dados de treinamento')

# Plotar a linha de regressão
#O método .unsqueeze(dim) em PyTorch é usado para adicionar uma dimensão extra ao tensor ao longo do eixo especificado. Isso é feito para garantir que o tensor tenha a forma adequada para ser passado ao modelo.
x_range = torch.arange(0, 7, 0.1).unsqueeze(1)
y_range = model(x_range)
plt.plot(x_range, y_range.detach(), color='red', label='Linha de regressão')

# Configurar o gráfico
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Regressão Linear com PyTorch')

# Mostrar o gráfico
plt.show()

