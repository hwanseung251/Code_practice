import sys
sys.stdin = open("input.txt")


def find_set(x):
    """
    집합의 대표자를 찾는다
    """
    # 만약 나의 대표가 내가 아니면
    if parent[x] != x:
        # 내 대표자를 계속 타고타고 올라가면서 대표자를 찾는다
        # 재귀를 통해 경로 압축하는 코드!! 다음번에 find_set(x)호출하면 바로 한번에 도달 가능
        parent[x] = find_set(parent[x])
    # 대표자는 대표가 자신임. 그것을 반환
    return parent[x]


def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    # 이미 같은 집합안에 속함
    if root_x == root_y:
        return

    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    else:
        parent[root_y] = root_x
        if rank[root_x] == rank[root_y]:
            # root_y가 대빵되는 상황이니까 root_x에 랭크 1을 줌
            rank[root_x] += 1


T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    students = list(map(int, input().split()))

    # 학생은 1~N
    # 학생 모두를 각자 자기 자신이 대표인 집합으로 만듬
    parent = list(range(N + 1))
    # 모든 원소의 랭크를 0으로 초기화
    rank = [0] * (N + 1)

    for i in range(M):
        p1, p2 = students[i*2], students[i*2 + 1]
        union(p1, p2)

    # 최종 수 = 대표자의 수
    root_nodes = set()
    for i in range(1, N+1):
        root_nodes.add(find_set(i))


    print(f"#{t} {len(root_nodes)}")