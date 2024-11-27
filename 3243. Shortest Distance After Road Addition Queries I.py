# Using BFS
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # Since the question asks for shorted distance for an non weighted graph so BFS is the most ideal
        adjList = {node:[] for node in range(n)}
        for i in range(n-1):
            adjList[i].append(i+1)
        dist = [i for i in range(n)]
        def bfs(node):
            q = deque([[node,dist[node]]])
            while q:
                node,d = q.popleft()
                if node == n-1:
                    return d
                for nei in adjList[node]:
                    if d+1<dist[nei]:
                        dist[nei] = d+1
                        q.append([nei,d+1])
            return dist[n-1]
        ans = [0]*len(queries)
        for i in range(len(queries)):
            n1,n2 = queries[i][0],queries[i][1]
            adjList[n1].append(n2)
            ans[i] = bfs(n1)
        return ans
# Time Complexity- O(q*(n+q)) Since there are n-1 edges intitally and at the worst case we can add q new edges
# Space Complexity- O(n)


# Using Djikstra's Algo

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        adj = {node:[] for node in range(n)}
        for i in range(n-1):
            adj[i].append(i+1)
        dist = [i for i in range(n)]
        def getDist(n1,n2):
            # print(adj)
            heap = [[dist[n1],n1]]
            # print(n1)
            while heap:
                # print(heap)
                d,node = heapq.heappop(heap)
                if node == n-1:
                    return d
                for i in adj[node]:
                    if d+1<dist[i]:
                        dist[i] = d+1
                        heapq.heappush(heap,[d+1,i])
            return dist[n-1]
        ans = []
        for n1,n2 in queries:
            adj[n1].append(n2)
            if dist[n1]+1<dist[n2]: 
                ans.append(getDist(n1,n2))
            else:
                ans.append(dist[n-1])
        return ans
# Time Complexity- O(q*((n+q)log(n))) Since there are n-1 edges intitally and at the worst case we can add q new edges
# Space Complexity- O(n)