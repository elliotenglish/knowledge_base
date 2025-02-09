# Fluid Mechanics

# General Compressible Flow Equations

Momentum equation:

$$\frac{\partial\rho\vec{u}}{\partial t}=-\nabla\cdot(\rho\vec{u}\vec{u}^T)-\nabla p+\mu\nabla^2\vec{u}+\frac{1}{3}\mu\nabla(\nabla\cdot\vec{u})$$

or ignoring viscosity we get the following:

$$\frac{\partial\rho\vec{u}}{\partial t}=-\nabla\cdot(\rho\vec{u}\vec{u}^T)-\nabla p$$

Density (mass transport/advection):

$$\frac{\partial\rho}{\partial t}=-\nabla\cdot(\rho\vec{u})$$

Total energy (advection, plus work done due to pressure):

$$\frac{\partial E}{\partial t}=-\nabla\cdot((E+p)\vec{u})$$

or

$$\frac{\partial E}{\partial t}=-\nabla\cdot(E\vec{u})-\nabla\cdot(p\vec{u})$$

And the definition of total energy:

$$E=\rho e+\frac{1}{2}\rho\vec{u}^T\vec{u}$$

Note that in theory we could derive the total energy time derivative from the total energy definition, however, this requires an additional equation to relate $e$ and $p$. Or looking at it another way we have $3+d$ equations (2,3(d),4,5) but $4+d$ unknowns ($\rho$,$\rho\vec{u}$(d),$E$,$p$,$e$). This equation needed is the equation of state (EoS). For ideal gases this is Boyle's law ($P=\rho R T$ combined with $T=C_v e$).

### Equation of State

The equation of state can be written as:

$$f(p,e,\rho)=0$$

For an ideal gas we have Boyle's law:

$$pV=nRT$$

- $n$ number of Moles
- $V$ volume in cubic meters
- $R$ Gas constant

And then the definition of internal energy:

$$U=\hat{c}_vnRT$$

