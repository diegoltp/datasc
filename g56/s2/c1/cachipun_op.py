from random import choice
from sys import argv
#Declarar variables
user_choice = argv[1]
error = True
while error:
    if user_choice == "Piedra" or user_choice == "Papel" or user_choice == "Tijera":
        sist_choice = choice(["Piedra", "Papel", "Tijera"])
        versus = user_choice+sist_choice
        opciones = {"PiedraPiedra":"Empate",
                    "PiedraPapel":"Gana la I.A.",
                    "PiedraTijera":"Gana el usuario",
                    "PapelPiedra":"Gana el usuario",
                    "PapelPapel":"Empate",
                    "PapelTijera":"Gana la I.A.",
                    "TijeraPiedra":"Gana la I.A.",
                    "TijeraPapel":"Gana el usuario",
                    "TijeraTijera":"Empate",
                    }
        print(f"""----------------------------------------
Tu jugaste {user_choice}
Nuestra I.A. Jugo {sist_choice}
{opciones[versus]}
----------------------------------------
        """)
        error = False
    else:
        print("Argumento inválido: Debe ser Piedra, Papel o Tijera.")
        user_choice = input("Ingrese nuevamente la opccion:\n> ")
print("Adios")
