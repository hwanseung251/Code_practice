import sys
sys.stdin = open("input.txt")

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    n_list = list(map(int, input().split()))
    m_list = list(map(int, input().split()))

    # 각 리스트를 내림차순으로 정렬한다. (큰값부터 고려하기 위해)
    n_list.sort(reverse=True)
    m_list.sort(reverse=True)

    # 화물을 지정해줄 포인트 역할
    n_point = 0
    # 트럭이 물건을 싣고가면 무게 추가
    result = 0
    for i in range(M):
        # 현재 화물 포인트가 화물의 개수를 초과하지 않으면 반복
        while n_point < N:
            # 못싣는 화물무게면 다음 화물로 이동
            if m_list[i] < n_list[n_point]:
                n_point += 1
            else:
                # 가능하면 싣고 반복문 중단하고 다음 트럭으로 이동
                result += n_list[n_point]
                n_point += 1
                break

    print(f"#{t} {result}")