- $\hat{c}_v=\left\{\begin{matrix}\frac{3}{2} & \text{monatomic gas} \\ \frac{5}{2} & \text{diatomic gas} \\ 3 & \text{simplified non-linear molecules}\end{matrix}\right.$ heat capacity

We then use the above definitions to get the desired equation of state, first defining temperature from our solution variables:

$$U=V\rho e$$

$$T=\frac{V\rho e}{\hat{c}_v nR}

<!-- $$=V(E-\frac{1}{2}\rho\vec{u}^T\vec{u})$$ -->

<!-- $$T=V\frac{E-\frac{1}{2}\rho\vec{u}^T\vec{u}}{\hat{c}_vnR}$$ -->

And then substitute this in:

$$p=\frac{nRT}{V}$$

$$=\frac{nRT}{V}\frac{V\rho e}{\hat{c}_v nR}$$

$$=\frac{\rho e}{\hat{c}_v}$$

Where

$$e=\rho^{-1}(E-\frac{1}{2}\rho\vec{u}^T\vec{u})$$

<!-- $$p=\frac{1}{V}nRV\frac{E-\frac{1}{2}\rho\vec{u}^T\vec{u}}{\hat{c}_vnR}$$

$$=\frac{E-\frac{1}{2}\rho\vec{u}^T\vec{u}}{\hat{c}_v}$$ -->

References:
- https://en.wikipedia.org/wiki/Ideal_gas

### Velocity time derivative

$$\frac{\partial\rho\vec{u}}{\partial t}=-\nabla\cdot(\rho\vec{u}\vec{u}^T)-\nabla p$$

$$\rho\frac{\partial\vec{u}}{\partial t}+\frac{\partial\rho}{\partial t}\vec{u}=...$$

$$\frac{\partial u}{\partial t}=-\rho^{-1}\frac{\partial\rho}{\partial t}\vec{u}-\rho^{-1}\nabla\cdot(\rho\vec{u}\vec{u}^T)-\rho^{-1}\nabla p$$

$$=-\rho^{-1}(-\nabla\cdot(\rho\vec{u}))\vec{u}-\rho^{-1}(\rho\nabla\cdot(\vec{u}\vec{u}^T)-\vec{u}\vec{u}^T\nabla\rho)-\rho^{-1}\nabla p$$

$$=\rho^{-1}\vec{u}(\rho\nabla\cdot\vec{u}+\vec{u}\cdot\nabla\rho)-\nabla\cdot(\vec{u}\vec{u}^T)-\rho^{-1}\vec{u}\vec{u}^T\nabla\rho-\rho^{-1}\nabla p$$

$$=\vec{u}\vec{u}\cdot\nabla\rho-\nabla\cdot(\vec{u}\vec{u}^T)-\rho^{-1}\nabla p$$

Using the identity $\nabla\cdot(\vec{u}\vec{u}^T)=\vec{u}\nabla\vec{u}+\vec{u}\nabla\cdot\vec{u}$ we then get the final form:

$$\frac{\partial\vec{u}}{\partial t}=-\vec{u}\nabla\cdot\vec{u}-\rho^{-1}\nabla p$$

### Internal energy time derivative

The internal energy time derivative can be derived as follows:

$$e=\frac{1}{\rho}(E-\frac{1}{2}\rho\vec{u}^T\vec{u})$$

$$=\rho^{-1}E-\frac{1}{2}\vec{u}^T\vec{u}$$

$$\frac{\partial e}{\partial t}
=-\rho^{-2}\frac{\partial\rho}{\partial t}E
+\rho^{-1}\frac{\partial E}{\partial t}
-\vec{u}^T\frac{\partial u}{\partial t}$$

$$=-\rho^{-2}\frac{\partial\rho}{\partial t}(\rho e+\frac{1}{2}\rho\vec{u}^T\vec{u})
+\rho^{-1}(-\nabla\cdot(E\vec{u})-\nabla\cdot(p\vec{u}))
-\vec{u}^T(-\vec{u}\nabla\cdot\vec{u}-\rho^{-1}\nabla p)$$

$$=-\rho^{-1}\frac{\partial\rho}{\partial t}e
-\frac{1}{2}\rho^{-1}\frac{\partial\rho}{\partial t}\vec{u}^T\vec{u}
-\rho^{-1}\nabla\cdot(\rho e\vec{u}+\frac{1}{2}\rho\vec{u}^T\vec{u}\vec{u})
-\rho^{-1}\nabla\cdot(p\vec{u})
+\vec{u}^T\vec{u}\nabla\cdot\vec{u}
+\rho^{-1}\vec{u}^T\nabla p$$

$$=-\rho^{-1}\frac{\partial\rho}{\partial t}e
-\frac{1}{2}\rho^{-1}\frac{\partial\rho}{\partial t}\vec{u}^T\vec{u}
-\rho^{-1}\nabla\cdot\rho e\vec{u}
-\rho^{-1}\nabla\cdot\frac{1}{2}\rho\vec{u}^T\vec{u}\vec{u}
-\rho^{-1}\nabla\cdot(p\vec{u})
+\vec{u}^T\vec{u}\nabla\cdot\vec{u}
+\rho^{-1}\vec{u}^T\nabla p$$

$$=-\rho^{-1}\frac{\partial\rho}{\partial t}e
-\frac{1}{2}\rho^{-1}\frac{\partial\rho}{\partial t}\vec{u}^T\vec{u}
-\rho^{-1}e\nabla\cdot\rho\vec{u}
-\rho^{-1}\rho\vec{u}\cdot\nabla e
-\frac{1}{2}\rho^{-1}\vec{u}^T\vec{u}\nabla\cdot\rho\vec{u}
-\frac{1}{2}\rho^{-1}\rho\vec{u}\cdot\nabla\vec{u}^T\vec{u}
-\rho^{-1}\nabla\cdot(p\vec{u})
+\vec{u}^T\vec{u}\nabla\cdot\vec{u}
+\rho^{-1}\vec{u}^T\nabla p$$

$$=-\rho^{-1}\frac{\partial\rho}{\partial t}e
-\frac{1}{2}\rho^{-1}\frac{\partial\rho}{\partial t}\vec{u}^T\vec{u}
+\rho^{-1}e\frac{\partial\rho}{\partial t}
-\vec{u}\cdot\nabla e
+\frac{1}{2}\rho^{-1}\vec{u}^T\vec{u}\frac{\partial\rho}{\partial t}
-\frac{1}{2}\vec{u}\cdot\nabla\vec{u}^T\vec{u}
-\rho^{-1}\nabla\cdot(p\vec{u})
+\vec{u}^T\vec{u}\nabla\cdot\vec{u}
+\rho^{-1}\vec{u}^T\nabla p$$

Using $\frac{1}{2}\nabla\vec{u}^T\vec{u}=\vec{u}\nabla\cdot{u}$:

$$=-\vec{u}\cdot\nabla e
-\vec{u}^T\vec{u}\nabla\cdot\vec{u}
-\rho^{-1}\nabla\cdot(p\vec{u})
+\vec{u}^T\vec{u}\nabla\cdot\vec{u}
+\rho^{-1}\vec{u}^T\nabla p$$

$$=-\vec{u}\cdot\nabla e
-\rho^{-1}\nabla\cdot(p\vec{u})
+\rho^{-1}\vec{u}^T\nabla p$$

$$=-\vec{u}\cdot\nabla e
-\rho^{-1}p\nabla\cdot\vec{u}
-\rho^{-1}\vec{u}\cdot\nabla p
+\rho^{-1}\vec{u}^T\nabla p$$

And finally eliminating terms we arrive at the final equation:

$$\frac{\partial e}{\partial t}=-\vec{u}\cdot\nabla e
-\frac{p}{\rho}\nabla\cdot\vec{u}$$

### Pressure time derivative

Although pressure is a pseudo variable, it the time derivative equation is useful for building numerical methods, such as when solving for pressure implicitly.

Given the definition of pressure:

$$p(\rho,e)=...$$

We can compute the time derivative (containing terms related to the advective term and divergence only) as:

$$\frac{\partial p}{\partial t}=
\frac{\partial p}{\partial\rho}\frac{\partial \rho}{\partial t}
+\frac{\partial p}{\partial e}\frac{\partial e}{\partial t}$$

Substituting equations from above in we get:

$$\frac{\partial p}{\partial t}=
\frac{\partial p}{\partial\rho}\frac{\partial \rho}{\partial t}
+\frac{\partial p}{\partial e}\frac{\partial e}{\partial t}$$

$$=-\frac{\partial p}{\partial\rho}\nabla\cdot(\rho\vec{u})
-\frac{\partial p}{\partial e}\vec{u}\cdot\nabla e
-\frac{\partial p}{\partial e}\frac{p}{\rho}\nabla\cdot\vec{u}$$

$$=-\frac{\partial p}{\partial\rho}\rho\nabla\cdot\vec{u}
-\frac{\partial p}{\partial\rho}\vec{u}\cdot\nabla\rho
-\frac{\partial p}{\partial e}\vec{u}\cdot\nabla e
-\frac{\partial p}{\partial e}\frac{p}{\rho}\nabla\cdot\vec{u}$$

$$=-\rho(\frac{\partial p}{\partial\rho}\rho+\frac{\partial p}{\partial e}\frac{p}{\rho^2})\nabla\cdot\vec{u}
-\frac{\partial p}{\partial\rho}\vec{u}\cdot\nabla\rho
-\frac{\partial p}{\partial e}\vec{u}\cdot\nabla e
$$

In order to change the last 2 terms into the non-conservative advection term for pressure we exploit the fact that $p$ is a function of $\rho$ and $e$ only, not time of spatial components. So we can apply the non-conservative advection operator (which is linear) to get the identity:

$$\vec{u}\cdot\nabla p=\vec{u}\frac{\partial p}{\partial\rho}\cdot\nabla\rho+\vec{u}\frac{\partial p}{\partial e}\cdot\nabla e$$

Which is exactly the last 2 terms, so we end up with the final pressure time derivative:

$$\frac{\partial p}{\partial t}=
-\vec{u}\cdot\nabla p
-\rho(\frac{\partial p}{\partial\rho}\rho+\frac{\partial p}{\partial e}\frac{p}{\rho^2})\nabla\cdot\vec{u}$$

$$\frac{\partial p}{\partial t}=
-\vec{u}\cdot\nabla p
-\rho c^2\nabla\cdot\vec{u}$$

Where $c=\sqrt{\frac{\partial p}{\partial\rho}\rho+\frac{\partial p}{\partial e}\frac{p}{\rho^2}}$ is the speed of sound.

### References
- https://en.wikipedia.org/wiki/Euler_equations_(fluid_dynamics)#Conservation_form_3
- https://physbam.stanford.edu/~fedkiw/papers/cam1996-01.pdf
- https://physbam.stanford.edu/~fedkiw/papers/cam1997-17.pdf
- https://physbam.stanford.edu/~fedkiw/papers/cam1997-27.pdf (pressure time derivative)

## Time integration

Below we show a time stepping scheme for the compressible flow equations. Note that all spatial derivatives are still left undefined and can be done using a number of methods (e.g FEM-CG, FEM-DG, FVM).

### Step 1: Explicitly advect quantities:
We first apply time splitting and use an explicit method for conservative advection:

$$\rho^{t+1}=\text{conservative\_advect}(\rho^t,\vec{u}^t,\Delta t)$$
$$(\rho\vec{u})^*=\text{conservative\_advect}((\rho\vec{u})^t,\vec{u}^t,\Delta t)$$
$$\tilde{E}=\text{conservative\_advect}(E^t,\vec{u}^t,\Delta t)$$

Where

$$\vec{u}^t=(\rho\vec{u})^t/\rho^t$$
$$p^t=p(e^t,\rho^t)$$
$$e^t=E^t/\rho^t-\frac{1}{2}(\vec{u}^t)^T\vec{u}^t$$

## Step 2: Solve for pressure

We similarly apply time splitting to the terms of the pressure update equation. First we non-conservatively advect pressure.

$$p^*=\text{nonconservative\_advect}(p^t,\vec{u}^t,\Delta t)$$

Then we solve for $p^{t+1}$ by substituting the final momentum update equation into the pressure divergence term:

$$p^{t+1}=p^*-\Delta t\rho^{t+1}c^2\nabla\cdot(\rho^{t+1})^{-1}((\rho\vec{u})^*-\Delta t \nabla p^{t+1})$$
$$=p^*
-\Delta t\rho^{t+1}c^2\nabla\cdot(\rho^{t+1})^{-1}(\rho\vec{u})^*
+\Delta t^2\rho^{t+1}c^2\nabla\cdot(\rho^{t+1})^{-1}\nabla p^{t+1}$$

Then moving components over to the LHS, we solve the following linear system for $p^{t+1}$.

$$(1-\Delta t^2\rho^{t+1}c^2\nabla\cdot(\rho^{t+1})^{-1}\nabla)p^{t+1}=
p^*-\Delta t\rho^{t+1}c^2\nabla\cdot(\rho^{t+1})^{-1}(\rho\vec{u})^*$$

## Step 3: Compute final momentum and total energy

Then we compute the final momentum and energy as:

$$(\rho\vec{u})^{t+1}=(\rho\vec{u})^*-\Delta t \nabla p^{t+1}$$

$$E^{t+1}=E^*-\Delta t\nabla\cdot p^{t+1}\vec{u}^{t+1}$$

## Energy equation derivation ignoring pressure

$\dd{\rho\u}{t}=-\nabla\cdot(\rho\u\u^T)$

$\rho\dd{\u}{t}=-\nabla\cdot(\rho\u\u^T)-\dd{\rho}{t}\u$

$\dd{E}{t}=-\nabla\cdot(E\u)$

$E=\frac{1}{2}\rho\u\u$

$\dd{E}{t}=\frac{1}{2}(\dd{\rho}{t}\u\u+\rho\dd{\u}{t}\u+\rho\u\dd{\u}{t})$

$\dd{E}{t}=\frac{1}{2}\dd{\rho}{t}\u\u+\rho\u\dd{\u}{t}$

$\dd{E}{t}=
-\frac{1}{2}\nabla\cdot(\rho\u)\u\u
-\u\nabla\cdot(\rho\u\u)
-\u\u\dd{\rho}{t}$

$\dd{E}{t}=
-\frac{1}{2}\nabla\cdot(\rho\u)\u\u
-\u\nabla\cdot(\rho\u\u)
+\u\u\nabla\cdot(\rho\u)$

$-\frac{1}{2}\nabla\cdot(\rho\u\u\u)=-\frac{1}{2}\nabla\cdot(\rho\u)\u\u-\frac{1}{2}\nabla\cdot(\u)\rho\u\u-\frac{1}{2}\nabla\cdot(\u)\rho\u\u$

$\dd{xx}{t}=\dd{x}{t}x+x\dd{x}{t}=2x\dd{x}{t}$

<!-- $\frac{\partial E}{\partial t}=
 \frac{\partial\rho}{\partial t}e
+\rho\frac{\partial e}{\partial t}
+\frac{1}{2}\frac{\partial\rho}{\partial t}\vec{u}^T\vec{u}
+\rho\vec{u}^T\frac{\partial\vec{u}}{\partial t}$ /-->

<!-- $-\nabla\cdot(e\vec{u})-\nabla\cdot\nabla e$ /-->

Equation of state:
https://en.wikipedia.org/wiki/Ideal_gas_law

$pV=nRT$

## Energy equation derivation

$\dd{E}{t}=-\nabla\cdot((E+p)\u)$

$E=\rho e+\frac{1}{2}\rho\u^T\u$

$\dd{E}{t}=-\nabla\cdot(E\u)-\nabla\cdot(p\u)$

$\dd{E}{t}=-\nabla\cdot(\rho e+\frac{1}{2}\rho\u^T\u\u)-\nabla\cdot(p\u)$

## Advection
The conservative advection term:
$\nabla\cdot\phi\vec{u}=\vec{u}\cdot\nabla\phi+\phi\nabla\cdot\vec{u}$

The equation can be proven to be conservative using the divergence rule. This is that the only change in a volume is due to flux on the boundary.

The first term $\vec{u}\cdot\nabla\phi$ is the flow due to the zero-divergence part of the velocity field. This term can generally not create extrema as it merely pulls from the values around it until the field has equalized. The second term $\phi\nabla\cdot\vec{u}$ is the flow due to the divergence part of the velocity field. This can create arbitrary extrema during compression and expansion.

Conservative semi-lagrangian advection treats nodes lagrangian, moving the quantity at each node with the node's velocity and then using some conservative local distribution coefficients (such as interpolation weights) to remap the values to the grid in the new location. A backward step may also be needed.

Reference: unconditionally stable conservative advection:
https://physbam.stanford.edu/~fedkiw/papers/stanford2010-01.pdf

## Pressure/Equation of State

"specific" = units per mass.

Pressure is non-bulk kinetic energy per volume. Temperature is non-bulk kinetic energy per mass.

$p=energy/volume$

E is conserved, and when changed in volume, increases proportionately to the change in density.

$p=nRT/V=\rho RT$

$p=R_e\rho e$

$p(\rho,e)=...$

$(\rho\u)^{t+1}=(\rho\u)^*-\Delta t\nabla p^{t+1}$

## Derivative of velocity time derivative

Ignoring viscous terms.

$\dd{\rho\u}{t}=-\nabla\cdot(\rho\u\u^T)-\nabla p$

$\dd{\u}{t}=\frac{1}{\rho}(-\nabla\cdot(\rho\u\u^T)-\nabla p-\dd{\rho}{t}\u)$

$\dd{\u}{t}=\frac{1}{\rho}(-\nabla\cdot(\rho\u\u^T)-\nabla p+\nabla\cdot(\rho\u)\u)$

## Derivation of energy time derivative

$E=\rho e+\frac{1}{2}\rho\u^T\u$

$e=\frac{E}{\rho}-\frac{1}{2}\u^T\u$

Take the time derivative.

$\dd{e}{t}=\dd{E}{t}\frac{1}{\rho}-\frac{E}{\rho^2}\dd{\rho}{t}-\frac{1}{2}2\u^T\dd{\u}{t}$

$\rho\dd{e}{t}=\dd{E}{t}-\frac{E}{\rho}\dd{\rho}{t}-\rho\u^T\dd{\u}{t}$

$\rho\dd{e}{t}=\dd{E}{t}+\frac{E}{\rho}\nabla\cdot(\rho\u)-\rho\u^T\dd{\u}{t}$

$\rho\dd{e}{t}=-\nabla\cdot((E+p)\u)+\frac{E}{\rho}\nabla\cdot(\rho\u)-\rho\u^T\dd{\u}{t}$

$\rho\dd{e}{t}=-\nabla\cdot(E\u)-\nabla\cdot(p\u)+\frac{E}{\rho}\nabla\cdot(\rho\u)-\rho\u^T\dd{\u}{t}$

$\rho\dd{e}{t}=-\nabla\cdot(E\u)-\nabla\cdot(p\u)+\nabla\cdot(\frac{E}{\rho}\rho\u)-\rho\u\cdot\nabla\frac{E}{\rho}-\rho\u^T\dd{\u}{t}$

$\rho\dd{e}{t}=-\rho\u\cdot\nabla\frac{E}{\rho}-\nabla\cdot(E\u)-\nabla\cdot(p\u)+\nabla\cdot(\frac{E}{\rho}\rho\u)-\rho\u^T\dd{\u}{t}$

$\rho\dd{e}{t}=
-\rho\u\cdot\nabla\frac{E}{\rho}
-\nabla\cdot(\rho e\u)
-\nabla\cdot(\frac{1}{2}\rho\u^T\u\u)
-\nabla\cdot(p\u)
+\nabla\cdot(\frac{E}{\rho}\rho\u)
-\rho\u^T\dd{\u}{t}$

$\rho\dd{e}{t}=
-\rho\u\cdot\nabla\frac{E}{\rho}
-\nabla\cdot(\rho e\u)
-\frac{1}{2}\u^T\u\nabla\cdot(\rho\u)
-\frac{1}{2}\rho\u\cdot\nabla(\u^T\u)
-\nabla\cdot(p\u)
+\nabla\cdot(\frac{E}{\rho}\rho\u)
-\rho\u^T\dd{\u}{t}$

$\rho\dd{e}{t}=
-\rho\u\cdot\nabla\frac{E}{\rho}
-\frac{1}{2}\rho\u\cdot\nabla(\u^T\u)
-\nabla\cdot(\rho e\u)
-\frac{1}{2}\u^T\u\nabla\cdot(\rho\u)
-\nabla\cdot(p\u)
+\nabla\cdot(\frac{E}{\rho}\rho\u)
-\rho\u^T\dd{\u}{t}$

$\rho\dd{e}{t}=
-\rho\u\cdot\nabla\frac{E}{\rho}
-\frac{1}{2}\rho\u\cdot\nabla(\u^T\u)
-\nabla\cdot(\rho e\u)
-\frac{1}{2}\u^T\u\nabla\cdot(\rho\u)
-\nabla\cdot(p\u)
+\nabla\cdot(\frac{E}{\rho}\rho\u)
-\rho\u^T(\frac{1}{\rho}(-\nabla\cdot(\rho\u\u^T)-\nabla p+\nabla\cdot(\rho\u)\u)$))

