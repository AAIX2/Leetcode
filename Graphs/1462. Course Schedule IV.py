# Approach 1 - Using BFS fpr every query
# T.C : O(Q*(V+E))
# S.C : O(V+E)

class Solution:
    def bfs(self,node1,vis,adj):
        vis[node1] = 1
        q = deque([node1])
        while q:
            node = q.popleft()
            for i in adj[node]:
                if not vis[i]:
                    vis[i] = 1
                    q.append(i)

    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        if len(prerequisites) == 0:
            return [False]*len(queries)
        adj = [[] for i in range(numCourses)]
        for node1,node2 in prerequisites:
            adj[node1].append(node2)
        ans = []
        for query in queries:
            node1 = query[0]
            node2 = query[1]
            vis = [0]*numCourses
            self.bfs(node1,vis,adj)
            if vis[node2] == 0:
                ans.append(False)
            else:
                ans.append(True)
        return ans
    

# Approach 2 - Using Kahn's algo
# T.C : O(Q+((V+E)*V))
# S.C : O(V+E)


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        indeg = [0]*numCourses
        for n1,n2 in prerequisites:
            adj[n1].append(n2)
            indeg[n2]+=1
        q = deque()
        for i in range(numCourses):
            if indeg[i] == 0:
                q.append(i)
        if len(q) == numCourses:
            return [False]*numCourses
        ancestors = defaultdict(set)
        while q:
            node = q.popleft()
            for nei in adj[node]:
                indeg[nei]-=1
                ancestors[nei].add(node)
                ancestors[nei].update(ancestors[node])
                if indeg[nei] == 0:
                    q.append(nei)
        
        ans = []
        for n1,n2 in queries:
            if n1 in ancestors[n2]:
                ans.append(True)
            else:
                ans.append(False)
        return ans


    