acciones = {
    1 : "Valorar la necesidad de llevarlo al hospital mas cernano",
    2 : "Abrir la via aérea",
    3 : "Permitirle posición de suficiente ventilación",
    4 : "Administrar 5 ventilaciones y llamar a la Ambulancia",
    5 : "Administrar compresiones torácicas hasta que llegue la ambulancia",
    6 : "Reevaluar a la espera de la ambulancia"
}
print(f"""
Asistente de primeros auxilios
------------------------------------------
Favor sigue las instrucciones del programa
""")
responde = input("¿Responde estimulos? s/n:\n>")
if responde == "s":
    print(f"{acciones[1]}")
elif responde == "n":
    print(f"{acciones[2]}")
    respira = input("¿Respira? s/n:\n>")
    if respira == "s":
        print(f"{acciones[3]}")
    elif respira == "n":
        print(f"{acciones[4]}")
        ambulancia = False
        while ambulancia == False:
            vida = input("¿Signos de vida? s/n:\n>")
            if vida == "n":
                print(f"{acciones[5]}")
            elif vida == "s":
                print(f"{acciones[6]}")               
            llega_amb = input("¿Llegó la ambulancia? s/n:\n>")
            if llega_amb == "s":
                ambulancia = True

            
                
                
                