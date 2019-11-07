import sys

num = int(sys.argv[1])

if num <= 0:
    sys.exit('Por favor, escriba un valor positivo.')
else:
    for i in range(1, num + 1):
        result = 1
        for k in range (i, 0, -1):
            result *= k
        print (i,'! =', result)
