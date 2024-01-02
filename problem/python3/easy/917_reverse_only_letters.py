#
# @lc app=leetcode id=917 lang=python3
#
# [917] Reverse Only Letters
#


# @lc code=start
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        s = list(s)

        while left < right:
            if not s[left].isalpha():
                left += 1
                continue

            if not s[right].isalpha():
                right -= 1
                continue

            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return "".join(s)


# @lc code=end

s = "ab-cd"
print(Solution().reverseOnlyLetters(s))
