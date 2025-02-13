# Statistics

## Entropy

The entropy $H$ of a probability distribution $X$ is defined as:

$$H(X)=-\sum_{x\sim X} P(x)\textbf{log}P(x)$$

$H(X)$ is at a maximum when $P(x_i)=\delta_{i,j}$ for some $j$. i.e. when only a single point is occurs all the time. It's a minimum when $P(x_i)=\frac{1}{|H|}$.

e.g.

$P(a)=.5$, $P(b)=.5$

$H(X)=-(.5\textbf{log}_2(.5)+.5\textbf{log}_2(.5))=-(.5*-1+.5*-1)=1$

$P(a)=1$, $P(b)=0$

$H(X)=-(1\textbf{log}_2(1)+0\textbf{log}_2(0))=???$ (not well defined)

$P(a)=3/4$, $P(b)=1/4$

$H(X)=-(3/4\textbf{log}_2(3/4)+1/4\textbf{log}_2(1/4))=.5515...$
