# **UT4-A1: Implantación de Wordpress**

## **Configuración de la base de datos**

Para empezar usaremos el intérprete de MySQL para acceder a una base de datos.

![1](img/1.png)

Creamos una base de datos, un usuario y le asignamos privilegios.

![2](img/2.png)

![3](img/3.png)

![4](img/4.png)

## **Descarga del código**

Descargamos el código fuente de Wordpress desde su página web.

![5](img/5.png)

Ahora descomprimimos el código y lo copiamos en */usr/share*

![6](img/6.png)

![7](img/7.png)

Establecemos los permisos necesarios para que el usuario web *www-data* pueda usar estos ficheros.

![8](img/8.png)

## **Editar ficheros de Configuración**

Para una configuración básica de WordPress debemos especificar lo siguiente:

    - El nombre de la base de datos.
    - El usuario.
    - La contraseña.

![9](img/9.png)

![10](img/10.png)

## **Acceso mediante Nginx**

Para que nuestro sitio Wordpress sea accesible desde un navegador web, debemos incluir las directivas necesarias en la configuración del servidor web Nginx.

Supongamos que queremos acceder a nuestro Wordpress desde la url wordpress.vps.claseando.es. Para ello tendremos que crear un nuevo virtual host de la siguiente manera:

![11](img/11.png)

![12](img/12.png)

Enlazamos la configuración para que el virtual host esté disponible:

![13](img/13.png)

Recargamos el servidor web Nginx para que los cambios sean efectivos:

![14](img/14.png)

## **Configuración del sitio vía web**

Cuando accedemos a http://wordpress.aluXXXX.me nos redirige a http://wordpress.aluXXXX.me/wp-admin/install.php

Elegimos Español (O el idioma deseado).

![15](img/15.png)

Rellenamos los campos que nos piden y pulsamos *Instalar Wordpress*.

![16](img/16.png)

![17](img/17.png)

Accedemos con uestras credenciales.

![18](img/18.png)

![19](img/19.png)

## **Ajustes de permalinks**

Nos dirigimos a Ajustes, en el panel a la izquierda, y seleccionamos *Enlaces permanentes*.

![20](img/20.png)

seleccionamos *Día y nombre* y guardamos los cambios.

![21](img/21.png)

Ahora indicamos a Nginx que enlace estas URLs:

![22](img/22.png)
(Solo hace falta añadir la última location que se muestra en la captura.)

Recargamos la configuración de Nginx con el comando **sudo systemctl reload nginx**

## **Límite de tamaño en la subida de archivos**

Por defecto, el tamaño límite de subida de los archivos es de 2MB, así que procedemos a cambiarlo:

Modificamos estas líneas del siguiente fichero.

![23](img/23.png)

![24](img/24.png)

![25](img/25.png)

![26](img/26.png)

A continuación reiniciamos el servicio *php-fpm*.
Además, deberemos añadir una líneaen el fichero de configuración de Nginx.

![27](img/27.png)

![28](img/28.png)

Para que los cambios se guarden, recargamos el servidor web Nginx.

![29](img/29.png)

## **Estructura de ficheros**

Comprobamos la estructura de ficheros.

![30](img/30.png)

![31](img/31.png)

## **Sitio web seguro**

Para hacer que este sitio web sea seguro, deberemos ejecutar *certbot* desde nuestro terminal.

![32](img/32.png)

Elegimos el sitio web que queremos que sea seguro y seleccionamos las otras opciones a nuestro gusto.

![33](img/33.png)

Comprobamos:

![34](img/34.png)

Una vez hecho todo esto, podemos editar nuestro WordPress.

![35](img/35.png)