$\rho\dd{e}{t}=
-\rho\u\cdot\nabla\frac{E}{\rho}
-\frac{1}{2}\rho\u\cdot\nabla(\u^T\u)
-\nabla\cdot(\rho e\u)
-\frac{1}{2}\u^T\u\nabla\cdot(\rho\u)
-\nabla\cdot(p\u)
+\nabla\cdot(\frac{E}{\rho}\rho\u)
-\u^T(-\nabla\cdot(\rho\u\u^T)-\nabla p+\nabla\cdot(\rho\u)\u)$)

..............




---------------------------

Backwards from solution


$\dd{e}{t}=-\u^T\nabla e-\frac{p}{\rho}\nabla\cdot\u$

$\rho\dd{e}{t}=-\rho\u^T\nabla e-p\nabla\cdot\u$

$\rho\dd{e}{t}=-\rho\u^T\nabla(\frac{E}{\rho}-\frac{1}{2}\u^T\u)-p\nabla\cdot\u$

$\rho\dd{e}{t}=-\rho\u^T\nabla\frac{E}{\rho}+\frac{1}{2}\rho\u^T\nabla(\u^T\u)-p\nabla\cdot\u$






## BLAH

Then we substitute the velocity and pressure time derivatives back into the energy time derivative:

$\dd{E}{t}=-\nabla\cdot(\rho\u)(e+\frac{1}{2}|\u|^2)+\rho\dd{e}{t}+\rho\u^T(\frac{1}{\rho}(-\nabla\cdot(\rho\u\otimes\u)-\nabla p+\nabla\cdot(\rho\u)\u))$

