# Approach-1 (Using max-heap + frequency table)
# T.C : O(n)
# S.C : O(26)

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        n = len(s)
        mp = defaultdict(int)
        for ch in s:
            mp[ord(ch)-ord('a')]+=1
        
        heap = []
        for i in mp:
            heap.append([-i,mp[i]])
        heapq.heapify(heap)
        
        res = ""
        while heap:
            val,f = heapq.heappop(heap)
            
            if f<=repeatLimit:
                res+=chr(abs(val)+ord('a'))*f
                
            else:
                res+=chr(abs(val)+ord('a'))*repeatLimit
                if heap:
                    val1,f1 = heapq.heappop(heap)
                    res+=chr(abs(val1)+ord('a'))
                    if f1-1:
                        heapq.heappush(heap,[val1,f1-1])
                else:
                    break
                heapq.heappush(heap,[val,f-repeatLimit])
                
            
        return res
    

# Approach-2 (Using pointers and frequency table)
# T.C : O(n)
# S.C : O(26)


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        n = len(s)
        freq = [0]*26
        for ch in s:
            freq[ord(ch)-ord('a')]+=1
        res = ""
        i = 25
        while i>=0:
            if freq[i] == 0:
                i-=1
                continue
            ch = chr(i+ord('a'))
            f = min(freq[i],repeatLimit)
            res+=ch*f
            freq[i]-=f
            if freq[i]:
                j = i-1
                while j>=0 and freq[j] == 0:
                    j-=1
                if j<0:
                    break
                res+=chr(j+ord('a'))
                freq[j]-=1 
            
        return res
