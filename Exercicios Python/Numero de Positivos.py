array = [11,20,-1,0,-5,-6,8,9,10]
negativos = []
positivos = []
zero = []

def plusMinus(arr):
    for i in arr:
        if i < 0:
            negativos.append(i)
        elif i > 0:
            positivos.append(i)
        elif i == 0:
            zero.append(i)

plusMinus(array)
resultado = len(negativos)/len(array)
print(round(resultado, 4))
