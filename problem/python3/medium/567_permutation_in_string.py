#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#


# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = collections.Counter(s1)

        for i in range(len(s1), len(s2) + 1):
            if collections.Counter(s2[i - len(s1) : i]) == s1_count:
                return True

        return False


# @lc code=end
s1 = "adc"
s2 = "dcda"
Solution().checkInclusion(s1, s2)
