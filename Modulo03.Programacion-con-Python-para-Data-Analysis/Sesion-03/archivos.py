import os

## Modelo-Vista-Controlador (MVC)

# Modelo: Obtiene datos
def obtiene_entradas(ruta):
    """
    Obtiene la lista de entradas de ruta y regresa una lista con el nombre y tamaño de cada una.
    """
    # Se obtine el nombre de las entradas
    nombres = os.listdir(ruta)

    # Obtener el tamaño de cada uno de los elementos que son archivos
    # Agregando ruta a los nombres
    nombres = [os.path.join(ruta, n) for n in nombres]  # listas de comprension

    entradas = []
    for n in nombres:
        if os.path.isfile(n):
            #-obtener el tamaño de n-
            #-agregarlo a la lista-
            tamanio = os.path.getsize(n)
            entrada = [n, tamanio]
            entradas.append(entrada)
        else:
            # Entonces es una carpeta
            #-asignar tamaño igual cero-
            #-asignarlo a la lista-
            entrada = [n, 0]
            entradas.append(entrada)
    
    return entradas

# Vista: Genera resultados para el usuario.
def imprime_entradas(entradas):
    """ 
    Imprime la lista de las entradas en la salida estándar en forma tabular.
    """
    for e in entradas:
        print("{:60} {:10}".format(*e))

# Contralador: Manipular las funciones del Modelo y la Vista
def main(): #Función principal
    """
    Función principal del script
    """
    ruta = '/Users/josecarlos/Documents/Github/CursoBD/Modulo03.Programacion-con-Python-para-Data-Analysis/Sesion-03'
    entradas = obtiene_entradas(ruta)
    imprime_entradas(entradas)

if __name__ == "__main__": # el script es el programa principal?
    main()