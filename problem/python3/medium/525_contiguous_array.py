#
# @lc app=leetcode id=525 lang=python3
#
# [525] Contiguous Array
#

from typing import List


# @lc code=start
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hash_table = {0: -1}
        count = 0
        max_len = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                count -= 1
            else:
                count += 1

            if count in hash_table:
                max_len = max(max_len, i - hash_table[count])
            else:
                hash_table[count] = i

        return max_len


# @lc code=end
nums = [0, 1, 0]
print(Solution().findMaxLength(nums))
