import sympy

def fit_polynomial_monotonic():
  """
  Currently this just fits a cubic to 2 points, and their derivatives.
  
  TODO: Make it monotic. Some notes are here:
  https://stellar.mit.edu/S/course/6/sp10/6.256/courseMaterial/topics/topic2/lectureNotes/lecture-10/lecture-10.pdf
  """

  x,a,b,c,d,T0,T1=sympy.symbols("x a b c d T0 T1")
  p0,dp0,p1,dp1=sympy.symbols("p0 dp0 p1 dp1")

  m=1
  y=a*x**(0*m)+b*x**(1*m)+c*x**(2*m)+d*x**(3*m)
  print(f"y={y}")
  dy=sympy.diff(y,x)
  print(f"dy={dy}")

  system=[
    sympy.Eq(y.subs(x,T0),p0),
    sympy.Eq(dy.subs(x,T0),dp0),
    sympy.Eq(y.subs(x,T1),p1),
    sympy.Eq(dy.subs(x,T1),dp1)]
  print(f"system={system}")

  sol=sympy.solve(system,
    [a,b,c,d])
  print(f"solution={sol}")
  
  p0_target=0
  dp0_target=0
  p1_target=1
  dp1_target=1 #10 will make the solution non-monotonic
  T0_target=0
  T1_target=1

  ysol=y.subs([
    (a,sol[a]),
    (b,sol[b]),
    (c,sol[c]),
    (d,sol[d]),
    (p0,p0_target),
    (dp0,dp0_target),
    (p1,p1_target),
    (dp1,dp1_target),
    (T0,T0_target),
    (T1,T1_target)])
  print(ysol)

  # Find roots of derivative
  root_sol=sympy.solve(sympy.Eq(sympy.diff(ysol,x),0),x)
  print(f"root_sol={root_sol}")

  for xr in root_sol:
    if xr>T0_target and xr<T1_target:
      print("non monotonic!")

  # Plot function
  p1=sympy.plot(ysol,xlim=(0,1),ylim=(-1,2),backend="matplotlib")

if __name__=="__main__":
  fit_polynomial_monotonic()
