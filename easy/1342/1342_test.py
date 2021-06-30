import unittest
from solution import Solution

class Tests1342(unittest.TestCase):

    def setUp(self) -> None:
        self.solution = Solution()

    def test0(self):
        self.assertEqual(self.solution.number_of_steps(0), 0)

    def test14(self):
        self.assertEqual(self.solution.number_of_steps(14), 6)

    def test8(self):
        self.assertEqual(self.solution.number_of_steps(8), 4)

    def test123(self):
        self.assertEqual(self.solution.number_of_steps(123), 12)

if __name__ == '__main__':
    unittest.main()