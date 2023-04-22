#método naive

lista_original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_pares = []
for x in lista_original:
    if x % 2 == 0:
        lista_pares.append(x)
print(lista_pares) # [2, 4, 6, 8, 10]



#método list comprehension:

lista_original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_pares = [x for x in lista_original if x % 2 == 0]
print(lista_pares) # [2, 4, 6, 8, 10]