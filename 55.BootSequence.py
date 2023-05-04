"""Ejudge"""
def main():
    """BootSequence"""
    num = int(input())
    for i in range(num):
        if i+1 == num:
            print(i+1, end="")
        else:
            print(i+1, end="_")
main()

