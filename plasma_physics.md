# Definitions

Note below that some vector quantities are bolded and capitalized. Which is typically reserved for matrices/higher dimension tensors. So this convention is an abuse of notation.

* $\textbf{E}$ - Electric field.
* $\textbf{B}$ - Magnetic field.
* $B=\sqrt{\textbf{B}\cdot\textbf{B}}=|\textbf{B}|$
* $\beta=\frac{p}{B^2/2\mu_0}$ - Plasma pressure.
* $P_B=\frac{B^2}{2\mu_0}$ - Magnetic pressure, so called because the Lorentz force can be rewritten in terms of a tension term and the gradient of this pressure.
* $f_T=\frac{(\textbf{B}\cdot\nabla)\textbf{B}}{\mu_0}$ - magnetic tension.
* $\mu_0$ - vacuum permeability, effectively the rate of change of the magnetic field.
* $\textbf{J}$ (or $\textbf{I}$) - Current density. It is relative to the motion of the different charge fields, e.g. $\textbf{J} ~= n_e \textbf{v}_e - n_i \textbf{v}_i$. ? TODO
* $\tau_E$ - Confinement time. This is the half life of the plasma's energy due to conduction and radiation, collectively transport.
* $\textbf{R}$ - TODO
* $\textbf{R}_c$ - TODO
* $R_c=\sqrt{\textbf{R}\cdot\textbf{R}}=|\textbf{R}|$
* Gyromotion - TODO
* $w_c=qB/m$ - The gyro frequency.
* $r_L=v_\perp/w_c$ - The gyro radius.
* Transport - TODO
* Classical transport - Transport of energy/particles in a cylindrical plasma? TODO
* Neoclassical transport - Transport energy/particles in a torus? TODO
* Troyon stability limit - TODO
* q - Safety factor? TODO
* $\kappa$ - Curvature? TODO
* Trapped particles - TODO
* Untrapped particles - TODO
* Bootstrap current - This is an automatically generated current in Tokamaks due to the collisions between trapped and untrapped particles. TODO
* $R$ - Major radius from origin to center of torus.
* $a$ - Minor radius from center of torus to plasma surface.
* Aspect ratio = $R/a$
* Elongation - How much the plasma profile is stretched from a base circle. TODO: precise definition
* Characteristic speed of waves in electromagnetic fields - speed of light? TODO: How much is this attenuated in dielectric mediums
* Characteristic speed of waves in fusion plasma - TODO
* Dielectric material - TODO
* Debye shielding - TODO
* Low vs high confinement mode - TODO
* $\tau_L$ vs $\tau_H$ - TODO


# Maxwell Equations

* $\nabla\cdot\textbf{B}=0$
* TODO

# Lorentz Force

$\textbf{f}_L=q(\textbf{E}+\textbf{v}\times\textbf{B})$

# Derivation of Magnetic Pressure and Tension

We have the Lorentz force term below:

$\textbf{J}\times \textbf{B}$

Using the identity:

$\frac{1}{2}\nabla(\textbf{A}\cdot\textbf{A})=(\textbf{A}\cdot\nabla)\textbf{A}+\textbf{A}\times(\nabla\times\textbf{A})$

And Ampere's law:

$\mu_0\textbf{J}=\nabla\times\textbf{B}$

$\textbf{J}\times\textbf{B}=\frac{1}{\mu_0}(\nabla\times\textbf{B})\times\textbf{B}$

$=-\frac{1}{\mu_0}\textbf{B}\times(\nabla\times\textbf{B})$

$=-\frac{1}{2\mu_0}\nabla(\textbf{B}\cdot\textbf{B})+\frac{1}{\mu_0}(\textbf{B}\cdot\nabla)\textbf{B}$

$=-\nabla\frac{|\textbf{B}|^2}{2\mu_0}+\frac{1}{\mu_0}(\textbf{B}\cdot\nabla)\textbf{B}$

# Models From Low to High Level Approximations

## Quantum Theory

The standard model?

## Kinetic Theory

Distributions of particles. Vlassov equations?

## Gyrokinetic Theory

Particles average over their gyroradius so that we only have position and velocity parallel to the magnetic field. How does this account for drift?

## Magnetohydrodynamics

Continuum models. Fluids + Maxwell equations.

### Frozen In Magnetic Field Lines

$\psi=\displaystyle\int_S\textbf{B}\cdot\textbf{n} d\textbf{r}$

