#
# @lc app=leetcode id=1748 lang=python3
#
# [1748] Sum of Unique Elements
#

import collections
from typing import List


# @lc code=start
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        res = 0

        for key, value in count.items():
            if value == 1:
                res += key
            continue

        return res


# @lc code=end
nums = [1, 2, 3, 2]
Solution().sumOfUnique(nums)
