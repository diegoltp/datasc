from getpass import getpass
from string import ascii_lowercase
abcdario = ascii_lowercase
pswrd = getpass("ingrese su contraseña:\n>")
pswrd = pswrd.lower()
intentos = 0
pswrd_hack = ""
for i in range(len(pswrd)):
    for j in range(len(abcdario)):
        intentos += 1
        if abcdario[j] == pswrd[i]:
            pswrd_hack = pswrd_hack+abcdario[j]
            break
print(f"Su contraseña {pswrd_hack} fue vulnerada en {intentos} intentos")

        