Where $\textbf{B}$ is the magnetic field, $\textbf{n}$ is the normal of the surface, and $S$ is the surface. We then take the derivative of this with respect to time.

$\frac{d\psi}{dt}=\displaystyle\int_S\frac{\partial\textbf{B}}{\partial t}\cdot\textbf{n}d\textbf{r}+\int_\textbf{l}\textbf{B}\times\textbf{u}_\perp d\textbf{r}$

Where $\textbf{l}$ is the line boundary of $S$, and $\textbf{u}_\perp$ is the perpendicular velocity of the boundary.

TODO: Finish. Page 300.

# Plasma Instabilities

## Internal vs External Modes

Internal modes do not affect the plasma surface. They are generally not as much of an issue for safety, but can affect the physics and reduce efficiency.

External modes affect the plasma surface and can lead to plasma wall contact.

## Interchange Modes

## Ballooning Modes

## Current Driven Modes

## Kink Modes

## Balloon Kink Modes

## Edge-localized Modes (ELM)



# Geometry

<svg width="500" height="300" xmlns="http://www.w3.org/2000/svg" style="background-color:white">
    <text x="10" y="165">(0,0)</text>
    <line x1="10" y1="150" x2="450" y2="150" stroke="grey"/>
    <text x="10" y="30">Z</text>
    <line x1="10" y1="150" x2="10" y2="50" stroke="grey"/>
    <text x="460" y="155">R</text>
    <g transform="translate(10,130) scale(1,.3)"><circle cx="0" cy="0" r="20" stroke="black" fill="transparent"/></g>
    <text x="40" y="130">𝜙</text>
    <!--plasma/-->
    <text x="160" y="50">plasma surface</text>
    <circle cx="300" cy="150" r="100" stroke="black" fill="transparent" />
    <line x1="300" y1="150" x2="392" y2="112" stroke="grey"/>
    <text x="340" y="120">r</text>
    <text x="350" y="145">𝛳</text>
</svg>

## Cylindrical Coordinates

* $x=Rcos(\phi)$
* $y=Rsin(\phi)$
* $z=Z$
* $R$ is the distance from the origin.
* $\phi$ is the angle about the z axis (toroidal angle).

## Toroidal Coordinates

We inherit the definition of $\phi$ from the cylindrical coordinates.

* $x=(R_0+rcos(\theta))cos(\phi)$
* $y=(R_0+rcos(\theta))sin(\phi)$
* $z=rsin(\theta)$
* $R_0$ is distance from the origin to the center of the torus ring.
* $\theta$ is the angle around the minor dimension of the torus (poloidal angle).

## Magnetic Coordinates

There are many definitions of magnetic coordinates, but effectively due to the divergence free nature of the magnetic field.

## Boozer Coordinates

# Charged Particle Motion in Magnetic and Electric Fields

## Constant magnetic field

This ignores the particle's effect on field itself.

$B(x,t)=constant=B$

$\frac{\partial x_p}{\partial t}=v_p$

$\frac{\partial v_p}{\partial t}=q_p (E+v_p \times B)$

We can solve these equations as follows:

First we rewrite the equation as a block structure linear equation.

$\begin{pmatrix}\frac{\partial x_p}{\partial t} \\ \frac{\partial v_p}{\partial t}\end{pmatrix}=
\begin{pmatrix}0 \\ q_p E\end{pmatrix}
+\begin{pmatrix}0 & 1 \\ 0 & -B \times\end{pmatrix}
\begin{pmatrix}x_p \\ v_p\end{pmatrix}$

# Electric and Magnetic Fields Generated by a Charge Particle

## Stationary particle

## Particle moving with constant velocity

## Particle with constant acceleration

# Confinement Types

## $\theta$-screw

A $\theta$-screw is the configuration when you have a current flowing in the $theta$ direction around the minor axis of the torus.

## $z$-screw

A $z$-screw is the configuration when you have a current flowing along the $\phi$ direction around the major axis of the torus.

# Tokamak Force Breakdown

## Tire Tube Force

## Hoop Force

## $1/R$ Force

# Software

- [Warp-X](https://github.com/ECP-WarpX/WarpX)
  - Based on [AMReX](https://amrex-codes.github.io/amrex/)
  - Particle-in-cell kinetic code
- [Gysela-X](https://gyselax.github.io/)
- [Proteus](https://github.com/aurora-multiphysics/proteus)

# References

- https://arxiv.org/abs/1908.05360
