import sys
sys.stdin = open("input.txt")


def recur(station, cur_cnt):
    global min_value
    if min_value <= cur_cnt:
        return

    if station >= len(bus_stop):
        min_value = min(min_value, cur_cnt)
        return

    for i in range(station + 1, station + bus_stop[station] + 1):
        recur(i, cur_cnt+1)

T = int(input())

for t in range(1, T+1):
    bus_stop = list(map(int, input().split()))
    min_value = 100 * len(bus_stop)

    recur(1, 0)
    # 출발지 배터리 장착은 제외하니까 min_value - 1
    print(f"#{t} {min_value-1}")