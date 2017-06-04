#!/usr/bin/python3

# This script computes the number of k-matchings of the Wanless 22x22-matrix graph,
# using a grotesque recursion.

import sys
import fractions

import stabpoly.wanless as wanless

DEF_DEBUG = False

def main():
  matchings = -1
  n1,n2,k = 3,4,22
  # compute the entire matching polynomial:
  if len(sys.argv) == 4 and sys.argv[3] == 'all':
    n1, n2 = int(sys.argv[1]), int(sys.argv[2])
    coeffs = []
    N = 3*(n1 + n2) + 1 # N-N-bipartite graph
    print("Attempting to compute the Wanless matchings ({},{},k) for k in [0, {}]...".format(n1, n2, N))
    print("Done:", end='')
    for k in range(N+1):
      coeffs.append(wanless.WanlessMatchings(n1,n2,k, int_quotient=True))
      print('',k, end='')
      sys.stdout.flush()
    print(".")
    min_coeffs = []
    max_denom = fractions.Fraction(coeffs[-1][0],coeffs[-1][1]).denominator
    for p,q in coeffs:
      x = fractions.Fraction(p,q)
      denom = x.denominator
      #min_coeffs.append((x.numerator * max_denom // denom, max_denom))
      min_coeffs.append(x.numerator * max_denom // denom)
    print("wanless_numerators = ", end='')
    print(min_coeffs, end=';\n')
    print("wanless_denominator = {};".format(max_denom))
  # compute the \sigma_k's of Wanless(n1,n2) for a given k
  elif len(sys.argv) in [1, 4]:
    if len(sys.argv) > 1:
      n1, n2, k = [int(sys.argv[i]) for i in range(1,4)]
    params = (n1, n2, k)
    print("Attempting to compute the Wanless matchings {}...".format(params))
    matchings = wanless.WanlessMatchings(n1, n2, k)
    print("Result: {}".format(matchings))
  elif len(sys.argv) == 5:
    if sys.argv[4] == 'quotient':
      n1, n2, k = [int(sys.argv[i]) for i in range(1,4)]
      N = 3*(n1 + n2) + 1
      matchings_hi = wanless.WanlessMatchings(n1,n2,k)
      matchings_lo = wanless.WanlessMatchings(n1,n2,k-1)
      print('Wanless quotient ({},{},{}) sig{}/sig{} = {}'.format(n1,n2,k,k,k-1,matchings_lo/matchings_hi))
      print('Compare to N*k/(N-k+1)^2 = {}'.format(N*k/(N-k+1)**2))
  else:
    print("Unsupported parameters.")

if __name__ == "__main__":
  main()
