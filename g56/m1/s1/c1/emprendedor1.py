"""
ππ‘ππππππππ  = π * π β πΊπ
P: Precio de SuscripciΓ³n
U: NΓΊmero de Usuarios
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