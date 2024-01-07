#
# @lc app=leetcode id=1695 lang=python3
#
# [1695] Maximum Erasure Value
#
from typing import List


# @lc code=start
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # Using prefix sum and hash
        prefix_sum = [0]
        for n in nums:
            prefix_sum.append(prefix_sum[-1] + n)

        ans = 0
        left = 0
        index_map = {}
        for right in range(len(nums)):
            if nums[right] in index_map:
                left = max(left, index_map[nums[right]] + 1)

            ans = max(ans, prefix_sum[right + 1] - prefix_sum[left])
            index_map[nums[right]] = right

        return ans


# @lc code=end
nums = [4, 2, 4, 5, 6]
Solution().maximumUniqueSubarray(nums)


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # Using two pointer and set
        left = 0
        prefix = set()
        prefixsum = 0
        ans = 0

        for i in range(len(nums)):
            if nums[i] in prefix:
                while nums[i] in prefix:
                    prefix.remove(nums[left])
                    prefixsum -= nums[left]
                    left += 1

            prefix.add(nums[i])
            prefixsum += nums[i]
            ans = max(ans, prefixsum)

        return ans
