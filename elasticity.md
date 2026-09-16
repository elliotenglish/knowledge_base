# Elasticity

## Finite Strain vs Infinitesimal Strain

https://en.wikipedia.org/wiki/Finite_strain_theory

Finite strain refers to the case where the solid undergoes non-negligible deformations. This is the real world case needed for accurate behavioral analysis given large and varying external conditions.

Infinitesimal strain looks at the the behavior of solids that are practically infinitely stiff, but still capture the load distribution implied by my complete models. This is useful for simplifying the analysis of structures not expected to undergo noticeable deformation such as large scale structures. This is also used in linear model analysis. It is computed using a Taylor expansion to look at the material behavior under a differential.

## Equations of motion (Cauchy formulation)

https://en.wikipedia.org/wiki/Cauchy_momentum_equation

https://en.wikipedia.org/wiki/Cauchy_momentum_equation

$$\frac{\partial\vec{x}}{\partial t}=\vec{v}$$

$$\frac{\partial\vec{v}}{\partial t}=\nabla\cdot\sigma$$

$$\sigma=F(\epsilon)$$

- $\vec{u}$ is the velocity vector
- $\sigma$ is the Cauchy stress tensor
- $\epsilon$ is the strain tensor

- $\sigma$ is symmetric: $$\sigma_{ij}=\sigma_{ji}$$


$$\vec{u}=\vec{x}(\vec{r})-\vec{r}$$

$$F=\frac{\partial\vec{x}(\vec{r})}{\partial\vec{r}}=\nabla_{\vec{r}}\vec{x}$$

Cauchy-Green tensor:

$$C=F^T F$$

Green-Lagrange strain tensor:

$$E=\frac{1}{2}(C-I)$$

First Piola-Kirchhoff stress tensor:

$$S=2\frac{\partial\psi(C)}{\partial C}=\frac{\partial\phi(E)}{\partial E}$$

Second Piola-Kirchhoff stress tensor:

$$P=\frac{\partial\psi(F)}{\partial F}=F S$$

The Cauchy stress tensor is then computed as:

$$\sigma=\frac{1}{J}P F^T=\frac{1}{J}F S F^T$$

## Material parameters

- Young's module: $E$
- Poisson's ratio: $\nu$
- Lame parameters:
  - $\lambda=\frac{E}{(1+\nu)(1-2\nu)}$
  - Shear modulus: $\mu=G=\frac{E}{2(1+\nu)}$
- Bulk modulus (resistance to compression): $K=\frac{E}{3-6\nu}=\lambda+\frac{2}{3}$

## Saint Venant–Kirchhoff

$$S=\lambda tr(E)I+2\mu E$$

## Neo-Hookean Materials

- https://en.wikipedia.org/wiki/Neo-Hookean_solid

## Mooney-Rivlin

https://en.wikipedia.org/wiki/Mooney%E2%80%93Rivlin_solid

## Hyperelasticity

## Discontinuous Galerkin Formulation

The position equation is straightforward. The velocity equation is a bit more involved.

$$\int_{x\in\Omega}\phi\frac{\partial\vec{v}}{\partial t}=\int_{x\in\Omega}\phi\nabla\cdot\sigma$$

$$=\int_{x\in\Omega}\nabla\cdot(\phi\sigma)-\int_{x\in\Omega}(\nabla\phi)\cdot\sigma$$

$$=\int_{x\in\partial\Omega}\vec{n}\cdot(\phi\sigma)-\int_{x\in\Omega}(\nabla\phi)\cdot\sigma$$

$$=\int_{x\in\partial\Omega}\phi\vec{n}\cdot\sigma-\int_{x\in\Omega}(\nabla\phi)\cdot\sigma$$

The boundary flux is the traction vector at the boundary. While the internal integral represents the usual exchange between basic function weights.
