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
  NUM_MATRICES = 30
  NUM_SYMBOLS = 3
  DEGREE = 3
  symbols = fpiter.getvars(count=NUM_SYMBOLS)
  valfunc = lambda p: elementary_symmetric_differential_operator(p, DEGREE, symbols)
  # test a bunch of matrices
  minval = 1e10
  minimizer = 0
  for i in range(NUM_MATRICES):
    # get a matrix
    A = generate_matrix(DEGREE, NUM_SYMBOLS)
    # get the polynomial
    p = product_polynomial(A)
    # compute value
    val = valfunc(p)
    # check if new minimum
    if val < minval:
      minval = val
      minimizer = A
    print('test {}: val = {}'.format(i+1, val))
  # report
  minval_theory = factorial(NUM_SYMBOLS) / NUM_SYMBOLS**NUM_SYMBOLS
  print('theoretical minimum val = {}'.format(minval_theory))
  print('computed min val        = {}'.format(minval))
  print('minimizer:')
  print(minimizer)

if __name__ == '__main__':
  main()
