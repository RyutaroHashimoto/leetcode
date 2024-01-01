#
# @lc app=leetcode id=1413 lang=python3
#
# [1413] Minimum Value to Get Positive Step by Step Sum
#

from typing import List


# @lc code=start
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix_sum = [nums[0]]

        for i in range(1, len(nums)):
            prefix_sum.append(nums[i] + prefix_sum[-1])

        return max(min(prefix_sum) * -1 + 1, 1)


# @lc code=end

nums = [1, -2, -3]

Solution().minStartValue(nums)
