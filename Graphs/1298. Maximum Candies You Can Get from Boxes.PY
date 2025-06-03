# Approach-1 (Using DFS)
# T.C : O(n), where n =  number of boxes, we don't visit any box more than once
# S.C : O(n)

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        n = len(status)
        
        vis = [0]*n
        found = set()
        def dfs(box):
            if vis[box]:
                return 0
            if status[box] == 0:
                found.add(box)
                return 0
            vis[box] = 1
            ans = candies[box]
            for b in containedBoxes[box]:
                ans+=dfs(b)
            
            for k in keys[box]:
                status[k] = 1
                if k in found:
                    ans+=dfs(k)
            return ans
        res = 0
        for b in initialBoxes:
            res+=dfs(b)
        return res
    
# Approach-2 (Using BFS)
# T.C : O(n), where n =  number of boxes, we don't visit any box more than once
# S.C : O(n)

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        n = len(status)
        q = deque()
        haskey = [0]*n
        hasBox = [0]*n
        
        for b in initialBoxes:
            if status[b] == 1:
                q.append(b)
                haskey[b] = 1
            hasBox[b] = 1
        
        res = 0
        while q:
            
            node = q.popleft()
            res+=candies[node]
        
            for box in containedBoxes[node]:
                if status[box] == 1:
                    hasBox[box] = 1
                    haskey[box] = 1
                    q.append(box)
                else:
                    hasBox[box] = 1
                    if haskey[box] == 1:
                        q.append(box)
            
            for key in keys[node]:
                if not haskey[key]:
                    haskey[key] = 1
                    if hasBox[key] == 1:
                        q.append(key)
            
        return res
                

        
        