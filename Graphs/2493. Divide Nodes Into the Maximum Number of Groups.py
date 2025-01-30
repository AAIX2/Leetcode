# Approach 1 - Using Bipartite, DFS and BFS
# T.C : O(V * (V+E))
# S.C : O(V+E)

class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)


        def isBipartite(adj):
            vis = [-1 for i in range(n+1)]
            def dfs(node,color):
                vis[node] = color
                for i in adj[node]:
                    if vis[i] == -1:
                        if vis[node] == 0:
                            vis[i] = 1
                        else:
                            vis[i] = 0
                        if dfs(i,1-color) == False:
                            return False
                    elif vis[i] == vis[node]:
                        return False
                return True
            for i in range(1,n+1):
                if vis[i] == -1:
                    if dfs(i,0) == False:
                        return False
            return True
        
        if isBipartite(adj) == False:
            return -1
        
        def bfs(node):
            vis = [0]*(n+1)
            q = deque([[node,1]])
            vis[node] = 1
            maxGrps = 1
            while q:
                
                curNode,grp = q.popleft()
                maxGrps = max(maxGrps,grp)
                for nei in adj[curNode]:
                    if not vis[nei]:
                        vis[nei] = 1
                        q.append([nei,grp+1])
            
            return maxGrps


        groups = [0]*(n+1)
        for i in range(1,n+1):
            groups[i] = bfs(i)
        
        vis = [0]*(n+1)

        def dfs(node):
            vis[node] = 1
            maxNode = groups[node]
            for nei in adj[node]:
                if not vis[nei]:
                    maxNode = max(maxNode,dfs(nei))
            return maxNode
        
        res = 0
        for i in range(1,n+1):
            if not vis[i]:
                res+=dfs(i)
        return res


# Approach 2 - Using Bipartite, DSU and BFS
# T.C : O(V * (V+E))
# S.C : O(V+E)
        
class DisjointSet:
    def __init__(self,n):
        self.parent = [i for i in range(n+1)]
        self.size = [1]*(n+1)
       
    def getPar(self,node):
        if self.parent[node] == node:
            return node
        self.parent[node] = self.getPar(self.parent[node])
        return self.parent[node]
    def UnionBySize(self,u,v):
        ulti_u,ulti_v = self.getPar(u),self.getPar(v)
        if ulti_u == ulti_v:
            return
        if self.size[ulti_u]>=self.size[ulti_v]:
            self.size[ulti_u] += self.size[ulti_v]
            self.parent[ulti_v] = ulti_u
        else:
            self.size[ulti_v] += self.size[ulti_u]
            self.parent[ulti_u] = ulti_v
class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        

        def isBipartite(adj):
            vis = [-1 for i in range(n+1)]
            def dfs(node,color):
                vis[node] = color
                for i in adj[node]:
                    if vis[i] == -1:
                        if vis[node] == 0:
                            vis[i] = 1
                        else:
                            vis[i] = 0
                        if dfs(i,1-color) == False:
                            return False
                    elif vis[i] == vis[node]:
                        return False
                return True
            for i in range(1,n+1):
                if vis[i] == -1:
                    if dfs(i,0) == False:
                        return False
            return True
        
        if isBipartite(adj) == False:
            return -1
        
        def bfs(node):
            
            vis = [0]*(n+1)
            q = deque([[node,1]])
            vis[node] = 1
            maxGrps = 1
            while q:
                curNode,grp = q.popleft()
                maxGrps = max(maxGrps,grp)
                for nei in adj[curNode]:
                    if not vis[nei]:
                        vis[nei] = 1
                        q.append([nei,grp+1])
            return maxGrps


        groups = [0]*(n+1)
        for i in range(1,n+1):
            groups[i] = bfs(i)
        
        dsu = DisjointSet(n)
        groupSizes = [1]*(n+1)
        for n1,n2 in edges:
            p1,p2 = dsu.getPar(n1),dsu.getPar(n2)
            if p1!=p2:
                maxi = max(groups[p1],groups[p2],groupSizes[p1],groupSizes[p2])
                dsu.UnionBySize(n1,n2)
                par = dsu.getPar(n1)
                groupSizes[par] = maxi
               
        res = 0
        for i in range(1,n+1):
            if dsu.getPar(i) == i:
                res+=groupSizes[i]
                

        return res



        