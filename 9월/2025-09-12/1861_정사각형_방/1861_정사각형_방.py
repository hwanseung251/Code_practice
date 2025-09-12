import sys
sys.stdin = open("input.txt")

T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * (N**2 + 1)

    # 옆으로 갈 수 있는 상황이면 그 위치에 1표기
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    for i in range(N):
        for j in range(N):
            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]
                if 0<=ni<N and 0<=nj<N:
                    if arr[i][j] + 1 == arr[ni][nj]:
                        visited[arr[i][j]] = 1
                        break

    # 1표기가 이어진 만큼 카운트하면서 최대 길이 갱신
    max_value = 0
    cnt = 0
    start = 0
    for i in range(1, N**2+1):
        if visited[i] == 1:
            cnt += 1
        else:
            if max_value < cnt:
                max_value = cnt
                start = i - cnt
            cnt = 0

    print(f"#{t} {start} {max_value+1}")