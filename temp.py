
# -*- coding: utf-8 -*-
import sys 
import math

try:
    b = float(sys.argv[1])    
    c = float(sys.argv[2])

    print('x^2 + ' + sys.argv[1] + 'x + ' + sys.argv[2])


    d = b*b - 4*c  # находим дискрименант d
        
    if d > 0:
        print('x1 =' + str((-b + math.sqrt(d))/2))
        print('x2=' + str((-b - math.sqrt(d))/2))
    else: print("it hasn't roots")
except:
    print("Error. Number must be float type")