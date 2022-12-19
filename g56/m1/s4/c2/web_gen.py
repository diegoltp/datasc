from list_gen import generar_lista_aves
from string import Template

nom_esp_template = Template('<li> $nom_esp </li>')
nom_eng_template = Template('<li> $nom_eng </li>')
img_template = Template('<li><img src="$url"/><li>')

html_template = Template('''<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Document</title>
</head>
<body>
<ul>
$body
</ul>
</body>
</html>
''')

lista_url = generar_lista_aves()
texto_html= ''

for url in lista_url:
    texto_html += nom_esp_template.substitute(nom_esp = url[0]) + nom_eng_template.substitute(nom_eng = url[1]) + img_template.substitute(url = url[2]) +'\n'
    
html = html_template.substitute(body = texto_html)

with open('output.html', 'w') as f:
    f.write(html)