-- Crear base de datos
CREATE DATABASE almacen
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Spanish_Chile.1252'
    LC_CTYPE = 'Spanish_Chile.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

-- Crear tabla
CREATE TABLE Inventario( 
        codigo_producto int,
        producto varchar(225),
        local varchar(225),
        precio int,
        existencia VARCHAR,
        stock int,
        ubicacion varchar(225),
        numero_bodega int,
        vendedor varchar(225),
        rut_vendedor int,
        numero_boleta int,
        cantidad_vendida int,
        rut_cliente int,
        nombre_cliente varchar(225)
        );

COPY Inventario FROM 'D:\1fromlinux\data_science\Apuntes data science\g56\4sql\s2\d_eval\Apoyo_desafio.csv' DELIMITER ',' CSV HEADER;

--visualizar tabla
SELECT * FROM Inventario;

UPDATE Inventario
    set existencia = 'TRUE'
    where existencia = 'Si'
        OR existencia = '1';

/*
PRIMERA FORMA NORMAL
•	Boleta_Producto( #numero_boleta, codigo_producto, producto, precio,
                  cantidad_vendida, stock, existencia)
•	Venta(#numero_boleta, #local, ubicacion, #rut_cliente, nombre_cliente, 
                     numero_bodega, vendedor, rut_vendedor)
*/ 


SELECT  numero_boleta, codigo_producto, producto, precio, cantidad_vendida,
        stock, existencia
    INTO Boleta_Producto	
    FROM Inventario;

SELECT  numero_boleta, local, ubicacion, rut_cliente, nombre_cliente,
        numero_bodega, vendedor, rut_vendedor
    INTO Venta	
    FROM Inventario;

DROP TABLE Inventario;

/*SEGUNDA FORMA NORMAL
•	Boleta_Producto( #numero_boleta, codigo_producto, cantidad_vendida, stock, existencia)
•	Venta(#numero_boleta,  #local,  #rut_cliente, nombre_cliente,  #numero_bodega)
•	producto(#codigo_producto, producto, precio)
•	local(#local, ubicacion, vendedor, rut_vendedor)
•	bodega(#numero_boleta,  numero_bodega)

*/

-- producto(#codigo_producto, producto, precio)
--
--local(#local, ubicacion, vendedor, rut_vendedor)
--

SELECT DISTINCT codigo_producto, producto, precio
    INTO producto
    FROM boleta_producto;

ALTER TABLE boleta_producto
    DROP COLUMN producto;
ALTER TABLE boleta_producto
    DROP COLUMN precio;

SELECT DISTINCT local, ubicacion, vendedor, rut_vendedor
    INTO local_venta
    FROM venta;

ALTER TABLE venta
    DROP COLUMN ubicacion;
ALTER TABLE venta
    DROP COLUMN vendedor;
ALTER TABLE venta
    DROP COLUMN rut_vendedor;

SELECT numero_boleta, numero_bodega
    INTO bodega
    FROM venta;
ALTER TABLE venta
    DROP COLUMN numero_bodega;

/*TERCERA FORMA NORMAL
•	Venta(#numero_boleta,  #local,  #rut_cliente)

•	Boleta_Producto( #numero_boleta, codigo_producto, cantidad_vendida)
•	cliente(#rut_cliente, nombre_cliente)
•	stock_producto(#codigo_producto, stock, existencia)
•	producto(#codigo_producto, producto, precio)
•	local(#local, ubicacion, vendedor, rut_vendedor)
•	bodega(#numero_boleta,  numero_bodega)
*/


SELECT DISTINCT rut_cliente, nombre_cliente
    INTO cliente
    FROM venta;

ALTER TABLE venta
    DROP COLUMN nombre_cliente;

SELECT DISTINCT codigo_producto, stock, existencia
    INTO stock_producto
    FROM boleta_producto;

ALTER TABLE boleta_producto
    DROP COLUMN stock;
ALTER TABLE boleta_producto
    DROP COLUMN existencia;





SELECT * FROM Boleta_Producto;
SELECT * FROM venta; 

SELECT * FROM bodega;
SELECT * FROM producto;
SELECT * FROM local_venta;

SELECT * FROM cliente;
SELECT * FROM stock_producto;


ALTER TABLE boleta_producto 
    ADD CONSTRAINT PK_boleta PRIMARY KEY (numero_boleta);

ALTER TABLE venta
    ADD CONSTRAINT PK_venta PRIMARY KEY (numero_boleta);

ALTER TABLE producto
    ADD CONSTRAINT PK_producto PRIMARY KEY (codigo_producto);

ALTER TABLE local_venta
    ADD CONSTRAINT PK_local PRIMARY KEY (local);

ALTER TABLE cliente
    ADD CONSTRAINT PK_cliente PRIMARY KEY (rut_cliente);

ALTER TABLE stock_producto
    ADD CONSTRAINT PK_stock PRIMARY KEY (codigo_producto);

ALTER TABLE bodega
    ADD CONSTRAINT PK_bodega PRIMARY KEY (numero_boleta);



ALTER TABLE venta 
    ADD CONSTRAINT FK_boleta FOREIGN KEY (numero_boleta)
        REFERENCES boleta_producto (numero_boleta);

ALTER TABLE boleta_producto 
    ADD CONSTRAINT FK_producto FOREIGN KEY (codigo_producto)
        REFERENCES producto (codigo_producto);

ALTER TABLE boleta_producto 
    ADD CONSTRAINT FK_stock_producto FOREIGN KEY (codigo_producto)
        REFERENCES stock_producto (codigo_producto);

ALTER TABLE venta
    ADD CONSTRAINT FK_local FOREIGN KEY (local)
        REFERENCES local_venta (local);

ALTER TABLE venta
    ADD CONSTRAINT FK_cliente FOREIGN KEY (rut_cliente)
        REFERENCES cliente (rut_cliente);

ALTER TABLE boleta_producto 
    ADD CONSTRAINT FK_bodega FOREIGN KEY (numero_boleta)
        REFERENCES bodega (numero_boleta);


