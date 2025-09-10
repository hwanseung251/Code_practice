import sys
sys.stdin = open("input.txt")


def get_winner(left_idx, right_idx):
    left_card = arr[left_idx]
    right_card = arr[right_idx]

    if left_card == right_card:
        return left_idx

    if (left_card - right_card) % 3 == 1:
        return left_idx
    else:
        return right_idx


def binary_search(left, right):
    if left == right:
        return left

    mid = (left + right) // 2

    left_winner = binary_search(left, mid)

    right_winner = binary_search(mid+1, right)

    return get_winner(left_winner, right_winner)


T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    win = binary_search(0, N-1)
    print(f"#{t} {win + 1}")
