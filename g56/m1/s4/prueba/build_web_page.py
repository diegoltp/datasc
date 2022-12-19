from get_data import conectar_api_nasa
from lista_gen import generar_lista
from base_variables import escribir_template_variables
from basehtml import base_html
from writehtml import escribir_html
from crear_html import crear_archivo_html

#coneccion con la API
raw_data = conectar_api_nasa('https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/latest_photos','z828q5vpbwXTK6Rfmer3BXcKLP87vcgymS5CBkgT')
#crear lista de imagenes filtrada
lista_data = generar_lista(raw_data)
#Template para reemplazar en la base html
contador_template, imagen_template = escribir_template_variables()
#base en html para el sitio
html_template = base_html('Imagenes Nasa', 'Diegoltp' )
#escribir en la base html
html = escribir_html(html_template, lista_data, imagen_template, contador_template)
#crear archivo web
crear_archivo_html(html, 'nasa')