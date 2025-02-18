# Approach-1 (Using Brute Force)
# T.C : O(n*q)
# S.C : O(1)


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        vowels = {"a","e","i","o","u"}
        ans = []
        for l,r in queries:
            cnt = 0
            for j in range(l,r+1):
                if words[j][0] in vowels and words[j][-1] in vowels:
                    cnt+=1
            ans.append(cnt)
        return ans

# Approach-1 (Using Prefix Sum)
# T.C : O(n+q)
# S.C : O(n)

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        vowels = {"a","e","i","o","u"}
        prefixSum = [0]*(n+1)
        for i in range(n):
            prefixSum[i+1] = prefixSum[i]
            if words[i][0] in vowels and words[i][-1] in vowels:
                prefixSum[i+1]+=1
        ans = []
        for l,r in queries:
            ans.append(prefixSum[r+1]-prefixSum[l])
        return ans