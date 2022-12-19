import preguntas as p
import random

def shuffle_alt(pregunta):
    """
    [retornar las alternativas mezcladas.]
    Args:
    pregunta ([str]): [pregunta de acceso a alternativas]
    Returns:
    [list]: [alternativas mezcladas]
    """
    #mezclar alternativas
    #######################################################################
    random.shuffle(pregunta["alternativas"])    
    #######################################################################
    
    return pregunta['alternativas']

if __name__ == '__main__':
    # si se ejecuta el  programa varias veces las alternativas debieran aparecer en distinto orden
    #x=[1,2,3,4,5,6]
    #random.shuffle(x)
    #print(x)
    print(shuffle_alt(p.pool_preguntas['basicas']['pregunta_1']))  
    # a modo de ejemplo
    # [['alt_1', 0], ['alt_3', 0], ['alt_2', 1], ['alt_4', 0]]