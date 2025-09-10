import sys
sys.stdin = open("input.txt")

def partition_lomuto(arr, start, end):
    pivot = arr[end]
    i = start - 1

    for j in range(start, end):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[end] = arr[end], arr[i + 1]

    return i + 1


def quick_sort(arr, start, end):
    if start < end:
        pivot_idx = partition_lomuto(arr, start, end)

        quick_sort(arr, start, pivot_idx - 1)
        quick_sort(arr, pivot_idx + 1, end)


T = int(input())

for t in range(1, T+1):
    arr = list(map(int,input().split()))

    quick_sort(arr, 0, len(arr) - 1)

    print(f"#{t}", *arr)
