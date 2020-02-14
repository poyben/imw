<!doctype html>
<html lang="es">
    <head>
        <meta charset="utf-8">
        <title>Tabla</title>
    </head>
    <style>
    table td {width: 50px; height: 50px}
    </style>
    <body>
      <form action="index.php" method="post">
        <p>Introduzca el número de columnas: <input type="text" name="columnas"/></p>
        <p>Introduzca el número de filas: <input type="text" name="filas"/></p>
        <input type="submit" value="enviar"/>
      </form>

      <table border="2">
        <?php
        if (isset($_POST["columnas"]) and isset($_POST["filas"])) {
          $columnas = (int)$_POST["columnas"];
          $filas = (int)$_POST["filas"];
          $n_columnas = 1;
          $n_filas = 1;

          if ($filas >= 1 and $columnas >= 1) {
            echo ("<p>$filas filas y $columnas columnas.</p>");
            while ($n_filas <= $filas) {
              $n_filas++;

              while ($n_columnas <= $columnas) {
                $n_columnas++;
            echo ("<td></td>");
              }
              $n_columnas = 1;
              echo ("</tr>");
            }
          }
        }?>
