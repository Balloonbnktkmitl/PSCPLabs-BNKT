"""Ejudge"""
def main():
    """All_primes"""
    num = int(input())
    ans = 0
    for i in range(2, num+1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            ans += 1
    print(ans)
main()
