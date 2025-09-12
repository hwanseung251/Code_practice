import sys
sys.stdin = open("input.txt")


def recur(depth, current_percent):
    global max_percent
    if current_percent <= max_percent:
        return

    if depth == N:
        max_percent = max(max_percent, current_percent)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            recur(depth+1, current_percent*success_percentage[depth][i]*0.01)
            visited[i] = False

T = int(input())

for t in range(1, T+1):
    N = int(input())

    success_percentage = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N
    max_percent = 0

    recur(0, 1)
    print(f"#{t} {max_percent*100:.6f}")