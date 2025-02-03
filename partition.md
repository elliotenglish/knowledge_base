# Meshing

## 1D Partitioning

If we have $N$ points and want to partition them into $M$ segments, there are several strategies.

We can divide $N$ by $M$ to get the number of points per bucket:

$$N=\left\lfloor\frac{N}{M}\right\rfloor M+N\bmod M$$

$$\bar{N}_b=\left\lfloor\frac{N}{M}\right\rfloor$$

$$\hat{N}_b=N\bmod N$$

Option 1 ($O(M)$ bucket size delta):

Naively we can put $\bar{N}_b$ points in the first $M-1$ buckets, and then $\bar{N}_b+\hat{N}_b$ in the last bucket. However this means that the last bucket will have between $\bar{N}_b$ and $\bar{N}_b-1$

However, the issue here is that the last bucket will have a number of points in $[\bar{N}_b,\bar{N}_b+M-1]$. Depending upon the scale of M this can be significant.

Option 2 ($\sout{O(1)}$ $1$ bucket size delta):

Instead what we can do is size the buckets size that the first $\hat{N}_b$ buckets receive an extra point, then the delta in bucket sizes is at most 1.

Given a point at position $i_p\in[0,N-1]$ we can determine the bucket index as follows:

$$i_b(i_p)=\left\{
\begin{matrix}
\frac{i_p}{\bar{N}_b+1} & i_p<\hat{N}_b(\bar{N}_b+1) \\
\bar{N}_b+\frac{i_p-\hat{N}_b(\bar{N}_b+1)}{\bar{N}_b} & otherwise
\end{matrix}\right.$$
