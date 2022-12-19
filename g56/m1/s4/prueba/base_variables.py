from string import Template

def escribir_template_variables():
    '''
    Resumen: [Escribe el formato en html de las variables a reemplazar]
    arg: [none]
    return:
    [contador_template][str][formato html con el nombre de la variable a reemplazar]
    [imagen_template][str][formato html con el nombre de la variable a reemplazar]
    '''
    contador_template = Template('<li>$contador<li>')
    imagen_template = Template('<li><img src="$imagen"/><li>')
    return contador_template, imagen_template