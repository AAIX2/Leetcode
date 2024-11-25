# Using BFS
# Approach-1:


# Code:


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        n = len(board)
        m = len(board[0])
        # Since we are given an intial state and we are told to look for a final state in minimum steps meaning we need shortest path to between source and destination.
        res = "123450"
        vis = set()
        # Adj list based on cells represented as a 1-D arr
        adj = {0:[1,3],1:[0,2,4],2:[1,5],3:[0,4],4:[3,5,1],5:[4,2]}
        # Swap function to swap chars 
        def swap(s,i,j):
            s = list(s)
            s[i],s[j] = s[j],s[i]
            return "".join(s)
        
        s = ""
        idx = -1
        for i in range(n):
            for j in range(m):
                s+=str(board[i][j])
                if board[i][j] == 0:
                    idx = i*3+j
        # BFS starting from the initial state
        q = deque([[s,idx,0]])
        vis.add(s)
        while q:
            state,ind,moves = q.popleft()
            # print(state,ind,moves)
            if state == res:
                return moves
            # Going through all the neighbours
            for i in adj[ind]:
                new_state = swap(state,ind,i)
                # print(new_state)
                if new_state not in vis:    
                    vis.add(new_state)
                    q.append([new_state,i,moves+1])
        
        return -1