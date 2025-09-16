import sys
sys.stdin = open("input.txt")
import heapq


def dijkstra(start_x, start_y):
    # 다익스트라 2차원 배열(무한대설정)
    dists = [[INF] * N for _ in range(N)]
    # 시작 지점 0설정
    dists[start_x][start_y] = 0
    pq = [(0, start_x, start_y)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    while pq:
        current_dist, x, y = heapq.heappop(pq)
        if dists[x][y] < current_dist:
            continue

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0<=nx<N and 0<=ny<N:
                # 만약 높은 곳이면 기본 1 + 높이차
                if arr[x][y] < arr[nx][ny]:
                    next_dist = current_dist + arr[nx][ny]-arr[x][y] + 1
                # 높은 곳이 아니면 기본값만 올라감
                else:
                    next_dist = current_dist + 1

                if next_dist >= dists[nx][ny]:
                    continue

                dists[nx][ny] = next_dist
                heapq.heappush(pq, (next_dist, nx, ny))
    return dists


T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    INF = float("inf")

    result = dijkstra(0,0)

    print(f"#{t} {result[N-1][N-1]}")