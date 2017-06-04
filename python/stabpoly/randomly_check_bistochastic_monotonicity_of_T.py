#!/home/sam/shared-space/linux-system/anaconda3/bin/python

import math
import sympy as sp
from bistochastic import generate_matrix
import fpiter
from polynomials import product_polynomial
from functionals import elementary_symmetric_differential_operator
import numpy.random

SEED = 1
numpy.random.seed(SEED)

ITERATIONS = 5
NUM_SYMBOLS = [3]
DEGREES = [3]
NUM_MATRICES_PER_ITER = 30

###############################################################
# Iterates over different numbers of variable and degrees,    #
# generating doubly stochastic stable homogeneous polynomials #
# which are tested for convergence of iterated operator       #
###############################################################
def main():
  valid_matrices = 0
  for symbol_count in NUM_SYMBOLS:
    symbols = fpiter.getvars(count=symbol_count)
    for degree in DEGREES:
      for i in range(NUM_MATRICES_PER_ITER):
        # generate and check a polynomial
        valid = test_matrix(symbols, degree)
        if valid:
          valid_matrices += 1
  print('Done!')
  print('Valid matrices: {}/{}.'.format(valid_matrices, NUM_MATRICES_PER_ITER * len(NUM_SYMBOLS) * len(DEGREES)))


def test_matrix(symbols, degree):
  valfuncT = lambda p: elementary_symmetric_differential_operator(fpiter.T(p,symbols), DEGREE, symbols)
  valfuncTcalc = lambda p: DEGREE**(-2) * elementary_symmetric_differential_operator(p, DEGREE-1, symbols)
  valfunc = lambda p: elementary_symmetric_differential_operator(p, DEGREE, symbols)

  # get a matrix
  A = generate_matrix(degree, len(symbols))
  # get the polynomial
  p = product_polynomial(A)
  # compute values
  k = min(degree, len(symbols))
  k = 2
  functional = lambda p: elementary_symmetric_differential_operator(p, k, symbols)
  values = [functional(p)]
  q = p
  for i in range(ITERATIONS):
    q = fpiter.T(q, symbols, factor=False)
    values.append(functional(q))
  # evaluate values
  # TODO really evaluate if it's good
  min_val = math.factorial(degree) / math.pow(degree, degree)
  diffs = [values[i]-min_val for i in range(ITERATIONS)]
  quots = [diffs[i]/diffs[i+1] for i in range(ITERATIONS-1)]
  print(values, ';')
#  print(diffs)
  print(quots)
#  print(min_val)
  return all([diff > 0 for diff in diffs])

if __name__ == '__main__':
  main()
