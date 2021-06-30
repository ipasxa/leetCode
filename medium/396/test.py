import unittest
from solution import Solution

class Tests(unittest.TestCase):

    def setUp(self) -> None:
        self.solution = Solution()

    def test1(self):
        self.assertEqual(self.solution.max_rotate_function([4, 3, 2, 6]), 26)

    def test2(self):
        self.assertEqual(self.solution.max_rotate_function([1000000007]), 0)

if __name__ == '__main__':
    unittest.main()