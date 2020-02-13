<!doctype html>
<html lang="es">
    <head>
      <meta charset="utf-8">
      <title>Cálculo salario</title>
  </head>
  <body>
<?php
$salario = (float)($_POST["salary"]);
$edad = (int)($_POST["age"]);
$nombre = $_POST["name"];
if ($salario > 1000 and $salario <= 2000) {
  if ($edad > 45) {
    $salario = $salario + ($salario * 3 / 100);
  }
  elseif ($edad <= 45) {
    $salario = $salario + ($salario * 10 /100);
  }
}
elseif ($salario < 1000) {
  if ($edad < 30) {
    $salario = 1100;
  }
  elseif ($edad > 30 and $salario < 45) {
    $salario = $salario + ($salario * 3 / 100);
  }
  elseif ($edad > 45) {
    $salario = $salario + ($salario * 15 / 100);

  }
}
echo("El nuevo salario de $nombre es $salario.");
?>
</body>
</html>
