# algoritmo secuencia de pasos para generar un programa
#herramientas previas al codigo pseudocodigo diagramas de flujo
#pruebas logicas comparan variables y
#entregan resultados del tipo boolean 
#operadores como and, or, XOR, in (valor in "lista")
#para terminar un ciclo while infinito ctrl+c
#iterar es cada vuelta que da un ciclo
#operador de asignacion = += -= *= /=
#   if contador == 5:
#        break
# funciones 
# enumerate() : devuelve dos valores el indice y el elemento
# recibe como argumento un iterable. el for se arma con 2 sub indices
# zip() permite unir varios iterables dentro de una iteracion
#comprension funcion exlusiva de python para resumir operaciones
"""
import time
contador = 0 
acumulador = 0
while contador < 10:
    print(contador)
    contador += 1
    acumulador += contador
    time.sleep(2)
print("exploto")
"""
"""
nombres = ["lala" , "juan" , "pepe"]
for i, e in enumerate(nombres):
    print(f"indice = {i} elemento = {e}")
notas = [10,9,10,8]
for i in zip(nombres,notas):
    print(f"{i}")
"""
#comprehensions : sirven para crear variables 
mi_lista = [i if i == "e" else "x" for i in "generacion 56"]
print(mi_lista)
mi_lista2 = [i for i in "generacion 56"]
print(mi_lista2)


