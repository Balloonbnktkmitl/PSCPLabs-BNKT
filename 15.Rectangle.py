"""Ejudge"""
def main():
    """Rectangle"""
    height = int(input())
    weight = int(input())
    print(area(height, weight))
    print(length(height, weight))
def area(height, weight):
    "area"
    area4 = height*weight
    return area4
def length(height, weight):
    "length"
    length4 = 2*(height+weight)
    return length4
main()

