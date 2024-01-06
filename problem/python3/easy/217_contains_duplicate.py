#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#


# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return False if len(set(nums)) == len(nums) else True


# @lc code=end
