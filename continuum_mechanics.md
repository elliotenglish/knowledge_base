# Continuum Mechanics

- Fluids: $\sigma=Ip$
- Solids: $\sigma=\frac{\partial{W}}{\partial\epsilon}\cdot\frac{F}{det(F)}$, $F=\frac{\partial{\vec{x}}}{\partial{\vec{r}}}$

Pressure is related to the determinant of F, measuring the compression of the material.

Generally cell centered quantities are desirable as they let you represent a continuum as non-diffuse subregions. This is often achieved using a discontinuous Galerkin approach where equations are broken up into both intracell dynamics (volume integrals) and intercell dynamics (facial integrals). The challenge with this is that at faces, there is typically no well defined value of the quantity. This has been used to advantage in some cases such as when there is a discontinuity in the material properties (material) or state itself (shocks), but also means that computing derivatives needed for evaluation of integrals is problematic (e.g. deformation rates).

In general however, strain only needs to know rates of deformation (velocity derivatives) or deformation itself (position derivatives relative to the reference configuration). To achieve the latter, a continuous representation is generally the most advantageous approach (an not a conserved quantity, as defined by a primary PDE).



Saddlepoint systems

Solving for stress directly

Multigrid
