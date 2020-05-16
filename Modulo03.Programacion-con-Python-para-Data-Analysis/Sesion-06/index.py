from bottle import route, run, HTTPResponse
import csv
import io
import lc

@route('/hola')
def hola():
    '''Función principal del script'''
    return 'Hola Python'

@route('/json')
def json():
    '''Función para responder las peticiones GET /'''

    # Obtener la lista de archivos
    carpeta = lc.Carpeta('.')
    carpeta.obtiene_entradas()

    # Devuelve resultado
    return {'resultado': carpeta.entradas}

@route('/')
def index():
    '''Función para responder las peticiones GET /'''

    # Leer el contenido de index.html
    with open('index.html') as da:
        pagina = da.read()

    # Obtener lista de archivos
    carpeta = lc.Carpeta('.')
    carpeta.obtiene_entradas()
    # Construir la lista de entradas de tipo dict()
    entradas = [
        {'nombre': e[0], 'tamanio':e[1], 'fecha': e[2]}
        for e in carpeta.entradas
    ]
    # Integrar a lista de entradas al dict()
    dictArchivos = {'Archivos':entradas}
    return dictArchivos

    #Integrar lista con html
    tablaHTML = '<table>'
    for file in carpeta.entradas:
        linea = '<tr>'
        for column in file:
            linea += linea
        tablaHTML += '</table>'

    # Devuelve el resultado
    return pagina.format(tablaHTML)

@route('/csv')
def apicsv():
    """Atiende peticion GET /csv"""
    # Obtener la list de archivos
    carpeta = lc.Carpeta('.')
    carpeta.obtiene_entradas()
    # Agregando fila de encabezaods
    encabezados = ['Nombre', 'Tamaño','Fecha']
    entradas = [encabezados]
    entradas += carpeta.entradas

    # Construir la lista en un archivo CSV en memoria RAM
    da = io.StringIO()
    csv_writer = csv.writer(da)
    csv_writer.writerows(carpeta.entradas)
    # Reiniciando índice del archivo
    da.seek(0)
    # Personalizar encabezados de respuesta del HTTP
    h = {}
    h['content-type'] = 'text/csv'
    h['Content-Disposition'] = "attachment;filename = archivos.csv"

    return HTTPResponse(
        body=da.read(),
        status=200,
        headers=h
    )

run(host = 'localhost', port = 8080, debug = True)
