arr = list(range(1, 11))


def recur(total, depth):
    if sum(total) > 10:
        return

    if depth == 10:
        if sum(total) == 10:
            print(*total)
        return

    # 원소를 넣은것
    recur(total + [arr[depth]], depth+1)
    # 원소를 넣지 않은것
    recur(total, depth+1)

recur([], 0)