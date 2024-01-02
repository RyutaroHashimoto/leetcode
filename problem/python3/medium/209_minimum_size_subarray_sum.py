#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#
from typing import List


# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = 10**5
        left = 0
        current_sum = 0

        if sum(nums) < target:
            return 0

        for right in range(len(nums)):
            current_sum += nums[right]
            while current_sum >= target:
                res = min(res, right + 1 - left)
                current_sum -= nums[left]
                left += 1

        return res


# @lc code=end
