"""Ejudge"""
def main():
    """3nPlus1"""
    while True:
        ans = 1
        num = int(input())
        if num == 0:
            break
        while num > 1:
            if num % 2 == 0:
                num //= 2
            else:
                num = num*3 + 1
            ans += 1
        print(ans)
main()
