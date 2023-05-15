--1 crear db
CREATE DATABASE Biblioteca;
--2 crear tabla
CREATE TABLE libro( 
        id_libro varchar(25),
        nombre_libro varchar(100),
        autor varchar(25),
        genero varchar(25),
        PRIMARY KEY (id_libro)
);
--3 y 4 insertar datos
INSERT INTO libro
    (id_libro,nombre_libro,autor,genero)
VALUES 
    ('sayse_n1', 'Sapo y Sepo', 'Leonardo Davinci', 'comedia'),
    ('metam_n1', 'La metamorfosis', 'Juanito ayala', 'autoayuda');

SELECT * FROM libro

--5 TABLA PRESTAMOS
CREATE TABLE Prestamo (
    id_prestamo varchar(25),
    id_libro varchar(25),
    nombre_persona varchar(25),
    fecha_inicio date,
    fecha_termino date,
    PRIMARY KEY (id_prestamo),
    FOREIGN KEY (id_libro) REFERENCES libro(id_libro);
)

--6 añadir columna

ALTER TABLE libro add prestado boolean;
SELECT * FROM libro;

--7 y 8 actualizar estado a ambos libros

UPDATE libro set prestado='False'
    WHERE id_libro = 'sayse_n1';
UPDATE libro set prestado='False'
    WHERE id_libro = 'metam_n1';

--9 y 10 ingresar prestamos

INSERT INTO Prestamo
    (id_prestamo, id_libro, nombre_persona, fecha_inicio, fecha_termino)
VALUES 
    ('1',       'sayse_n1',  'pedro',       '2021/01/01',      '2021/01/10'),
    ('2',       'sayse_n1',  'juan',        '2021/02/01',      '2021/02/10'),
    ('3',       'sayse_n1',  'diego',       '2021/03/01',      '2021/03/10'),
    ('4',       'sayse_n1',  'sepo',        '2021/04/01',      '2021/04/10'),
    ('5',       'sayse_n1',  'alonso',      '2021/05/01',      '2021/05/15'),
    ('6',       'metam_n1',  'diego',       '2021/02/01',      '2021/02/05'),
    ('7',       'metam_n1',  'sepo',        '2021/04/10',      '2021/4/20'),
    ('8',       'metam_n1',  'arnaldo',     '2021/05/01',      '2021/05/10'),
    ('9',       'metam_n1',  'patricio',    '2021/06/01',      '2021/06/15'),
    ('10',       'metam_n1',  'paola',      '2021/07/01',      '2021/07/13'),
    ('11',       'metam_n1',  'karen',      '2021/12/01',      '2021/12/28');

SELECT * FROM prestamo

--11 nuevo libro

INSERT INTO libro 
    (id_libro,nombre_libro,autor,genero)
VALUES 
    ('hobbi_n1', 'El hobbit', 'J. R. R. Tolkien', 'Fantasia heroica');


--12 seleccionar libros y personas que pidieron prestado

SELECT  t1.nombre_libro, t2.nombre_persona
    FROM libro t1
    JOIN prestamo  t2 ON (t1.id_libro = t2.id_libro);

--13 seleccionar todas las columnas de prestamo para sapo y sepo ordenado decreciente por
--fecha de inicio

SELECT prestamo.* FROM prestamo WHERE id_libro='sayse_n1'
    ORDER BY fecha_inicio;

--OPCIONAL

CREATE TABLE contabilidad(
    usuario VARCHAR(25),
    deuda INT,
    id_usr VARCHAR(25),
    PRIMARY KEY (id_usr)
);

INSERT INTO contabilidad
    (usuario, deuda, id_usr)
VALUES 
    ('pedro',   '0',  'usr1'),
    ('juan',   '10',  'usr2'),
    ('diego',   '20',  'usr3'),
    ('sepo',   '30',  'usr4'),
    ('alonso',   '40',  'usr5'),
    ('arnaldo',   '110',  'usr6'),
    ('patricio',   '220',  'usr7'),
    ('paola',   '4440',  'usr8'),
    ('karen',   '11110',  'usr9');


SELECT * FROM contabilidad

ALTER TABLE prestamo add usr_id VARCHAR(25);

UPDATE prestamo set usr_id='usr1'
    WHERE nombre_persona = 'pedro';
UPDATE prestamo set usr_id='usr2'
    WHERE nombre_persona = 'juan';
UPDATE prestamo set usr_id='usr3'
    WHERE nombre_persona = 'diego';
UPDATE prestamo set usr_id='usr4'
    WHERE nombre_persona = 'sepo';
UPDATE prestamo set usr_id='usr5'
    WHERE nombre_persona = 'alonso';
UPDATE prestamo set usr_id='usr6'
    WHERE nombre_persona = 'arnaldo';
UPDATE prestamo set usr_id='usr7'
    WHERE nombre_persona = 'patricio';
UPDATE prestamo set usr_id='usr8'
    WHERE nombre_persona = 'paola';
UPDATE prestamo set usr_id='usr9'
    WHERE nombre_persona = 'karen';

SELECT * FROM prestamo

--ALTER TABLE child_table
--ADD CONSTRAINT constraint_name FOREIGN KEY (c1) REFERENCES parent_table
--(p1);

--crear relacion foranea en caso que se desee completar otras funciones no requeridas

ALTER TABLE prestamo 
ADD CONSTRAINT fk_usr_id 
FOREIGN KEY (usr_id) REFERENCES contabilidad (id_usr);


