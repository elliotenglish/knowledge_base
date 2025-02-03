# Shock Dynamics

PDEs with discontinuities.

- Shock capturing schemes

## Riemann Problem

https://en.wikipedia.org/wiki/Riemann_problem

A Riemann problem is any ODE where the initial conditions are piecewise constant:

$$\frac{\partial u}{\partial t}=\nabla\cdot\vec{f}(u)$$

Where $u(x,t)$ is the solution variable and $\vec{x}(\cdot)$ is the flux. The initial conditions are defined as:

$$u(\vec{x},0)=
\left\{ \begin{matrix}
u_l, \vec{x}\in\Omega_l \\
u_r, \vec{x}\in\Omega_r
\end{matrix}\right.$$

Where $u_l$,$u_r$ are the initial values, and $\Omega_l\bigcap\Omega_r=\Omega$ are the domains.

## Godunov Method

https://en.wikipedia.org/wiki/Godunov%27s_scheme
