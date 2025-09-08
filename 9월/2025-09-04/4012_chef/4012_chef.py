import sys
sys.stdin = open("input.txt")
import itertools

T = int(input())

for t in range(1, T+1):
    N = int(input())
    synergy = [list(map(int, input().split())) for _ in range(N)]

    min_value = float("inf")
    for A in itertools.combinations(range(N), N//2):
        A = list(A)
        B = [i for i in range(N) if i not in A]

        A_synergy = 0
        B_synergy = 0
        for one, two in itertools.combinations(range(N//2), 2):
            A_synergy += synergy[A[one]][A[two]]
            A_synergy += synergy[A[two]][A[one]]
            B_synergy += synergy[B[one]][B[two]]
            B_synergy += synergy[B[two]][B[one]]

        diff = abs(A_synergy - B_synergy)

        min_value = min(min_value, diff)

    print(f"#{t} {min_value}")