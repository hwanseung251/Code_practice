import sys
sys.stdin = open("input.txt")


def merge_sort(arr):
    global cnt
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    merge_arr = []
    left_idx, right_idx = 0, 0

    # 각 끝부분 비교
    if left_half[-1] > right_half[-1]:
        cnt += 1

    while left_idx < len(left_half) and right_idx < len(right_half):
        if left_half[left_idx] <= right_half[right_idx]:
            merge_arr.append(left_half[left_idx])
            left_idx += 1

        else:
            merge_arr.append(right_half[right_idx])
            right_idx += 1

    merge_arr.extend(left_half[left_idx:])
    merge_arr.extend(right_half[right_idx:])

    return merge_arr

T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    result = merge_sort(arr)

    print(f"#{t} {result[N//2]} {cnt}")