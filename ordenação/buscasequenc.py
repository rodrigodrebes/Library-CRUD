lista = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21]

def busca_sequencial(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1

indice = busca_sequencial(lista, 13)
if indice != -1:
    print(f"O elemento 13 foi encontrado na posição {indice}")
else:
    print("O elemento 13 não foi encontrado na lista")


def busca_binaria(lista, item):
    inicio = 0
    fim = len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == item:
            return meio
        elif lista[meio] < item:
            inicio = meio + 1
        else:
            fim = meio - 1
    raise ValueError("Elemento não encontrado na lista")

indice2 = busca_binaria(lista, 13)
print(f'O elemento foi encontrado na posição {indice2}')