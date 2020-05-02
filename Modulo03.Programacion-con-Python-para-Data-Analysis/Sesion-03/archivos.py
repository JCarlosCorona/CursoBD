import csv
import json
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

def guarda_entradas_csv(entradas, arch_salida_csv):
    """ 
    Guarda la lista de las entradas en el arch_salida en formato csv.
    """
    with open(arch_salida_csv, 'w', encoding='utf-8') as da:
        da_csv = csv.writer(da)
        da_csv.writerow(['Nombre','Tamaño','Fecha'])
        for e in entradas:
            da_csv.writerow(e) # e = ['nombre', 123, 'fecha'] 

def guarda_entradas_json(entradas, total, arch_salida_json):
    """ 
    Guarda la lista de las entradas en el arch_salida en formato JSON.
    """
    with open(arch_salida_json, 'w') as da:
        json.dump(entradas, da, indent=4)

def guarda_entradas_json2(entradas, total, arch_salida_json2):
    """ 
    Guarda la lista de las entradas en el arch_salida en formato JSON usando objetos.
    """
    with open(arch_salida_json2, 'w') as da:
        json.dump(entradas, da, indent=4) ##### TAREA


# Contralador: Manipular las funciones del Modelo y la Vista
def main(): #Función principal
    """
    Función principal del script
    """
    ruta = '/Users/josecarlos/Documents/Github/CursoBD/Modulo03.Programacion-con-Python-para-Data-Analysis/Sesion-03'
    arch_salida_csv = ("salida.csv")
    arch_salida_json = ("salida.json")
    arch_salida_json2 = ("salida2.json")
    entradas, total = obtiene_entradas(ruta)
    imprime_entradas(entradas, total)
    guarda_entradas_csv(entradas, arch_salida_csv)
    guarda_entradas_json(entradas, total, arch_salida_json)
    guarda_entradas_json2(entradas, total, arch_salida_json2)

if __name__ == "__main__": # el script es el programa principal?
    main()