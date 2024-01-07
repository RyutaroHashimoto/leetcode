#
# @lc app=leetcode id=930 lang=python3
#
# [930] Binary Subarrays With Sum
#
from collections import defaultdict
from typing import List


# @lc code=start
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ans = 0
        prefix = 0
        count = defaultdict(int)
        count[0] = 1

        for n in nums:
            prefix += n
            ans += count[prefix - goal]
            count[prefix] += 1

        return ans


# @lc code=end
nums = [1, 0, 1, 0, 1]
goal = 2

Solution().numSubarraysWithSum(nums, goal)
