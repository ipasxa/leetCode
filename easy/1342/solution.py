class Solution:
    def number_of_steps(self, num: int) -> int:
        steps = 0
        result = num
        
        while result != 0:
            if result % 2 == 0:
                result = result / 2
            else:
                result = result - 1
            steps += 1

        return steps