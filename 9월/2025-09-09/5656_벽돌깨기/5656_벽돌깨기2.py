import sys
sys.stdin = open("sample_input.txt")
from collections import deque

def recur(depth, current, arr):
    global max_value
    if depth == C:
        max_value = max(max_value, current)
        return

    for m in range(M):
        top = -1
        for n in range(N):
            if arr[n][m] > 0:
                top = arr[n][m]
                break

        if top != -1:
            cnt, new_arr = bfs(top,m, arr)
            recur(depth+1, current+cnt, new_arr)


def bfs(i,j, arr):
    q = deque()
    visited = [[False]*M for _ in range(N)]
    q.append((i,j))

    while q:
        if


T = int(input())

for t in range(1, T+1):
    C, M, N = map(int, input().split())
    input_arr = [list(map(int, input().split())) for _ in range(N)]
    max_value = 0

    recur()