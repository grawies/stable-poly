import stabpoly_testing

import unittest
import numpy

import stabpoly.subpermanents as subpermanents

_EPSILON = 1e-10

class TestPermanents(stabpoly_testing.TestCase):

  def test_subpermanents(self):
    A = numpy.array([[0.5,0,0,1],[1,1,0,0],[0,1,1,0],[0,0,1,1]])
    sigma2 = subpermanents.getsubpermanentsum(A, 2)
    sigma2_true = 17.5
    self.assertAlmostEqual(sigma2, sigma2_true, _EPSILON)

if __name__ == '__main__':
  unittest.main()
