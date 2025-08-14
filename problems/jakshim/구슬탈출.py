from collections import deque

def solution():
    rows, cols = map(int, input().split())
    maze = [list(input()) for _ in range(rows)]
    
    def bfs(red, blue, maze):
        queue = deque([(red, blue, 0)])
        visited = set([(red, blue)])
        while queue:
            position = queue.popleft()
            rr, rc = position[0]
            br, bc = position[1]
            count = position[2]
            if count == 10:
                continue
            for nx, ny in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nrr, nrc = rr, rc
                rf, bf = 0, 0 
                while 0 < nrr < rows -1 and 0 < nrc < cols -1:
                    nrr += nx
                    nrc += ny
                    if maze[nrr][nrc] == '#':
                        nrr -= nx
                        nrc -= ny
                        break
                    if maze[nrr][nrc] == 'O':
                        rf = 1
                
                nbr, nbc = br, bc
                while 0 < nbr < rows -1 and 0 < nbc < cols -1:
                    nbr += nx
                    nbc += ny
                    if maze[nbr][nbc] == '#':
                        nbr -= nx
                        nbc -= ny
                        break
                    if maze[nbr][nbc] == 'O':
                        bf = 1
                # 빨간 구슬과 파란 구슬이 같은 위치에 있을 때 처리
                if (nrr, nrc) == (nbr, nbc):
                    # 빨간 구슬이 더 멀리 이동했다면 한 칸 뒤로
                    if abs(nrr - rr) + abs(nrc - rc) > abs(nbr - br) + abs(nbc - bc):
                        nrr -= nx
                        nrc -= ny
                    # 파란 구슬이 더 멀리 이동했다면 한 칸 뒤로
                    else:
                        nbr -= nx
                        nbc -= ny
                if bf == 1:
                    continue
                if rf == 1:
                    return 1
                if ((nrr, nrc), (nbr, nbc)) not in visited:
                    visited.add(((nrr, nrc), (nbr, nbc)))
                    queue.append(((nrr, nrc), (nbr, nbc), count+1))
        return 0
    red, blue = None, None
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 'R':
                red = (i, j)
            if maze[i][j] == 'B':
                blue = (i, j)

    return bfs(red, blue, maze)
    
print(solution())

"""
from sys import stdin
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]
input = stdin.readline

n,m = map(int, input().split())
board = []

srx=sry=sbx=sby=-1
for x in range(n):
    board.append(list(input().strip()))
    for y in range(m):
        if board[x][y] == 'R':
            srx,sry = x,y
        elif board[x][y] == 'B':
            sbx,sby = x,y

def solv():
    visited = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
    q = deque([(srx,sry,sbx,sby,0)])

    visited[srx][sry][sbx][sby] = True
    while q:
        rx,ry,bx,by,cnt = q.pop()

        if board[rx][ry] == 'O':
            print(1)
            return

        if cnt == 10:
            continue

        for d in range(4):
            nbx,nby,bcnt = move_ball(bx,by,d)
            if board[nbx][nby] == 'O':
                continue

            nrx,nry,rcnt = move_ball(rx,ry,d)

            if nrx == nbx and nry == nby:
                if bcnt > rcnt:
                    nbx -= dx[d]
                    nby -= dy[d]
                else:
                    nrx -= dx[d]
                    nry -= dy[d]

            if not visited[nrx][nry][nbx][nby]:
                visited[nrx][nry][nbx][nby] = True
                q.appendleft((nrx,nry,nbx,nby,cnt+1))
    print(0)
def move_ball(x,y,d):
    cnt = 0
    while True:
        x += dx[d]
        y += dy[d]
        if not point_validator(x,y):
            x -= dx[d]
            y -= dy[d]
            return x,y,cnt
        if board[x][y] == 'O':
            return x,y,cnt
        cnt += 1

def point_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    elif board[x][y] == '#':
        return False
    return True

solv()
"""