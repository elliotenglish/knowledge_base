# Notation

## Best practices

It is common to struggle with notation. Best practices are as follows:
- State all notation
- List all variables (if not self-evident, or specific to context) at the first usage, when redefined and when further clarification or clarity is helpful.

## References

https://en.wikipedia.org/wiki/Vector_notation

## Rules

### Variables

* Scalars are lower case: $x$
* Vectors are lower case bolded or have an arrow above them: $\textbf{x}$ or $\vec{x}$
* Matrices are upper case bolded: $\textbf{A}$
  * Individual elements are generally indexed with (row, column) ordered indices: $\textbf{A}_{ij}$ for the $i$-th row and $j$-th column.
* Higher order tensors generally have explicit indices used.

### Ranges

* Inclusive ranges use square brackets: $[a,b]$
* Exclusive ranges use round parenthesis: $(a,b)$
* Mixed ranges: $(a,b]$ or $[a,b)$

Note that often the type is implied based on the context, either integer or real. Otherwise, it is stated as below:

* $[a,b] \in \real$

### Number groups

* Real: $\real$
* Integer: $\mathcal{N}$

### Derivatives

* Derivatives: $\frac{\partial f}{\partial x}$
* Higher derivatives: $\frac{\partial^n f}{\partial x^n}$
* Integrals: $\displaystyle\int_{x=a}^b x$

Use `\displaystyle` for integrals.

### Summation

* Sums: $\displaystyle\sum_{i=a}^b x$

Use `\displaystyle` for sums.

### Superscripts/subscripts

- Scalars are lower case letters: $a$
- Vectors are bold lower case letters: $\textbf{a}$
- Matrices are bold upper case letters: $\textbf{A}$
- Subscript indices generally refer to spatial/vector dimensions:
  - $\textbf{a}_i$
  - $\textbf{A}_{ij}$.
- Superscript indices generally refer to time dimensions.

### References

Markdown does not natively support automatically referencing equations. However, you can add tags by placing `\tag{some_id}` as the end of an equation and then referencing it explicitly. For example:

```
$$y=Ax+b\tag{1}$$
```

Which renders as:

$$y=Ax+b\tag{1}$$

Note that these only work in some interpretters. They work in VSCode but not Github.
