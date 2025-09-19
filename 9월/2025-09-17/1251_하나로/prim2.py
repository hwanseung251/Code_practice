import sys
sys.stdin = open("input.txt")
import heapq


def prim():
    visited = [False] * N
    distance = [float('inf')] * N
    edges_count = 0     # 간선 수
    min_tax = 0  # 최소 세율

    pq = [(0, 0)]
    distance[0] = 0

    while pq and edges_count < N:
        cost, node = heapq.heappop(pq)

        if visited[node]:
            continue

        visited[node] = True
        min_tax += cost
        edges_count += 1

        for i in range(N):
            if not visited[i]:
                next_cost = ((x_list[node] - x_list[i])**2 + (y_list[node] - y_list[i])**2) * tax
                if next_cost < distance[i]:
                    distance[i] = next_cost
                    heapq.heappush(pq, (next_cost, i))
    return min_tax

T = int(input())
INF = float("inf")
for t in range(1, T+1):
    N = int(input())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    tax = float(input())

    ans = prim()

    print(f"#{t} {round(ans)}")
