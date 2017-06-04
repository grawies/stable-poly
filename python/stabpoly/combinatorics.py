#!/home/sam/shared-space/linux-system/anaconda3/bin/python

from sys import stderr

import numpy as np
import numpy.random

# generates an integer <rows>x<cols> numpy matrix with <degree> ones per column and no all-zero rows
# suitable for doubly stochastic locally degree-bound polynomials
def getzeros(rows, cols, degree=0):
  matrix = np.zeros((rows, cols), dtype=np.int64)
  if degree == 0:
    return matrix
  if degree > cols:
    print('error! too few columns to adher to degree specifications.', file=stderr)
    print('undefined behavior.', file=stderr)
  # ensure columns are non-zero
  first_nonzeros = random_bounded_choice(rows, cols, degree)
  for i,j in enumerate(first_nonzeros):
    matrix[i][j] = 1
  # randomize the remaining column elements
  ones = matrix.sum(axis=0)
  for j in range(cols):
    col_ones = ones[j]
    if col_ones == degree:
      continue
    # randomly pick the remaining <degree> - <col_ones> elements
    zeros = np.where(matrix[:,j] == 0)[0]
    remaining_ones = numpy.random.choice(zeros, degree - col_ones, replace=False)
    for i in remaining_ones:
      matrix[i,j] = 1
  return matrix

# distribute <balls> balls into <bins> bins with at most <bound[i]> balls in bin[i]
# returns ordered choices
def random_bounded_choice(balls, bins, bounds):
  if type(bounds) == int:
    bounds = [bounds] * bins
  if sum(bounds) < balls:
    print('error! too many balls to adher to bound specification.', file=stderr)
    print('undefined behavior.', file=stderr)
  unmaxed = [i for i in range(bins)]
  unmaxed_count = bins
  bin_counts = [0] * bins
  choices = []
  for i in range(balls):
    choice = int(numpy.random.random()*unmaxed_count)
    choice_bin = unmaxed[choice]
    choices.append(choice_bin)
    bin_counts[choice_bin] += 1
    if bin_counts[choice_bin] >= bounds[choice_bin]:
      unmaxed.remove(choice_bin)
      unmaxed_count -= 1
  return choices 
