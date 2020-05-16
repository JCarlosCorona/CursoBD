# Ecommerce Product Analysis
Analizar datos del rendimiento de productos de Google Analytics para extraer insights valiosos y accionables que permitan aumentar el revenue de un eCommerce.  

## Esquema  
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

**Proyecto.ProductoCategory_SKU**  
Descripción: Categorías de producto y SKU

| Campo | Detalle |
| ------------- | ------------- |
| _id  | ID Único Autogenerado |
| CategoriaProducto | Categoría al que pertenece el producto |
| SKU | Código único del producto vendido |

### Pre-requisitos 📋
Descargar: Mongo DB Comppas
https://downloads.mongodb.com/compass/mongodb-compass-community_1.20.5_amd64.deb
```
Acceso: mongodb+srv://Guest:BemxIKNGIaR0xSk3@cluster0-favba.mongodb.net/test
Usser: Guest
Pass: BemxIKNGIaR0xSk3
```

## Autores ✒️
* **José Carlos Corona** - *Trabajo Inicial* - [JCarlosCorona](https://github.com/JCarlosCorona)
* **Manuel Soto** - *Asesoramiento* - [manu-msr](https://github.com/manu-msr)
* **Ricardo Torres** - *Asesoramiento* - [rctorr](https://github.com/rctorr)


## Expresiones de Gratitud 🎁
* Comenta a otros sobre este proyecto 📢
* Muchas Gracias a BEDU por lo aprendido!!

---
⌨️ con ❤️ por [JCarlosCorona](https://github.com/JCarlosCorona/) 😊