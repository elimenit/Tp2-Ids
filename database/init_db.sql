CREATE DATABASE IF NOT EXISTS mundial_futbol;

CREATE TABLE IF NOT EXISTS equipos (

);
CREATE TABLE IF NOT EXISTS partidos (

);
CREATE TABLE IF NOT EXISTS estadios (

);
CREATE TABLE IF NOT EXISTS ciudades (

);
CREATE TABLE IF NOT EXISTS fase_torneo (

);
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER NOT NULL AUTO_INCREMENENT PRIMARY KEY;
    nombre VARCHAR(20),
    email VARCHAR(20)
);
CREATE TABLE IF NOT EXISTS prediccion (
    id_usuario INTEGER,
    id_equipo_local VARCHAR(20),
    id_equipo_visitante VARCHAR(20)
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id) ON DELETE CASCADE,
    FOREIGN KEY (id_equipo_local) REFERENCES equipos(id) ON DELETE CASCADE,
    FOREIGN KEY (id_equipo_visitante) REFERENCES equipos(id) ON DELETE CASCADE  
);
CREATE TABLE IF NOT EXISTS ranking (

);
CREATE TABLE IF NOT EXISTS resultados (
    
);
INSERT INTO usuarios(nombre, email) VALUES ('Juan Gonzales', 'jgonzales@gmail.com');
INSERT INTO usuarios(nombre, email) VALUES ('Lanuss', 'lanuss@gmail.com');