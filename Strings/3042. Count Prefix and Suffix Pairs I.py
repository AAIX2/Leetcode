# Approach-1 (Using Brute Force)
# T.C : O(n**2*m)
# S.C : O(1)


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)
        def isPrefixAndSuffix(w1,w2):
            
            i = 0
            j = 0
            while i<len(w1) and j<len(w2):
                if w1[i]!=w2[j]:
                    break
                else:
                    i+=1
                    j+=1
            ans = (i == len(w1))
            i = len(w1)-1
            j = len(w2)-1
            while i>=0 and j>=0:
                if w1[i]!=w2[j]:
                    break
                else:
                    i-=1
                    j-=1
            ans = ans and (i<0)
            return ans

        cnt = 0
        for i in range(n):
            for j in range(i+1,n):
                if isPrefixAndSuffix(words[i],words[j]):
                    cnt+=1
        return cnt
    

# Approach-2 (Using trie)
# T.C : O(n**2*m)
# S.C : O(n*l)  


class Node:
    def __init__(self):
        self.children = [None]*26
class Trie:
    def __init__(self):
        self.root = Node()
    def insert(self,w):
        root = self.root
        for ch in w:
            idx = ord(ch)-ord('a')
            if root.children[idx] == None:
                root.children[idx] = Node()
            root = root.children[idx]
    def startsWith(self,w):
        root = self.root
        for ch in w:
            idx = ord(ch)-ord('a')
            if root.children[idx] == None:
                return False
            root = root.children[idx]
        return True
            
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)

        cnt = 0
        for i,w in enumerate(words):
            prefixTrie = Trie()
            suffixTrie = Trie()
            prefixTrie.insert(w)
            suffixTrie.insert(w[::-1])
            for j in range(i):
                if len(words[j])>len(words[i]):
                    continue
                prefix = words[j]
                suffix = prefix[::-1]
                if prefixTrie.startsWith(prefix) and suffixTrie.startsWith(suffix):
                    cnt+=1

        return cnt