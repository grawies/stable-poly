#!/home/sam/shared-space/linux-system/anaconda3/bin/python

from sys import stderr

import numpy as np
import numpy.random

import stabpoly.combinatorics as combinatorics

# do not iterate alterating projection more than MAX_ITER times
MAX_ITER = 100
EPSILON = 1e-12

# generats a bistochastic matrix with the given dimensions
def generate_matrix(rows, cols, max_local_degree=None, func_getzeros=combinatorics.getzeros):
  # default to no degree bound
  if max_local_degree == None:
    max_local_degree = cols
  if rows == 0 or cols == 0 or max_local_degree == 0:
    print('Error! Too small outcome space defined. Reconsider matrix dimensions or nonzero entry count.', file=stderr)
    print('Undefined behavior.', file=stderr)
  matrix = numpy.random.uniform(size=(rows, cols))
  # cap the maximum degrees
  if max_local_degree < cols:
    zeros = func_getzeros(rows, cols, max_local_degree)
    matrix = np.multiply(matrix, zeros)
  # iterate alternating normalization
  rowsum = 1
  colsum = rows/cols
  converged = False
  for i in range(MAX_ITER):
    # normalize columns
    matrix = colsum * matrix / matrix.sum(axis=0).reshape(1,cols)
    # normalize rows
    matrix = matrix / matrix.sum(axis=1).reshape(rows,1)
    if max(abs(matrix.sum(axis=0) - colsum)) < EPSILON and max(abs(matrix.sum(axis=1)-1)) < EPSILON:
      converged = True
      break
  if not converged:
    print('Error! Sinkhorn algorithm did not converge to double stochastic matrix.', file=stderr)
    print('Undefined behavior.', file=stderr)
    error = max(max(abs(matrix.sum(axis=0) - colsum)), max(abs(matrix.sum(axis=1)-1)))
    print('error: {}\nmatrix: {}\n'.format(error, matrix), file=stderr)
  return matrix

