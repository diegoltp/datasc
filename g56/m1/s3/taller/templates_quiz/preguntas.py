"""
[contiene pool de preguntas y alternativas almacenados en diccionarios]
"""
preguntas_basicas = {
    'pregunta_1': {'enunciado':['Enunciado básico 1'],
                    'alternativas': [['alt_1', 0], 
                                    ['alt_2', 1], 
                                    ['alt_3', 0], 
                                    ['alt_4', 0]]},
    'pregunta_2': {'enunciado':['Enunciado básico 2'],
    'alternativas': [['alt_1', 0], 
                     ['alt_2', 1], 
                     ['alt_3', 0], 
                     ['alt_4', 0]]},
    
'pregunta_3': {'enunciado':['Enunciado básico 3'],
    'alternativas': [['alt_1', 0], 
                     ['alt_2', 1], 
                     ['alt_3', 0], 
                     ['alt_4', 0]]}
}

preguntas_intermedias = {
    'pregunta_1': {'enunciado':['Enunciado intermedio 1'],
                    'alternativas': [['alt_1', 0], 
                                    ['alt_2', 1], 
                                    ['alt_3', 0], 
                                    ['alt_4', 0]]},
    'pregunta_2': {'enunciado':['Enunciado intermedio 2'],
                    'alternativas': [['alt_1', 0], 
                                    ['alt_2', 1], 
                                    ['alt_3', 0], 
                                    ['alt_4', 0]]},
    
'pregunta_3': {'enunciado':['Enunciado intermedio 3'],
    'alternativas': [['alt_1', 0], 
                     ['alt_2', 1], 
                     ['alt_3', 0], 
                     ['alt_4', 0]]}
}

preguntas_avanzadas = {
    'pregunta_1': {'enunciado':['Enunciado avanzado 1'],
    'alternativas': [['alt_1', 0], 
                     ['alt_2', 1], 
                     ['alt_3', 0], 
                     ['alt_4', 0]]},
    'pregunta_2': {'enunciado':['Enunciado avanzado 2'],
    'alternativas': [['alt_1', 0], 
                     ['alt_2', 1], 
                     ['alt_3', 0], 
                     ['alt_4', 0]]},
    
'pregunta_3': {'enunciado':['Enunciado avanzado 3'],
    'alternativas': [['alt_1', 0], 
                     ['alt_2', 1], 
                     ['alt_3', 0], 
                     ['alt_4', 0]]}
}

pool_preguntas = {'basicas': preguntas_basicas,
                  'intermedias': preguntas_intermedias,
                  'avanzadas': preguntas_avanzadas}


if __name__ == '__main__':
    print(list(pool_preguntas["intermedias"].keys())[0])
    print(pool_preguntas["intermedias"][f"pregunta_{1}"]["enunciado"])
    print(pool_preguntas["intermedias"]["pregunta_1"]["alternativas"])
    print(type(pool_preguntas["intermedias"]["pregunta_1"]["alternativas"][1][1]))