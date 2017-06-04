# This script computes the coefficients of the matching polynomials of a number of matrices.

import stabpoly.bistochastic as bistochastic
import stabpoly.polynomials as polynomials

def main():
  NUM_MATRICES = 10
  NUM_SYMBOLS = 5
  DEGREE = 4
  print("Generating the coefficients of {} random matching polynomials of {}x{}-matrices.".format(NUM_MATRICES,DEGREE,NUM_SYMBOLS))
  for i in range(NUM_MATRICES):
    matrix = bistochastic.generate_matrix(DEGREE, NUM_SYMBOLS)
    print(polynomials.matching_polynomial(matrix)[0].coeffs())

if __name__ == "__main__":
  main()
