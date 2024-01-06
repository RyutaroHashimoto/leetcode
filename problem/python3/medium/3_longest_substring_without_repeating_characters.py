#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#


# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        res = 0
        tab = {}

        for right in range(len(s)):
            if s[right] in tab:
                left = max(tab[s[right]], left)

            tab[s[right]] = right + 1
            res = max(res, right - left + 1)

        return res


# @lc code=end
s = "bbbbb"
Solution().lengthOfLongestSubstring(s)
