"""
La velocidad de escape se calcula mediante la siguiente fórmula:
𝑉e= sqrt(2𝑔𝑟)
Ve: corresponde a la Velocidad de Escape en [m/s].
g: corresponde a la constante gravitacional en [m/s**2].
r: Corresponde al radio del planeta en [m].
"""
from math import *
print("""
      Calcular la velocidad de escape de un planeta
      ---------------------------------------------
      """)
r = float(input("ingrese el radio del planeta en metros (Km*1000):\n>"))
g = float(input("ingrese la gravedad del planeta en metros por segundo cuadrado:\n>"))

ve = sqrt(2*g*r)

print(f"""
      -------------------------------------------
      La velocidad de escape es de {ve:.1f} [m/s]
      -------------------------------------------
      """)