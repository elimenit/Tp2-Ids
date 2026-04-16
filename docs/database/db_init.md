# /datbase/get_conexion.py
Obtiene la conexion con el DBMS mysql
## Correr el DBMS mysql
Iniciar el servicio de mysql
´´´
sudo systemctl start mysql
´´´
Entrar a mysql como super usuario
´´´
sudo mysql -u root -p
´´´
Cambiar la contraseña por si no se logran conectar desde mysql
Una vez haber entrado a mysql ejecutar
´´´
FLUSH PRIVILEGES;
ALTER USER 'root'@'localhost' IDENTIFIED BY 'tu_nueva_contraseña';
EXIT;
´´´
Reiniciar el servicio de mysql
´´´
sudo systemctl restart mysql
´´´
Intentar de vuelta si funciona¡
## Inportante
Recuerden configurar el archivo .env en la raiz del proyecto y siempre
 verificar que este agregado en el .gitignore