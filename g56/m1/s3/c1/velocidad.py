def calcular_media(iterable):
    return sum(iterable)/len(iterable)
def encontrar_posiciones(iterable):
    media = calcular_media(iterable)
    posiciones = []
    for i in range(len(iterable)):
        if iterable[i] > media:
            posiciones.append(iterable.index(iterable[i]))        
            iterable.remove(iterable[i])
            iterable.insert(i,0)
    print(posiciones)

velocidad = [25, 12, 19, 16, 11, 11, 24, 1,
            14, 14, 16, 10, 6, 23, 13, 25, 4, 19,
            14, 20, 18, 9, 18, 4, 18, 1, 3, 4, 2,
            14, 23, 19, 23, 9, 18, 20, 22, 14, 1,
            10, 5, 23, 3, 5, 9, 5, 3, 12, 20, 5,
            11, 10, 18, 10, 14, 5, 23, 20, 23, 21]

encontrar_posiciones(velocidad)