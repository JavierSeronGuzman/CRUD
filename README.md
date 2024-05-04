Para levantar el contenedor de la base de datos en la terminal se ingresa
## cd db
Una vez se este en la carpeta se coloca el siguiente comando para levantar el contenedor 
## docker compose up -d --build
y despues uno se va a la carpeta de TareaAPI
## cd ..
Utilizando el mismo contenedor para levantar ese contenedor igualmente
## docker compose up -d --build

Una vez esten levantados todos los contenedores, estara funcionando la API y se podran probar las solicitudes

En la base de datos conectarse con la extensión de mysql al puerto 3306, usuario root y contraseña root, nombre de la conexión db,
luego ir al archivo my_collections.sql activar la conexión y correr todas las query que se encuentran en orden, para crear la tabla, en caso de tirar 
error de permisos cambiar a usuario seron.

*SIEMPRE SE TIENE QUE LEVANTAR EL DOCKER DE LA BASE DE DATOS PRIMERO Y CREAR LA BASE DE DATOS Y LA TABLA*