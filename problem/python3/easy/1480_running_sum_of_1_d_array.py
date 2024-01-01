#
# @lc app=leetcode id=1480 lang=python3
#
# [1480] Running Sum of 1d Array
#


# @lc code=start
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = [nums[0]]
        for i in range(1, len(nums)):
            runningSum.append(nums[i] + runningSum[i - 1])

        return runningSum


# @lc code=end
