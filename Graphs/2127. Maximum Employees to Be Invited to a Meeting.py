# Approach - Using BFS and Cycle Checks
# T.C : ~O(n)
# S.C : ~O(n)

class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        adj = defaultdict(list)
        for i in range(n):
            adj[favorite[i]].append(i)
        
        def bfs(node,fav):
            q = deque([[node,0]])
            maxDist = 0
            while q:
                val,dist = q.popleft()
                if val == fav:
                    continue
                maxDist = max(maxDist,dist)
                for nei in adj[val]:
                    q.append([nei,dist+1])

            return maxDist

        longestCycleLenOfLengthTwo = 0
        maxCycleLen = 0
        vis = [0]*n

        for i in range(n):
            if not vis[i]:
                countOfNodesSeenSoFar = defaultdict(int)
                curNode = i
                curNodeCnt = 0
                while not vis[curNode]:
                    vis[curNode] = 1
                    countOfNodesSeenSoFar[curNode] = curNodeCnt
                    curNodeCnt+=1
                    nextNode = favorite[curNode]
                    if nextNode in countOfNodesSeenSoFar:
                        cycleLen = curNodeCnt-countOfNodesSeenSoFar[nextNode]
                        maxCycleLen = max(maxCycleLen,cycleLen)
                        if cycleLen == 2:
                            n1 = curNode
                            n2 = nextNode
                            longestCycleLenOfLengthTwo+=2+bfs(n1,n2)+bfs(n2,n1)
                        break
                    else:
                        curNode = nextNode
        return max(maxCycleLen,longestCycleLenOfLengthTwo)
                