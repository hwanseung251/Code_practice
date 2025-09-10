import sys
sys.stdin = open("input.txt")


def binary_search(num, start, end, direction):
    global cnt
    if start > end:
        return

    mid = (start + end)//2

    if num == A[mid]:
        cnt += 1
        return

    if num > A[mid]:
        if direction == 'right':
            return
        binary_search(num, mid + 1, end, 'right')
    else:
        if direction == 'left':
            return
        binary_search(num, start, mid - 1, 'left')


T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())

    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))

    cnt = 0
    for b in B:
        binary_search(b, 0, N-1, 'start')

    print(f"#{t} {cnt}")