# Using in_built functions

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        s = sentence.split(" ")
        n = len(s)
        i = j = 0
        while i<n:
            if s[i][:len(searchWord)] == searchWord:
                return i+1
            i+=1
        return -1

# Time Complexity- O(n+n*w)
# Space- O(n)


# Using 2 pointers

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        curPos = 1
        i = 0
        n = len(sentence)
        while i<n:
            while i<n and sentence[i] == " ":
                i+=1
                curPos+=1
            j = 0
            while j<len(searchWord) and i<n and sentence[i] == searchWord[j]:
                i+=1
                j+=1
            if j == len(searchWord):
                return curPos
            while i<n and sentence[i]!=" ":
                i+=1
        return -1 
# Time Complexity- O(n+n*w)
# Space- O(1)


# Using Trie

class Node:
    def __init__(self):
        self.children = [None]*26
        self.ind = -1
class Trie:
    def __init__(self):
        self.root = Node()
    def insert(self,w,i):
        root = self.root
        for ch in w:
            idx = ord(ch)-ord('a')
            if root.children[idx] == None:
                root.children[idx] = Node()
            root = root.children[idx]
            if root.ind == -1:
                root.ind = i
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        s = sentence.split(" ")
        trie = Trie()
        for i,w in enumerate(s):
            trie.insert(w,i)
        root = trie.root
        for ch in searchWord:
            idx = ord(ch)-ord('a')
            if root.children[idx] == None:
                return -1
            root = root.children[idx]
        return root.ind+1


# Time Complexity- O(n+m)
# Space- O(n)