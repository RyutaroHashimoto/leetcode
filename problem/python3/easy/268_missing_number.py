#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

from typing import List


# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = set(nums)

        for i in range(len(nums) + 1):
            if i not in nums:
                return i


# @lc code=end

nums = [3, 0, 1]
print(Solution().missingNumber(nums))
