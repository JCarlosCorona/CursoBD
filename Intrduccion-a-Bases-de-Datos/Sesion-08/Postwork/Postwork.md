# Bases de datos en la nube aplicado a tú Proyecto.
## OBJETIVO
- Que el alumno aplique los conocimientos de esta sesión en su proyecto personal.
## REQUISITOS
1. Repositorio actualizado
2. Usar la carpeta de trabajo Sesion-08/Postwork
3. MongoDB Atlas configurado
4. Compass instalado, corriendo y conectado al Cluster MongoDB
5. Conjuntos de datos del proyecto que deses analizar
6. Cuenta en MongoDB Atlas
## DESARROLLO
1. Realizar una conexión desde Compass a la base de datos creada en MongoDB Atlas.
```
Acceso: mongodb+srv://Guest:BemxIKNGIaR0xSk3@cluster0-favba.mongodb.net/test
Usser: Guest
Pass: BemxIKNGIaR0xSk3
```
- Desactive el filtro de IP por lo que puedes conectarte usando la conexión anterior
- La ruta de la data es: Proyecto.ProductPerformance

2. Analizar la estructura de los datos para conocer el contexto y poder formular preguntas.
El esquema de la data es la siguiente:
**Proyecto.ProductPerformance**  
Descripción: Rendimiento de los productos del sitio

| Campo | Detalle |
| ------------- | ------------- |
| _id  | ID Único Autogenerado |
| Cantidad  | Cantidad de productos comprados |
| CantidadMedia | Cantidad media de productos comprados |
| ComprasUnicas | Cantidad de productos únicos comprados |
| Ingresos | Ingresos Totales de los productos en USD |
| PorcentCarritoDetalle | Cantidad de productos añadidos a carrito divididas entre visualizaciones del producto |
| PorcentCompraDetalle | Cantidad de productos compradas divididas entre visualizaciones del producto |
| PrecioMedio | Ticket Promedio |
| Producto | Nombre del Producto |
| Reembolso | Importe devuelto asociado al producto |
| SKU | Código único del producto vendido |

3. Después, formular preguntas sobre el conjuntos de datos
- ¿Qué cantidad de productos se vendieron el el periódo?
- ¿De que fechas es el periodo de datos?
- ¿Cuanto es el ingreso total del periódo?
- ¿Cuál es el producto con mayor ingreso?
- Cuál es el producto más comprado?


1. Por cada pregunta, realizar las consultas o ajustes necesarios a los datos para poder responderlas.
- ¿Qué cantidad de productos se vendieron el el periódo?
![alt text](https://github.com/adam-p//Users/josecarloscorona/Documents/GitHub/CursoBD/Intrduccion-a-Bases-de-Datos/Sesion-08/Postwork "Logo Title Text 1")   

- ¿Qué cantidad de productos se vendieron el el periódo?
- ¿De que fechas es el periodo de datos?
- ¿Cuanto es el ingreso total del periódo?
- ¿Cuál es el producto con mayor ingreso?
- Cuál es el producto más comprado?
