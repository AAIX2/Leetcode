# Approach (straight forward traversal)
# T.C : O(n)
# S.C : O(1)

class Solution:
    def possibleStringCount(self, word: str) -> int:
        count = 0
        for i in range(1, len(word)):
            if word[i] == word[i - 1]:
                count += 1
        return count + 1  # +1 for when Alice does no long press