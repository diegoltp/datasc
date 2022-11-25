from string import Template

def base_html(titulo, autor):
    '''
    Resumen: [Entrega el script base para el sitio web]
    args: 
    [titulo][str][Titulo del sitio web]
    [autor][str][Autor para agregar al titulo]
    return: [html_template] [scrip html base]
    '''
    html_template = Template(f'''<!DOCTYPE html>
    <html>
    <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{titulo} - {autor}</title>
    </head>
    <body>
    <ul>
    $body
    </ul>
    </body>
    </html>
    ''')
    return html_template