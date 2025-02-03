#!/usr/bin/env python3

"""
This file contains some notes on sympy syntax relevant to differential geometry calculations.
"""

import sympy

x=sympy.Matrix([[sympy.Symbol("x%d"%i)] for i in range(3)])
print(x)

f=sympy.Matrix([[sympy.Function("f%d"%i)(x[0,0],x[1,0],x[2,0])] for i in range(3)])
print(f)
dfdx=f.jacobian(x)
print(dfdx)
