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
