#!/usr/bin/env python 3.9
# -*- coding: utf-8 -*-
import sys 
import math

b=float(sys.argv[1])
c=float(sys.argv[2])

d=b*b-4*c  # находим дискрименант d

print('x^2+'+sys.argv[1]+'x+'+sys.argv[2])
    
if d > 0:
    print('x1='+str((-math.sqrt(b)+d)/2))
    print('x2='+str((-math.sqrt(b)-d)/2))
else: 
    print("it hasn't roots")