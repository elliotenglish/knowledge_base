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

### Integrals

* Formula notation: $\displaystyle\int_a^b f(x) dx$
* $a$ is the lower bound.
* $b$ is the upper bound.
* $dx$ is the differential. This defines the variable (e.g. $x$) being integrated over.
* $f(x)$ is the integrand.
* Integrals over 
* Sometimes the differential is omitted: $\displaystyle\int_a^b f(x)$
* Sometimes the differential is specified before the $\displaystyle\int_a^b dx f(x)$=$\displaystyle\int_a^b f(x) dx$. This is confusing as the first factor could simply be an integral with integrand of 1.
* Integrals over set or multidimensional domain: $\displaystyle\int_{\Omega}f(x)dx$.

Use `\displaystyle` for integrals.

### Summation

* Sums: $\displaystyle\sum_{i=a}^b x$

Use `\displaystyle` for sums.

### Evaluation

In order to write and expression and then mark that it should be evaluated at a specific point, "bar notation" is used.

* Evaluation: $\left.\frac{x^2}{\sqrt{x+3}}\right|_{x=1.5}^{x=4}$
* Two-sided evaluation is precisely defined as: $\left.f(x)\right|_{x=a}^{x=b}=f(b)-f(a)$
* One-sided evaluation is precisely defined as: $\left.f(x)\right|_{x=a}=f(a)$


### Vector/Matrix/Tensor notation

- Scalars are lower case letters: $a$
- Vectors are bold lower case letters: $\textbf{a}$
- Matrices are bold upper case letters: $\textbf{A}$
- Subscript indices generally refer to spatial/vector dimensions:
  - Value at row or column $i$: $\textbf{a}_i$
  - Value at row $i$, column $j$: $\textbf{A}_{ij}$
- Superscript indices generally refer to time dimensions.

## Operators

- $\oplus$ - The [Direct Sum](https://en.wikipedia.org/wiki/Direct_sum)
- $:=$ - The definition equals, used for specifying that the LHS is defined as the RHS.
- $\triangleq$ ($\overset{\Delta}{=}$) - A synonym for $:=$.
- $\sim$ - This is the sampling operator. In order to say that some variable $a$ is sampled from a distribution $\mathcal{D}$ you write $a \sim \mathcal{D}$.
- $:$ - Tensor contraction operator over the 2 inner indices. $\textbf{A}:\textbf{B}=\sum_{i,j}\textbf{A}_{ij}\textbf{B}_{ij}$.
- $::$ - Tensor contraction over 4 indices.

### References

Markdown does not natively support automatically referencing equations. However, you can add tags by placing `\tag{some_id}` as the end of an equation and then referencing it explicitly. For example:

```
$$y=Ax+b\tag{1}$$
```

Which renders as:

$$y=Ax+b\tag{1}$$

Note that these only work in some interpretters. They work in VSCode but not Github.
