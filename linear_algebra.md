# Linear algebra

The matrix cookbook is a tremendous resource for all things linear algebra. It covers many basics such as terminology, matrix multiplication, differentiation, and many identities.

https://www2.imm.dtu.dk/pubdb/pubs/3274-full.html

## Terminology/notation

- $\textbf{e}_i=\{e_j=\delta_{i,j},j\in[1,N]\}$ - A one hot vector with the $1$ value at the $i$-th position.

## Cramer's rule

https://en.wikipedia.org/wiki/Cramer%27s_rule

Given the linear system of equations:

$$\textbf{A}\textbf{x}=\textbf{b}$$

Where $\textbf{A}\in\R^{n\times n}$, $\textbf{x},\textbf{b}\in\R^n$. We have Cramer's rule:

$$x_i=\frac{det(\textbf{A}(i|\textbf{b}))}{\det(\textbf{A})}$$

Where $\textbf{A}(i|\textbf{b})$ is equal to $\textbf{A}$ with the $i$-th column replaced by $\textbf{b}$.

This can be extended to the matrix inverse by letting $\textbf{b}$ be the columns of $\textbf{I}$ as follows:

$$\textbf{A}\textbf{A}^{-1}=\textbf{I}$$

Hence:

$$(\textbf{A}^{-1})_{i,j}=\frac{det(\textbf{A}(i|\textbf{e}_i))}{\det{\textbf{A}}}$$

## Matrix Exponentiation

In a number of fields the concept of exponentials, in particular of Euler's number, $e^a$, is expanded to include support for matrix exponents, $e^\mathbf{A}$. One way to do this is to use the series expansion and inspect the effect of swapping in a matrix for the scalar exponent. To first take the taylor series of a scalar exponential expanded around 0:

$e^{h}=\displaystyle\sum_{n=0}^\infin\frac{1}{n!}\lbrace\frac{\partial^n e^x}{\partial x^n}\rbrace_{x=0}h^n$

$=\displaystyle\sum_{n=0}^\infin\frac{1}{n!}\lbrace e^x\rbrace_{x=0}h^n$

$=\displaystyle\sum_{n=0}^\infin\frac{1}{n!}h^n$

So if we instead have a matrix exponent we can write the following:

$e^H=\displaystyle\sum_{n=0}^\infin\frac{1}{n!}H^n$

Unlike the original form, this is at least something computable, although only to a fixed number of terms. So we take the further step of assuming that we can take a diagonalization of the matrix:

$H=U\Sigma U^*$

Where

$U^*U=I$

Note that this only works for Then substituting this back into the matrix series form we get:

$e^H=\displaystyle\sum_{n=0}^\infin\frac{1}{n!}(U\Sigma U^*)^n$

$=\displaystyle\sum_{n=0}^\infin\frac{1}{n!}U(\Sigma^n)U^*$

$=U(\displaystyle\sum_{n=0}^\infin\frac{1}{n!}\Sigma^n)U^*$

$=Ue^\Sigma U^*$

Which is now tractable as $e^\Sigma$ is just an elementwise operation.

* https://en.wikipedia.org/wiki/E_(mathematical_constant)
* https://en.wikipedia.org/wiki/Singular_value_decomposition

## Divergence of outer product identity

TODO: Generalize for $\vec{u}\vec{v}$ or just matrix products in general.

$$\nabla\cdot(\vec{u}\vec{u}^T)=\left(\begin{matrix}\nabla\cdot(u_1\vec{u}) \\ .. \\ \nabla\cdot(u_n\vec{u})\end{matrix}\right)$$

$$\nabla\cdot(\vec{u}\vec{u}^T)=\left(\begin{matrix}\vec{u}\cdot\nabla u_1+u_1\nabla\cdot \vec{u} \\ .. \\ \vec{u}\cdot\nabla u_n+u_n\nabla\cdot \vec{u}\end{matrix}\right)$$

$$\nabla\cdot(\vec{u}\vec{u}^T)=(\nabla\vec{u}^T)^T\vec{u}+\vec{u}\nabla\cdot\vec{u}$$
