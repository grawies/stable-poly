#!/home/sam/shared-space/linux-system/anaconda3/bin/python

import sympy as sp

# function converging to uniform multiaffine polynomial
def T(poly, symbols, factor=True):
  op = sum(symbols) * sum([poly.diff(s) for s in symbols])
  if factor:
    op = op.factor()
  return op / len(symbols) / sp.Poly(op).total_degree()



from sympy.abc import x,y,z
#p = 7 * x**3 * y **2 * z **2 + 4 * x**2 * z**5
#p = 7 * x**1 * y * z + 4 * x * z**2
#p = 2 * x**2 + 8 * y**2 + 8 * z**2 + 9 * x * y + 9 * x * z + 20 * y * z + 2 * x + 3 * y + 3 * z
#p = x * p

#p = (y + 2*z) * (z + 2*x) * (x + 2*y) * (x + y + z) / 81
p = (y + 2*z) * (z + 2*x) * (x + 2*y) / 27
p = p * p

d = 6
pp = (x + y + z)**d / 3**d
symbols = [x,y,z]

def iterate(q, symbols, valfunc, N):
  print("p_0 =", q)
  print("vf(p_0) =", float( valfunc(q, symbols) ) )
  for i in range(1,N+1):
    q = T(q, symbols)
#    print("p_{} =".format(i), q)
    print("vf(p_{}) =".format(i), float( valfunc(q, symbols) ) )

# should be degree / variable_count for doubly stochastic polynomials
valfunc = lambda p, syms: sp.Poly(p.diff(syms[0]))(*[1 for i in range(len(syms))])

# e_k(delta)-operator evaluated at (1,...,1)
import itertools
def valfunc(p,syms):
  k = 2
  term_seq = itertools.combinations(syms, k)
  res = 0
  for term_syms in term_seq:
    q = p
    for sym in term_syms:
      q = q.diff(sym)
    res += sp.Poly(q, *syms)(*[1 for s in syms])
  return res

def main():
  iterate(p, symbols, valfunc, 60)

if __name__ == '__main__':
  main()
