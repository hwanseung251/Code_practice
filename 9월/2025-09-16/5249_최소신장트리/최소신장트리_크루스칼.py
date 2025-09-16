import sys
sys.stdin = open("input.txt")

def find_set(x):
    if parents[x] != x:
        parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    rx, ry = find_set(x), find_set(y)

    if rx == ry:
        return

    if rx < ry:
        parents[ry] = rx
    else:
        parents[rx] = ry


T = int(input())

for t in range(1, T+1):
    V, E = map(int, input().split())
    ## 엣지 자료구조
    edges = []

    for _ in range(E):
        n1, n2, w = map(int, input().split())
        edges.append((w, n1, n2))

    edges.sort()

    parents = list(range(0,V+1))

    cnt = 0
    result = 0
    for weight, node1, node2 in edges:
        if find_set(node1) != find_set(node2):
            union(node1, node2)
            cnt += 1
            result += weight

        if cnt == V:
            break

    print(f"#{t} {result}")