# T.C : O(n^2), The maximum number of cells is n^2 and each cell is visited at most once.
# S.C : O(n^2)


class Solution:
    def getCoord(self, s: int, n: int) -> tuple[int, int]:
        row = n - 1 - (s - 1) // n
        col = (s - 1) % n
        
        if (n % 2 == 1 and row % 2 == 1) or (n % 2 == 0 and row % 2 == 0):
            col = n - 1 - col
        
        return (row, col)

    def snakesAndLadders(self, board: list[list[int]]) -> int:
        n = len(board)
        steps = 0
        queue = deque()
        visited = [[False] * n for _ in range(n)]
        
        visited[n - 1][0] = True
        queue.append(1)

        while queue:
            for _ in range(len(queue)):
                x = queue.popleft()
                if x == n * n:
                    return steps

                for k in range(1, 7):
                    if x + k > n * n:
                        break

                    r, c = self.getCoord(x + k, n)
                    if visited[r][c]:
                        continue

                    visited[r][c] = True
                    if board[r][c] == -1:
                        queue.append(x + k)
                    else:
                        queue.append(board[r][c])
            steps += 1

        return -1


# T.C : O(n^2), The maximum number of cells is n^2 and each cell is visited at most once.
# S.C : O(n^2)

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        cells = [0]*(n**2+1)
        num = 1
        dir = 1
        for i in range(n-1,-1,-1):
            for j in range(n):
                if dir == 1:
                    cells[num] = (i,j)
                else:
                    cells[num] = (i,n-j-1)
                num+=1
            dir*=-1
        vis = [0]*(n**2+1)
        vis[1] = 1
        q = deque([[1,0]])
        while q:
            node,d = q.popleft()
            if node == n**2:
                return d
            for i in range(node+1,min(node+6,n**2)+1):
                if not vis[i]:
                    r,c = cells[i]
                    if board[r][c] == -1:
                        q.append([i,d+1])
                    else:
                        q.append([board[r][c],d+1])
                    vis[i] = 1
        return -1
                