import matplotlib.pyplot as plt
import torch
import pandas as pd
import numpy as np

#criando um Tensor
scalar = torch.tensor(7)

#dimensões do tensor
scalar.ndim

#formato do tensor
scalar.shape

#formato [2,2], dimensão 2 (duas [] [])
MATRIX = torch.tensor([[7,8],
                      [9,10]])
print(MATRIX.shape)
print(MATRIX.ndim)

#Tensor aleatório
random_tensor = torch.rand(3,4)
print(random_tensor)

#Tensor 3 dimensões com valores similares a uma Imagem
random_image_tensor = torch.rand(size=(224, 224,3)) #comprimento, largura, cores RGB