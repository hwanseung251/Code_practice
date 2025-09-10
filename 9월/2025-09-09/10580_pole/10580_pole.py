import sys
sys.stdin = open("input.txt")

T = int(input())

for t in range(1, T+1):
    N = int(input())
    lst = []
    for i in range(N):
        lst.append(list(map(int, input().split())))
    # 교차점의 개수 카운팅
    cnt = 0
    for i in range(N):
        # 맨위 전선
        A1, B1 = lst[i][0], lst[i][1]
        for j in range(i+1, N):
            # 아래 전선들
            A2, B2 = lst[j][0], lst[j][1]
            # 교차점 계산
            if A1 > A2 and B1 < B2:
                cnt += 1
            elif A1 < A2 and B1 > B2:
                cnt += 1

    print(f"#{t} {cnt}")