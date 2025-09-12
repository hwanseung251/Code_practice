arr = list(range(1, 11))

def subset_recur(depth, cur):
    if sum(cur) == 10:
        print(*cur)
        return
    if sum(cur) > 10:
        return

    if depth == len(arr):
        return

    subset_recur(depth+1, cur + [arr[depth]])
    subset_recur(depth+1, cur)

subset_recur(0, [])