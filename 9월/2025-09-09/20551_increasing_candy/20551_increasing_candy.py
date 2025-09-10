import sys
sys.stdin = open("input.txt")

T = int(input())

for t in range(1, T+1):
    A, B, C = map(int, input().split())

    cnt = 0
    # 불가능을 표시하는 변수
    cant = False

    # B가 C보다 같거나 크면 먹어야함
    if C <= B:
        # 다음을 고려해 2보다 같거나 커야함
        if C - 1 >= 2:
            # 먹은만큼 카운팅하고 B변수 재할당
            cnt += B-C+1
            B = C - 1
        else:
            # 불가능
            cant = True

    # A도 같은 방법으로
    if not cant and B <= A:
        if B - 1 >= 1:
            cnt += A-B+1
        else:
            cant = True


    print(f"#{t} {-1 if cant else cnt}")

