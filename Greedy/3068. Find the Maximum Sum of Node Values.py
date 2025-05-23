# Approach-1 (Greedily picking nodes to xor)
# T.C : O(n)
# S.C : O(1)

class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        # To get the ideal sum meaning if a value on xoring with k inc then we take that value else if it dec then we take the original value so we bascially take the best value out of both
        idealSum = 0

        # This tells us how many values we have to xor where xor inc if the cnt is odd meaning we need one more to make it even since we can only apply ops on an edge meaning pair of nodes
        cnt = 0
        # This tells us if the cnt is odd in case then we have to select one more node to make it even but which one to choose. We will choose greedily the one where the loss of value is minimum
        loss = float('inf')
        for num in nums:
            if num^k>num:
                cnt+=1
                idealSum+=(num^k)
            else:
                idealSum+=num
            
            loss = min(loss,abs(num-(num^k)))
        if cnt%2:
            return idealSum-loss
        return idealSum

        
# Approach-2(Greedy  + Sorting)
# T.C : O(nlogn)
# S.C : O(n)

class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n = len(nums)
        initialSum = 0
        profit = []
        for i in range(n):
            profit.append(((nums[i]^k)-nums[i]))
            initialSum+=nums[i]
        profit.sort(reverse = True)
        for i in range(0,n-1,2):
            val = (profit[i]+profit[i+1])
            initialSum+=((val if val>=0 else 0))
        return initialSum
        