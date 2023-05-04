"""Ejudge"""
def main():
    """EuclideanDistance2D"""
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    num4 = float(input())
    print(euclidean_distance(num1, num2, num3, num4))
def euclidean_distance(num1, num2, num3, num4):
    """EuclideanDistance2D"""
    return ((num1-num3)**2+(num2-num4)**2)**0.5
main()

