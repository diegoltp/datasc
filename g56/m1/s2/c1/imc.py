"""
IMC = W/H**2
W:peso en [Kg]
H:altura en [m]
IMC: [KG/m**2]
IMC             Clasificación OMS
< 18.5             Bajo Peso
[ 18.5, 25 [       Adecuado
[ 25, 30 [         Sobrepeso
[ 30, 35[        Obesidad Grado I
[ 35, 40 [       Obesidad Grado II
> 40             Obesidad Grado III
"""
#ingresar el peso en Kg y la talla (altura) en centímetros
from sys import argv
peso = float(argv[1])
talla = float(argv[2])
#validar unidades:
#hombre mas gordo de la historia 594kg
#hombre mas alto de la historia 251 cm

if peso > 0 and peso < 700 and talla > 10 and talla < 300:
    #Calcular el IMC
    imc = peso/((talla/100)**2)
    #Mostrar IMC además de la clasificación dada por la OMS
    clasificacion = {
        1 : "Bajo peso",
        2 : "Adecuado",
        3 : "Sobrepeso",
        4 : "Obesidad Grado I",
        5 : "Obesidad Grado II",
        6 : "Obesidad Grado III",
    }
    categoria = 0
    if imc < 18.5:
        categoria = 1
    elif imc < 25:
        categoria = 2                  
    elif imc < 30:
        categoria = 3                 
    elif imc < 35:
        categoria = 4
    elif imc < 40:
        categoria = 5
    elif imc >= 40:
        categoria = 6
    #el cuadro de la tarea deja fuera el 40... pense incluirlo
    print(f"""
Su IMC es de {imc:.2f}
La clasificacion OMS es {clasificacion[categoria]}
          """)
else:
    print("error en datos ingresados")
