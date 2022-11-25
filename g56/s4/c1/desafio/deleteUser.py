from requests import delete

def eliminar_usuario():
    url = 'https://reqres.in/api/users/6'

    response = delete('https://reqres.in/api/users/6')
    
    print(f'''
Respuesta del servidor {response}
Usuario eliminado
          ''')