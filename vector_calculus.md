# Vector Calculus

## Vector-scalar product divergence expansion

$$\nabla\cdot\rho\vec{u}=\rho\nabla\cdot\vec{u}+\vec{u}\cdot\nabla\rho$$

## Divergence rule

The divergence rule converts the volume integral of the divergence of a vector function over a domain to a surface integral of the component of the vector function in the outward normal direction over the boundary of that same domain.

$$\int_\Omega\nabla\cdot\vec{u}d\vec{x}=\int_{\partial\Omega}\vec{u}\cdot\vec{n}d\vec{x}$$

Where:

- $\Omega$ is the domain
- $\partial\Omega$ is the boundary of the domain
- $\vec{u}$ is the vector function being integrated
- $\vec{n}$ is the outward facing normal of the domain

## Integration by parts

We can use the divergence rule and scalar-vector product expansion to form a higher order integration by parts rule:

$$\int_\Omega\rho\nabla\cdot\vec{u}$$

$$=\int_\Omega(\nabla\cdot\rho\vec{u}-\vec{u}\cdot\nabla\rho)$$

$$=\int_\Omega\nabla\cdot\rho\vec{u}-\int_\Omega\vec{u}\cdot\nabla\rho$$

$$=\int_{\partial\Omega}\rho\vec{u}\cdot\vec{n}-\int_\Omega\vec{u}\cdot\nabla\rho$$

## Integration by parts for laplacians

$$\int_\Omega a\nabla\cdot(c\nabla b)$$

$$=\int_{\partial\Omega}ac\nabla b\cdot\vec{n}-\int_\Omega c\nabla b\cdot\nabla a$$
