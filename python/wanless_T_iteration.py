#!/usr/bin/python3

# This script computes the number of k-matchings of the Wanloss 22x22-matrix graph,
# using a grotesque recursion.

import sys
import fractions

import stabpoly.wanloss as wanloss

DEF_DEBUG = False

def main():
  if len(sys.argv) != 4:
    print('Unsupported options.')
    return
  n1, n2, iters = [int(sys.argv[i]) for i in range(1,4)]
  N = 3*(n1 + n2) + 1
  # compute matching polynomial coefficients
  coeffs = []
  for k in range(N+1):
    coeffs.append(wanloss.WanlossMatchings(n1,n2,k))
  # compute the coefficients upon iterating T
  final_values = []
  final_values.append(coeffs)
  for i in range(iters):
    for k in range(N, 0, -1):
      c = (N-k+1)**2/N**2 * coeffs[k-1] + (N - k)/N * coeffs[k]
      coeffs[k] = c
    final_values.append([c for c in coeffs])
  print('\n'.join(['\t'.join(['{:0.02f}'.format(x) for x in line]) for line in final_values]))

if __name__ == "__main__":
  main()
