import sys
sys.stdin = open("input.txt")


def merge_sort_and_count(arr):
    '''
    병합정렬 함수 (재귀)
    왼쪽과 오른쪽을 나눠서 각각 정렬한다.
    그 후 합칠 때 오른쪽이 왼쪽보다 작으면(A로 정렬했을땐 컷지만 B는 작아서 왼쪽으로 가야하면)
    인버젼(inversion) 교차했다는 뜻이므로 이를 카운팅 해준다
    '''

    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left_half, left_count = merge_sort_and_count(arr[:mid])
    right_half, right_count = merge_sort_and_count(arr[mid:])

    merged_arr = []
    inversion = left_count + right_count

    i = j = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            merged_arr.append(left_half[i])
            i += 1

        else:
            merged_arr.append(right_half[j])
            j += 1
            # 이때 왼쪽에 남아있는 개수들은 방금 비교한 왼쪽애들보다 큰 수임
            # 즉 그만큼 모두 인버젼된 애들이므로 카운팅해준다.
            inversion += len(left_half) - i

    merged_arr.extend(left_half[i:])
    merged_arr.extend(right_half[j:])

    return merged_arr, inversion

T = int(input())


for t in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]

    lst.sort(key=lambda x: x[0])

    B_lst = [l[1] for l in lst]

    _, cnt = merge_sort_and_count(B_lst)

    print(f"#{t} {cnt}")