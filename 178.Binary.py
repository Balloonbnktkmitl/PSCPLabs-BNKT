"""Ejudge"""
def main():
    """Binary"""
    num = int(input())
    ans = ""
    if num == 0:
        print(0)
    while num > 0:
        if num % 2 == 0:
            ans += "0"
        else:
            ans += "1"
        num //= 2
    print(ans[::-1])
main()

