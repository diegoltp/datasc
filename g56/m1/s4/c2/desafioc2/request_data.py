from requests import get
from json import loads
def get_data():
    '''
    resumen:
    [llama toda la info de la API https://aves.ninjas.cl/api/birds]
    args: 
    [none]
    return:
    [lista] [toda la info de la api en formato python]
    '''
    response = get('https://aves.ninjas.cl/api/birds')
    result = loads(response.text)
    return result


if __name__ == '__main__':
    result = get_data()
    print(result[0]['name']['spanish'])
    print(result[0]['name']['english'])
    print(result[0]['images']['main'])
    
    