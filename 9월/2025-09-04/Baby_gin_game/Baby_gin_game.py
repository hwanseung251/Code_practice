import sys
sys.stdin = open("input.txt")
import itertools


def is_run(arr):
    return arr[0]+1 == arr[1] and arr[1]+1 == arr[2]


def is_triplet(arr):
    return len(set(arr)) == 1


T = int(input())

for t in range(1, T+1):
    cards = list(map(int, input()))
    is_babygin = False

    # 순열을 활용한 그룹나누기
    for p in set(itertools.permutations(cards)):
        group1 = sorted(list(p[:3]))
        group2 = sorted(list(p[3:]))

        check1 = is_run(group1) or is_triplet(group1)
        check2 = is_run(group2) or is_triplet(group2)

        if check1 and check2:
            is_babygin = True
            break

    print(f"#{t} {is_babygin}")

    # 조합을 활용한 그룹나누기
    for group1_indices in itertools.combinations(range(6), 3):
        group1 = [cards[i] for i in group1_indices]
        group2_indices = list(set(range(6)) - set(group1_indices))
        group2 = [cards[i] for i in group2_indices]

        check1 = is_run(group1) or is_triplet(group1)
        check2 = is_run(group2) or is_triplet(group2)

        if check1 and check2:
            is_babygin = True
            break

    print(f"#{t} {is_babygin}")

