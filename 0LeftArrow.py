"""Ejudge"""
def main():
    """LeftArrow"""
    size = int(input())
    high = int(input())
    tmp = int(high/2)
    for i in range(high):
        if i < high/2:
            print(" "*(tmp)+"*"*size)
            tmp -= 1
        else:
            if tmp < 0:
                tmp = 0
            tmp += 1
            print(" "*(tmp)+"*"*size)
main()
