#Testing and Debugging
def add(a, b):
    return a + b

import unittest

class TestMathOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

if __name__ == '__main__':
    unittest.main()


import pdb

def add(a, b):
    pdb.set_trace()
    return a + b

result = add(2, 3)
