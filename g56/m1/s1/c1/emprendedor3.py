"""
๐๐ก๐๐๐๐๐๐๐๐  = ๐ * ๐ โ ๐บ๐
P: Precio de Suscripciรณn
U: Nรบmero de Usuarios
GT: Gastos Totales
"""
print("""
Programa Emprendedor 1: 
      
Solo ingresar caracteres numericos y numeros enteros
      """)
p=int(input("Ingrese el Precio de Suscripcion \n>"))
u=int(input("Ingrese la cantidad de usuarios \n>"))
gt=int(input("Ingrese los gastos toales \n>"))
utilidades= (p*u)-gt
print(f"Las utilidades obtenidas por suscripciones son:\n>{utilidades}")
print("------------------------------------------------------------------")
u_Aรฑo_ant=int(input("Ingrese las utilidades del aรฑo anterior (solo valores distintos a 0):\n>"))
razon=utilidades/u_Aรฑo_ant
print(
f""" 
La razon entre utilidad obtenida actual y anterior es: 
>{razon:.2f} 
""")