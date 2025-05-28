# Approach-1 (Using BFS)
# T.C : O(V*(V+E))
# S.C : O(V+E)

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        n = len(edges1)+1
        m = len(edges2)+1
        adj1 = defaultdict(list)
        for n1,n2 in edges1:
            adj1[n1].append(n2)
            adj1[n2].append(n1)

        adj2 = defaultdict(list)
        for n1,n2 in edges2:
            adj2[n1].append(n2)
            adj2[n2].append(n1)
        
        def bfs(node,par,tar,adj):

            q = deque([[node,par,0]])
            c = 0
            while q:
                node1,p,d = q.popleft()
                c+=1
                for nei in adj[node1]:
                    if nei!=p and d+1<=tar:
                        q.append([nei,node1,d+1])
            return c

            
        d1 = [0]*n
        for i in range(n):
            d1[i] = bfs(i,-1,k,adj1)
        
        
        maxi = 0
        for i in range(m):
            if k-1>=0:
                maxi = max(maxi,bfs(i,-1,k-1,adj2))
        
        ans = [0]*n
        for i in range(n):
            ans[i] = d1[i]+maxi
        return ans
        

# Approach-2 (Using DFS)
# T.C : O(V*(V+E))
# S.C : O(V+E)

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        n = len(edges1)+1
        m = len(edges2)+1
        adj1 = defaultdict(list)
        for n1,n2 in edges1:
            adj1[n1].append(n2)
            adj1[n2].append(n1)

        adj2 = defaultdict(list)
        for n1,n2 in edges2:
            adj2[n1].append(n2)
            adj2[n2].append(n1)
        
        def dfs(node,par,d,tar,adj):
            
            if d>tar:
                return 0
            cnt = 0
            for nei in adj[node]:
                if nei!=par:
                    cnt += dfs(nei,node,d+1,tar,adj) 

            return 1+cnt
        d1 = [0]*n
        for i in range(n):
            d1[i] = dfs(i,-1,0,k,adj1)
        
        maxi = 0
        for i in range(m):
            maxi = max(maxi,dfs(i,-1,0,k-1,adj2))
        
        ans = [0]*n
        for i in range(n):
            ans[i] = d1[i]+maxi
        return ans
        