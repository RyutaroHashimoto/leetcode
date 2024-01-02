#
# @lc app=leetcode id=557 lang=python3
#
# [557] Reverse Words in a String III
#


# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([word[::-1] for word in s.split()])


# @lc code=end

s = "Let's take LeetCode contest"
print(Solution().reverseWords(s))


# long
class Solution:
    def reverseWords(self, s: str) -> str:
        left = 0
        s = list(s)
        for i in range(len(s)):
            if s[i] == " ":
                right = i
                s[left:right] = s[left:right][::-1]
                left = i + 1

        s[left : len(s)] = s[left : len(s)][::-1]

        return "".join(s)
