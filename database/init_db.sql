CREATE DATABASE IF NOT EXISTS mundial_futbol;
USE mundial_futbol;
CREATE TABLE IF NOT EXISTS equipos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    pais VARCHAR(50) NOT NULL
);
CREATE TABLE IF NOT EXISTS fases (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL
);
CREATE TABLE IF NOT EXISTS partidos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    equipo_local_id INT NOT NULL,
    equipo_visitante_id INT NOT NULL,
    fecha DATETIME,
    fase_id INT NOT NULL,
    FOREIGN KEY (equipo_local_id) REFERENCES equipos(id),
    FOREIGN KEY (equipo_visitante_id) REFERENCES equipos(id),
    FOREIGN KEY (fase_id) REFERENCES fases(id)
);
CREATE TABLE IF NOT EXISTS usuarios (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL
);
CREATE TABLE IF NOT EXISTS prediccion (
    usuario_id INT NOT NULL,
    partido_id INT NOT NULL,
    goles_local INT NOT NULL,
    goles_visitante INT NOT NULL,
    PRIMARY KEY (usuario_id, partido_id),
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE,
    FOREIGN KEY (partido_id) REFERENCES partidos(id) ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS ranking (
    usuario_id INT PRIMARY KEY NOT NULL,
    puntos INT NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS resultados (
    partido_id INT PRIMARY KEY NOT NULL,
    goles_local INT,
    goles_visitante INT,
    FOREIGN KEY (partido_id) REFERENCES partidos(id) ON DELETE CASCADE
);
INSERT INTO usuarios(nombre, email) VALUES ('Juan Gonzales', 'jgonzales@gmail.com');
INSERT INTO usuarios(nombre, email) VALUES ('Lanuss', 'lanuss@gmail.com');