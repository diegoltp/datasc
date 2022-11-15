lista1 = [1,2,3,4,5]
lista2 = ["a","b","c","d","e"]
diccionario = dict(zip(lista1,lista2))
print(diccionario)
comp = {i:j for i,j in zip(lista1, lista2) }
print(comp)