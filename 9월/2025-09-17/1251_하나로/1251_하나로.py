import sys
sys.stdin = open("input.txt")


def find_set(x):
    if x != parents[x]:
        parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    rx = find_set(x)
    ry = find_set(y)

    if rx == ry:
        return False

    parents[ry] = rx
    return True

T = int(input())

for t in range(1, T+1):
    N = int(input())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))

    tax = float(input())

    edges = []

    # 점만 주어졌고 각 간선의 가중치를 모두 직접 추가
    for i in range(N):
        for j in range(i+1, N):
            cost = ((x_list[i] - x_list[j])**2 + (y_list[i] - y_list[j])**2) * tax
            edges.append((cost, i, j))

    edges.sort()

    parents = list(range(N))

    mst_cost = 0
    edges_count = 0
    for c, n1, n2 in edges:
        if union(n1, n2):
            mst_cost += c
            edges_count += 1

            if edges_count == N - 1:
                break
    print(f"#{t} {round(mst_cost)}")