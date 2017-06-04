import unittest
import stabpoly.combinatorics as combinatorics
import stabpoly.bistochastic as bistochastic
import numpy
import stabpoly_testing

_EPSILON = 1e-10
cols_list = [3, 7, 5, 2]
rows_list = [3, 5, 8, 2]
degree_list = [3, 4, 4, 1]

class TestBistochastic(stabpoly_testing.TestCase):

  def test_generate_matrix(self):
    for cols,rows,degree in zip(cols_list,rows_list,degree_list):
      matrix = bistochastic.generate_matrix(rows, cols, max_local_degree=degree)
      # check degrees
      self._verify_zeros(matrix, rows, cols, degree)
      # check column and row sums (double stochasticity)
      true_colsum = rows/cols
      true_rowsum = 1.0
      self.assertAlmostEqual(max(abs(matrix.sum(axis=0) - true_colsum)), 0, delta=_EPSILON)
      self.assertAlmostEqual(max(abs(matrix.sum(axis=1) - true_rowsum)), 0, delta=_EPSILON)
    
  def test_getzeros(self):
    for cols,rows,degree in zip(cols_list,rows_list,degree_list):
      matrix = combinatorics.getzeros(rows,cols,degree)
      self._verify_zeros(matrix, rows, cols, degree)

  def _verify_zeros(self, matrix, rows, cols, degree):
    bin_matrix = (abs(matrix) > _EPSILON).astype(numpy.int64)
    cols_have_degree_ones = bin_matrix.sum(axis=0) == degree
    self.assertTrue(all(cols_have_degree_ones))
    rowsum_is_zero = bin_matrix.sum(axis=1) == 0 
    self.assertFalse(any(rowsum_is_zero))

if __name__ == '__main__':
  unittest.main()
