# Notas del Curso  
## Chuleta Shell  
- Borrar Recursivo: rm -r  
- Agregar contenido: echo  
- Ver contenido de un archivo: cat  
- Cambiar nombre de archivo: mv  
- Para abrir archivos grandes: less  
- Para ver la docu de cun comando: man  
- Para ver el árbol de archivos: tree  
- Para ejecutar los archivos bash: bash  
- Ver la primera/ultima parte de la data: head/tail  
- Remplazar texto: sed  
- Contar caracteres: wc  
- Hacer búsquedas en texto con Regex: grep 

## Conceptos teóricos
- Formatos para almacenar datos.  
        - CSV y JSON.  
- Tabla: Columnas(campos, atributos) y Registros(renglones, filas, tuplas).  
- PLSQL: Lenguaje de programación para SQL.  
- Sistemas de gestor de base de datos: existen dos tipos que pueden instalarse en un servidor.  
  - Relacionales (SQL).  
  - No Relacionales (NoSQL).  
- Clientes: las consultas son una forma de buscar y recopilar  información de una BBDD.  
- Miniconda: genera ambientes de trabajo para trabajar en versiónes especificas de software.  
- MyCli: Herramienta de código abierto para hacer consultas en SQL en la consola.  

### Sesión 3 y 4: MySQL
- Crear Tablas: CREATE TABLE IF NOT EXISTS ratings (userID INT PRIMARY KEY, movieID INT, rating INT, tiempo TIMESTAMP);
- Cargar CSV locales a SQL: LOAD DATA LOCAL INFILE "/Users/josecarloscorona/Documents/GitHub/CursoBD/Intrduccion-a-Bases-de-Datos/Sesion-03/Ejemplo-02/Datos/ml-1m/users.csv" INTO TABLE users;
- Para borrar registros: TRUNCATE ratings;
- Llave Primaria: Clave única para identificar campos  
        **- Comandos SQL:**
        - ORDER BY (DESC | ASC)
        - WHERE (Operadores lógicos: AND, OR, NOT)
        - FROM
        - LIKE (% = sustituye por cualquier carácter, _ = sustituye 1 solo caacter)
        **Joins**
        - Inner Join (Registros que estén en ambas tablas)
        - Left Outer Join (Regístros que estén en la columna izquierda)
        - Right Outer Join (Regístros que estén en la columna derecha)
        - Full Outer Join (Todos los registros)


