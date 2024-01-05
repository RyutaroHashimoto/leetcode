#
# @lc app=leetcode id=1832 lang=python3
#
# [1832] Check if the Sentence Is Pangram
#


# @lc code=start
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        hash_table = {}
        for c in sentence:
            hash_table[c] = 1

        return len(hash_table) == 26


# @lc code=end

sentence = "leetcode"
print(Solution().checkIfPangram(sentence))
