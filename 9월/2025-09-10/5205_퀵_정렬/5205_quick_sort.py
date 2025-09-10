import sys
sys.stdin = open("input.txt")


def partition_hoare(arr, start, end):
    pivot = arr[start]
    left = start + 1
    right = end

    # 포인터가 역전되지 않았으면 반복
    while left <= right:
        # left < end 이면 left가 end에서 멈춰버림 → 절대 end+1로 가지 않음.
        # 이러면 left와 right가 교차하지 않고 left == right에서 멈춘 상태가 될 수 있다
        while left <= end and arr[left] <= pivot:
            left += 1
        while right > start and arr[right] >= pivot:
            right -= 1
        if left > right:
            arr[start], arr[right] = arr[right], arr[start]
        else:
            arr[left], arr[right] = arr[right], arr[left]
    return right


def quick_sort(arr, start, end):
    if start < end:
        pivot_idx = partition_hoare(arr, start, end)
        quick_sort(arr, start, pivot_idx - 1)
        quick_sort(arr, pivot_idx + 1, end)


T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    quick_sort(arr, 0, N - 1)
    print(f"#{t} {arr[N//2]}")