# Finite Element Method

## Terminology

- $\phi$ are the basis functions and typically have a subscript to index them.

## General formulation and assembly

1. Given a multifunction (multiple PDEs in a system), multivalue (multiple solution variables), multivariate (multiple dimension space) PDE: $$f_k(\{\frac{\partial^m u_i(x)}{\partial x_j^m}\})=0$$ where
  - $m=[0,N_o]$ describes the order of the problem.
  - $u_i(x),i=[1,N_u]$ are the dependent variables.
  - $x_j,j=[1,N_x]$ are the independent variables (e.g. spatial variables).
  - $f_k(\cdot),k=[1,N_f]$ are the equation functions (e.g. residual functions).
  - $\vec{x}\in\Omega$ is the domain.
  - $\{\frac{\partial^m u_i(x)}{\partial x_j^m}\}=\{u_1(x),...,u_{N_u}(x),\frac{\partial u_1(x)}{\partial x_1},...,\frac{\partial u_{N_u}(x)}{\partial x_{N_x}},...,\frac{\partial^{N_o} u_1(x)}{\partial x_1^{N_o}},...,\frac{\partial^{N_o} u_{N_u}(x)}{\partial x_{N_x}^{N_o}}\}$ are the elements of derivatives of $u$ and $x$.
  - TODO: Boundary conditions.
This full continuum equation is converted to a discrete equation in the following steps:
2. Divide the domain into elements: $$\Omega=\bigcup_e\Omega_e,e\in [1,N_e]$$ where
3. Define basis functions for describing the solution space: $$\phi_n(x),n\in [1,N_n]$$ where $$0<=\phi_n(x)<=1$$ and $$\sum_n\phi_n(x)=1,\forall x\in \Omega$$. In general $\phi_n(x)$ has finite support (i.e. domain with non-zero value) on a small number of elements incident to a node.
4. Define the solution space as some linear combination of these basis functions: $$u_i({x_j})=\sum_n u_{i,n}\phi_n(x_j)$$ where $u_{i,n}$ is the discrete solution variable for the $nth$ basis node and $\phi_n(\cdot)$ is the $nth$ basis function.
5. Define residual functions (also known as test functions) for describing how we're weakly enforcing the PDE: $\alpha_l$, analogously to the basis functions $\phi_n$.
6. Convert the PDE to the weak form of the problem by first multiplying the equations by a residual weight function: $$\alpha_l(x)f_k(\{\frac{\partial^m u(x)}{\partial x_j^m}\})=0,l\in N_\alpha$$ where we have a separate equation now for each residual weight function.
7. Second, integrate each equation over the support region for each basis function. This forms the discrete residual equations: $$\int_{\Omega_{\alpha_l}}\alpha_l(x) f(\{\frac{\partial^m u(x)}{\partial x_j^m}\}) dx=0,l\in\N_\alpha$$ where $\Omega_{\phi_n}$ is the support region for the $nth$ basis function.
8. Substitute in the solution space: $$\int_{\Omega_{\alpha_l}}\alpha_l(x) f(\{\frac{\partial^m \sum_n u_{n}\phi_n(x)}{\partial x_j^m}\}) dx=0$$. and move the sum out of the derivative: Substitute in the solution space: $$\int_{\Omega_{\alpha_l}}\alpha_l(x) f(\{ \sum_n u_{n}\frac{\partial^m\phi_n(x)}{\partial x_j^m}\}) dx=0$$. In the case of a linear PDE we further move the sum all the way to the outside of the integral. In the case of a non-linear PDE we need will need to linearize the PDE with a Taylor expansion and iteratively solve it.
9. In the general Galerkin method, the weight functions and basis functions are equal so $$\alpha_i(x)=\phi_i(x)$$. This also guarantees that the resulting linear system if $N_n\times N_n$ is a square and in general invertible. This yields the most common form: $$\int_{\Omega_{\phi_l}}\phi_l(x) f(\{\sum_n u_{n}\frac{\partial^m\phi_n(x)}{\partial x_j^m}\}) dx=0$$.

**It is important to note that in most finite element explanations they break this integral up into portions that correspond to the elements the cover the support region. This is required for software implementation. It is however, critical to understand that the actual discrete equation (and hence matrix row), corresponds to the full integral. It is through this that we end up with an $N_n \times N_n$ invertible linear system.**

## Integration on reference elements

### Spatial transformation

Like solving PDEs on curvilinear grids, the integration is typically performed in the reference space. This is done by incorporating metric terms.

We define the spatial transform from the reference space $\vec{\xi}$ to world space $\vec{x}$ as:

$$\begin{pmatrix}x_1(\xi_1,\cdots,\xi_d)\\\vdots\\x_d(\xi_1,\cdots,\xi_d)\end{pmatrix}=\vec{x}(\vec{\xi})$$

