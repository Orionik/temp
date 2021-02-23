
# -*- coding: utf-8 -*-
import sys 
import math

try:
    b = float(sys.argv[1])    
    c = float(sys.argv[2])
except:
    print("Error. Number must be float type")
    
print('x^2 + ' + sys.argv[1] + 'x + ' + sys.argv[2])

d = b*b - 4*c  # находим дискриминант d
        
if d >= 0:
    x1 = str((-b + math.sqrt(d))/2)
    x2 = str((-b - math.sqrt(d))/2)
    
    print('x1 =' + x1)
    print('x2 =' + x2)
else: 
    print("it hasn't roots")
