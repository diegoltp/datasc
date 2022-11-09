from random import choice
from sys import argv
#Declarar variables
user_choice = argv[1]
sist_choice = choice(["Piedra", "Papel", "Tijera"])
versus = user_choice+sist_choice
if versus == "PiedraPiedra":
    resultado = "Empate"
elif versus == "PiedraPapel":
    resultado = "Gana la I.A."
elif versus == "PiedraTijera":
    resultado = "Gana el usuario"
elif versus == "PapelPiedra":
    resultado = "Gana el usuario"
elif versus == "PapelPapel":
    resultado = "Empate"
elif versus == "PapelTijera":
    resultado = "Gana la I.A."
elif versus == "TijeraPiedra":
    resultado = "Gana la I.A."
elif versus == "TijeraPapel":
    resultado = "Gana el usuario"
elif versus == "TijeraTijera":
    resultado = "Empate"
            
print(f"""----------------------------------------
Tu jugaste {user_choice}
Nuestra I.A. Jugo {sist_choice}
{resultado}
----------------------------------------
""")