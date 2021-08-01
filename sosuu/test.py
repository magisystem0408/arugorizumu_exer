# ユニットテスト
import unittest
from sosuu02 import is_prime_v1 as is_prime

class PrimeTest(unittest.TestCase):

    def test_is_prime_ok(self):
        for i in [2,3,4,5,6,76,7]:
            self.assertTrue(is_prime(i))

    def test_is_prime_no(self):
        for i in [21,235,142,53,123]:
            self.assertFalse(is_prime(i))

    def test_is_prime_negative(self):
        self.assertFalse(is_prime(-1))


    def test_is_prime_raise_typeerror(self):
        with self.assertRaises(TypeError):
            is_prime('string')

if __name__ == '__main__':
    unittest.main()