import sys
sys.stdin = open("input.txt")


def find_set(x):
    if x != parents[x]:
        parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    rx, ry = find_set(x), find_set(y)

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

    # 현재 노드좌표만 주어짐(N개의 노드) 간선은 없음
    # 모든 노드끼리 연결해서 간선과 가중치를 생성
    edges = []
    for i in range(N):
        for j in range(i+1,N):
            cost = ((x_list[i] - x_list[j])**2 + (y_list[i] - y_list[j])**2) * tax
            edges.append((cost,i,j))
    edges.sort()


    parents = list(range(N))
    edge_count = 0
    mst_cost = 0

    for c, n1, n2 in edges:
        if union(n1, n2):
            mst_cost += c
            edge_count += 1

            if edge_count == N-1:
                break

    print(f"#{t} {mst_cost:.0f}")



