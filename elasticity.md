# Elasticity

## Finite Strain vs Infinitesimal Strain

https://en.wikipedia.org/wiki/Finite_strain_theory

Finite strain refers to the case where the solid undergoes non-negligible deformations. This is the real world case needed for accurate behavioral analysis given large and varying external conditions.

Infinitesimal strain looks at the the behavior of solids that are practically infinitely stiff, but still capture the load distribution implied by my complete models. This is useful for simplifying the analysis of structures not expected to undergo noticeable deformation such as large scale structures. This is also used in linear model analysis. It is computed using a Taylor expansion to look at the material behavior under a differential.

## Equations of motion (Cauchy formulation)

https://en.wikipedia.org/wiki/Cauchy_momentum_equation

https://en.wikipedia.org/wiki/Cauchy_momentum_equation

$$\frac{\partial\vec{x}}{\partial t}=\vec{v}$$

$$\frac{\partial\rho\vec{v}}{\partial t}=\nabla\cdot\sigma$$

$$\sigma=F(\epsilon)$$

- $\vec{x}$ is the physical space coordinate.
- $\vec{r}$ is the reference space coordinate.
- $\vec{u}$ is the velocity vector
- $\sigma$ is the Cauchy stress tensor
  - $\sigma$ is symmetric: $\sigma_{ij}=\sigma_{ji}$
- $\epsilon$ is the strain tensor
- $F$ is the defination Deformation: $F=\frac{\partial\vec{x}(\vec{r})}{\partial\vec{r}}=\nabla_{\vec{r}}\vec{x}\in \mathbb{R}^{DxD}$

Cauchy-Green tensor:

$$C=F^T F$$

Green-Lagrange strain tensor:

$$E=\frac{1}{2}(C-I)$$

Strain energy density function has 2 common symbols:

$$W(F)=\psi(F)$$

First Piola-Kirchhoff stress tensor:

$$S=2\frac{\partial\psi(C)}{\partial C}=\frac{\partial\phi(E)}{\partial E}$$

Second Piola-Kirchhoff stress tensor:

$$P=\frac{\partial\psi(F)}{\partial F}=F S$$

The Cauchy stress tensor is then computed as:

$$\sigma=\frac{1}{J}P F^T=\frac{1}{J}F S F^T$$

$$J=det(F)$$

or

$$\sigma=\frac{1}{J}\frac{\partial\psi(F)}{\partial F}\cdot F^T$$

## Material parameters

- Young's modulus: $E$
- Poisson's ratio: $\nu$
- Lame parameters:
  - $\lambda=\frac{E}{(1+\nu)(1-2\nu)}$
  - Shear modulus: $\mu=G=\frac{E}{2(1+\nu)}$
- Bulk modulus (resistance to compression): $K=\frac{E}{3-6\nu}=\lambda+\frac{2}{3}$

## Hyperelasticity

https://en.wikipedia.org/wiki/Hyperelastic_material

$$P=\frac{\partial\psi(F)}{\partial F}$$

### Saint Venant–Kirchhoff

$$S=\lambda tr(E)I+2\mu E$$

### Neo-Hookean Materials

https://en.wikipedia.org/wiki/Neo-Hookean_solid

### Mooney-Rivlin

https://en.wikipedia.org/wiki/Mooney%E2%80%93Rivlin_solid


## Discontinuous Galerkin Formulation

### Timestepping scheme

- Update positions explicitly, using forward euler.
- Solve for velocity implicitly, using backward euler.

### Implicit solve

The position equation is straightforward and can simply be evaluated using a Lagrangian approach by time evolving mesh nodes. The velocity equation is a bit more involved.

$$\int_{x\in\Omega}\phi\frac{\partial\rho\vec{v}}{\partial t}=\int_{x\in\Omega}\phi\nabla\cdot\sigma$$

$$=\int_{x\in\Omega}\nabla\cdot(\phi\sigma)-\int_{x\in\Omega}(\nabla\phi)\cdot\sigma$$

$$=\int_{x\in\partial\Omega}\vec{n}\cdot(\phi\sigma)-\int_{x\in\Omega}(\nabla\phi)\cdot\sigma$$

$$=\int_{x\in\partial\Omega}\phi\vec{n}\cdot\sigma-\int_{x\in\Omega}(\nabla\phi)\cdot\sigma$$

Giving us:

$$\int_{x\in\Omega}\phi\frac{\partial\rho\vec{v}}{\partial t}=\int_{x\in\partial\Omega}\phi\vec{n}\cdot\sigma-\int_{x\in\Omega}(\nabla\phi)\cdot\sigma$$

The boundary flux is the traction vector at the boundary. While the internal integral represents the usual exchange between basic function weights.

Ignoring spatial discretization for now, let's discretize this equation using backward euler:

$$\int_{\vec{x}\in\Omega}\phi\rho\frac{\vec{v}^{n+1}-\vec{v}^n}{\Delta t}=\int_{\vec{x}\in\partial\Omega}\phi\vec{n}\cdot\sigma(\vec{x}^{n+1})-\int_{\vec{x}\in\Omega}(\nabla\phi)\cdot\sigma(\vec{x}^{n+1})$$

The challenge now is to compute $\sigma(\vec{x}^{n+1})$. Let's begin by making a first order expansion:

$$\sigma(\vec{x}^{n+1})=\sigma(\vec{x}^n)+\frac{\partial\sigma(\vec{x}^n)}{\partial\vec{x}}(\vec{x}^{n+1}-\vec{x}^n)$$

$$=\sigma(\vec{x}^n)+\frac{\partial\sigma(\vec{x}^n)}{\partial\vec{x}}(\Delta t\vec{v}^{n+1})$$

And now the challenge is to compute $\frac{\partial\sigma}{\partial\vec{x}}$. 

## Element choice

We need to use at least first order elements in order to get an element local deformation gradient. This can exactly match the nodal deformation of the element.

We also choose to use simplex elements.

## Boundary conditions

Boundary conditions are enforced using a constraint + lagrange multiplier force on the velocity within the implicit solve.
