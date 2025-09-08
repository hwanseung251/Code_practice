import sys
sys.stdin = open("input.txt")

T = int(input())

for t in range(1, T+1):
    N = int(input())

    time_arr = [list(map(int, input().split())) for _ in range(N)]

    # 끝나는 시간 기준으로 오름차순 정렬
    time_arr.sort(key = lambda x: x[1])

    # 가능한 화물 이용 횟수
    cnt = 0
    # 현재 시작점 포인트
    current_start = 0
    for i in time_arr:
        # 현재 시작포인트가 다음 화물차 이용 가능 시간보다 작으면
        if current_start <= i[0]:
            # 시직포인트를 다음 화물차 이용 끝나는 시간으로 갱신해주고
            current_start = i[1]
            # 횟수 카운팅
            cnt += 1
            continue

    print(f"#{t} {cnt}")