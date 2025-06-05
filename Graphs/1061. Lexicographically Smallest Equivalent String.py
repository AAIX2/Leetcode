# Approach-1 (DFS)
# T.C : O(m* ( V+E)), we try DFS m times
# S.C : O(V+E)

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        n = len(s1)
        adj = defaultdict(list)
        for i in range(n):
            adj[ord(s1[i])-ord('a')].append(ord(s2[i])-ord('a'))
            adj[ord(s2[i])-ord('a')].append(ord(s1[i])-ord('a'))
        
        def dfs(node):
            vis[node] = 1
            res = node
            for nei in adj[node]:
                if not vis[nei]:
                    res = min(res,dfs(nei))
            return res
        ans = []
        for ch in baseStr:
            idx = ord(ch)-ord('a')
            if idx not in adj:
                ans.append(ch)
                continue
            vis = [0]*26
            a = dfs(idx)
            
            ans.append(chr(a+ord('a')))
        return "".join(ans)

# Approach-2 (BFS)
# T.C : O(m* ( V+E)), we try BFS m times
# S.C : O(V+E)          
        

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        n = len(s1)
        adj = defaultdict(set)
        for i in range(n):
            adj[ord(s1[i])-ord('a')].add(ord(s2[i])-ord('a'))
            adj[ord(s2[i])-ord('a')].add(ord(s1[i])-ord('a'))
        
        def bfs(node):
            vis[node] = 1
            q = deque([node])
            res = float('inf')
            while q:
                val = q.popleft()
                res = min(res,val)
                for nei in adj[val]:
                    if not vis[nei]:
                        vis[nei] = 1
                        q.append(nei)
            return res
        ans = []
        for ch in baseStr:
            
            idx = ord(ch)-ord('a')
            if idx not in adj:
                ans.append(ch)
                continue
            vis = [0]*26
            a = bfs(idx)
            
            ans.append(chr(a+ord('a')))
        return "".join(ans)

# Approach-3 (DSU)
# T.C : O(n*alpha+m), we try BFS m times
# S.C : O(26)              
        
class DisjointSet:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.size = [1]*n
    def findPar(self,node):
        if self.parent[node] == node:
            return node
        self.parent[node] = self.findPar(self.parent[node])
        return self.parent[node]
    def UnionBySize(self,u,v):
        ulti_u,ulti_v = self.findPar(u),self.findPar(v)
        if ulti_u == ulti_v:
            return 
        if self.size[ulti_u]>=self.size[ulti_v]:
            self.size[ulti_u]+=self.size[ulti_v]
            self.parent[ulti_v] = ulti_u
        else:
            self.size[ulti_v]+=self.size[ulti_u]
            self.parent[ulti_u] = ulti_v
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        n = len(s1)
        dsu = DisjointSet(26)
        smallest = [float('inf')]*26
        for i in range(n):
            idx1 = ord(s1[i])-ord('a')
            idx2 = ord(s2[i])-ord('a')
            
            if dsu.findPar(idx1)!=dsu.findPar(idx2):
                dsu.UnionBySize(idx1,idx2)
            par = dsu.findPar(idx1)
            smallest[par] = min(idx1,idx2,smallest[par])
        ans = []
        for ch in baseStr:
            idx = ord(ch)-ord('a')
            par = dsu.findPar(idx)
            if smallest[par] == float('inf'):
                ans.append(ch)
                continue
            ans.append(chr(smallest[par]+ord('a')))
        return "".join(ans)


        
            
        