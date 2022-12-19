from sys import argv

def criterio(argv):
    """ Tipo de filtrado """
    if len(argv) < 3:
        mod_filtrado = False #filtrado por defecto
    else:
        mod_filtrado = True  #filtrado segun argv
    return mod_filtrado

def filtrar(umbral,criterio = "mayor"):
    """ Filtrado: devuelve la llave correspondiente """
    if criterio=="menor":
        valores_filtrados = {precio:costo for (precio, costo) in precios.items() if costo < umbral}
    else:
        valores_filtrados = {precio:costo for (precio, costo) in precios.items() if costo > umbral}
    return valores_filtrados.keys()

def error(argv):
    """ Valida el segundo parametro ingresado por el usuario """
    if argv[2] == "mayor" or argv[2] == "menor":
        continuar = True
    else:
        continuar= "Lo sentimos, no es una opcion valida"
    return continuar

precios = { 'Notebook': 700000,
            'Teclado': 25000,
            'Mouse': 12000,
            'Monitor': 250000,
            'Escritorio': 135000,
            'Tarjeta de Video': 1500000}

umbral = int(argv[1])

if criterio(argv):       
    if type(error(argv)) == bool:
        key_filtrada = ", ".join(filtrar(umbral, argv[2]))
        print(f"Los productos {argv[2]} al umbral son: {key_filtrada}")
    else:
        print(error(argv))
else:
    key_filtrada = ", ".join(filtrar(umbral))
    print(f"Los productos mayores al umbral son: {key_filtrada}")