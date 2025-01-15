# Approach - (Using num1 to build the answer)
# T.C : O(1)
# S.C : O(1)


class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        num = 0
        cntBits = bin(num2).count("1")
        # Unsetting all the leftmost set bits until cntBits reaches 0 
        for i in range(31,-1,-1):
            if num1&(1<<i)!=0:
                num|=(1<<i)
                cntBits-=1
            if cntBits == 0:
                break
        # Setting the rightmost bits in the ans if the bit is not set in ans and if we have cntBits left after the above operation
        for i in range(32):
            if not cntBits:
                break
            if num&(1<<i)!=0:
                continue
            num|=(1<<i)
            cntBits-=1
            
        return num