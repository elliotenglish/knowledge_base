import sympy

def fit_polynomial_monotonic():
  x,a,b,c,d,T=sympy.symbols("x a b c d T")
  p0,dp0,pT,dpT=sympy.symbols("p0 dp0 pT dpT")

  y=a*x**3+b*x**2+c*x+d
  dy=sympy.diff(y,x)

  print(y.subs(x,0))

  system=[
    sympy.Eq(y.subs(x,0),p0),
    sympy.Eq(dy.subs(x,0),dp0),
    sympy.Eq(y.subs(x,T),pT),
    sympy.Eq(dy.subs(x,T),dpT)]
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
    (pT,1),
    (dpT,2),
    (T,1)])
  print(ynum)
  p1=sympy.plot(ynum,xlim=(0,1),ylim=(-.1,1.1),backend="matplotlib")

if __name__=="__main__":
  fit_polynomial_monotonic()
