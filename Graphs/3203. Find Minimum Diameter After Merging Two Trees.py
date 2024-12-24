# Approach (Using BFS)
# T.C : O(V+E)
# S.C : O(V+E)

class Solution:
    def BFS(self, adj, source):
        que = deque([source])
        visited = {source: True}
        
        distance = 0
        farthestNode = source

        while que:
            size = len(que)  # Number of nodes at the current level

            for _ in range(size):
                curr = que.popleft()
                farthestNode = curr

                for nbr in adj[curr]:
                    if nbr not in visited:
                        visited[nbr] = True
                        que.append(nbr)

            if que:
                distance += 1

        return farthestNode, distance

    def findDiameter(self, adj):
        # Step 1: Find the farthest node from an arbitrary node (0)
        farthestNode, _ = self.BFS(adj, 0)

        # Step 2: Find the farthest node from the farthestNode found above
        _, diameter = self.BFS(adj, farthestNode)

        return diameter

    def buildAdj(self, edges):
        adj = defaultdict(list)
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        return adj

    def minimumDiameterAfterMerge(self, edges1, edges2):
        adj1 = self.buildAdj(edges1)
        adj2 = self.buildAdj(edges2)

        d1 = self.findDiameter(adj1)
        d2 = self.findDiameter(adj2)

        combined = (d1 + 1) // 2 + (d2 + 1) // 2 + 1

        return max(d1, d2, combined)
    


# Approach (Using DFS)
# T.C : O(V+E)
# S.C : O(V+E)

class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:

        def createGraph(edges):
            adj = defaultdict(list)
            for i,j in edges:
                adj[i].append(j)
                adj[j].append(i)
            return adj
        
        farthestNode1 = -1
        maxi1 = -1
        def dfs(node,par,dist,adj):
            nonlocal farthestNode1,maxi1
            if dist>maxi1:
                maxi1 = dist
                farthestNode1 = node
            for i in adj[node]:
                if i!=par:
                    dfs(i,node,dist+1,adj)
        g1 = createGraph(edges1)
        g2 = createGraph(edges2)
        dfs(0,-1,0,g1)
        dfs(farthestNode1,-1,0,g1)
        firstGraphDiameter = maxi1

        farthestNode2 = -1
        maxi2 = -1
        def dfs1(node,par,dist,adj):
            nonlocal farthestNode2,maxi2
            if dist>maxi2:
                maxi2 = dist
                farthestNode2 = node
            for i in adj[node]:
                if i!=par:
                    dfs1(i,node,dist+1,adj)



        dfs1(0,-1,0,g2)
        dfs1(farthestNode2,-1,0,g2)
        secondGraphDiameter = maxi2
        return max(ceil(firstGraphDiameter/2) + ceil(secondGraphDiameter/2) +1,max(firstGraphDiameter,secondGraphDiameter))

        
        