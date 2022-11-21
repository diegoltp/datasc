import preguntas as p


def verificar(alternativas, eleccion):
    """
    [Verifica la altenativa del usuario]
    Args:
    altenativas([list]): [lista de alternativas a,b,c,d]
    eleccion([str]): [opcion seleccionada por el usuario validada por el validador]
    Returns:
    [bool]: [acierto o error en modo boleano]
    """
    #devuelve el índice de elección dada
    eleccion = ['a', 'b', 'c','d'].index(eleccion)

    # generar lógica para determinar respuestas correctas
    ##########################################################################################
    acierto = [alternativas.index(opcion_correcta) for opcion_correcta in alternativas if opcion_correcta[1] == 1]
    if eleccion == acierto[0]:
        print("Respuesta correcta")
        correcto= True
    else:
        print("Respuesta incorrecta")
        correcto= False  
    ##########################################################################################
    return correcto



if __name__ == '__main__':
    from print_preguntas import print_pregunta
    
    # Siempre que se escoja la alternativa con alt_2 estará correcta, e incorrecta en cualquier otro caso
    pregunta = p.pool_preguntas['basicas']['pregunta_2']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    respuesta = input('Escoja la alternativa correcta:\n> ').lower()
    verificar(pregunta['alternativas'], respuesta)






