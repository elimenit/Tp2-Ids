CREATE DATABASE IF NOT EXISTS mundial_futbol;
USE mundial_futbol;
CREATE TABLE IF NOT EXISTS fases (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL UNIQUE
);
CREATE TABLE IF NOT EXISTS partidos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    equipo_local VARCHAR(100),
    equipo_visitante VARCHAR(100),
    fecha DATE,
    fase_id INT NOT NULL,
    FOREIGN KEY (fase_id) REFERENCES fases(id) ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS usuarios (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL
);
CREATE TABLE IF NOT EXISTS predicciones (
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
INSERT IGNORE INTO fases(nombre) VALUES ('GRUPOS');
INSERT IGNORE INTO fases(nombre) VALUES ('CUARTOS');
INSERT IGNORE INTO fases(nombre) VALUES ('OCTAVOS');
INSERT IGNORE INTO fases(nombre) VALUES ('DIECISEISAVOS');
INSERT IGNORE INTO fases(nombre) VALUES ('SEMIS');
INSERT IGNORE INTO fases(nombre) VALUES ('FINAL');


