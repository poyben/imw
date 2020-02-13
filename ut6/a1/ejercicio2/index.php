<!doctype html>
<html lang="es">
    <head>
        <meta charset="utf-8">
        <title>Cálculo salario</title>
    </head>
    <body>
        <form action="process.php" method="post">
            <label for="nombre">Nombre:</label>
            <input type="text" name="name"/><br>
            <label for="apellidos">Apellidos:</label>
            <input type="text" name="surnames"/><br>
            <label for="salario">Salario:</label>
            <input type="text" name="salary"/><br>
            <label for="edad">Edad:</label>
            <input type="text" name="age"/><br>
            <input type="submit" value="enviar"/>
        </form>
    </body>
</html>
