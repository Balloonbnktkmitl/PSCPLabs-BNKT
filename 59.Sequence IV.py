"""Ejudge"""
def main():
    """Sequence IV"""
    num = int(input())
    rnd = 1
    for i in range(1, num+1):
        i = i
        for j in range(1, num+1):
            j = j
            print(rnd, end=" ")
            rnd += 1
        print()
main()
