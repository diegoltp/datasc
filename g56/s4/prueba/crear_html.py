
def crear_archivo_html(script_html, nombre_archivo):
    '''
    Resumen: [Escribe un archivo nuevo en html con el script proporcionado]
    arg: 
    [script_html][str][script generado en html]
    [nombre_archivo][str][nombre para el archivo a crear]
    return:[none]
    '''
    with open(f'{nombre_archivo}.html', 'w') as f:
        f.write(script_html)
        print('Archivo creado')
