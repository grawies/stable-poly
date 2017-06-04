import unittest
import stabpoly.wanless as wanless

class TestWanless(unittest.TestCase):

  def test_wanless_necklace(self):
    matchings = wanless.NecklaceMatchings(1,3)
    matchings_true = 20
    self.assertEqual(matchings, matchings_true)

  def test_wanless_matchings(self):
    subpermanent,_ = wanless.WanlessMatchings(3,4,21,int_quotient=True)
    subpermanent_true = 143644347 * 2**23
    self.assertEqual(subpermanent, subpermanent_true)

if __name__ == '__main__':
  unittest.main()
