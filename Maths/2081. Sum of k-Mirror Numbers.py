# Approach - Using palindrome generation logic
# T.C : ~O((10 ^ D) * D), where D = number of digits in k-mirror number
# S.C : O(D), where D = number of digits in k-mirror number


class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def isPossible(num,k):
            base = []
            curNum = num
            while curNum:
                rem = curNum%k
                base.append(rem)
                curNum//=k
            
            return base == base[::-1]

        def generate(length,rem):
            halfLen = (length+1)//2
            minNum = pow(10,halfLen-1)
            maxNum = pow(10,halfLen)-1
            
            res = 0
            cnt = 0
            for i in range(minNum,maxNum+1):
                s = str(i)
                if length%2:
                    s = s+s[::-1][1:]
                else:
                    s = s+s[::-1]
                
                if isPossible(int(s),k):
                    res+=int(s)
                    cnt+=1
                if cnt == rem:
                    break
            
            return res,cnt

        ans = 0
        rem = n
        length = 1
        while rem:
            val,c = generate(length,rem)
            rem-=c
            ans+=val
            length+=1
            
        return ans

