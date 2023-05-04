"""Ejudge"""
def main():
    """Timing"""
    time = int(input())
    day = time//86400
    hours = time%86400
    hours = hours//3600
    minutes = time%3600
    minutes = minutes//60
    second = time%60
    print("%d %d %d %d" %(day, hours, minutes, second))
main()

