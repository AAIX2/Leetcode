# Approach-1 (Using Same code of DFS Cycle Check in directed Graph)
# T.C : O(V+E)
# S.C : O(V+E)


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        vis = [0]*n
        def dfs(node):
            vis[node] = 2
            for nei in graph[node]:
                if vis[nei] == 2:
                    return True
                elif not vis[nei]:
                    if dfs(nei):
                        return True
            vis[node] = 1
            return False
            
        for i in range(n):
            if not vis[i]:
                dfs(i)
        ans = []
        for i in range(n):
            if vis[i] == 1:
                ans.append(i)
        return ans         
            
# Approach-2 (Using BFS) (Toplogical Sort)
# T.C : O(V+E)
# S.C : O(V+E)


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        revGraph = [[] for i in range(n)]
        indeg = [0]*n
        for i,g in enumerate(graph):
            for nei in g:
                revGraph[nei].append(i)
                indeg[i]+=1
        q = deque()
        for i in range(n):
            if indeg[i] == 0:
                q.append(i)
        safe = [0]*n
        while q:
            node = q.popleft()
            safe[node] = 1
            for nei in revGraph[node]:
                indeg[nei]-=1
                if indeg[nei] == 0:
                    q.append(nei)
        return [i for i in range(n) if safe[i] == 1]
                    