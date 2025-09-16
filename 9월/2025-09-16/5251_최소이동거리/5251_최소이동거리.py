import sys
sys.stdin = open("input.txt")
import heapq


def dijkstra(start_node):
    pq = [(0, start_node)]
    # 다익스트라 누적값을 저장할 배열 생성
    dists = [float("inf")] * (N+1)
    # 시작점 0
    dists[start_node] = 0

    while pq:
        current_dist, node = heapq.heappop(pq)
        # 현재 팝한 가중치가 기존보다 크다면 더 볼 필요가 없음
        if dists[node] < current_dist:
            continue

        for next_dist, next_node in graph[node]:
            new_dist = current_dist + next_dist
            if dists[next_node] <= new_dist:
                continue
            dists[next_node] = new_dist
            heapq.heappush(pq, (new_dist, next_node))
    return dists


T = int(input())

for t in range(1, T+1):
    N, E = map(int, input().split())
    graph = [[] for _ in range(N+1)]

    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((w, e))

    result = dijkstra(0)
    print(f"#{t} {result[N]}")

