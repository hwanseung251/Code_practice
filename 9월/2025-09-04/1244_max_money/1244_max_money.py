import sys
sys.stdin = open("input.txt")

T = int(input())

for t in range(1,T+1):
    cards, N = input().split()
    N = int(N)

    cards = list(cards)
    sort_cards = cards[:]
    sort_cards.sort()
    max_card = sort_cards[-1]

