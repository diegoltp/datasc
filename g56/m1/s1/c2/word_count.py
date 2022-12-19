with open("lorem_ipsum.txt","r") as file:
    texto = file.read()
#parte a 
parte_a = set(texto)
print(f"El número de caracteres distintos es: {str(len(parte_a))}")
#parte b
parte_b = set(texto.split(" "))
print(f"El número de elementos distintos es: {str(len(parte_b))}")
