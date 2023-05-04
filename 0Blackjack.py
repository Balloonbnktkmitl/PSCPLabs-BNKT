"""Ejudge"""
def main():
    """Blackjack"""
    numcard = int(input())
    point = 0
    tmp = 0
    for i in range(numcard):
        i = i
        card = input()
        if card in "JQKjqk":
            point += 10
        elif card in "Aa":
            tmp += 1
        else:
            point += int(card)
    while tmp > 0:
        tmp -= 1
        if point + 11 > 21:
            point += 1
        elif point == 10 and tmp == 1:
            point += 1
        else:
            point += 11
    print(point)
main()

