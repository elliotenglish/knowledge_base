## Quaternions

A quaternion is represented as:

$$\mathbf{q}=q_r+q_i\mathbf{i}+q_j\mathbf{j}+q_k\mathbf{k}$$
or
$$\mathbf{q}=\begin{pmatrix}q_r\\q_i\\q_j\\q_k\end{pmatrix}$$

Inverse:

$$q^{-1}=\frac{q_r-q_i\mathbf{i}-q_j\mathbf{j}-q_k\mathbf{j}}{q_r^2+q_i^2+q_j^2+q_k^2}$$

Rotation formula:

$$\begin{pmatrix}\mathbf{p}'\\ 0\end{pmatrix}=q\begin{pmatrix}\mathbf{p}\\ 0\end{pmatrix}q^{-1}$$

## Rodrigues vectors

A Rodrigues vector is a unit axis scaled by the magnitude of the rotation.

$$v=\theta\begin{pmatrix}a_x\\ a_y \\a_z\end{pmatrix}$$

Where $a_x^2+a_y^2+a_z^2=1$.

Rotation formula:

$$\theta=norm(\mathbf{p})$$
$$\mathbf{a}=\mathbf{p}\theta^{-1}$$

$$\mathbf{p}'=cos(\theta)\mathbf{p}+(1-cos(\theta))\mathbf{a}\mathbf{a}^T+sin(\theta)\mathbf{a}\times$$

and the cross product can be expressed as the matrix:

$$\mathbf{a}\times=\begin{pmatrix}0 & -a_z & a_y \\ a_z & 0 & -a_x \\ -a_y & a_x & 0\end{pmatrix}$$

## Quaternions vs Rodrigues vectors

Note that calculating the Rodrigues equation is singular at small rotations and thus would need elimination of the angle terms by rewriting with exponentials. Most codes to simply compute this would use conditionals to avoid rotating at small angles. This poses problems with derivatives. So the quaternion formulation tends to be better as the inverse there is well-defined for all angles.

## Equidistant points on a sphere

It's often useful to have an equal area set of points on a sphere. There is no analytical solution for this. Geodesics produce perhaps the best looking results. However, it requires a recursive computation. Instead, a closed form approximation can be achieved by combining the Fibonacci lattice and the cylindrical equal area projection.

The Fibonacci on the unit ([0,1]^2) is defined as:

$$\vec{x}_i=(\text{mod}(\frac{i}{\phi},1),\frac{i}{n-1}), 0<=i<n$$

Where

$$\phi=\frac{1+\sqrt{5}}{2}$$

Is the golden ratio.

Then we map each pair to the sphere:

$$\vec{\theta}_i=(2\pi x_{i,0},\text{arccos}(1-2x_{i,1}))$$

$$\vec{z}_i=
(\text{cos}\theta_{i,0}\text{sin}\theta_{i,1},
\text{sin}\theta_{i,0}\text{sin}\theta_{i,1},
\text{cos}\theta_{i,1})$$

References:
- https://en.wikipedia.org/wiki/Young%E2%80%93Fibonacci_lattice
- https://en.wikipedia.org/wiki/Cylindrical_equal-area_projection
- https://observablehq.com/@meetamit/fibonacci-lattices

fiblat library:
- https://github.com/erikbrinkman/fibonacci_lattice
