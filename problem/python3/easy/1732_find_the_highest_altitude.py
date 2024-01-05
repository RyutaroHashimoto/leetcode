#
# @lc app=leetcode id=1732 lang=python3
#
# [1732] Find the Highest Altitude
#


# @lc code=start
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        pre_sum = [0]
        for i in range(len(gain)):
            pre_sum.append(pre_sum[-1] + gain[i])

        return max(pre_sum)


# @lc code=end
