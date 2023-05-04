"""Ejudge"""
def main():
    """BrickBridge"""
    small = int(input())
    big = int(input())
    goal = int(input())
    if (big*5) + small < goal or big%5 > small:
        print(-1)
    else:
        if big*5 >= goal:
            print(goal%5)
        else:
            print(goal-(big*5))
main()
