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

--2.- RESPONDER LAS CONSULTAS

--Canciones que salieron el 2018
SELECT  t1.titulo_cancion, t2.anio
    FROM cancion t1
    JOIN album  t2 ON (t1.album = t2.titulo_album)
    WHERE t2.anio='2018';

--Albums y nacionalidad de su artista
SELECT  t1.titulo_album, t2.nombre_artista, t2.nacionalidad
    FROM Album t1
    JOIN Artist  t2 ON (t1.artista = t2.nombre_artista)
    ORDER BY t2.nacionalidad;

/* Número de track, canción, album, año de lanzamiento y artista donde las
canciones deberán estar ordenadas por año del anzamiento del álbum, álbum
y artista correspondiente */

SELECT  t1.*, t2.anio
    FROM cancion t1
    JOIN album  t2 ON (t1.album = t2.titulo_album)
    ORDER BY (t2.anio, t1.album, t1.artista);



--Fuera del desafio, agregar la nacionalidad a la tabla anterior
SELECT t1.nacionalidad, t2.*
    --definir tabla 1
    FROM (
        SELECT  tmp_t1.titulo_album, tmp_t2.nacionalidad
        FROM Album tmp_t1
        JOIN Artist  tmp_t2 ON (tmp_t1.artista = tmp_t2.nombre_artista)
    ) AS t1
    --unirla a tabla 2
    JOIN (
        SELECT  tmp_t3.titulo_cancion, tmp_t3.artista, tmp_t3.album, tmp_t4.anio
        FROM cancion tmp_t3
        JOIN album  tmp_t4 ON (tmp_t3.album = tmp_t4.titulo_album)
    ) AS t2
    ON (t1.titulo_album = t2.album)
    ORDER BY (t2.anio, t2.album, t2.artista);