References:
- https://crd.lbl.gov/assets/pubs_presos/AMCS/ANAG/SciDAC2009.pdf
- https://mfem.org/integration/

TODO: Figure out why their formulation is different.

### Jacobian

$$\textbf{J}=\begin{pmatrix}
\frac{\partial x_1}{\partial \xi_1} & \cdots & \frac{\partial x_1}{\partial \xi_d} \\
\vdots & \ddots & \vdots \\
\frac{\partial x_d}{\partial \xi_1} & \cdots & \frac{\partial x_d}{\partial \xi_d}
\end{pmatrix}$$

Noting that for an orthogonal coordinate system (which is implicit in any local basis):

$$\frac{\partial x_i}{\partial x_j}=\delta_{ij}$$

We can expand the derivative as terms in another basis using the chain rule:

$$\frac{\partial x_i}{\partial x_j}=\sum_k \frac{\partial x_i}{\partial \xi_k}\frac{\partial \xi_k}{\partial x_j}$$

Noting that the first terms are the elements of the Jacobian we get the following:

$$\begin{pmatrix}
\frac{\partial x_1}{\partial \xi_1} & \cdots & \frac{\partial x_1}{\partial \xi_d} \\
\vdots & \ddots & \vdots \\
\frac{\partial x_d}{\partial \xi_1} & \cdots & \frac{\partial x_d}{\partial \xi_d}
\end{pmatrix}
\begin{pmatrix}
\frac{\partial \xi_1}{\partial x_1} & \cdots & \frac{\partial \xi_1}{\partial x_d} \\
\vdots & \ddots & \vdots \\
\frac{\partial \xi_d}{\partial x_1} & \cdots & \frac{\partial \xi_d}{\partial xi_d}
\end{pmatrix}
=\begin{pmatrix}
1 & & \\
& \ddots & \\
 & & 1
\end{pmatrix}
=J J^{-1}$$

Therefore:

$$J^{-1}
=\begin{pmatrix}
\frac{\partial \xi_1}{\partial x_1} & \cdots & \frac{\partial \xi_1}{\partial x_d} \\
\vdots & \ddots & \vdots \\
\frac{\partial \xi_d}{\partial x_1} & \cdots & \frac{\partial \xi_d}{\partial x_d}
\end{pmatrix}$$

### Integral change of basis

Here we give the formulas for changing the integration variable from $\vec{x}\in\Omega$ to $\vec{\xi}\in\Omega_\xi$.

$$\int_{\Omega} f(\vec{x})d\vec{x}=\int_{\Omega_\xi}f(\vec{x}(\vec{\xi}))\text{det}\left(\frac{\partial\vec{x}}{\partial\vec{\xi}}\right) d\xi=\int_{\Omega_\xi}f(\vec{x}(\vec{\xi}))|J|d\xi$$

Note that we can reparameterize $f$ with coordinate transform and just get the following:

$$\int_{\Omega} f(\vec{x})d\vec{x}=\int_{\Omega_\xi}f(\vec{\xi})|J|d\xi$$

Note that $|J|$ is the determinant of $J$ and represents the size of parallelpiped formed by that matrix. See the notes on differential geometry for more information. The general proof of this multivariable substitution in integrals is very difficult to find.

### Numerical integration/quadrature

In order to compute an integral without using a closed form we use numerical integration (aka quadrature). This works by subdividing the domain into subdomains and then sampling a point in each subdomain. The approximate integral is then the volume of those subdomains multiplied by the sampled point. In this case of finite elements we summarize this follows:

$$\int_\Omega f(\vec{x})d\vec{x}=\sum_k w_k f(\vec{x}_k)$$

Where $w_k$ is the volume of the subdomain $\Omega_k$ and $\vec{x}_k$ is the point sampled within that subdomain.

### Derivatives

$$\frac{\partial f(\vec{x})}{\partial x_i}
=\sum_j\frac{\partial f(\vec{\xi})}{\partial \xi_j}\frac{\partial \xi_j}{\partial x_i}$$

Noting that we can rearrange the factors:

$$\frac{\partial f(\vec{x})}{\partial x_i}
=\sum_j\frac{\partial \xi_j}{\partial x_i}\frac{\partial f(\vec{\xi})}{\partial \xi_j}$$

### Gradient

Then we can extend this to gradients:

$$\nabla_{\vec{x}}f(\vec{x})=
\begin{pmatrix}
\frac{\partial f(\vec{x})}{\partial x_1} \\
\vdots \\
\frac{\partial f(\vec{x})}{\partial x_d}
\end{pmatrix}$$

$$=\begin{pmatrix}
\sum_j\frac{\partial \xi_j}{\partial x_1}\frac{\partial f(\vec{\xi})}{\partial \xi_j} \\
\vdots \\
\sum_j\frac{\partial \xi_j}{\partial x_d}\frac{\partial f(\vec{\xi})}{\partial \xi_j}
\end{pmatrix}$$

