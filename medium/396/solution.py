from typing import List


class Solution:

    def max_rotate_function(self, nums: List[int]) -> int:
        f_n, n = 0, len(nums)

        for i in range(n):
            f_n += i * nums[i]

        max_n = f_n
        total = sum(nums)

        for i in range(1, n):
            f_n = total - n * nums[-i] + f_n
            max_n = max(max_n, f_n)

        return max_n
