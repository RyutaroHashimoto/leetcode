#
# @lc app=leetcode id=2000 lang=python3
#
# [2000] Reverse Prefix of Word
#


# @lc code=start
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        word = list(word)

        left = 0
        for right in range(len(word)):
            if word[right] == ch:
                while left < right:
                    word[left], word[right] = word[right], word[left]
                    left += 1
                    right -= 1
                break

        return "".join(word)


# @lc code=end

word = "abcd"
ch = "z"

print(Solution().reversePrefix(word, ch))
