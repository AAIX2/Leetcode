# //Binary Search + Greedy (This is the same Qn of pattern "Applying binary search on answer" (Time Compplexity - O(m * log(n)) where m = max diff in pair
# //How to identify -> Notice the keywords - "min max"
# /*
    # Whenever we see in Question to Find Min(Max) or Max(Min) 
    # we will try to use Binary search on the result
# */
# //T.C : O(nlogn)
# //S.c : O(1)

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        n = len(nums)
        if n == 1:
            return 0
        nums.sort()

        def isPossible(mid):
            cnt = 0
            i = 1
            while i<n:
                if nums[i]-nums[i-1]<=mid:
                    cnt+=1
                    i+=1
                i+=1
                if cnt == p:
                    return True
            return cnt>=p
                

        low = 0
        high = nums[-1]-nums[0]
        while low<=high:
            mid = (low+high)//2
            if isPossible(mid):
                high = mid-1
            else:
                low = mid+1
        return low