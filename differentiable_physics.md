# Differentiable Physics

## References

- https://simulately.wiki/docs/domain/differentiable/

## Software

General
- [NVIDIA Warp](https://github.com/NVIDIA/warp)

FEM
- [JAX-FEM](https://github.com/deepmodeling/jax-fem)
- [JAXSSO](https://github.com/GaoyuanWu/JaxSSO)

Fluids
- [JAXFLUIDS](https://github.com/tumaer/JAXFLUIDS) https://arxiv.org/abs/2203.13760

Robotics/Articulated Bodies
- Mujoco-JAX (MJX)
- https://github.com/ami-iit/jaxsim

Fusion/Electromagnetics
- [DESC-Opt](https://github.com/PlasmaControl/DESC)
- [Stellacode](https://github.com/rob3315/stellacode)

Additive Manufacturing
- [JAX-AM](https://github.com/tianjuxue/jax-am)

Stress/strain structure optimization
- [JAX FDM](https://github.com/arpastrana/jax_fdm)

## Research

- DiffCSG [paper](https://arxiv.org/abs/2409.01421) [github](https://github.com/YYYYYHC/Differentiable-CSG-via-Rasterization) - Extension of differentiable rendering to 3D
- [Nvdiffrast](https://github.com/NVlabs/nvdiffrast) - Differentiable rendering

## ML Based Subgrid Solutions

TODO: This belongs in a simulation page

- [DeepONet](https://github.com/lululxvi/deeponet)

## JAX-FEM Notes

- https://arxiv.org/abs/2212.00964
- By default, JAX-FEM solves a Poisson equation. This is not clear from the examples, other than that the Poisson example omits the definition of a Laplacian and only has to construct a right-hand side.
- The code follows a standard FEM code structure by iterating over cells and boundary faces and integrating in the local space with the correct weight.
- In order to solve general equations you need to define a kernel that defines the matrix coefficients. In general this is a discretized version of the form $F(v,x)=RHS$ where $v$ is the residual weight and $x$ is the solution. This is implemented via the `universal_kernel` callback.
  - `universal_kernel(cell_sol_flat, physical_quad_points, cell_shape_grads, cell_JxW,cell_v_grads_JxW,*cell_internal_var)`
  - Parameters:
    - `cell_sol_flat: (num_nodes*vec + ...,)` - The current values of the node solutions. See computed quantities for how to unpack.
    - `physical_quad_points: (num_quads, dim)` - `(x,y[,z])` physical space locations of quadrature points.
    - `cell_shape_grads: (num_quads, num_nodes + ..., dim)` - $\frac{\partial\phi_i}{\partial x_d}$ The derivative of the shape function for each for node $i$.
    - `cell_JxW: (num_vars, num_quads)` - $J$ is the reference to physical space expansion coefficient. $W$ is the reference space quadrature weight.
    - `cell_v_grads_JxW: (num_quads, num_nodes + ..., 1, dim)` - TODO: ???
    - `*cell_internal_var` unrolled into extra parameters than can be used to for other solution vectors
  - Computed quantities:
    - `cell_sol_list=self.unflatten_fn_dof: [(num_nodes, vec), ...]` - A method inherited from the base `Problem` used to reshape the array into something more accessible.
  - Missing quantities:
    - Shape functions