$$=\begin{pmatrix}
\frac{\partial \xi_1}{\partial x_1} & \cdots & \frac{\partial \xi_d}{\partial x_1} \\
\vdots & \ddots & \vdots \\
\frac{\partial \xi_1}{\partial x_d} & \cdots & \frac{\partial \xi_d}{\partial x_d} \\
\end{pmatrix}
\begin{pmatrix}
\frac{\partial f(\vec{\xi})}{\partial \xi_1} \\
\vdots \\
\frac{\partial f(\vec{\xi})}{\partial \xi_d}
\end{pmatrix}$$

$$=J^{-T}\nabla_{\xi}(f(\vec{\xi}))$$

### Divergence

$$\nabla_x\cdot\vec{u}=\sum_i\frac{\partial u_i}{\partial x_i}$$

$$=\sum_i\sum_j\frac{\partial u_i}{\partial\xi_j}\frac{\partial\xi_j}{\partial x_i}$$

$$=Tr(\begin{pmatrix}
\sum_j\frac{\partial u_1}{\partial\xi_j}\frac{\partial\xi_j}{\partial x_1} & \cdots & \sum_j\frac{\partial u_1}{\partial\xi_j}\frac{\partial\xi_j}{\partial x_d} \\
\vdots & \ddots & \vdots \\
\sum_j\frac{\partial u_d}{\partial\xi_j}\frac{\partial\xi_j}{\partial x_1} & \cdots & \sum_j\frac{\partial u_d}{\partial\xi_j}\frac{\partial\xi_j}{\partial x_d} \\
\end{pmatrix})$$

$$=Tr(
\begin{pmatrix}
\frac{\partial \xi_1}{\partial x_1} & \cdots & \frac{\partial \xi_d}{\partial x_1} \\
\vdots & \ddots & \vdots \\
\frac{\partial \xi_1}{\partial x_d} & \cdots & \frac{\partial \xi_d}{\partial x_d} \\
\end{pmatrix}
\begin{pmatrix}
\frac{\partial u_1}{\partial \xi_1} & \cdots & \frac{\partial u_d}{\partial \xi_1} \\
\vdots & \ddots & \vdots \\
\frac{\partial u_1}{\partial \xi_d} & \cdots & \frac{\partial u_d}{\partial \xi_d} \\
\end{pmatrix})$$

$$=Tr(J^{-T}(\nabla_{\xi}\vec{u})^T)$$

Note that we should probably be able to move the Jacobian into the gradient operator since the resulting derivative of a product, and the resulting product rule second term would go to 0 due to rearranging the order of derivatives using the "equivalence of second derivatives" and having terms like $\frac{\partial}{\partial\xi_k}\frac{\partial\xi_i}{\partial x_j}=\frac{\partial}{\partial x_j}\frac{\partial\xi_i}{\partial\xi_k}=\frac{\partial}{\partial x_j}\delta_{ik}=0$.

This gives us the following:

$$\nabla_x\cdot\vec{u}=\sum_i\frac{\partial u_i}{\partial x_i}$$

Expand in terms of reference space partial derivatives:

$$=\sum_i\sum_j\frac{\partial u_i}{\partial\xi_j}\frac{\partial\xi_j}{\partial x_i}$$

Use product derivative identity:

$$=\sum_i\sum_j\frac{\partial}{\partial\xi_j}(u_i\frac{\partial\xi_j}{\partial x_i})-u_i\frac{\partial}{\partial\xi_j}(\frac{\partial\xi_j}{\partial x_i})$$

Merge derivatives:

$$=\sum_i\sum_j\frac{\partial}{\partial\xi_j}(u_i\frac{\partial\xi_j}{\partial x_i})-u_i\frac{\partial^2\xi_j}{\partial\xi_j\partial x_i}$$

Change derivative order using the equivalence of second derivatives:

$$=\sum_i\sum_j\frac{\partial}{\partial\xi_j}(u_i\frac{\partial\xi_j}{\partial x_i})-u_i\frac{\partial^2\xi_j}{\partial x_i\partial\xi_j}$$

Break out reference coordinate derivatives:

$$=\sum_i\sum_j\frac{\partial}{\partial\xi_j}(u_i\frac{\partial\xi_j}{\partial x_i})-u_i\frac{\partial}{\partial x_i}\frac{\partial\xi_j}{\partial\xi_j}$$

Evaluate reference coordinate derivative to $1$:

$$=\sum_i\sum_j\frac{\partial}{\partial\xi_j}(u_i\frac{\partial\xi_j}{\partial x_i})-u_i\frac{\partial}{\partial x_i}1$$

Derivative of constant is 0:

$$=\sum_i\sum_j\frac{\partial}{\partial\xi_j}(u_i\frac{\partial\xi_j}{\partial x_i})-u_i\cdot 0$$

Term goes to 0:

