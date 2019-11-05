import sys

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

if num1 < 0 or num2 < 0:
    sys.exit('Por favor, escriba dos valores positivos.')
else:
    if num1 < num2:
        var3 = num1
    else:
        var3 = num2
    for value in range(var3, 0, -1):
        if num1 % value == 0:
            if num2 % value == 0:
                print(value)
                break
