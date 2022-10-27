"""
𝑈𝑡𝑖𝑙𝑖𝑑𝑎𝑑𝑒𝑠 = 𝑃 * 𝑈 − 𝐺𝑇
P: Precio de Suscripción
U: Número de Usuarios
GT: Gastos Totales
"""
print("""
Programa Emprendedor 1: 
      
Solo ingresar caracteres numericos y numeros enteros
      """)
p=int(input("Ingrese el Precio de Suscripcion \n>"))
u_n=int(input("Ingrese la cantidad de usuarios normales\n>"))
u_p=int(input("Ingrese la cantidad de usuarios premium\n>"))
gt=int(input("Ingrese los gastos toales \n>"))
utilidades_normales = (p*u_n)-gt
utilidades_premium = (1.5*p*u_p)-gt
print(f"""
----------------------------------------------------------------------------------
Utilidades obtenidas por:

--->Suscripciones normales:\n>{utilidades_normales}

--->Suscripciones premium:\n>{int(utilidades_premium)}
----------------------------------------------------------------------------------
""")