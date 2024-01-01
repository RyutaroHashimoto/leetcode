#
# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
#
# from typing import List


# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        current_sum = sum(nums[0:k])
        ans = current_sum

        for right in range(k, len(nums)):
            current_sum = current_sum - nums[left] + nums[right]
            if ans < current_sum:
                ans = current_sum

            left += 1
        return ans / k


# @lc code=end
