import sys
sys.stdin = open("input2.txt")
import itertools

T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    min_value = N * 100
    # 경로를 순열로 모두  (0은 무조건 앞에와야되니까 제외시키고 순열)
    paths = list(itertools.permutations(range(1, N)))

    for path in paths:
        # 마지막 도착은 0이니까 패딩
        tmp = [*path] + [0]
        # 시작 값은 0으로 출발해서 경로0으로 도착한 값
        total = arr[0][tmp[0]]
        # 경로대로 값 추가해나감
        for i in range(1, N):
            start, end = tmp[i-1], tmp[i]
            total += arr[start][end]

        min_value = min(min_value, total)

    print(f"#{t} {min_value}")