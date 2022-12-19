from json import loads
from requests import get

response1 = get('https://reqres.in/api/users?page=1')
result1 = loads(response1.text)

response2 = get('https://reqres.in/api/users?page=2')
result2 = loads(response2.text)

users_data = result1['data']+result2['data']
print(users_data)

lista1 = [list(i.items()) for i in users_data]
imprimir =[print(f'{imp[imp.index(j)]}') for imp in lista1 for j in imp]
print(imprimir)




"""
print(f'''
Request pagina 1: {response1}
Request pagina 2:{response2}
-----------------------------------------------
''')
for info_usr in users_data:
    for llave_usr in info_usr:
        print(f'{llave_usr}: {info_usr[llave_usr]}')
    print(f'\n-----------------------------------------------\n')
    """