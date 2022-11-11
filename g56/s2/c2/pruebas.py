#afivinar la contraseña con comprehension

from getpass import getpass
from string import ascii_lowercase
abcdario = ascii_lowercase
pswrd = getpass("ingrese su contraseña:\n>")
pswrd = pswrd.lower()
intentos = 0
match = ""
pswrd_hack = [j for i in pswrd for j in abcdario if i==j]

print(pswrd_hack)
print(intentos)
