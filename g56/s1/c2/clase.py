
"""
# estructura de datos
alumnos = ["angelina","Daniel","hector"]
a=[1,2,3,4,"hola",8]
print(a[0])
# no corre i llega a 5 print(a[7])
print(a[a[0]])
print(a[4])
print(a[-1])


import sys
print(sys.argv)

alumnos.append("marco")
print(alumnos)
alumnos.insert(1, "javier")
print(alumnos)
eliminado=alumnos.pop(2)
print(alumnos)
print(eliminado)
alumnos.remove("hector")
print(alumnos)
alumnos[0]="angelina peña"
print(alumnos)

"""

#libreria

notas = {
    "vicente":7,
    "Antonia":6,
    "raul":5,
    "diego":8
}
del notas["diego"]
print(notas)

notasb = {
    "Mauricio":0,
    "raul":7
}
notas.update(notasb)
print(notas)

alumnos2 = [("angelina",7),("Daniel",5),("hector",5)]

dict(alumnos2)
print(alumnos2)    