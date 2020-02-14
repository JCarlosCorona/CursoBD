USE JCarlosCorona
CREATE TABLE IF NOT EXISTS ProductPerf (SKU VARCHAR(20) PRIMARY KEY, Producto VARCHAR(300), Ingresos FLOAT(30,2), ComprasUnicas INT, Cantidad INT, PrecioMedio FLOAT(30,2), Reembolso FLOAT(30,2), PorcentCarritoDetalle FLOAT(2,2), PorcentCompraDetalle FLOAT(2,2));
LOAD DATA LOCAL INFILE "/Users/josecarloscorona/Documents/GitHub/CursoBD/Intrduccion-a-Bases-de-Datos/MiProyecto/ProdPerf.2019.csv" INTO TABLE ProductPerf;