$$=\sum_i\sum_j\frac{\partial}{\partial\xi_j}(u_i\frac{\partial\xi_j}{\partial x_i})$$

Change order of summations:

$$=\sum_j(\frac{\partial}{\partial\xi_j}\sum_i u_i\frac{\partial\xi_j}{\partial x_i})$$

Rewrite as divergence in reference space:

$$=\nabla_\xi\cdot
\begin{pmatrix}
\sum_i u_i\frac{\partial\xi_1}{\partial x_i} \\
\vdots \\
\sum_i u_i\frac{\partial\xi_d}{\partial x_i}
\end{pmatrix}$$

Rewrite internal expression as jacobian inverse matrix product:

$$=\nabla_\xi\cdot((\nabla_x\xi)\vec{u})$$

Effectively this is just rotating $\vec{u}$ into the $\vec{\xi}$ space. TODO: Using symbolic calculation to verify this result.

$$\int_\Omega\nabla\cdot\vec{u}d\vec{x}=\int_{\Omega_\xi} \ldots d\vec{\xi}$$

We want to convert the $\nabla$ from $\nabla_{\vec{x}}$ to $\nabla_{\vec{\xi}}$. Noting that $\vec{u}$ is in the world space basis.

From https://crd.lbl.gov/assets/pubs_presos/AMCS/ANAG/SciDAC2009.pdf:

$$\nabla_x\cdot\vec{u}=\frac{1}{det(J)}\nabla_\xi\cdot(N^T\vec{u})$$
$$J=\nabla_\xi\vec{x}$$
$$N^T_{p,q}=det((\nabla_\xi\vec{x})(p|e^q))$$
where $A(a|b)$ is $A$ with row $a$ replaced with vector $b$, and $e^q$ is the $q$-th one-hot vector. This is effectively cramer's rule.

### Dot products of vectors and gradients

$$\int_\Omega\vec{u}\cdot\nabla \rho d\vec{x}=\int_{\Omega_\xi} \ldots d\vec{\xi}$$

See the gradient definition above and simply subtituting that in. One could also then proceed to redefine the basis of $\vec{u}$ and further rewrite the equation in the reference space.

## Element types

- Lagrange elements are the most obvious and encompass the linear simplex elements. They also include higher order elements by equally spacing nodes within elements
  - http://femwiki.wikidot.com/elements:lagrange-elements
