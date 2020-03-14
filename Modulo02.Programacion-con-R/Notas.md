# Notas del modulo 2: Programación con R  
## BigData
Procesar grandes volúmenes de datos
- Volumen
- Velocidad
- Variedad

## Tipología de datos

- Generados por personas
- Generados por transacciones
- Generados por navegación web
- Generados por machine 2 machine
- Generados por biométrica
  
|BI | BIG DATA|
| ------------- | ------------- |
| Data Conocida | Extraer data, modelos|
| SQL | Py, R |

### Tipos de Datos en R

- integer
- numeric
- character
- logical
- factor
- complex

- Vector: dato lineal, mismo tipo de dato.
- Matriz: Vectores de más de una dimensión y que solo puede contener el mismo tipo de dato.  
- Data Frame: Tabla con vectores y distintos tipos de datos.  
- Lista: 
- Array: 

### Para ejecutar R desde la consula: 

```shell
cat Ejemplo-01.R | R --no-save
```

## Programación orientada a Objetos
- Objetos con atributos.
- Clase: objetos que comparten atributos entre sí.
- Funciónes: cosas que hace un objeto.  
- Método: función definido dentro de una clase.
- Instanciación: Materializar un objeto con sus métodos.  

### Funciónes básicas
- (): Para usar funciones sobre una variable.
- []: Para hacer extracciónes sobre una variable
- <-: Para definir variables
- class(): Para conocer la clase de una variable
- colnames(): Para conocer el nombre de las columnas de un dataset
- str(): Para conocer la estructura de un objeto
- ncol(): Para conocer la cantidad de columnas de un objeto
- $: para

### IF ELSE

- Si la expresión evaluada se es verdadera, arroja un resultado dependiendo del resultado.
  
### FOR
Se itera sobre un vector, de forma secuencial

### While
Se evalúa una expresión hasta que la expresión se cumpla.

## Análisis Exploratorió de Datos  

**Pasos:**  
1. Conocer las dis, observaciones y variables.  
2. Comprobar los registros vacíos.  
3. Medición, comparación y descripción: medidas de tendencia central, de dispersión, estadística multivariante.  
4. Plantear Hipótesis.  
5. Visualizar para entender la concentración y dispersión de los datos.  
6. Validar hipótesis. 