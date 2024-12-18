# Approach-1 (Brute Force)
# T.C : O(n^2)
# S.C : O(1)


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        ans = []
        for i in range(n):
            curPrice = prices[i]
            for j in range(i+1,n):
                if prices[j]<=curPrice:
                    curPrice-=prices[j]
                    break
            ans.append(curPrice)
        return ans
            

# Approach-2 (Monotonic Stack)
# T.C : O(2*n) ~= O(n)
# S.C : O(n) due to stack


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        st = []
        ans = [0]*n
        for i in range(n-1,-1,-1):
            while st and prices[st[-1]]>prices[i]:
                st.pop()
            if st:
                ans[i] = prices[i]-prices[st[-1]]
            else:
                ans[i] = prices[i]
            st.append(i)
       
        return ans
            