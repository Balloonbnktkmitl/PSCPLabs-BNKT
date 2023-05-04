"""Ejudge"""
def main():
    """Quadrant"""
    numx = int(input())
    numy = int(input())
    if numx > 0 and numy > 0:
        print("Q1")
    elif numx < 0 and numy > 0:
        print("Q2")
    elif numx < 0 and numy < 0:
        print("Q3")
    elif numx > 0 and numy < 0:
        print("Q4")
    elif numx == 0 and numy == 0:
        print("O")
    elif numx == 0 and numy != 0:
        print("Y")
    elif numx != 0 and numy == 0:
        print("X")
main()

