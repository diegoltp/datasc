def validador(eleccion,opciones):
    while eleccion not in opciones:
        eleccion = input((f"ingrese una opcion valida {opciones}\n>"))
    return eleccion