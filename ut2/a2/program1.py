import sys
import math
from math import sqrt

a = int(sys.arvg[1])
b = int(sys.arvg[2])
c = int(sys.arvg[3])

if a == 0:
    x = -c / b
    print ('x =' x)
else:
    x1 = (-b + sqrt (b ** 2 -4 * a * c)) / 2 * a
    x2 = (-b - sqrt (b ** 2 -4 * a * c)) / 2 * a

if b ** 2 - 4 * a * c < 0:
    print ('Esta ecuación no tiene una solución real.')
