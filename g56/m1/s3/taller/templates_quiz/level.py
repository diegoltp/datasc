def choose_level(n_pregunta, p_level):
    """
    [que permite escoger el nivel de dificultad de la pregunta a realizar.]
    Args:
    n_pregunta ([int]): [Nro de pregunta actual]
    p_level ([str]): [Preguntas por nivel req por el usuario]
    Returns:
    [str]: [nivel elegido]
    """
    # Construir lógica para escoger el nivel
    ##################################################
    p_por_nivel={}
    if p_level == 1:
        p_por_nivel = {
            1:"basicas",
            2:"intermedias",
            3:"avanzadas"
        }
    elif p_level == 2:
        p_por_nivel = {
            1:"basicas",
            2:"basicas",
            3:"intermedias",
            4:"intermedias",
            5:"avanzadas",
            6:"avanzadas",
        }  
    elif p_level == 3:
        p_por_nivel = {
            1:"basicas",
            2:"basicas",
            3:"basicas",
            4:"intermedias",
            5:"intermedias",
            6:"intermedias",
            7:"avanzadas",
            8:"avanzadas",
            9:"avanzadas",
        }
    level = p_por_nivel[n_pregunta]
    ##################################################
    
    return level

if __name__ == '__main__':
    # verificar resultados
    print(choose_level(2, 2)) # basicas
    print(choose_level(3, 2)) # intermedias
    print(choose_level(6, 2)) # avanzadas  #cambie el 7 por el 6
    print(choose_level(4, 3)) # intermedias