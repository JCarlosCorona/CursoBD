from bottle import route, run
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

    #Integrar lista con html
    tablaHTML = '<table>'
    for file in carpeta.entradas:
        linea = '<tr>'
        for column in file:
            linea += linea
        tablaHTML += '</table>'

    # Devuelve el resultado
    return pagina.format(tablaHTML)

run(host = 'localhost', port = 8080, debug = True)
