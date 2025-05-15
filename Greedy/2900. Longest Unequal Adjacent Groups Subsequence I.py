# Approach Using normal check
# T.C : O(n)
# S.C : O(1)

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        ans = [words[0]]
        prev = groups[0]
        for i in range(1,n):
            if groups[i]!=prev:
                prev = groups[i]
                ans.append(words[i])
        return ans
        


