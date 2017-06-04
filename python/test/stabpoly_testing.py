import unittest
import numpy.random

SEED = 1

class TestCase(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    numpy.random.seed(SEED)
