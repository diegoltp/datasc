
def validate(opciones, eleccion):
    # Definir validación de eleccion
    ##########################################################################
    """
    [Valida que la opcion entregada este correcta, reinicia si no]
    Args:
    opciones ([list]): [lista de opciones segun main]
    eleccion ([str]): [opcion seleccionada por el usuario]
    Returns:
    [str]: [opcion validada correctamente]
    """
    while eleccion not in opciones:
        eleccion = input(f"Opcion no valida ingrese una de las opciones validas {opciones}:\n>")
    ##########################################################################
    return eleccion

if __name__ == '__main__':
    
    eleccion = input('Ingresa una Opción: ').lower()
    # letras = ['a','b','c','d'] # pueden probar con letras también para verificar su funcionamiento.
    numeros = ["1","2","3"]
    # Si se ingresan valores no validos a eleccion debe seguir preguntando
    variable1 , variable2 = validate(numeros, eleccion)
    print(type(variable1),type(variable2))
    
    
