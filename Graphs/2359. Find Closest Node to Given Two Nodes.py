# Approach-1 (BFS)
# T.C : O(V+E), V = number of vertices and E = number of edges
# S.C : O(n)
from collections import deque
import sys

class Solution:
    def __init__(self):
        self.n = 0

    def bfs(self, edges, startNode, dist_node):
        que = deque()
        que.append(startNode)
        dist_node[startNode] = 0
        visited = [False] * self.n
        visited[startNode] = True

        while que:
            u = que.popleft()
            v = edges[u]

            if v != -1 and not visited[v]:
                visited[v] = True
                dist_node[v] = 1 + dist_node[u]
                que.append(v)

    def closestMeetingNode(self, edges, node1, node2):
        self.n = len(edges)
        
        dist1 = [sys.maxsize] * self.n
        dist2 = [sys.maxsize] * self.n

        self.bfs(edges, node1, dist1)
        self.bfs(edges, node2, dist2)

        minDistNode = -1
        minDistTillNow = sys.maxsize

        for i in range(self.n):
            maxD = max(dist1[i], dist2[i])
            if dist1[i] != sys.maxsize and dist2[i] != sys.maxsize and maxD < minDistTillNow:
                minDistTillNow = maxD
                minDistNode = i

        return minDistNode

# Approach-2 (DFS)
# T.C : O(V+E), V = number of vertices and E = number of edges
# S.C : O(n)

import sys

class Solution:
    def __init__(self):
        self.n = 0

    def dfs(self, edges, startNode, dist_node, visited):
        visited[startNode] = True
        v = edges[startNode]
        
        if v != -1 and not visited[v]:
            dist_node[v] = 1 + dist_node[startNode]
            self.dfs(edges, v, dist_node, visited)

    def closestMeetingNode(self, edges, node1, node2):
        self.n = len(edges)

        dist1 = [sys.maxsize] * self.n
        dist2 = [sys.maxsize] * self.n
        visited1 = [False] * self.n
        visited2 = [False] * self.n

        dist1[node1] = 0
        dist2[node2] = 0

        self.dfs(edges, node1, dist1, visited1)
        self.dfs(edges, node2, dist2, visited2)

        minDistNode = -1
        minDistTillNow = sys.maxsize

        for i in range(self.n):
            if dist1[i] != sys.maxsize and dist2[i] != sys.maxsize:
                maxD = max(dist1[i], dist2[i])
                if maxD < minDistTillNow:
                    minDistTillNow = maxD
                    minDistNode = i

        return minDistNode
