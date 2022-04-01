import unittest
from nina import Prob

params = [1,2]
energy = [3,4]
prob = Prob(params=params,func = lambda x: x)

class TestProb(unittest.TestCase):
  
    def test_prob_params(self):
        self.assertEqual( prob.params, params)
    def test_prob_calculate(self):
        self.assertEqual( prob.calculate(energy), energy)

if __name__ == '__main__':
    unittest.main()