from Calculator import Calculator
import unittest

class CalculatorTests(unittest.TestCase):
   def test_add (self): 
    calc = Calculator() 
    self.assertEqual(10, calc.add (7, 3))

if __name__ == '__main__':
    unittest.main()