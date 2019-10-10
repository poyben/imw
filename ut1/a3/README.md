# **UT1-A3: Trabajo con virtual hosts**

En esta actividad, vamos a configurar 4 sitios web (virtual hosts) en nuestro servidor web *nginx*.

## Sitio web 1

Para este sitio web, asignaremos la siguiente dirección: *"http://imw.aluXXXX.me"*.
Dicha dirección nos deberá enseñar una página con la imagen "Diagrama de unidades de trabajo de IMW", la cual habremos descargado como se enseñará a continuación.

![descarga imagen](img/web1/1.1descargadiagrama.png)

Crearemos un directorio *imw* dentro de la carpeta **webapps** y guardamos ahí la imagen.

![guarda](img/web1/1.3imagenimg.png)

Luego creamos el servidor editando el fichero */etc/nginx/sites-available/imw.aluXXXX.me* usando el comando **nano**.

![crearserver1](img/web1/1.2creacionruta.png)

Creamos un index.html dentro de la carpeta */webapps/imw/* en el que pondremos la imagen para que se muestre correctamente.

Ahora dentro de esta carpeta deberían estar la carpeta **img** y el **index.html**.

![indexfoto](img/web1/1.4indexfoto.png)

A continuación tenemos que enlazar el fichero que hemos creado para que esté disponible desde los **sites-enabled**.

![enlace](img/web1/1.5enlazarvirtualhost.png)

Ahora, para comprobar que hemos realizado este apartado correctamnete, no tenemos que hacer más que abrir el navegador y buscar la URL "**imw.aluXXXX.me**". Si se ve el diagrama, hemos realizado este ejercicio con éxito.

![diagrama](img/web1/1.6diagramfinal.png)

>En caso de que no aparezca, ejecutar el comando "*sudo systemctl reload nginx*"

A continuación, vamos a hacer la segunda parte de este apartado, la cual consiste en mostrar una página con un enlace al Real decreto del título de Administración de Sistemas Informáticos en Red - MEC.

Primero nos dirigimos a la carpeta **webapps** y creamos la carpeta **mec**.

![carpetamec](img/web1/1.6.2carpetamec.png)

Tras haberla creado, modificamos el archivo */etc/nginx/sites-available/imw.aluXXXX.me* para añadir la segunda parte de la dirección.

![locationmec](img/web1/1.7creacionmec.png)

En la carpeta **mec** que creamos anteriormente, escribimos un fichero *index.html* usando el comando *nano* para añadir el enlace que nos lleve al archivo que pide el ejercicio.

![indexmec](img/web1/1.7enlacemec.png)

Ejecutamos el siguiente comando para reiniciar el servicio Nginx y se guarden los cambios.

![reloadmec](img/web1/1.8reload.png)

Para comprobar que hemos finalizado este primer ejercicio, nos vamos a dirigir a la página *imw.aluXXXX.me/mec* haremos click sobre el único enlace que nos debe aparecer, y por último veremos el archivo del Real Decreto.

![pagina mec](img/web1/1.9paginamec.png)

![pdf mec](img/web1/1.10pdf.png)

## Sitio web 2

En este segundo ejercicio debemos Debe mostrar el listado de ficheros y directorios de /var/lib de nuestra máquina.

Primero crearemos el fichero */etc/nginx/sites-available/varlib.alu6616.me* y escribimos lo siguiente:

![crearpagina](img/web2/2.1crearpagina.png)

>La línea "listen 9000;" es para que la página se pueda ver desde ese puerto.

Ahora crearemos la carpeta **varlib** en la carpeta **webapps**.

![carpetavarlib](img/web2/2.2crearcarpeta.png)

Enlazamos el fichero que creamos en el paso anterior desde */etc/nginx/sites-enabled*

![enlace](img/web2/2.2.1.png)

![enlacevarlib](img/web2/2.2ls.png)

Volvemos a recargar el servicio nginx para que se guarden los cabios con el comando "*sudo systemctl reload nginx*"

Comprobamos que la página *warlib.alu6616.me:9000* enseña un index con un único enlace y que dentro de ese enlace, se pueden ver todos los ficheros de la carpeta.

![final1](img/web2/final.png)

![final2](img/web2/final2.png)

## Sitio web 3

En este ejercicio debemos mostrar una página web con el nombre de todo el alumnado de clase a través de la página *https://ssl.aluXXXX.me/students/* que crearemos a continuación.

Antes que nada, tenemos que crear el fichero que dará lugar al servidor en la carpeta */etc/nginx/sites-available/* al que llamaremos *ssl.aluXXXX.me*.

![locationssl](img/web3/3.1location.png)

Creamos la carpeta **/webapps/students** y dentro de ella el **index.html** en el que pondremos la lista de todos los alumnos.

![carpetastudents](img/web3/3.2crearcarpeta.png)

![indexssl](img/web3/3.3crearindex.png)

Ahora vamos anlazar en la carpeta */etc/nginx/sites-enabled* como en los apartados anteriores.

![enlazarssl](img/web3/3.4enlazar.png)

Recargamos otra vez el servicio **nginx** si queremos comprobar que vamos bien encaminados.

![1comprobacion](img/web3/3.5comprobarlista.png)

