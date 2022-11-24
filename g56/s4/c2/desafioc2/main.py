from list_gen import generar_lista_aves
from base_variables import escribir_template_variables
from basehtml import base_html
from writehtml import escribir_html
#generar variables
nom_esp_template, nom_eng_template, imagen_template = escribir_template_variables()
#generar html
html_template = base_html()
#generar lista con datos
lista_url = generar_lista_aves()
#generar script en html completo
html = escribir_html(html_template, lista_url, nom_esp_template, nom_eng_template, imagen_template)
#crear archivo html final
with open('output1.html', 'w') as f:
    f.write(html)