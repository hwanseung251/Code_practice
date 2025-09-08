import sys
sys.stdin = open("input.txt")


T = int(input())

for t in range(1, T+1):
    N = int(input())
    carrots = list(map(int, input().split()))

    ## 같은 숫자 묶음 찾기
    counting_list = [0] * 31
    for carrot in carrots:
        counting_list[carrot] += 1

    bundle = [i for i in range(1, 31) if counting_list[i] != 0]
    max_bundle = max(counting_list)

    if max_bundle > N//2:
        print(f"#{t} -1")
        continue

    INF = float("inf")
    min_value = INF

    # 몇 종류가 있냐
    bun_len = len(bundle)

    # 당근 종류 별로 3박스로 구분
    for i in range(1, bun_len-1):
        for j in range(i+1, bun_len):
            # 각각 박스의 담긴 총 당근 수
            sm = sum([counting_list[b] for b in bundle[:i]])
            md = sum([counting_list[b] for b in bundle[i:j]])
            lg = sum([counting_list[b] for b in bundle[j:]])

            if max(sm, md, lg) > N//2:
                continue

            diff = max(sm, md, lg) - min(sm, md, lg)
            min_value = min(min_value, diff)

    print(f"#{t} {-1 if min_value == INF else min_value}")

