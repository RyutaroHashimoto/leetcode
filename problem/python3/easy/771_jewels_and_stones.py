#
# @lc app=leetcode id=771 lang=python3
#
# [771] Jewels and Stones
#


# @lc code=start
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_set = set(jewels)
        res = 0

        for s in stones:
            if s in jewels_set:
                res += 1

        return res


# @lc code=end
