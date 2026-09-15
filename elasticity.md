# Elasticity

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

$$E=\frac{1}{2}(F^T F-I)$$

$$E=\frac{1}{2}(\nabla_{\vec{r}}\vec{x}^T \nabla_{\vec{r}}\vec{x}-I)$$


Cauchy-Green tensor:

$$C=F^T F$$

Green-Lagrange strain tensor:

$$E=\frac{1}{2}(C-I)$$

$$\sigma=\frac{1}{J}F S F^T$$