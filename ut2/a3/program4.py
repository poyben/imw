import sys

num = int(sys.argv[1])

if num < 0:
    sys.exit('Por favor, escriba dos valores positivos.')
else:
    for i in range(1, num + 1):
        j = 1
        for k in range (i, 0, -1):
            j *= k
        print (i, '!=', j)
