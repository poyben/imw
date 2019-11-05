import sys

num = int(sys.argv[1])

if num < 0:
    sys.exit('Por favor, introduzca un valor positivo.')

else:
    for value in range(2, num + 1):
        if value % num == 0:
            print ('Es primo!')
            break
    else:
        print ('No es primo!')
