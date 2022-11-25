# https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/latest_photos/?api_key=z828q5vpbwXTK6Rfmer3BXcKLP87vcgymS5CBkgT
from requests import get
from json import loads

def conectar_api_nasa(url, token):
    '''
    Establecer coneccion con la API NASA
    args: 
    [url][str][Direccion web de la API, hasta el ultimo directorio sin / al final]
    [token][str][token de seguridad para entrar a la url. Ingresar solo el token]
    Return:
    [result][dict][diccionario completo con la informacion]
    '''
    response = get(f'{url}/?api_key={token}')
    result = loads(response.text)
    return result


    
if __name__ == '__main__':
    print(conectar_api_nasa()['latest_photos'][1]['img_src'])
    
    
'''    
    if response.status_code in [200,201,202,203,204]:
        return data.json() if data.text else data.status_code
    return None
    '''