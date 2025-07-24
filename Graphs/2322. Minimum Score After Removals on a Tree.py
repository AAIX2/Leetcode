# Approach - Using DFS
# T.C : O(n^2)
# S.C : O(V+E), V = number of vertices and E = number of edges

class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)

        adj = defaultdict(list)
        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        xorArr = [nums[i] for i in range(n)]
        outTime = [0]*n
        inTime = [0]*n
        time = 0
        def dfs(node,par):
            nonlocal time
            curXor = nums[node]
            inTime[node] = time
            time+=1
            for nei in adj[node]:
                if nei!=par:
                    curXor^=dfs(nei,node)
            xorArr[node] = curXor
            outTime[node] = time
            time+=1
            return curXor
        dfs(0,-1)
        
        def isAncestor(u,v):
            if inTime[u]<=inTime[v] and outTime[u]>=outTime[v]:
                return True
            return False

        res = float('inf')
        for u in range(1,n):
            for v in range(u+1,n):
                if isAncestor(u,v):
                    xor1 = xorArr[u]^xorArr[v]
                    xor2 = xorArr[v]
                    xor3 = xorArr[0]^xor1^xor2
                elif isAncestor(v,u):
                    xor1 = xorArr[v]^xorArr[u]
                    xor2 = xorArr[u]
                    xor3 = xorArr[0]^xor1^xor2
                else:
                    xor1 = xorArr[u]
                    xor2 = xorArr[v]
                    xor3 = xorArr[0]^xor1^xor2
                res = min(res,max(xor1,xor2,xor3)-min(xor1,xor2,xor3))
        return res
        

