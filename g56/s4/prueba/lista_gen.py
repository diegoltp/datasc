from typing import Dict, Optional, List

def generar_lista(raw_data:Dict, limite = 25):
    '''
    Resumen:[Selecciona y convierte en lista los datos obtenidos desde la API]
    Args: 
    [raw_data][dict]:[variable obtenida desde la api con json, sin tabajar]
    [limite][int][opcional]:[limite de imagenes con la cual trabajaremos]
    return:
    [lista_data][list]:[Lista con la URL de las imagenes]
    '''
    lista_data = []
    for i in range(limite):
        try:
            lista_data = lista_data + [raw_data['latest_photos'][i]['img_src']]
        except(IndexError):
            break
    return lista_data

if __name__ == '__main__':
    from get_data import conectar_api_nasa
    raw_data = conectar_api_nasa()
    print(raw_data)