# Approach-1 (Simulation)
# T.C : O(k)
# S.C : O(k)


class Solution:
    def kthCharacter(self, k: int) -> str:
        s = "a"
        while len(s)<k:
            temp = ""
            for ch in s:
                temp+=chr(ord(ch)+1)
            s+=temp
        return s[k-1]
    


# Approach-2 (bit observation to find shift)
# T.C : O(log(k-1))
# S.C : O(1)

class Solution:
    def kthCharacter(self, k: int) -> str:
        flips = bin(k-1).count("1")
        return chr(ord('a')+flips)