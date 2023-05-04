"""Ejudge"""
def jumping():
    """Jumping"""
    num = 1
    while num < 5:
        i = 0
        while i < 3:
            print_output(num)
            i += 1
        num += 1
def print_output(num):
    """print_output"""
    print("Output%d" %(num))
jumping()

