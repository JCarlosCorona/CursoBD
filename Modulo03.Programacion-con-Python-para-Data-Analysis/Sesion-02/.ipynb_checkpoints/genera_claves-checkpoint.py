# Importar módulos
import random
import collections
import string

# Lee el valor del número de claves n
n = 1

esCorrecto = False # Bandera para cicnlo while
while not esCorrecto:
    n = input("Cuantas claves a generar n: ")
    esCorrecto = n.isdigit()
    if not esCorrecto:
        print('El valor', n, " no es un entero, por favor ingrese un entero")
    else:
         n = int(n)
            
            
# Lee el valor de la longitud de claves
m = 8
esCorrecto = False # Bandera para cicnlo while
while not esCorrecto:
    r = input("Ingresa longitud de claves (8): ")
    print(r)
    esCorrecto = r.isdigit() or r == ""
    if not esCorrecto:
        print('El valor', m, " no es un entero, por favor ingrese un entero")
    else:
        if r.isdigit():
            m = int(r)
            
print(n, type(n))
print(m, type(m))

# Incluye mayúsculas
mayusculas = "ABCDEFGHIJKLMNÑOPQRTUVWXYZ"
minusculas = mayusculas.lower()
digitos = "1234567890"
simbolos = "#&%&/"
alfabeto = mayusculas + minusculas + digitos + simbolos
# Generando n claves
for x in range(n):
# Generando clave        
    clave = random.choice(mayusculas)
    clave += random.choice(minusculas)
    digitos += random.choice(digitos)

     # Cuántas letras nos faltan?
    nl = m - 2
    faltan = random.choices(alfabeto, k=nl) # regresa una lista
    faltan = "".join(faltan) #convertimos lista a str
    clave += faltan

    print(clave)