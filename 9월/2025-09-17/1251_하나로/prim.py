import sys
sys.stdin = open("input.txt")


T = int(input())
INF = float("inf")
for t in range(1, T+1):
    N = int(input())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    tax = float(input())

    # 각 노드들 좌표를 (x,y)로 가지게끔 변경
    island = list(zip(x_list, y_list))

    # MST 만들면서 이미 정한 노드인지 아닌지 확인하기 위한 자료구조
    visited = [False] * N
    # 가중치를 따로 계산해야 되기 때문에 그때그때 계산하면서 작은 가중치로 저장할 자료구조
    min_costs = [INF] * N

    # 0노드부터 시작
    min_costs[0] = 0
    # MST의 최종 결과
    result_cost = 0

    for _ in range(N):
        min_cost = INF
        min_node = -1
        # 모든 노드를 순환하면서
        # 방문 하지 않았고(간선을 연결하지 않았고) 현재 가장 효율적인 cost를 가진다면
        for i in range(N):
            if not visited[i] and min_costs[i] < min_cost:
                min_cost = min_costs[i]
                min_node = i

        # 방문처리(간선 연결)하고
        visited[min_node] = True
        # 최종 값에 cost 더해준다
        result_cost += min_cost

        # 방금 방문처리를 한 노드와 다른 모든 노드들끼리의 가중치를 하나씩 계산해보면서
        for i in range(N):
            if not visited[i]:
                cost = tax * ((island[min_node][0] - island[i][0])**2 + (island[min_node][1] - island[i][1])**2)
                # 전노드와 다른노드들과의 가중치가 저장된 min_costs에서 방금 방문처리를 한 노드와 다른노드들과의 가중치를 비교해서
                # 더 작은 가중치값을 저장
                # 즉 다른노드들로 가는 가장 효율적인 가중치가 저장됨
                min_costs[i] = min(min_costs[i], cost)

    print(f"#{t} {result_cost:.0f}")