#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#
import collections


# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        letters = collections.Counter(magazine)

        for c in ransomNote:
            if c in letters:
                if letters[c] == 0:
                    return False
                else:
                    letters[c] -= 1
            else:
                return False
        return True


# @lc code=end
ransomNote = "aa"
magazine = "aab"
print(Solution().canConstruct(ransomNote, magazine))
