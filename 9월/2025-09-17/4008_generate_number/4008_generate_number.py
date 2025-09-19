import sys
sys.stdin = open("input.txt")


def recur(depth, current):
    global min_value, max_value
    if depth == N-1:
        min_value = min(min_value, current)
        max_value = max(max_value, current)
        return

    if operator[0] >= 1:
        operator[0] -= 1
        recur(depth+1, current + numbers[depth+1])
        operator[0] += 1
    if operator[1] >= 1:
        operator[1] -= 1
        recur(depth+1, current - numbers[depth+1])
        operator[1] += 1
    if operator[2] >= 1:
        operator[2] -= 1
        recur(depth+1, current * numbers[depth+1])
        operator[2] += 1
    if operator[3] >= 1:
        operator[3] -= 1
        recur(depth+1, int(current / numbers[depth+1]))
        operator[3] += 1

T = int(input())

for t in range(1, T+1):
    N = int(input())
    operator = list(map(int, input().split()))
    numbers = list(map(int, input().split()))

    min_value = 100000000
    max_value = -100000000

    recur(0, numbers[0])

    print(f"#{t} {max_value - min_value}")
