from string import Template

def escribir_html(html_template, lista_url, imagen_template, contador_template):
    '''
    Resumen: Toma las variables creadas itera con ellas para entregar el script html final
    args:
    [html_template]: [script base en html]
    [lista_url]: [list][lista contenedora de informacion]
    [imagen_template]: [str][script html donde escribiremos el url de la imagen]
    [contador_template]: [str][script html donde escribiremos el contador]
    return
    [html]:[str][script en html final]
    '''
    texto_html= ''
    contador = 1
    for url in lista_url:
        texto_html += contador_template.substitute(contador = f'Imagen Numero {contador}') + imagen_template.substitute(imagen = url) +'\n'
        contador+=1
    html = html_template.substitute(body = texto_html)
    return html

