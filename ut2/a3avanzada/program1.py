#PROGRAMA 1

#REQUISITOS DEL PROGRAMA:

#Leer un número (entero positivo) por línea de comandos.
#Emitir un error si el número no es positivo, y salir del programa.
#Mostrar por pantalla tantos elementos de la sucesión de Fibonacci como indique el número leído.

import sys

num = int(sys.argv[1])
value1 = 0
value2 = 1

if num <= 0:
    sys.exit('Escribe un valor positivo.')
else:
    for i in range(num):
        print(value1, end = ' ')
        value1, value2 = value2, value1 + value2
print('')
