# Python Programming

## Script shebang
The shebang (https://en.wikipedia.org/wiki/Shebang_(Unix)) is used to specify the interpreter for the script.

In order to get the broadest support for multiple platforms using the following shebang. It's confirmed to work on Linux, MacOS test. The `env` command searches the path for the specified path. Shebangs are limited to 2 arguments, so you can't pass `-u` to suppress buffered output in case you want to pipe the output to other tools without getting out of order and delayed results, but the trade-off is generally worth it (TODO: is there a solution to this).

```
#!/usr/bin/env python3
```

## Command line interfaces

Use argparse

## Formatting strings

Use f-strings (https://docs.python.org/3/reference/lexical_analysis.html#f-strings_).

```
>>> a=5432.546
>>> print(f"unformatted number: {a}")
unformatted number: 5432.546
>>> print(f"a formatted number: {a: 16g}")
a formatted number:          5432.55
```

## Profiling

```
python -m cProfile -o out.prof <script> <args> ...

snakeviz out.prof
```

https://github.com/joerick/pyinstrument?tab=readme-ov-file

## Data Structs

A data struct is a pure field struct. These are useful for example:

```
class A:
  field0: int = 5432
  field1: str = "foo"
```

You can then construct new instances and then read/write fields. In order to have a constructor that accepts named parameters you need to either use `dataclass` or `NamedTuple`:

```
from dataclasses import dataclass

@dataclass
class A:
  field0: int = 5432
  field1: str = "foo"

a=A(field0=1235,field1="bar")
```

In order to make the struct hashable you must set the dataclass to be frozen, i.e. `@dataclass(frozen=True)`.
