# Using Recursive DFS
# This question is based on Eulerian path
class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        adj = defaultdict(list)
        deg = defaultdict()
        for i,j in pairs:
            adj[i].append(j)
            if i not in deg:
                deg[i] = [0,1]
            else:
                deg[i][1] += 1
            if j not in deg:
                deg[j] = [1,0]
            else:
                deg[j][0]+=1
        # print(adj,deg)
        ans = []
        def dfs(node):
            # vis.add(node)
            for i in reversed(adj[node]):
                adj[node].pop()
                dfs(i)
               
                    
            ans.append(node)
        start = pairs[0][0]
        for i in deg:
            if deg[i][1]-deg[i][0] == 1:
                start = i
                break
        
        dfs(start)
        # print(ans)
        res = []
        for i in range(len(ans)-2,-1,-1):
            res.append([ans[i+1],ans[i]])
        return res
# Time Complexity- O(V+E)
# Space Complexity- O(V+E)


#  Hierholzer's Algorithm

class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        adj = defaultdict(list)
        deg = defaultdict()
        for i,j in pairs:
            adj[i].append(j)
            if i not in deg:
                deg[i] = [0,1]
            else:
                deg[i][1] += 1
            if j not in deg:
                deg[j] = [1,0]
            else:
                deg[j][0]+=1
        # print(adj,deg)
        
        
        start = pairs[0][0]
        for i in deg:
            if deg[i][1]-deg[i][0] == 1:
                start = i
                break
        ans = []
        st = [start]
        while st:
            node = st[-1]
            if adj[node]:
                next = adj[node].pop()
                st.append(next)
            else:
                ans.append(node)
                st.pop()
        # print(ans)
        res = []
        for i in range(len(ans)-2,-1,-1):
            res.append([ans[i+1],ans[i]])
        return res
# Time Complexity- O(V+E)
# Space Complexity- O(V+E)