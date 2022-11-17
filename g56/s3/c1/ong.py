def calcular_factorial(valor):
    lista_factorial = [i for i in range(1,valor+1)]
    n_factorial = 1
    for i in lista_factorial[::-1]:
        n_factorial = n_factorial * i
    return n_factorial

def calcular_productoria(lista):
    productoria = 1
    for i in lista:
        productoria = productoria * i
    return productoria

def calcular(**kwarg):
    requisitos = list(kwarg.items())
    resultados = []
    for i in range(len(requisitos)):
        if "fact" in requisitos[i][0]:
            resultados.append(["El factorial",requisitos[i][1],calcular_factorial(requisitos[i][1])])
        else:
            resultados.append(["La productoria",requisitos[i][1],calcular_productoria(requisitos[i][1])])     
    imprime_respuestas(resultados)

def imprime_respuestas(resultados):
    for i in range(len(resultados)):
        print(f"{resultados[i][0]} de {resultados[i][1]} es {resultados[i][2]}")
        
calcular(prod_2=[1,2,3,4,5,6,7,8], fact_1 = 5, prod_1 = [4,6,7,4,3], fact_2 = 6, fact_3 = 10)