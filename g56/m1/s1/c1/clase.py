from random import *
from math import *
print("hola mundo")
i=0
x=0
y=[]

for z in range(1,11):
    while x!=10:
        x=randint(0,10)
        i=i+1
    y.append(i)      
    i=0
    x=0
print(y)
print("la mayor cantidad de intentos fue " + str(max(y)))
print("la menor cantidad de intentos fue " + str(min(y)))
print("Chao mundo")
hola="hola"
print(hola.__len__())
#comentario
"""
otros
comentario
largos
"""

    
