import sys
sys.stdin = open("input.txt")


def find_set(x):
    if parent[x] != x:
        parent[x] = find_set(parent[x])
    return parent[x]


def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    if root_x == root_y:
        return

    if rank[root_x] > rank[root_y]:
        parent[root_x] = root_y
    else:
        parent[root_y] = root_x
        if rank[root_x] == rank[root_y]:
            rank[root_x] += 1


T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    students = list(map(int, input().split()))

    parent = list(range(N+1))
    rank = [0] * (N+1)

    for i in range(M):
        p1, p2 = students[i*2], students[i*2+1]
        union(p1, p2)


    root_nodes = set()
    for i in range(1, N+1):
        root_nodes.add(find_set(i))

    print(f"#{t} {len(root_nodes)}")

