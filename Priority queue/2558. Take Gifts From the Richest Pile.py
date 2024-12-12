# Approach (Using max-heap)
# T.C : O(n + k*logn)
# S.C : O(n)


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = [-g for g in gifts]
        heapq.heapify(heap)
        ans = sum(gifts)
        while k:
            numberOfGifts = heapq.heappop(heap)
            ans-=abs(numberOfGifts)
            rem = floor(sqrt(abs(numberOfGifts)))
            heapq.heappush(heap,-rem)
            ans+=rem
            k-=1
        return ans