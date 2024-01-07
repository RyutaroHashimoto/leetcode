#
# @lc app=leetcode id=1512 lang=python3
#
# [1512] Number of Good Pairs
#
from collections import defaultdict
from typing import List


# @lc code=start
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ht = defaultdict(int)
        ans = 0

        for n in nums:
            ans += ht[n]
            ht[n] += 1

        return ans


# @lc code=end
nums = [1, 2, 3]
Solution().numIdenticalPairs(nums)
