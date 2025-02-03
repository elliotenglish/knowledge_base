# Symbolic Mathematics

## Software Packages

Open source:

- Maxima
- SymPy

## Declare arbitrarily sized vectors/matrices in SymPy

MatrixSymbol works to declare

```
import sympy as sp
x=sympy.matrices.MatrixSymbol(name,rows,cols)
```

Then to actually get a sympy Matrix object you need to call `MatrixSymbol.as_explicit()`.


Unfortunately it's not always clear how the underlying symbols are declared. So you can generate all the symbol names yourself instead and then call the symbols method which accepts lists/tuples of symbols, not just a string to parse. So you can generate names in a loop comprehension and pass them in as in the example below.

Relevant reference:
https://docs.sympy.org/latest/modules/core.html#sympy.core.symbol.symbols

```
import sympy as sp

def generate_symbols(prefix,num):
  names=[prefix+str(i) for i in range(num)]
  elems=sp.symbols(tuple(names))
  return elems

```

## Code generation in SymPy
