import sys
sys.stdin = open("input.txt")
import heapq


def mst(start_node):
    pq = [(0, start_node)]
    visited = [False]*(V+1)
    cnt = 0

    while pq:
        weight, node = heapq.heappop(pq)

        if visited[node]:
            continue

        visited[node] = True
        cnt += weight

        for next_weight, next_node in graph[node]:
            if not visited[next_node]:
                heapq.heappush(pq, (next_weight, next_node))
    return cnt


T = int(input())

for t in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]

    for i in range(E):
        n1, n2, w = map(int, input().split())
        graph[n1].append((w, n2))
        graph[n2].append((w, n1))

    print(f"#{t} {mst(0)}")