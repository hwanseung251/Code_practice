import sys
sys.stdin = open("sample_input.txt")
from collections import deque


def recur(depth, arr, current):
    global max_value
    if depth == N:
        max_value = max(current, max_value)
        return

    moved = False

    for w in range(W):
        # 해당 열에서 가장 위의 벽돌 찾기
        top_h = -1
        for h in range(H):
            if arr[h][w] != 0:
                top_h = h
                break
        if top_h == -1:
            continue  # 이 열은 빈 열

        moved = True
        # 분기별로 보드 복사 후 BFS 실행
        next_arr = [row[:] for row in arr]  # 얕은 복사지만 2차원엔 이 방식이면 충분
        bfs_arr, bfs_cnt = bfs(top_h, w, next_arr)
        recur(depth + 1, bfs_arr, current + bfs_cnt)

    if not moved:
        max_value = max(max_value, current)


def bfs(i, j, arr):
    q = deque()
    q.append((i, j))
    chk = [[False]*W for _ in range(H)]
    chk[i][j] = True

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    cnt = 0

    while q:
        ci, cj = q.popleft()
        K = arr[ci][cj]
        if arr[ci][cj] != 0:
            cnt += 1
        arr[ci][cj] = 0

        for d in range(4):
            for k in range(1, K):
                ni = ci + di[d]*k
                nj = cj + dj[d]*k
                if 0<=ni<H and 0<=nj<W:
                    if arr[ni][nj] != 0 and not chk[ni][nj]:
                        chk[ni][nj] = True
                        q.append((ni, nj))
                else:
                    break

    # 중력 적용: 각 열마다 아래로 떨어뜨리기
    for w in range(W):
        stack = []
        for h in range(H-1, -1, -1):  # 아래에서 위로
            if arr[h][w] != 0:
                stack.append(arr[h][w])
        # 아래부터 채우고 나머진 0
        h_ptr = H-1
        for v in stack:
            arr[h_ptr][w] = v
            h_ptr -= 1
        for h in range(h_ptr, -1, -1):
            arr[h][w] = 0

    return arr, cnt


T = int(input())

for t in range(1, T+1):
    N, W, H = map(int, input().split())
    input_arr = [list(map(int, input().split())) for _ in range(H)]
    all_rock = 0
    for h in range(H):
        for w in range(W):
            if input_arr[h][w] != 0:
                all_rock += 1
    max_value = 0
    recur(0, input_arr, 0)

    print(f"#{t} {all_rock-max_value}")