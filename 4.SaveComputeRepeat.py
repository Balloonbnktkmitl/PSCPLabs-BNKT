"""Ejudge"""
def main():
    """SaveComputeRepeat"""
    start_here = 492137954293754252786
    millilseconds = start_here
    seconds = millilseconds // 1000
    millilseconds = millilseconds % 1000
    minutes = seconds // 60
    seconds = seconds % 60
    hours = minutes // 60
    minute = minutes % 60
    days = hours // 24
    hours = hours % 24
    print("%d %d %d %d %d" %(days, hours, minute, seconds, millilseconds))
main()

