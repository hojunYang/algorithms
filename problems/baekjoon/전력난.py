import sys
input = sys.stdin.readline

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n  # 또는 size를 써도 됨

    def find(self, x):
        # 경로 압축
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        # union by rank
        if self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb
        elif self.rank[ra] > self.rank[rb]:
            self.parent[rb] = ra
        else:
            self.parent[rb] = ra
            self.rank[ra] += 1
        return True

def solve():
    while True:
        m, n = map(int, input().split())
        if m == 0 and n == 0:
            break

        edges = []
        total = 0

        for _ in range(n):
            x, y, z = map(int, input().split())
            edges.append((z, x, y))  # (가중치, u, v)
            total += z

        edges.sort()  # 가중치 오름차순
        dsu = DSU(m)
        mst = 0
        cnt = 0

        for w, u, v in edges:
            if dsu.union(u, v):
                mst += w
                cnt += 1
                if cnt == m - 1:
                    break

        # 절약액 = 전체 - MST
        print(total - mst)

solve()
