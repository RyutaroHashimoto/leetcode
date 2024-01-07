#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#


# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapping_c_w = {}
        mapping_w_c = {}

        s = s.split()

        if len(pattern) != len(s):
            return False

        for c, word in zip(pattern, s):
            if (c not in mapping_c_w) and (word not in mapping_w_c):
                mapping_c_w[c] = word
                mapping_w_c[word] = c
            elif mapping_c_w.get(c) != word or mapping_w_c.get(word) != c:
                return False

        return True


# @lc code=end
