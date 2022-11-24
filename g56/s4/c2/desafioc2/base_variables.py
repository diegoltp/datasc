from string import Template

def escribir_template_variables():
    '''
    Resumen: [Escribe el formato en html de las variables a reemplazar]
    arg: [none]
    return:
    [nom_esp_template][str][formato html con el nombre de la variable a reemplazar 'nom_esp']
    [nom_eng_template][str][formato html con el nombre de la variable a reemplazar 'nom_eng']
    [imagen_template][str][formato html con el nombre de la variable a reemplazar 'imagen']
    '''
    nom_esp_template = Template('<li> $nom_esp </li>')
    nom_eng_template = Template('<li> $nom_eng </li>')
    imagen_template = Template('<li><img src="$imagen"/><li>')
    return nom_esp_template, nom_eng_template, imagen_template