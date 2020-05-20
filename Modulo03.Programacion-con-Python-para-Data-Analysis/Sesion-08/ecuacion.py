import numpy as np

def main():
    """Función principal del script """
    # a X = b 3x3
    
    # Matriz de coeficientes
    a = np.array(
        [
            [2, 1, -3],
            [5, -4, 1],
            [1, -1, -4]
        ]
    )
    # Vector de resultados
    b = np.array([8, -19, 4])

    # Resolver el sistema de ecuaciones
    x = np.linalg.solve(a, b)
    
    print('El vector solucion es: ', x)

    # a x -> b
    b1 = np.dot(a, x)
    print(b)
    print(b1)

    ok= np.allclose(b, b1)
    if ok: 
        print('Resultado correcto')
    else:
        print('No seas zope!')

    # Guardar el vector resultado en el archivo soluciones.txt
    nomarch = 'soluciones.txt'
    np.savetxt(nomarch, x, fmt='%d')
    print(
        'La solución se ha guardado en',
        nomarch
    )

if __name__ == "__main__":
    pass