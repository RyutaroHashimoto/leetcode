#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#


# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        res = [] * len(nums)

        while left < right:
            l = nums[left] ** 2
            r = nums[right] ** 2

            if l < r:
                res.insert(0, r)
                right -= 1
            elif l >= r:
                res.insert(0, l)
                left += 1

        res.insert(0, nums[left] ** 2)

        return res


# @lc code=end
