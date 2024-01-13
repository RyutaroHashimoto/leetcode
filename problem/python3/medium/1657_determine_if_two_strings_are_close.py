#
# @lc app=leetcode id=1657 lang=python3
#
# [1657] Determine if Two Strings Are Close
#


# @lc code=start
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        if set(word1) != set(word2):
            return False

        clunts_1 = collections.Counter(word1)
        clunts_2 = collections.Counter(word2)
        for i, j in zip(clunts_1.most_common(), clunts_2.most_common()):
            if i[1] != j[1]:
                return False
        return True


# @lc code=end
