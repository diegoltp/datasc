from json import loads
from requests import put

def actualizar_usuario():
    payload = '''{"name": "morpheus",
    "residence": "zion"}'''
    response = put('https://reqres.in/api/users/2', data = payload)
    updated_user = response.text
    print(f'''
Respuesta del servidor: {response}
Usuario actualizado: {updated_user}         
          ''')