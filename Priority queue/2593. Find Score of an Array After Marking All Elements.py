# Approach-1 (Sorting array with indices)
# T.C : O(nlogn)
# S.C : O(n)


class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        arr = [[v,i] for i,v in enumerate(nums)]
        arr.sort()
        marked = set()
        score = 0
        for val,ind in arr:
            if ind not in marked:
                score+=val
                marked.add(ind)
                if ind+1<n and ind+1 not in marked:
                    marked.add(ind+1)
                if ind-1>=0 and ind-1 not in marked:
                    marked.add(ind-1)
        return score
    


# Approach-2 (Using min-heap)
# T.C : O(nlogn)
# S.C : O(n)


class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        heap = [[v,i] for i,v in enumerate(nums)]
        heapq.heapify(heap)
        marked = set()
        score = 0
        while heap:
            val,ind = heapq.heappop(heap)
            if ind not in marked:
                score+=val
                marked.add(ind)
                if ind+1<n and ind+1 not in marked:
                    marked.add(ind+1)
                if ind-1>=0 and ind-1 not in marked:
                    marked.add(ind-1)
        return score
    

# Approach-3 (Using monotonic q or stack)
# T.C : O(n)
# S.C : O(n)


class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        st = []
        score = 0
        for i in range(len(nums)):
            if not st or st[-1]>nums[i]:
                st.append(nums[i])
            else:
                while st:
                    score+=st.pop()
                    if st:
                        st.pop()
        while st:
            score+=st.pop()
            if st:
                st.pop()
        return score
    

# Approach-3 (Using 2 pointers)
# T.C : O(n)
# S.C : O(1)


class Solution:
    def findScore(self, nums: List[int]) -> int:
        nums.append(float('inf'))
        n = len(nums)
        start = -1
        score = 0
        i = 1
        while i<n:
            if nums[i]>=nums[i-1]:
                for j in range(i-1,start,-2):
                    score+=nums[j]
                start = i
                i+=1
            i+=1

        return score