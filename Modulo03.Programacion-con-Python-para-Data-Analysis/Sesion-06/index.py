from bottle import route, run
import lc

@route('/hola')
def hola():
    '''
    Función principal del script
    '''
    return 'Hola Python'

@route('/')
def index():
    '''
    Función para esponder la petición GET /
    '''
    # Leer el contenido de index.html
    with open('index.html') as da:
        pagina = da.read()
    
    # Obtener la lista de archivos
    carpeta = lc.Carpeta('.')
    carpeta.obtiene_entradas()
    # Integrar la lista con el html
    tabla = '<table>\n'
    for file in carpeta.entradas:
        linea = '<tr>'
        tabla += linea
    tabla += '</table>\n'
    # Insertando la tabla en la página
    pagina = pagina.replace('{TABLA}',tabla)

    return pagina

#-----
@route('/json')
def apijson():
    '''
    Atiende la peticion GET  /json
    '''
    # Leer el contenido de index.html
    with open('index.html') as da:
        pagina = da.read()
    
    # Obtener la lista de archivos
    carpeta = lc.Carpeta('.')
    carpeta.obtiene_entradas()
    # Integrar la lista con el html
    tabla = '<table>\n'
    for file in carpeta.entradas:
        linea = '<tr>'
        for column in file:
            linea += '<td>{0}<td>'.format(column)
        linea += '</tr>'
        tablaHTML = linea
    tablaHTML = '</table>'

    # Devuelve el resultado
    return pagina.format(tablaHTML)

run(host = 'localhost', port = 8080, debug = True)