import unittest

class TestDemo(unittest.TestCase):

  def test_demotest(self):
    self.assertTrue(1 == int('1'))

if __name__ == '__main__':
  unittest.main()
