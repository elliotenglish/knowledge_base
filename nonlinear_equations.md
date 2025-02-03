# Non-Linear Equations

There are truly very few non-linear equations we can solve analytically. And doing so is one of those tasks that often requires like and considerable brute force. In a general system of equations, we can only solve linear equations, resorting to complex techniques involving SVDs and other types of expensive methods for the most ill conditioned. More often, to solve general equations we use iterative numerical approximations/linearizations. But many of these methods exploit the solution of more tractable non-linear forms.

## Quadratic Equation

$$ax^2+bx+c=0$$

Solution:

$$x^2+b/ax+c/a=0$$

$$x^2+b/ax=-c/a$$

The trick here is to make it easy to take the square root of each side of the left side of the equation. To do this we add a value to both sides.

Imagine we have $(x+d)^2=x^2+2dx+d^2$, since $2d=b/a$, $d=b/(2a)$ and hence we add $(b/(2a))^2$ to either side. This is refered to as "completing the square".

$$x^2+b/ax+(b/(2a))^2=-c/a+(b/(2a))^2$$

$$(x+b/(2a))^2=-c/a+(b/(2a))^2$$

$$x+b/(2a)=\pm\sqrt{-c/a+(b/(2a))^2}$$

$$x=\pm\sqrt{-c/a+(b/(2a))^2}-b/(2a)$$

$$=\pm\sqrt{-4ac/4a^2+b^2/(4a^2)}-b/(2a)$$

$$=\pm\sqrt{-4ac+b^2}/(2a)-b/(2a)$$

$$=\frac{-b\pm\sqrt{-4ac+b^2}}{2a}$$

Which is the standard quadratic equation solution formula (so called "quadratic equation").

## Cubic Equation

TODO: Cardano formulas