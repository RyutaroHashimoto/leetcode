#
# @lc app=leetcode id=2958 lang=python3
#
# [2958] Length of Longest Subarray With at Most K Frequency
#
from collections import defaultdict
from typing import List


# @lc code=start
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ht = defaultdict(int)
        res = 0
        left = 0

        for right in range(len(nums)):
            ht[nums[right]] += 1

            while ht[nums[right]] > k:
                ht[nums[left]] -= 1
                left += 1

            res = max(right - left + 1, res)

        return res


# @lc code=end
nums = [5, 5, 5, 5, 5, 5, 5]
k = 4
Solution().maxSubarrayLength(nums, k)
