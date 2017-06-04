#!/home/sam/shared-space/linux-system/anaconda3/bin/python

# This script generates matrices and outputs the one whose matching polynomial is closest to a given one.

import sys

import numpy

import stabpoly.bistochastic as bistochastic
import stabpoly.subpermanents as subpermanents

INFINITY = 1e20

degree = variable_count = 3
local_degree = degree # no fixed zeros
# Target MCP coefficients, leading first.
#target_mcp = [1.0, 3.0, 9.0/4, 1.0/4]
target_mcp = [1.0, 3.0, 25.0/12, 1.0/4]

def print_report(matrix, coeffs, dist):
  print('Matrix:\n')
  print('{}\n'.format(matrix))
  print('Target coefficients: {}'.format(target_mcp))
  print('Matrix coefficients: {}'.format(coeffs))
  print('Distance: {}'.format(dist))

# computes the coefficients of the mcp of the product polynomial of a given matrix
def get_mcp(matrix):
  k_max = min(matrix.shape)
  return [1] + [subpermanents.getsubpermanentsum(matrix, k) for k in range(1, k_max + 1)]

def get_sqdist(c1, c2):
  return sum([(x-y)**2 for x,y in zip(c1,c2)])

def get_matrix(base=None):
  new_matrix = bistochastic.generate_matrix(degree, variable_count, max_local_degree=local_degree)
  return new_matrix

def find_close_matrix():
  # generate N polynomials
  NUM_MATRICES = 100000
  best_matrix = None
  best_coeffs = None
  best_dist = INFINITY
  for n in range(NUM_MATRICES):
    matrix = get_matrix(best_matrix)
    mcp = get_mcp(matrix)
    dist = get_sqdist(mcp, target_mcp)
    if dist < best_dist:
      best_matrix = matrix
      best_coeffs = mcp
      best_dist = dist
  print_report(best_matrix, best_coeffs, best_dist**.5)

def compare_matrices():
  matrix = numpy.array([[ 0.53414614, 0.19984595, 0.26600791],
                        [ 0.35242895, 0.42697114, 0.22059991],
                        [ 0.11342491, 0.37318292, 0.51339218]
                        ])
  matrix = numpy.array([[200, 37, 123 ],
                        [ 72,145, 143 ],
                        [ 88,177,  94 ],
                        ]) / 360.0
  matrix = numpy.array([[ 4.3216029 ,  3.24055125,  1.43784585],
                        [ 3.67839459,  2.85943896,  2.46216645],
                        [ 1.0, 2.9, 5.1 ]
                        ]) / 9.0
  matrix = numpy.array([[ 0.4801781 ,  0.36006125,  0.15976065],
         [ 0.40871051,  0.31771544,  0.27357405],
                [ 0.11111139,  0.32222331,  0.56666531]])



  mcp = get_mcp(matrix)
  dist = get_sqdist(target_mcp, mcp)**.5
  print_report(matrix, mcp, dist)

def main():
  if len(sys.argv) > 1:
    compare_matrices()
  else:
    find_close_matrix()

if __name__ == '__main__':
  main()