A continuación, con estos dos comandos, crearemos una contraseña encriptada eligiendo una contraseña, en este caso "**2asir**" y una palabra clave par la encriptación "**anacardo**". Luego ejecutaremos el segundo comando con un usuario a nuestra elección (**usuario1**) y poniendo la contraseña encriptada que nos ha dado el primer comando.

![contra](img/web3/3.6creacionfichero.png)

Tras haber hecho esto, para conseguir que la página nos pida el usuario y la contraseña, modificaremos el fichero */etc/nginx/sites-available/ssl.aluXXXX.me* añadiendo las siguientes líneas:

![completlocation](img/web3/3.7completarlocation.png)

A modo de comprobación buscaremos en el navegador la página **ssl.aluXXXX.me** y veremos que nos pide identificación.

![final1](img/web3/3.8final.png)

![final2](img/web3/3.9final2.png)

Ahora vamos a restringir el acceso al archivo **.htpasswd**, que es donde se guardan las contraseñas.

![restrin](img/web3/3.10restringir.png)

Recargamos una vez más el servicio **nginx** para que los cambios se guarden y vemos que al dirigirnos a *ssl.aluXXXX.me/students/.htpasswd* nos manda a una página con un error, eso significa que hemos restringido el acceso a ese archivo correctamente.

![restringido](img/web3/3.11restringido.png)

Para conseguir que ésta sea una página segura con certificado, tenemos que instalar la aplicación **certbot**, la cual se encargará de modificar los archivos necesarios para cumplir el objetivo según la configuración que hagamos.

Para ello, ejecutamos los siguientes comandos:

![update](img/web3/3.12update.png)

![install](img/web3/3.13install.png)

![add](img/web3/3.14add.png)

![python](img/web3/3.15python.png)

Ahora lo ejecutamos con el siguiente comando, y para configurarlo, respondemos lo que nos va preguntando a gusto de cada uno:

![ejecutarcert](img/web3/3.16ejecutar.png)

>**OJO**, a esta pregunta responder a la dirección que pide el ejercicio.

>![eleccion](img/web3/3.17elegir3.png)

Al entrar en el fichero */etc/nginx/sites-available/ssl.aluXXXX/students* vemos que la aplicación a añadido líneas automáticamente.

![postcert](img/web3/postcerbot.jpg)

Procedemos a volver a recargar el servicio **nginx**.

Al comprobar entrando a la URL que configuramos, vemos que al lado de ella aparece un candado, lo que significa que es un sitio web seguro.

![finalcandado](img/web3/final.jpg)

![finalcandado2](img/web3/final2.jpg)

## Sitio web 4

Lo que nos pide este último ejrcicio es la  redirección cualquier petición del dominio http://redirect.aluXXXX.me al dominio http://target.aluXXXX.me.

Como en los otros tres ejercicios, debemos empezar creando el fichero */etc/nginx/sites-available/redirect.aluXXXX.me*.

![fichero](img/web4/4.1creacionserver.png)

Dentro de la carpeta **webapps** descargamos el siguiente **.zip** usando el comando *wget*.

```
https://github.com/sdelquin/claseando/raw/master/imw/UT1/assignments/assignment3/initializr-verekia-4.0.zip
```

![wget](img/web4/4.2descargar.png)

Descomprimimos lo que hemos descargado usando el comando **unzip**.

![unzip](img/web4/4.3unzip.png)

Y seguimos los siguientes pasos para borrar lo descargado y quedarnos con el fichero descomprimido y transformarlo en la carpeta **target**.

![carpetatarget](img/web4/4.3carpetatarget.png)

Ahora crearemos el fichero */etc/nginx/sites-available/target.aluXXXX.me*.

![servertarget](img/web4/4.4servertarget.png)

Y enlazamos las dos direcciones desde */etc/nginx/sites-enabled*.

![enlazartarget](img/web4/4.5enlazar.png)

Si queremos comprobar, abrimos un navegador y buscamos *redirect.aluXXXX.me/test*, *redirect.aluXXXX.me/probando*, *redirect.aluXXXX.me/hola* o *redirect.aluXXXX.me/cualquiercosa*.

![compro](img/web4/4.6test.png)

![compro2](img/web4/4.7probando.png)

![compro3](img/web4/4.8hola.png)

![comprobacion](img/web4/4.6comprobacion.png)

Vemos que nos ha redirigido a *target.aluXXXX.me*.

Ahora vamos a ir al directorio */var/log/nginx*

![varlognginx](img/web4/4.9cdvar.png)

Y dentro crearemos la carpeta **redirect**.

![mkdir](img/web4/4.10mkdirred.png)

Y creamos el archivo *redirect.aluXXXX.me*. (**OJO**, si no usamos **sudo** el sistema no nos dejará)

![sudo](img/web4/4.11sudored.png)

En dicho fichero escribiremos lo siguiente:

![nano](img/web4/4.12logs.png)

Comprobamos que en la carpeta **redirect** se han creado los archivos **access.log** y **error.log**.

![complogs](img/web4/4.13complogs.png)

Ahora cada vez que se entre a la página, quedará registrado, como se ve en la siguiente imagen:

![final](img/web4/4.14comprobacionfinal.png)
