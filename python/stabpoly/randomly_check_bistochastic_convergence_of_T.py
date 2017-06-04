#!/home/sam/shared-space/linux-system/anaconda3/bin/python

from math import factorial
import sympy as sp
from bistochastic import generate_matrix
import fpiter
from polynomials import product_polynomial
from functionals import elementary_symmetric_differential_operator
import numpy.random

SEED = 1
numpy.random.seed(SEED)

def main():
  NUM_MATRICES = 300
  NUM_SYMBOLS = DEGREE = 3
  symbols = fpiter.getvars(count=NUM_SYMBOLS)
  valfuncT = lambda p: elementary_symmetric_differential_operator(fpiter.T(p,symbols), DEGREE, symbols)
  valfuncTcalc = lambda p: DEGREE**(-2) * elementary_symmetric_differential_operator(p, DEGREE-1, symbols)
  valfunc = lambda p: elementary_symmetric_differential_operator(p, DEGREE, symbols)

  # test a bunch of matrices
  minval = 1e10
  minimizer = 0
  for i in range(NUM_MATRICES):
    # get a matrix
    A = generate_matrix(DEGREE, NUM_SYMBOLS)
    # get the polynomial
    p = product_polynomial(A)
    # compute values
    val = (valfuncT(p), valfuncTcalc(p)/ valfunc(p),0)
    # check if new minimum
#    if val < minval:
#      minval = val
#      minimizer = A
    print('test {num:02d}: vals = {}\t{}\t{}'.format(num=i+1, *val))
  # report
#  minval_theory = factorial(NUM_SYMBOLS) / NUM_SYMBOLS**NUM_SYMBOLS
#  print('theoretical minimum val = {}'.format(minval_theory))
#  print('computed min val        = {}'.format(minval))
#  print('minimizer:')
#  print(minimizer)

if __name__ == '__main__':
  main()
