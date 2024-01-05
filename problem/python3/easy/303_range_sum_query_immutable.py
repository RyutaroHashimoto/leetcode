#
# @lc app=leetcode id=303 lang=python3
#
# [303] Range Sum Query - Immutable
#

from typing import List


# @lc code=start
class NumArray:
    def __init__(self, nums: List[int]):
        self.pre_sum = [0]
        for i in range(0, len(nums)):
            self.pre_sum.append(self.pre_sum[-1] + nums[i])

    def sumRange(self, left: int, right: int) -> int:
        return self.pre_sum[right + 1] - self.pre_sum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end

c = NumArray([-2, 0, 3, -5, 2, -1])
print(c.sumRange(0, 2))
