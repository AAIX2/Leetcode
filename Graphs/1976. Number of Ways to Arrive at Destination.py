# Approach (Using Dijkstra's Algorithm)
# T.C : O(((V+E)*log(V))
# S.C : O(V+E)

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        mod = 10**9+7
        adj = defaultdict(list)
        for n1,n2,wt in roads:
            adj[n1].append([n2,wt])
            adj[n2].append([n1,wt])
        dist = [float('inf')]*n
        dist[0] = 0
        ways = [0]*n
        ways[0] = 1
        heap = [[0,0]]
        while heap:
            d,node = heapq.heappop(heap)
            if d>dist[n-1]:
                continue
            for nei,w in adj[node]:
                if w+d<dist[nei]:
                    dist[nei] = w+d
                    heapq.heappush(heap,[w+d,nei])
                    ways[nei] = ways[node]
                elif w+d == dist[nei]:
                    ways[nei]+=ways[node]
        return ways[n-1]%mod