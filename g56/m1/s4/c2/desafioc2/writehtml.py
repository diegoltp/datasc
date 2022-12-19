from string import Template

def escribir_html(html_template, lista_url, nom_esp_template, nom_eng_template, imagen_template):
    '''
    Resumen: Toma las variables creadas itera con ellas para entregar el script html final
    args:
    [html_template]: [script base en html]
    [lista_url]: [list][lista contenedora de informacion sobre aves]
    [nom_esp_template]: [str][script html donde escribiremos el nombre en español]
    [nom_eng_template]: [str][script html donde escribiremos el nombre en ingles]
    [imagen_template]: [str][script html donde escribiremos el url de la imagen]
    return
    [html]:[str][script en html final]
    '''
    texto_html= ''
    for url in lista_url:
        texto_html += nom_esp_template.substitute(nom_esp = url[0]) + nom_eng_template.substitute(nom_eng = url[1]) + imagen_template.substitute(imagen = url[2]) +'\n'
        
    html = html_template.substitute(body = texto_html)
    return html

