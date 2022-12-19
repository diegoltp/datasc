from request_data import get_data

def generar_lista_aves():
    '''
    resumen:
    [Utiliza func get data para generar la lista de aves]
    args: 
    [none]
    return:
    [lista]:
    aves_de_chile [ave de chile][nombre esp, nombre, eng, img]
    '''
    result = get_data()
    aves_de_chile = []
    for ave in result:
        aves_de_chile = aves_de_chile+[[
                                        ave['name']['spanish'] ,
                                        ave['name']['english'] ,
                                        ave['images']['main']
                                        ]]
    return aves_de_chile

if __name__ == '__main__':
    print(len(generar_lista_aves()))
    #print(generar_lista_aves())