- [Legendre polynomials](https://en.wikipedia.org/wiki/Legendre_polynomials)
- [Gauss-Legendre points](https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_quadrature)

## Continuous Galerkin (CG) Method

The continuous Galerkin method assumes that the basis functions are continuous across elements by being continuous everywhere within their domain and smoothly decaying to 0 at the edge of the basis function support region.

- Degrees of freedom are stored at nodes

References:
- https://www.sciencedirect.com/science/article/pii/S002199910096577X

## Discontinuous Galerkin (DG) Method

The discontinuous Galerkin method assumes that the basis functions are only continuous within an element. In general this allows the divergence theorem to be used and effectively bridge the gap between FEM and FVM methods.

For advection terms, they even permit upwinding (see the notes [here]](https://www-users.cse.umn.edu/~bcockbur//lecture_notes/DG-4.pdf)).

Since they utilize node boundary fluxes they respect the conservation properties of PDEs.

TODO: Figure out what the prototypical variable representations. If they're just a polynomial within the element, where do the degrees of freedom live? It's clear for CG where you typically have nodal, edge and interior values.

- Degrees of freedom are stored at elements

References:
- https://en.wikipedia.org/wiki/Discontinuous_Galerkin_method
- https://www3.nd.edu/~zxu2/acms60790S15/DG-general-approach.pdf
- https://www.oden.utexas.edu/media/reports/2001/0121.pdf
- https://cdn.nr.re.kr/nrgwss2022/lecture/2022NRGWSchool_DG_method.pdf

## Nodal vs Modal Basis Functions

Nodal refers to values being stored at specific points in space or at certain geometry elements like a node, edge, face or element. Modal refers to values being stored across the domain at solution frequencies instead. In some sense because these are all multipliers for basis functions they form a spectrum of options.

## Poisson equation on continuous elements

The general Poisson equation is as follows:

$$\nabla\cdot\nabla u(x)=g(x)$$

Where $g(x)$ is a forcing function. Note that this is equivalent to the above (where $f(x)=\nabla\cdot\nabla u(x)-g(x)$). Note that the weighted form ($\nabla\cdot h(x)\nabla u(x)=g(x)$) is needed in the case of variable viscosity fluids, and variable material heat equations, but can be solved similarly after expanding the equation using the chain rule.

Discretizing the equation as above we end up with the following:

$$\int_{\Omega_n}\phi_n(x)\nabla\cdot\nabla u(x)dx=\int_{\Omega_n}\phi_n(x)g(x)dx$$

$$\int_{\Omega_n}\phi_n(x)\nabla\cdot\nabla \sum_i u_i\phi_i(x)dx=\int_{\Omega_n}\phi_n(x)g(x)dx$$

$$\sum_i u_i\int_{\Omega_n}\phi_n(x)\nabla\cdot\nabla\phi_i(x)dx=\int_{\Omega_n}\phi_n(x)g(x)dx$$

Where the solution variables are now $u_i$. Note that since $\phi_i$ is linear, the second derivative will be 0, so we can't proceed with this exact formulation. Instead, the strategy is typically to use integration by parts (specifically in higher dimensions, using Green's first identity https://en.wikipedia.org/wiki/Integration_by_parts#Higher_dimensions) to move the derivative to the residual weight.

$$\sum_i u_i\left ( \int_{\Omega_n}-\nabla\phi_n(x)\cdot\nabla\phi_i(x)dx+\int_{\partial \Omega_n}\phi_n(x)n\cdot\nabla \phi_i(x)\right )=\int_{\Omega_n}\phi_n(x)g(x)dx$$

Note that for internal nodes with basis functions decaying to 0 within the domain that the boundary term goes to 0. For nodes on the domain boundary the integral portion that lies on the boundary face incident to the node corresponds to one sided derivative that is balanced with boundary conditions.

Also note that the gradient of the weight node basis ($\phi_n$) is effectively a normal direction for a dual element around the node basis, and that the derivative of the solution basis ($\phi_i$) is the derivative within the incident element. Hence this formulation is equivalent to a finite volume formulation (TODO: reference proof).

One problem with this equation is that the boundary term is not well defined. So if we instead were to perform the steps above in a different order and leave that term undiscretized we get the following:

$$\sum_i u_i\left ( \int_{\Omega_n}-\nabla\phi_n(x)\cdot\nabla\phi_i(x)dx\right )+\int_{\partial \Omega_n}\phi_n(x)n\cdot\nabla u(x)=\int_{\Omega_n}\phi_n(x)g(x)dx$$

This formula instead shows that we actually want the normal derivative of the solution at the boundary. This is equivalent to a Neumann boundary condition. We must either set this, or apply a Dirichlet boundary condition and remove the degree of freedom. If instead we were to stick with the discrete formula above, a one sided derivative based upon the interior incident element, we will tend to 0 out the row and make the system matrix singular.

References:
- https://medium.com/@ariel.yaniv/finite-element-method-explained-how-to-solve-the-1d-poisson-equation-part-i-206b5bce1cfb

## Advection term on continuous elements

$$\nabla\cdot\rho\vec{u}$$

Multiplying by the residual weight function and integrating we get the weak form:

$$\int_{\Omega_i}\phi_i\nabla\cdot\rho\vec{u}$$

### Option 1:

While this is the CG form, we can't compute it due to the derivative involving a product. Most FEM frameworks only provide derivatives of basis functions. So we need to use the divergence of a product identity:

$$=\int_{\Omega_i}\phi_i(\rho\nabla\cdot\vec{u}+\vec{u}\cdot\nabla\rho)$$

This is now something we can compute. However, if we need to solve an equation for $\vec{u}$ and $\rho$ simultaneously we need to convert it to a linear problem first. Assuming a fixed velocity we get the following integration rule:

$$=\int_{\Omega_i}\phi_i(\sum_j\rho_j\phi_j\nabla\cdot\vec{u}+\vec{u}\cdot\nabla\sum_j\rho_j\phi_j)$$

$$=\sum_j\rho_j\int_{\Omega_i}\phi_i(\phi_j\nabla\cdot\vec{u}+\vec{u}\cdot\nabla\phi_j)$$

This is sufficient for integrating through a prespecified, or fixed velocity field.

### Option 2:

However, the above method tends to introduce oscillations so we can reformulate as follows:

$$\int_{\Omega_i}\phi_i\nabla\cdot\rho\vec{u}=
\int_{\Omega_i}\nabla\cdot\phi_i\rho\vec{u}
-\rho\vec{u}\cdot\nabla\phi_i$$

$$=\int_{\partial\Omega_i}\phi_i\rho\vec{u}\cdot\vec{n}
-\int_{\Omega_i}\rho\vec{u}\cdot\nabla\phi_i$$

In general for interior domains, the first term goes to 0. When discretizing the second term, you can view is as a pseudo-face flux to the overlapping elements. This allows you to apply upwinding in the interpolation dimension.

$$-\int_{\Omega_i}\rho\vec{u}\cdot\nabla\phi_i=
-\int_{\Omega_i}\sum_j\rho_j\phi_j\vec{u}\cdot\nabla\phi_i$$

Here $\rho_j$ is the value at pseudo-face $j$, $\phi_j$ is the area of face $j$, and $\nabla\phi_i$ is the pseudo-face normal. In order for this to be conservative, the same term must appear for other node integrals, e.g. when swapping $j$/$i$. Conservation is guaranteed because of the following:

$$\sum_i\phi_i=1$$

Therefore

$$\nabla\sum_i\phi_i=0$$
$$=\sum_i\nabla\phi_i$$

And

$$\vec{u}\cdot\sum_i\nabla\phi_i=0$$

So to show conservation we sum the $j$-th term over all the cells, indexed by $i$, it contributes to:

$$\sum_i\rho_j\phi_j\vec{u}\cdot\nabla\phi_i=0$$

We can then view this as a type of $n$-way face and modify the flux to be upwinded to stabilize the method. Since we are referring to $\rho_j$ we look at the sign of $\vec{u}\cdot\nabla\phi_j$.

$$\rho_j^*=\left\{\begin{matrix}
\rho_j & \vec{u}\cdot\nabla\phi_j \le 0 \\
\frac{\sum_{k!=j}\phi_k\rho_k}{\sum{k!=j}\phi_k} & \vec{u}\cdot\nabla\phi_j < 0
\end{matrix} \right.$$

So we end up with the scheme:

$$\int_{\Omega_i}\phi_i\nabla\cdot\rho\vec{u}=
\int_{\partial\Omega_i}\phi_i\rho\vec{u}\cdot\vec{n}
-\int_{\Omega_i}\sum_j\rho_j^*\phi_j\vec{u}\cdot\nabla\phi_i$$

### Non-conservative advection term

$$\vec{u}\cdot\nabla\rho$$

Weak form:

$$\int_{\Omega_i}\phi_i\vec{u}\cdot\nabla\rho$$

$$=\int_{\Omega_i}\phi_i\vec{u}\cdot\nabla\sum_j\rho_j\phi_j$$

$$=\int_{\Omega_i}\sum_j\rho_j\phi_i\vec{u}\cdot\nabla\phi_j$$

Note that difference compared to the conservative form is the overall sign and the swapping of $\phi_i$ and $\phi_j$. We can similarly convert this to an upwind scheme by replacing the $\phi_j$ value with the upwind form as in the conservative case.

## Advection term on discontinuous elements

$$\nabla\cdot\rho\vec{u}$$

Weak form:

$$\int_{\Omega_i}\phi_i\nabla\cdot\rho\vec{u}$$

We then convert this using integration by parts:

$$=\int_{\partial\Omega_i}\phi_i\rho\vec{u}\cdot\vec{n}-\int_{\Omega_i}\rho\vec{u}\cdot\nabla\phi_i$$

For constant elements we can assume $\nabla\phi_i=0$. Otherwise the second term represents flow between variables within an element.

- Upwinding - use the flux defined at points just inside the cell the velocity is pointing away from)
- Flux limiting
- Slope limiting
- Preventing variables from become negative - this typically requires a global pass to reduce fluxes at cell within fluxes going to 0
- Timestep restrictions

## Continuity equation on continuous elements

$$\frac{\partial\rho}{\partial t}=-\nabla\cdot\vec{u}+f(x,t)$$

For the moment we ignore the forcing term:

$$\frac{\partial\rho}{\partial t}=-\nabla\cdot(\vec{u}\rho)$$

Then multiply by residual weight and integrate over node basis domain.

$$\int_{\Omega_n}\phi_n(x)\frac{\partial\rho}{\partial t}=-\int_{\Omega_n}\phi_n(x)\nabla\cdot(\vec{u}\rho)$$

Then apply the chain rule to separate out the product in the divergence so that we avoid taking numerical derivatives composite quantities:

$$\int_{\Omega_n}\phi_n(x)\frac{\partial\rho}{\partial t}=
-\int_{\Omega_n}\phi_n(x)(\rho\nabla\cdot\vec{u}-\vec{u}\cdot\nabla\rho)$$

Then substitute in the approximation for $\rho=\sum_i\rho_i\phi_i(x)$:

$$\int_{\Omega_n}\phi_n(x)\frac{\partial\sum_i\rho_i\phi_(x)}{\partial t}=
-\int_{\Omega_n}\phi_n(x)(\sum_i\rho_i\phi_i(x)\nabla\cdot\vec{u}-\vec{u}\cdot\nabla\sum_i\rho_i\phi_i(x))$$

Then move the summations out:

$$\sum_i\rho_i\int_{\Omega_n}\phi_n(x)\frac{\partial\phi_i(x)}{\partial t}=
-\sum_i\rho_i\int_{\Omega_n}\phi_n(x)(\phi_i(x)\nabla\cdot\vec{u}-\vec{u}\cdot\nabla\phi_i(x))$$

Then given $\nabla\phi_i$, and analytical values for $\vec{u}$ and $\nabla\cdot\vec{u}$ we can implement the equations in code.

## Weighted Laplacian term on continuous elements

$$w_0\nabla\cdot(w_1\nabla\rho)$$

$$\int_{\Omega_i}\phi_i w_0\nabla\cdot(w_1\nabla\rho)$$

$$=\int_{\Omega_i}\phi_i w_0\nabla\cdot(w_1\nabla\rho)$$

$$=\int_{\partial\Omega_i}\phi_i w_0 w_1\nabla\rho\cdot\vec{n}-\int_{\Omega_i}w_1\nabla \rho\cdot\nabla\phi_i w_0$$

$$=\int_{\partial\Omega_i}\phi_i w_0 w_1\nabla\rho\cdot\vec{n}
-\int_{\Omega_i}w_1\nabla \rho\cdot(w_0\nabla\phi_i+\phi_i\nabla w_0)$$

$$=\int_{\partial\Omega_i}\phi_i w_0 w_1\nabla(\sum_j\rho_j\phi_j)\cdot\vec{n}
-\int_{\Omega_i}w_1\nabla(\sum_j\rho_j\phi_j)\cdot(w_0\nabla\phi_i+\phi_i\nabla w_0)$$

$$=\sum_j\rho_j\int_{\partial\Omega_i}\phi_i w_0 w_1\nabla\phi_j\cdot\vec{n}
-\sum_j\rho_j\int_{\Omega_i}w_1\nabla\phi_j\cdot(w_0\nabla\phi_i+\phi_i\nabla w_0)$$

In the continuous domain, typically the first term goes to $0$ as $\phi_i$ is defined as 0 on $\partial\Omega_i$. This is not the case where you have Neumann boundary conditions however, so extra steps need to be performed with these partial domain integrals.

With Neumann boundary conditions you end up with:

$$=\sum_j\rho_j\int_{\partial\Omega_i\backslash\partial\Omega_N}\phi_i w_0 w_1\nabla\phi_j\cdot\vec{n}
+\int_{\partial\Omega_i\bigcap\partial\Omega_N}\phi_i w_0 w_1\nabla\rho\cdot\vec{n}
-\sum_j\rho_j\int_{\Omega_i}w_1\nabla\phi_j\cdot(w_0\nabla\phi_i+\phi_i\nabla w_0)$$

## Weighted Laplacian term on discontinuous elements

The derivation is the same as in the continuous case, however the second term goes to 0 on constant value elements. The additional challenge is that the gradient of the basis functions is now 0, so the gradient term $\nabla\phi_j$ also goes to 0.

## Weighted divergence term on continuous elements

$$w_0\nabla\cdot w_1\vec{u}$$

$$=>\int_{\Omega_i}\phi_i w_0\nabla\cdot w_1\vec{u}$$

$$=\int_{\Omega_i}\phi_i w_0(w_1\nabla\cdot\vec{u}+\vec{u}\cdot\nabla w_1)$$

$$=\int_{\Omega_i}\phi_i w_0(w_1\nabla\cdot\sum_j\phi_j\vec{u}_j+\sum_j\phi_j\vec{u}_j\cdot\nabla w_1)$$

$$=\int_{\Omega_i}\sum_j\phi_i w_0(w_1\nabla\cdot\phi_j\vec{u}_j+\phi_j\vec{u}_j\cdot\nabla w_1)$$

$$=\int_{\Omega_i}\sum_j\phi_i w_0(w_1\phi_j\nabla\cdot\vec{u}_j+w_1\vec{u}_j\cdot\nabla\phi_j+\phi_j\vec{u}_j\cdot\nabla w_1)$$

$$=\int_{\Omega_i}\sum_j\phi_i w_0(w_1\vec{u}_j\cdot\nabla\phi_j+\phi_j\vec{u}_j\cdot\nabla w_1)$$

## Weighted gradient term on continuous elements

$$w_0\nabla w_1\rho$$

$$=>\int_{\Omega_i}\phi_i w_0\nabla w_1\rho$$

$$=\int_{\Omega_i}\phi_i w_0(w_1\nabla\rho+\rho\nabla w_1)$$

$$=\int_{\Omega_i}\phi_i w_0(w_1\nabla\sum_j\rho_j\phi_j+\sum_j\rho_j\phi_j\nabla w_1)$$

$$=\int_{\Omega_i}\sum_j\rho_j\phi_i w_0(w_1\nabla\phi_j+\phi_j\nabla w_1)$$

## Curl term on continuous elements

$$\nabla\times\vec{v}(x)$$

$$\int_{\Omega_i}\phi_i\nabla\times\vec{v}$$

## Approximating non-linear differentials

Option 1:

Naively applying the Galerkin method above gives use term similar to the following:

$$\frac{\partial ab}{\partial x}=\frac{\partial(\sum_i a_i\phi_i)(\sum_j b_j\phi_j)}{\partial x}$$

However, these are complex and expensive to implement.

Option 2:

Instead, we can multiply together the solution variables together and then substitute in the approximation:

$$\frac{\partial ab}{\partial x}=\frac{\partial\sum_i a_i b_i\phi_i}{\partial x}$$

These methods both approximate the same expression. However, option 1 captures the nonlinearity within the element while option 2 relies upon the solution space to approximate the nonlinearity.

## Solving non-linear equations

General formulation:

$$\textbf{f}(\textbf{x})=0$$

- $\textbf{x}\in\R^{N_x}$
- $\textbf{f}\in\R^{N_f}$

In many problems we end up with equations involving products of solution variables. There are several common methods for doing so. Some general formulae are listed below.

### Newton's method

We first use a multivariate Taylor expansion around a point:

$$\textbf{f}(\textbf{x}+\textbf{h})\approx\textbf{f}(\textbf{x})+\left.\frac{\partial\textbf{f}}{\partial\textbf{x}}\right|_{x,y}\textbf{h}$$

Where $\frac{\partial\textbf{f}}{\partial\textbf{x}}=\nabla_\textbf{x}\textbf{f}=\textbf{J}$. For the rest of the derivation we drop the bar notation.

$$\textbf{f}(\textbf{x}+\textbf{h})=\textbf{f}(\textbf{x})+\textbf{J}\textbf{h}$$

We then set the left-hand side to $0$ and solve for $h$:

$$\textbf{h}=-\textbf{J}^{-1}\textbf{f}(\textbf{x})$$

We then define a Newton iteration as:

$$\textbf{x}^{k+1}=\textbf{x}^k-\textbf{J}^{-1}\textbf{f}(\textbf{x}^k)$$

### Fixed point iteration



### Time integration

We often see non-linear equations in time integration problems. In this case, if stability supports it, we can use a partially explicit scheme to replace all but one variable with a given value from a previous step.

## Software Packages
- Trilinos
- libmesh
- MFEM
- Moose

## libmesh notes

- `FEBase` is used to get certain properties of an Elem. The calling order with retrieving these references and calling reinit is important to inform the system as to what properties to compute. (TODO: get specific lifecycle details). QBase also has similar constraints.
- `FEBase::get_dphi()` returns $\frac{\partial\phi}{\partial\xi}$ in the physical space at the quadrature points (inner array) for each non-zero basis function in the elment (outer array). Specifically dphi[outer_index=basis_index][inner_index=quadrature_index].
- `FEBase::get_JxW()` returns the quadrature weights multiplied by the jacobian determinant, for each quadrature point. Using the previous notes on the change of basis and quadrature this corresponds to $w_k |J(\vec{x_k})|$
- Call `ReferenceCounter::disable_print_counter_info()` to disable default reference counting printing on libmesh deinitialization.
- Weak enforcement of Neumann boundary conditions: https://github.com/libMesh/libmesh/discussions/3796
- Interpolation at arbitrary points: https://github.com/libMesh/libmesh/discussions/3745
- Real is either defined as float or double based upon LIBMESH_DEFAULT_SCALAR_TYPE (libmesh_common.h)
- Number is either defined as Real of Complex (libmesh_common.h)
- VectorValue (e.g. Point) (type_vector.h)
- Fields are stored as "variables", where each is assigned an id when you call `int new_var_id=sys.add_variable("name",...)`
- Indices of variables in the global system are retrived by calling `std::vector<int> indices;dof_map.dof_indices(elem/node,indices,var_id)`
- For each variable-variable pair, construct a separate `DenseMatrix` and then call `add_matrix(submat,row_indices,col_indices)` to add the elements.
- For vector valued elements, `dof_indices(...)` will return D*N indices where the components are the inner dimension i.e. `indices=[(N=0,C=0),...(N=0,C=D-1),(N=1,C=0),...(N=0,C=D-1),...]`.
- To allocate a temporary vector you need a `Communicator` and a `DofMap`. Then you can call `vec=NumericVector::Build(comm)` followed by `vec.Init(dof_map.n_dofs(),dof_map.n_local_dofs(),false,PARALLEL)`. This was taken from the `System::add_vector` implementation. This will create a vector for all the variables managed by the `DofMap`.

General system assembly pattern
- Loop over full elements
  - Loop over interior quadrature points
    - Accumulate matrix coefficients
  - Loop over faces
    - If face is boundary face
      - Accumulate matrix coefficients

Note that while the FEBase instance for the full dimension element and FEBase for the codimension 1 elements are of the same dimension in the code, a quadrature rule of 1 dimension less is used and will cause the codimension 1 FEBase element to generate quadrature points on the element, but corresponding to the points of the full element. This allows you to integrate full dimension element quantities on the codimension 1 element but with the appropriate lower dimensional integration weights and points.

References:
- http://scisoftdays.org/pdf/2016_slides/stogner.pdf
- https://ntrs.nasa.gov/api/citations/20130013759/downloads/20130013759.pdf
