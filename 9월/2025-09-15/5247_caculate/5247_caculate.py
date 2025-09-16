import sys
sys.stdin = open("input.txt")
from collections import deque

def bfs(start_num):
    q = deque([(start_num, 0)])
    # 방문한 숫자를 기록하여 중복 계산 방지
    visited = {start_num}

    while q:
        current_num, cnt = q.popleft()

        if current_num == M:
            return cnt

        next_cnt = cnt + 1

        # +1 연산 : 결과가 자연수이면서 1000000이하여야하고, 계산했던 그결과가 아니어야함
        next_num = current_num + 1
        if 0 < next_num <= 1000000 and next_num not in visited:
            visited.add(next_num)
            q.append((next_num, next_cnt))

        # -1 연산 : 결과가 자연수이면서 1000000이하여야하고, 계산했던 그결과가 아니어야함
        next_num = current_num - 1
        if 0 < next_num <= 1000000 and next_num not in visited:
            visited.add(next_num)
            q.append((next_num, next_cnt))

        # *2 연산 : 결과가 자연수이면서 1000000이하여야하고, 계산했던 그결과가 아니어야함
        next_num = current_num * 2
        if 0 < next_num <= 1000000 and next_num not in visited:
            visited.add(next_num)
            q.append((next_num, next_cnt))

        # 4. -10 연산 : 결과가 자연수이면서 1000000이하여야하고, 계산했던 그결과가 아니어야함
        next_num = current_num - 10
        if 0 < next_num <= 1000000 and next_num not in visited:
            visited.add(next_num)
            q.append((next_num, next_cnt))

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())

    print(f"#{t} {bfs(N)}")



