# Electromagnetism

## Maxwell Equations

$$\nabla\cdot\mathbf{E}=\frac{\rho}{\epsilon_0}$$
$$\nabla\cdot\mathbf{B}=0$$
$$\frac{\partial\mathbf{B}}{\partial t}=-\nabla\times\mathbf{E}$$
$$\frac{\partial\mathbf{E}}{\partial t}=\frac{\nabla\times\mathbf{B}-\mu_0\mathbf{J}}{\mu_0\epsilon_0}$$

- $\epsilon_0$: vacuum permittivity
- $\mu_0$: vacuum permeability
- $\rho$: charge density
- $\mathbf{J}$: current density
- $\mathbf{E}$: electric field
- $\mathbf{B}$: magnetic field

## Perfectly Match Layer (PML)

$$\vec{n}\times(\mathbf{E}-\mathbf{E}_{PML})=0$$
$$\vec{n}\times(\mathbf{B}-\mathbf{B}_{PML})=0$$

If $\mathbf{E}_{PML}$ and $\mathbf{B}_{PML}$ are 0, then all energy is absorbed

## Port Boundary

$$\vec{n}\times\mathbf{E}=\vec{n}\times f(t)$$

Note that the other component of $\mathbf{E}$ is determined by the divergence equation. $\mathbf{B}$ is also determined using the maxwell equations themselves by solving for $\mathbf{B}$.

$$\nabla\times\mathbf{B}=\mu_0\epsilon_0(\frac{\partial\mathbf{E}}{\partial t}+\mu_0\mathbf{J})$$

## Relationship between voltage and electric field

https://en.wikipedia.org/wiki/Electric_potential

## Relationship Between $\mathbf{B}$ and $\mathbf{H}$

In a vacuum:

$$\mathbf{B}=\mu_0\mathbf{H}$$

In a material:

$$\mathbf{B}=\mu_0(\mathbf{H}+\mathbf{M})$$

## Relationship Between $\mathbf{E}$ and $\mathbf{D}$

$$\mathbf{D}=\epsilon_0\mathbf{E}+\mathbf{P}$$
