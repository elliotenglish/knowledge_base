import sympy

def fit_polynomial_monotonic():
  """
  Currently this just fits a cubic to 2 points, and their derivatives.
  
  TODO: Make it monotic. Some notes are here:
  https://stellar.mit.edu/S/course/6/sp10/6.256/courseMaterial/topics/topic2/lectureNotes/lecture-10/lecture-10.pdf
  """

  x,a,b,c,d,T0,T1=sympy.symbols("x a b c d T0 T1")
  p0,dp0,p1,dp1=sympy.symbols("p0 dp0 p1 dp1")

  y=a*x**3+b*x**2+c*x+d
  dy=sympy.diff(y,x)

  print(y.subs(x,0))

  system=[
    sympy.Eq(y.subs(x,T0),p0),
    sympy.Eq(dy.subs(x,T0),dp0),
    sympy.Eq(y.subs(x,T1),p1),
    sympy.Eq(dy.subs(x,T1),dp1)]
  print(system)

  sol=sympy.solve(system,
    [a,b,c,d])
  print(sol)

  print(y)
  ysol=y.subs([
    (a,sol[a]),
    (b,sol[b]),
    (c,sol[c]),
    (d,sol[d])])
  ynum=ysol.subs([
    (p0,0),
    (dp0,0),
    (p1,1),
    (dp1,10),
    (T0,0),
    (T1,1)])
  print(ynum)
  p1=sympy.plot(ynum,xlim=(0,1),ylim=(-1,2),backend="matplotlib")

if __name__=="__main__":
  fit_polynomial_monotonic()
