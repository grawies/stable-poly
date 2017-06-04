#!/home/sam/shared-space/linux-system/anaconda3/bin/python

import sympy as sp
import itertools

# e_k(delta)-operator evaluated at (1,...,1)
def elementary_symmetric_differential_operator(p,k,syms):
  term_seq = itertools.combinations(syms, k)
  res = 0
  for term_syms in term_seq:
    q = p
    for sym in term_syms:
      q = q.diff(sym)
    res += sp.Poly(q, *syms)(*[1 for s in syms])
  return res

