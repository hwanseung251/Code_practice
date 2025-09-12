import sys
sys.stdin = open("input.txt")

T = int(input())

for t in range(1, T+1):
    day, month, month3, year = map(int, input().split())
    calender = [0] + list(map(int, input().split()))
    dp = [0] * 13

    # 1월과 2월은 각각 누적값을 구해놓는다
    dp[1] = min(day * calender[1], month)
    dp[2] = dp[1] + min(day * calender[2], month)

    # 3월부터 점화식처럼 누적값을 구해놓는다
    for m in range(3, 13):
        dp[m] = min(
            dp[m-3] + month3,
            dp[m-1] + month,
            dp[m-1] + day * calender[m]
        )
    # 최종 누적값이 있는 dp 12월과 year가격과 비교해서 최종값을 갱신한다
    answer = min(dp[12], year)
    print(f"#{t} {answer}")