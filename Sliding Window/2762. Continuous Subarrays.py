# Approach-1 (Using Map)
# S.C : ~O(1) - Explained in the video why O(1) 
# T.C : ~O(n) - Explained in the video why O(n) 

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        mp = defaultdict(int)
        i = j = 0
        cnt = 0
        while j<n:
            mp[nums[j]]+=1
            while i<j and max(mp)-min(mp)>2:
                mp[nums[i]]-=1
                if mp[nums[i]] == 0:
                    del mp[nums[i]]
                i+=1
            cnt+=(j-i+1)
            j+=1
        return cnt


# Approach-2 (Using 2 heaps)
# S.C :  O(n) 
# T.C : O(nlogn)


class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0
        i = j = 0
        maxHeap = []
        minHeap = []
        while j<n:
            heapq.heappush(maxHeap,[-nums[j],j])
            heapq.heappush(minHeap,[nums[j],j])
            while i<j and abs(abs(maxHeap[0][0])-minHeap[0][0])>2:
                i = min(maxHeap[0][1]+1,minHeap[0][1]+1)
                while maxHeap and maxHeap[0][1]<i:
                    heapq.heappop(maxHeap)
                while minHeap and minHeap[0][1]<i:
                    heapq.heappop(minHeap)
            cnt+=(j-i+1)
            j+=1
        return cnt
    

# Approach-3(Using monotonic deque)
# S.C :  O(n) 
# T.C : O(n)


class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0
        i = j = 0
        maxq = deque()
        minq = deque()
        while j<n:
            while maxq and nums[maxq[-1]]<=nums[j]:
                maxq.pop()
            while minq and nums[minq[-1]]>=nums[j]:
                minq.pop()
            maxq.append(j)
            minq.append(j)
            if i<=j and abs(nums[minq[0]]-nums[maxq[0]])>2:
                i = min(minq[0]+1,maxq[0]+1)
                while maxq and maxq[0]<i:
                    maxq.popleft()
                while minq and minq[0]<i:
                    minq.popleft()
            cnt+=(j-i+1)
            j+=1
        return cnt
    

# Approach-4(Using 2 pointers)
# S.C :  O(n) 
# T.C : O(1)


class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        maxi = nums[0]
        mini = nums[0]
        i = j = 0
        cnt = 0
        windowLen = 0
        while j<n:
            maxi = max(maxi,nums[j])
            mini = min(mini,nums[j])
            if maxi-mini>2:
                windowLen = j-i
                cnt+=(windowLen*(windowLen+1))//2
                i = j
                maxi = nums[j]
                mini = nums[j]
                while i>0 and abs(nums[j]-nums[i-1])<=2:
                    i-=1
                    maxi = max(maxi,nums[i])
                    mini = min(mini,nums[i])
                if i<j:
                    windowLen = j-i
                    cnt-=(windowLen*(windowLen+1))//2
            j+=1
        windowLen = j-i
        cnt+=(windowLen*(windowLen+1))//2
        return cnt
