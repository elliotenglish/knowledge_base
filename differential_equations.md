# Differential equations

This page examines basic forms of differential equations as these are often used to build up more sophisticated numerical solutions to complex non-linear partial differential equations (PDEs).

## Homogeneous vs heterogeneous forms

A homogeneous differential equation only includes terms that have factors of the solution variable and its derivatives.

Homogeneous:

$\displaystyle\sum_{n=0}^{N}a_n(x)\frac{\partial^n u}{\partial x^n}=0$

Heterogeneous:

$\displaystyle\sum_{n=0}^{N}a_n(x)\frac{\partial^n u}{\partial x^n}=g(x)$

## Linear vs non-linear forms

A linear differential equation is one that can be written as linear operator.

$\mathcal{L}u=\displaystyle\sum_{n=0}^{N}a_n(x)\frac{\partial^n u}{\partial x^n}$

Where

$\mathcal{L}=\displaystyle\sum_{n=0}^{N}a_n(x)\frac{\partial^n}{\partial x^n}$

## Equation order

The order of a differential equation refers to the maximum level of differentiation involved. $\frac{\partial^n}{\partial x^n}$ is the $n$-th order differential operator.

### Specific examples

#### First order, linear, homogeneous

$\frac{\partial u}{\partial t}=au$

In this case we have the family of trivial solutions, of which a linear combination is also a solution:

$u=ce^{at}$

or

$u=\displaystyle\sum_{n=0}^{N}c_n e^{a_n t}$

Where $c$ is solved for using boundary conditions.

#### First order, linear operator, constant heterogeneous term

$\frac{\partial u}{\partial t}=b+au$

$u=c_1e^{at}+c_0$

We then substitute this into the ODE:

$c_1ae^{at}=b+a(c_1e^{at}+c_0)$

And solve for $c_0$:

$0=b+ac_0$

$c_0=-\frac{b}{a}$

So we have a solution of the form:

$u=c_1e^{at}-\frac{b}{a}$

#### First order, linear operator, linear heterogeneous term

$\frac{\partial u}{\partial t}=b+au+wt$

$u=c_1e^{at}+c_0+c_2t$

$c_1ae^{at}+c_2=b+ac_1e^{at}+ac_0+ac_2t+wt$

$c_2=ac_0+b$

$ac_2t+wt=0$

$c_2=-\frac{w}{a}$

$c_0=-\frac{w}{a^2}-\frac{b}{a}$

## Multivariate Linear ODE

We can extend this to a system of linear ODEs as follows:

$\frac{\partial\mathbf{u}}{\partial t}=\mathbf{A}\mathbf{u}+\mathbf{b}$

For the solution we use the same form as that for a scalar equation/function, exploiting the concepts used in matrix exponentiation (assuming certain conditions on $\mathbf{A}$).

$\mathbf{u}=c_1e^{\mathbf{A}t}+\mathbf{c_0}$

$\mathbf{A}=\mathbf{U}\Sigma\mathbf{U}^*$

Substituting this into the ODE we get.

$c_1\mathbf{A}e^{\mathbf{A}t}=\mathbf{A}c_1e^{\mathbf{A}t}+\mathbf{A}\mathbf{c}_0+\mathbf{b}$

Then solving for $\mathbf{c}_0$ we get

$\mathbf{c}_0=-\mathbf{A}^{-1}\mathbf{b}$

Which is analogous to what we have above. So we end up with the following solution family:

$\mathbf{u}=c_1e^{\mathbf{A}t}-\mathbf{A}^{-1}\mathbf{b}$

## Linear time dependent PDEs

We are solving for a function that is both dependent upon time and space, $u(x,t)$.

$\frac{\partial u}{\partial t}=au+bx$

## Directional derivatives

The Gateaux derivate is a form of directional differentiation. Under reasonable assumptions it is equal the inner product of the gradient and direction, like other definitions of directional differentiation.

https://en.wikipedia.org/wiki/Gateaux_derivative

## Differential equations of distribution functions

In general the time derivative of a distribution function is composed of 2 parts. The first is the physical space flux due to bulk flow. The second is the phase space flux due to the flow within the distribution. This term is equal to the phase space gradient times the force applied as in the non-distributional case. Both terms are conservative.

This can be seen in Vlasov equations.
