import sys
sys.stdin = open("input.txt")

R, C, M = map(int, input().split())
beach = [[False] * (C+1) for _ in range(R+1)]

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    beach[r][c] = (s, d, z)


di = [0, -1, 1, 0, 0] # 1상 2하 3우 4좌
dj = [0, 0, 0, 1, -1]
opp = {1:2, 2:1, 3:4, 4:3}

cnt = 0
for peaple in range(1, C+1):
    # 낚시
    for r in range(1, R+1):
        if beach[r][peaple] != False:
            cnt += beach[r][peaple][2]
            beach[r][peaple] = False
            break

    # 상어 이동
    next_beach = [[False] * (C+1) for _ in range(R+1)]

    for i in range(1, R+1):
        for j in range(1, C+1):
            if beach[i][j] == False:
                continue

            speed = beach[i][j][0]
            direction = beach[i][j][1]
            size = beach[i][j][2]

            if direction in [1, 2]:
                next_i = (i + speed) % R
            else:
                next_j = (j + speed) % C