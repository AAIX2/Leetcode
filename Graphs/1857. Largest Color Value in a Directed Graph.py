# Approach - 1 (Using Topological Sorting with BFS)
# T.C : O(V+E)
# S.C : O(V+E)

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        indeg = [0]*n
        adj = defaultdict(list)
        for n1,n2 in edges:
            adj[n1].append(n2)
            indeg[n2]+=1
        q = deque()
        freq = [[0 for i in range(26)]for i in range(n)]
        for i in range(n):
            if indeg[i] == 0:
                freq[i][ord(colors[i])-ord('a')]+=1
                q.append([i,1])
        cnt = 0
        maxFreq = 0
        while q:
            node,f = q.popleft()
            cnt+=1
            maxFreq = max(maxFreq,f)
            maxi = 0
            for nei in adj[node]:
                indeg[nei]-=1
                idx = ord(colors[nei])-ord('a')
                for j in range(26):
                    if j == idx:
                        freq[nei][j] = max(freq[nei][j],1+freq[node][idx])
                    else:
                        freq[nei][j] = max(freq[nei][j],freq[node][j])
                    maxi = max(maxi,freq[nei][j])
                if indeg[nei] == 0:
                    q.append([nei,maxi])
        return -1 if cnt!=n else maxFreq
        

# Approach - 1 (Using DFS)
# T.C : O(V+E)
# S.C : O(V+E)

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)

        adj = defaultdict(list)
        for n1,n2 in edges:
            adj[n1].append(n2)

        vis = [0]*n
        freq = [[0]*26 for i in range(n)]
        def dfs(node):
            if vis[node] == 2:
                return -1
            if vis[node]:
                return freq[node][ord(colors[node])-ord('a')]
            vis[node] = 2
            for nei in adj[node]:
                res = dfs(nei)
                if res == -1:
                    return -1
                for i in range(26):
                    freq[node][i] = max(freq[node][i],freq[nei][i])
            freq[node][ord(colors[node])-ord('a')]+=1
            vis[node] = 1
            return freq[node][ord(colors[node])-ord('a')]
        maxColorFreq = 0
        for i in range(n):
            ans = dfs(i)
            if ans == -1:
                return -1
            maxColorFreq = max(maxColorFreq,ans)
        return maxColorFreq
