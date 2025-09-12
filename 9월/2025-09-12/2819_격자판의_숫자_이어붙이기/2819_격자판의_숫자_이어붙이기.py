import sys
sys.stdin = open("input.txt")


def dfs(i, j, number):
    # 수열의 길이가 7이되면 set인 result에 추가
    if len(number) == 7:
        result.add(number)
        return

    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]
    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        if 0<=ni<4 and 0<=nj<4:
            dfs(ni, nj, number + str(arr[ni][nj]))


T = int(input())

for t in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    result = set()

    # 각 위치에서 수열 생성 시작
    for i in range(4):
        for j in range(4):
            dfs(i, j, str(arr[i][j]))

    # 최종적으로 결과에 들어있는 수를 출력
    print(f"#{t} {len(result)}")