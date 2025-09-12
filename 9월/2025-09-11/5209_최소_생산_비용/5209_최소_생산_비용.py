import sys
sys.stdin = open("input.txt")


def recur(product, cur):
    global min_value
    # 현재 가망없으면 가지치기
    if cur >= min_value:
        return
    # 물건분배 완료했으면 min_value 갱신
    if product == N:
        min_value = min(min_value, cur)
        return

    for i in range(N):
        # 제품을 아직 맞기지 않은 공장이면
        if not visited[i]:
            visited[i] = True
            recur(product+1, cur + arr[product][i])
            visited[i] = False



T = int(input())

for t in range(1, T+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N
    min_value = N * 99

    recur(0, 0)

    print(f"#{t} {min_value}")