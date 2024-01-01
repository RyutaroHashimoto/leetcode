#
# @lc app=leetcode id=2090 lang=python3
#
# [2090] K Radius Subarray Averages
#

from typing import List


# @lc code=start
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if len(nums) <= 2 * k:
            return [-1] * len(nums)
        if k == 0:
            return nums

        avg = [sum(nums[: 2 * k + 1])]

        for i in range(k, len(nums) - k - 1):
            avg.append(avg[-1] - nums[i - k] + nums[i + k + 1])

        return [-1] * k + [i // (2 * k + 1) for i in avg] + [-1] * k


# @lc code=end
nums = [40527, 53696, 10730, 66491]
k = 3
print(Solution().getAverages(nums, k))