$\dd{E}{t}=-\nabla\cdot(\rho\u)(e+\frac{1}{2}|\u|^2)+\rho\dd{e}{t}+\u^T(-\nabla\cdot(\rho\u\otimes\u)-\nabla p+\nabla\cdot(\rho\u)\u)$

$\dd{E}{t}=-\nabla\cdot(\rho\u)(e-\frac{1}{2}|\u|^2)+\rho\dd{e}{t}+\u^T(-\nabla\cdot(\rho\u\otimes\u)-\nabla p)$

Next we need to compute the internal energy time derivative from the equation of state.

$p=R \rho T$

Then substituting $T=c e$ where c is an unknown constant.

$p=R \rho c e$

Then absorbing the 2 constants.

$p=R_c \rho e$

And solving for e

$e=\frac{p}{R_c\rho}$

And taking the time derivative.

$\dd{e}{t}=\dd{p}{t}\frac{1}{R_c\rho}-\frac{p}{R_c\rho^2}\dd{\rho}{t}$



Steps to finish derivation:
1. Derive pressure update. Should only end up with a non-conservative pressure advection term, and a rho*div.vel term.
2. Substitute time update into pressure update.


Reference - Unconditionally stable equation of state integration:
https://physbam.stanford.edu/~fedkiw/papers/stanford2008-04.pdf
