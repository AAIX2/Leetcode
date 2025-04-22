# Approach - Using Maths (combinatorics) and DP
# T.C : O(maxVal * log(maxVal) + n)
# S.C : O(maxVal + n)
class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        mod = 10**9+7
        dp = [[0 for i in range(15)]for i in range(maxValue+1)]
        count = [0]*15

        def findSets(val,count,dp):
            if dp[val][1]!=0:
                return

            dp[val][1] = 1
            count[1]+=1

            for div in range(2,val+1):
                if val%div == 0:
                    findSets(val//div,count,dp)

                    for l in range(1,15):
                        if dp[val//div][l]!=0:
                            dp[val][l+1]+=dp[val//div][l]
                            count[l+1]+=dp[val//div][l]
        def findPower(val,power):
            if not power:
                return 1
            half = findPower(val,power//2)
            res = (half*half)%mod
            if power%2:
                return (val*res)%mod
            return res
        
        def modularNcR(n,r):
            if r<0 or r>n:
                return 0
            a = fact[n]
            b = (fact[r]*fact[n-r])%mod
            return (a*findPower(b,mod-2))%mod

        # Precompute factorial
        fact = [1]*(n+1)
        for i in range(2,n+1):
            fact[i] = (fact[i-1]*i)%mod
        # Find set counts

        for val in range(1,maxValue+1):
            findSets(val,count,dp)


        res = 0
        for l in range(1,15):
            if n<l:
                break
            if count[l]!=0:
                possibilities = modularNcR(n-1,l-1)
                res+=(possibilities*count[l])%mod
        return res%mod