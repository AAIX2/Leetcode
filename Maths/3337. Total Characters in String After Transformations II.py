# Approach - Using Matrix Exponentiation
# T.C : O(n + log(t))
# S.C : O(26*26) ~ O(1)

class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        mod = 10**9+7
        identitiyMat = [[0 for i in range(26)]for i in range(26)]
        for i in range(26):
            identitiyMat[i][i] = 1

        def matrixMul(matA,matB):
            matC = [[0 for i in range(26)]for i in range(26)]
            for i in range(26):
                for j in range(26):
                    for k in range(26):
                        matC[i][j] = (matC[i][j]+matA[i][k]*matB[k][j])%mod
            return matC
        
        def matrixExpo(baseMat,exponent):
            if exponent == 0:
                return identitiyMat
            half = matrixExpo(baseMat,exponent//2)
            res = matrixMul(half,half)
            if exponent%2 == 1:
                res = matrixMul(baseMat,res)
            return res
        
        freq = [0]*26
        for ch in s:
            freq[ord(ch)-ord('a')]+=1
        
        # T matrix

        T = [[0 for i in range(26)]for i in range(26)]

        for i in range(26):
            for add in range(1,nums[i]+1):
                T[(i+add)%26][i]+=1

        # Find T^t

        ans = matrixExpo(T,t)

        finalFreq = [0]*26
        for i in range(26):
            for j in range(26):
                finalFreq[i] = (finalFreq[i]+ans[i][j]*freq[j])%mod
        
        return sum(finalFreq)%mod