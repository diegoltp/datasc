/*
SE DEJA EL PRE PROCESO DE LA BASE DE DATO A MODO INFORMATIVO
AL FINAL DEL CODIGO SE ENCUENTRA LA QUERY SLICITADA.
*/

-- Crear base de datos
CREATE DATABASE best2018_spotify;

-- Crear tablas contenedoras
CREATE TABLE Artist( 
        nombre_artista varchar(25),
        fecha_de_nacimiento varchar(25),
        nacionalidad varchar(25)
);

CREATE TABLE Cancion( 
        titulo_cancion varchar(25),
        artista varchar(25),
        album varchar(25),
        numero_del_track varchar(25)
);

CREATE TABLE Album( 
        titulo_album varchar(25),
        artista varchar(25),
        anio varchar(25)
);

-- Cargar datos desde archivo CSV en las tablas creadas

COPY Artist FROM 'D:\\1fromlinux\\data_science\\Apuntes data science\\g56\\4sql\\s1\\d_eval\\Artista.csv' DELIMITER ',' CSV HEADER;

COPY Cancion FROM 'D:\\1fromlinux\\data_science\\Apuntes data science\\g56\\4sql\\s1\\d_eval\\Cancion.csv' DELIMITER ',' CSV HEADER;

COPY Album FROM 'D:\\1fromlinux\\data_science\\Apuntes data science\\g56\\4sql\\s1\\d_eval\\Album.csv' DELIMITER ',' CSV HEADER;

--CREAR RELACIONES Y LLAVES

-- llave padre nombre del artista en artist 
-- llave hija artista en album
ALTER TABLE artist
ADD PRIMARY KEY (nombre_artista);

ALTER TABLE album ADD CONSTRAINT fk_album_artist 
    FOREIGN KEY (artista)
    REFERENCES artist (nombre_artista);

-- llave padre titulo del album en album
-- llave hija album en cancion
ALTER TABLE Album
ADD PRIMARY KEY (titulo_album);

ALTER TABLE Cancion ADD CONSTRAINT fk_cancion_album
    FOREIGN KEY (album)
    REFERENCES album (titulo_album);

SELECT * FROM album;

SELECT * FROM artist;

SELECT * FROM cancion;

----------------------------------------------------------

--Tablas a unir
SELECT artista, numero_del_track FROM cancion
     WHERE numero_del_track = '4'

SELECT nombre_artista, nacionalidad, fecha_de_nacimiento
     FROM artist
     WHERE fecha_de_nacimiento >= '1992-01-01' 
        and nacionalidad = 'Estadounidense'
        LIMIT 1;

/*
DESAFIO 3
La canción que es el track número 4, del primer artista que aparece en la 
querie que indica los artistas de nacionalidad estadounidense que
nacieron después de 1992.
*/

SELECT 
    t1.artista, t1.titulo_cancion, t1.numero_del_track,
    t2.nacionalidad, t2.fecha_de_nacimiento
        FROM(
            SELECT 
                tmp_t1.artista, tmp_t1.titulo_cancion,
                tmp_t1.numero_del_track
                    FROM cancion tmp_t1
                    WHERE tmp_t1.numero_del_track = '4'
            ) as t1      
        JOIN(
            SELECT
                tmp_t2.nombre_artista, tmp_t2.nacionalidad,
                tmp_t2.fecha_de_nacimiento
                    FROM artist tmp_t2
                    WHERE tmp_t2.fecha_de_nacimiento >= '1992-01-01' 
                    and tmp_t2.nacionalidad = 'Estadounidense'
                    LIMIT 1
            ) as t2
        ON (t1.artista = t2.nombre_artista);