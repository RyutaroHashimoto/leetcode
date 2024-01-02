#
# @lc app=leetcode id=1456 lang=python3
#
# [1456] Maximum Number of Vowels in a Substring of Given Length
#


# @lc code=start
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        current_sum = 0
        for i in s[:k]:
            if i in "aeiou":
                current_sum += 1
        res = current_sum

        for right in range(k, len(s)):
            if s[right - k] in "aeiou":
                current_sum -= 1

            if s[right] in "aeiou":
                current_sum += 1

            res = max(res, current_sum)

        return res


# @lc code=end
