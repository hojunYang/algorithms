import sys
sys.setrecursionlimit(1_000_000)
input = sys.stdin.readline

dirs = [(-1,0),(1,0),(0,1),(0,-1)]

N = int(input())
grid = [list(input().strip()) for _ in range(N)]

# 1) 노드 인덱싱
id_of = [[-1]*N for _ in range(N)]
nodes = []
for r in range(N):
    for c in range(N):
        if grid[r][c] == '#':
            id_of[r][c] = len(nodes)
            nodes.append((r, c))

V = len(nodes)
if V == 0:
    print(0)
    # 결과 없음
    exit(0)

# 2) 인접 리스트 생성 (중복 방지 위해 오른쪽/아래만 보며 간선 추가)
adj = [[] for _ in range(V)]
deg = [0]*V
E = 0

for u_idx, (r, c) in enumerate(nodes):
    for dr, dc in ((1,0),(0,1)):  # 아래/오른쪽만
        nr, nc = r+dr, c+dc
        if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] == '#':
            v_idx = id_of[nr][nc]
            adj[u_idx].append(v_idx)
            adj[v_idx].append(u_idx)
            E += 1  # 무향 간선 1개
# degree 채우기
for i in range(V):
    deg[i] = len(adj[i])

# 3) 컴포넌트 라벨링
comp_id = [-1]*V
comp_size = []
def dfs_comp(s, cid):
    stack = [s]
    comp_id[s] = cid
    size = 0
    while stack:
        u = stack.pop()
        size += 1
        for v in adj[u]:
            if comp_id[v] == -1:
                comp_id[v] = cid
                stack.append(v)
    return size

cid = 0
for i in range(V):
    if comp_id[i] == -1:
        size = dfs_comp(i, cid)
        comp_size.append(size)
        cid += 1
k = cid  # 컴포넌트 개수

# 4) 절단점(Tarjan)
time = 0
disc = [-1]*V
low  = [0]*V
parent = [-1]*V
is_ap = [False]*V

def tarjan(u):
    global time
    disc[u] = low[u] = time; time += 1
    child_cnt = 0
    for v in adj[u]:
        if disc[v] == -1:
            parent[v] = u
            child_cnt += 1
            tarjan(v)
            low[u] = min(low[u], low[v])
            if parent[u] != -1 and low[v] >= disc[u]:
                is_ap[u] = True
        elif v != parent[u]:
            low[u] = min(low[u], disc[v])
    if parent[u] == -1 and child_cnt > 1:
        is_ap[u] = True

for i in range(V):
    if disc[i] == -1:
        tarjan(i)

# 5) 전역 상수 D = |E| - |V| + 2
D = E - V + 2

# 6) 각 정점 제거 시 트리 여부 판정
ans = []
for i, (r, c) in enumerate(nodes):
    if deg[i] != D:
        continue  # 간선 수 조건 탈락
    ok = False
    if k == 1:
        # 전체가 연결이면, 제거 정점이 절단점이 아니어야 연결 유지
        ok = (not is_ap[i])
    elif k == 2:
        # 두 컴포넌트뿐이고, 그중 하나가 (i) 혼자여야 한다
        ok = (comp_size[comp_id[i]] == 1)
    else:
        ok = False

    if ok:
        ans.append((r+1, c+1))

# 7) 출력
ans.sort()
print(len(ans))
for r, c in ans:
    print(r, c)
