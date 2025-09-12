import sys
sys.stdin = open("input.txt")

def recur(depth, cur):
    global min_value
    if min_value < cur:
        return

    if depth == N:
        min_value = min(min_value, cur)
        return

    for i in range(N):
        if not included[i]:
            included[i] = True
            recur(depth+1, cur + arr[depth][i])
            included[i] = False



T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    included = [False] * N
    min_value = 10 * N

    recur(0, 0)
    print(f"#{t} {min_value}")