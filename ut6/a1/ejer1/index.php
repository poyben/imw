<!doctype html>
<html lang="es">
    <head>
        <meta charset="utf-8">
        <title>Sistemas Operativos aleatorios!</title>
    </head>
    <body>
        <?php
            $rand = mt_rand (1,2);
            echo("<img src='img/$rand.png'>");
        ?>
    </body>
</html>
