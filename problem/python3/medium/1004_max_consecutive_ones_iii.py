#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#

from typing import List


# @lc code=start
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0

        for right in range(len(nums)):
            k -= 1 - nums[right]
            if k < 0:
                k += 1 - nums[left]
                left += 1

        return right - left + 1


# @lc code=end
nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2


c = Solution()
c.longestOnes(nums, k)
