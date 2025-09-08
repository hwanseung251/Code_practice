import sys
sys.stdin = open("input.txt")


def is_win(arr):
    for i in range(10):
        if arr[i] >= 3:
            return True

        if i < 8:
            if arr[i] and arr[i+1] and arr[i+2]:
                return True
    return False


T = int(input())

for t in range(1, T+1):
    cards = list(map(int, input().split()))

    player1 = [0] * 10
    player2 = [0] * 10

    for i in range(6):
        # 카운팅 정렬
        player1[cards[i*2]] += 1
        player2[cards[i*2+1]] += 1
        # 2미만이면 continue
        if i < 2:
            continue
        # player1부터 순차적으로 검사
        if is_win(player1):
            print(f"#{t} 1")
            break
        elif is_win(player2):
            print(f"#{t} 2")
            break
    else:
        print(f"#{t} 0")

