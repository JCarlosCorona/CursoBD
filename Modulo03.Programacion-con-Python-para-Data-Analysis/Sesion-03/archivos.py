import os
import time
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
    total = 0
    for n in nombres:
        fecha = time.ctime(os.path.getmtime(n))
        if os.path.isfile(n):
            #-obtener el tamaño de n-
            #-agregarlo a la lista-
            tamanio = os.path.getsize(n)
            entrada = [n, tamanio, fecha]
            entradas.append(entrada)
            total += tamanio
        else:
            # Entonces es una carpeta
            #-asignar tamaño igual cero-
            #-asignarlo a la lista-
            entrada = [n, 0, fecha]
            entradas.append(entrada)
    
    return entradas, total

# Vista: Genera resultados para el usuario.
def imprime_entradas(entradas, total):
    """ 
    Imprime la lista de las entradas en la salida estándar en forma tabular.
    """
    for e in entradas:
        print("{:60} {:10} {:24}".format(*e))
    print('Total de bytes: {}'.format(total))

# Contralador: Manipular las funciones del Modelo y la Vista
def main(): #Función principal
    """
    Función principal del script
    """
    ruta = '/Users/josecarlos/Documents/Github/CursoBD/Modulo03.Programacion-con-Python-para-Data-Analysis/Sesion-03'
    entradas, total = obtiene_entradas(ruta)
    imprime_entradas(entradas, total)

if __name__ == "__main__": # el script es el programa principal?
    main()