from string import Template

def base_html():
    '''
    Resumen: [Entrega el script base para el sitio web]
    args: [none]
    return: [html_template] [scrip html base]
    '''
    html_template = Template('''<!DOCTYPE html>
    <html>
    <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aves de Chile - Diegoltp</title>
    </head>
    <body>
    <ul>
    $body
    </ul>
    </body>
    </html>
    ''')
    return html_template