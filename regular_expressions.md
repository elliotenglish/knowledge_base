# Regular Expressions

## Floating point numbers

This works for general floating point numbers in at least Python's `re` module.

```
[-+]?(?:[0-9]+[.][0-9]*|[0-9]*[.][0-9]+)(?:[eE][-+]?[0-9]+)?
```
