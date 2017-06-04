#!/home/sam/shared-space/linux-system/anaconda3/bin/python

import sympy
from sympy.abc import x,y,z,u,v

#p = 7 * x**3 * y **2 * z **2 + 4 * x**2 * z**5
#p = 7 * x**1 * y * z + 4 * x * z**2
p = 2 * x**2 + 8 * y**2 + 8 * z**2 + 9 * x * y + 9 * x * z + 20 * y * z + 2 * x + 3 * y + 3 * z
p = x * p

#pp = (x + y + z)**7
pp = (x + y + z)**3

def T(poly):
  op = (x + y + z) * (poly.diff(x) + poly.diff(y) + poly.diff(z)).factor()
  return op / 3 / sympy.Poly(op).degree()

def pval(poly):
  return sympy.Poly(poly).as_expr().coeff(x*y*z)

def iterate(q, N):
  print("p_0 =", q)
  print("[p_0]_c =", float( pval(q) ) )
  for i in range(N):
    q = T(q)
    print("p_i =", q)
    print("[p_i]_c =", float( pval(q) ) )
 
iterate(p, 10)
