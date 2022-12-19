from usersData import obtener_datos
from createdUser import crear_usuario
from updatedUser import actualizar_usuario
from deleteUser import eliminar_usuario
from validar import validador
from menu import menu_eleccion
import time
import os
import sys

op_sys = 'cls' if sys.platform == 'win32' else 'clear'

os.system(op_sys) # limpiar pantalla

eleccion = ""
continuar = True
while continuar:
    menu_eleccion()
    eleccion = input("> ")
    eleccion = validador(eleccion, ['0','1','2','3','4'])
    os.system(op_sys) # limpiar pantalla
    if eleccion == '1':
        obtener_datos()
    elif eleccion == '2':
        crear_usuario()
    elif eleccion == '3': 
        actualizar_usuario()   
    elif eleccion == '4':
        eliminar_usuario()
    elif eleccion == '0':
        continuar = False
        break
    time.sleep(5)    
print("Adios")