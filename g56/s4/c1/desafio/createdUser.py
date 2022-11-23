from json import loads
from requests import post

def crear_usuario():
    payload = '''{"Name": "Ignacio",
                    "Job": "Profesor"}'''
    response = post('https://reqres.in/api/users',
                    data = payload)
    created_user = response.text
    print(f'''
Codigo de respuesta del servidor: {response}
Usuario creado: {created_user}
          ''')
