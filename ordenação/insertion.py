lista = [20, 55, 60, 1, 44, 78, 100]

def ordenacao_por_insercao(lista):
    n = len(lista)

    for i in range(1, n):
        chave = lista[i]
        j = i - 1
        while j >= 0 and chave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave

    return lista

lista_ordenada = ordenacao_por_insercao(lista)
print(lista_ordenada)