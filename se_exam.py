"doc string"
import unittest
import math

def my_ldexp(entry_x, entry_i):
    'use only lists'
    if not entry_x:
        raise TypeError("x cannot be empty")
    if not entry_i:
        raise TypeError("i cannot be empty")
    if not isinstance(entry_x, int):
        raise TypeError("Input should be int")
    if not isinstance(entry_i, int):
        raise TypeError("Input should be int")
    return math.ldexp(entry_x, entry_i)

class TestIdexpMath(unittest.TestCase):
    "class to test custom idexp function"

    def test_correct_param(self):
        "correct params"
        expected = 72.0
        test_data_x = 9
        test_data_i = 3
        self.assertEqual(math.ldexp(test_data_x, test_data_i), expected)
        self.assertEqual(my_ldexp(test_data_x, test_data_i), expected)

    def test_empty_param(self):
        "empty params"
        with self.assertRaises(TypeError):
            self.assertEqual(my_ldexp(), True)

    def test_missing_param(self):
        "missing params"
        test_data_x = 9
        with self.assertRaises(TypeError):
            self.assertEqual(my_ldexp(test_data_x), True)

    def test_wrong_param_type(self):
        "wrong params"
        with self.assertRaises(TypeError) as err:
            my_ldexp("test")
        with self.assertRaises(TypeError) as err:
            my_ldexp([])


if __name__ == '__main__':
    unittest.main()
