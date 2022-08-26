import code_coverage.mymath as mymath
import unittest


class TestAdd(unittest.TestCase):
    def test_add_integer(selfself):
        result = mymath.add(10, 5)
        self.assertEqual(result, 15)

    def test_add_string(self):
        result = mymath.add('flower', 'tree')
        self.assertEqual(result, 'flowertree')

if __name__ == '__main__':
    unittest.main()