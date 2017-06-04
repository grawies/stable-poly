import unittest
import stabpoly.polynomials as polynomials
import numpy
from sympy import Poly

_EPSILON = 1e-10

class TestPolynomials(unittest.TestCase):

  def test_product_polynomial(self):
    matrix = numpy.array([[2,1],[1,2]])
    polynomial = Poly(polynomials.product_polynomial(matrix))
    syms = polynomials.getvars(count=2)
    true_polynomial = Poly(2 * syms[0] * syms[0] + 5 * syms[0] * syms[1] + 2 * syms[1] * syms[1])
    self.assertEqual(polynomial, true_polynomial)

  def test_matching_polynomial(self):
    matrix = numpy.array([[1,0,0,1],[1,1,0,0],[0,1,1,0],[0,0,1,1]])
    polynomial = polynomials.matching_polynomial(matrix)[0]
    coeffs = polynomial.coeffs()
    coeffs_true = [1, -8, 20, -16, 2]
    mse = sum([(x-y)**2 for x,y in zip(coeffs,coeffs_true)])
    self.assertAlmostEqual(mse, 0, _EPSILON)

  def test_uniform_polynomial_coefficients(self):
    m = 3
    d = 3
    # scaled up: [1,3,2,2/9]
    coeffs_true = [27, 81, 54, 6]
    coeffs = polynomials.get_uniform_polynomial_coefficients(m,d)
    for c,c_true in zip(coeffs, coeffs_true):
      self.assertEqual(c,c_true)

if __name__ == '__main__':
  unittest.main()
