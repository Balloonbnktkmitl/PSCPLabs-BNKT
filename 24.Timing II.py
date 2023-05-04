"""Ejudge"""
def main():
    """Timing II"""
    time = int(input())
    day = time//86400
    hours = time%86400
    hours = hours//3600
    minutes = time%3600
    minutes = minutes//60
    second = time%60
    if len(str(day)) > 4 or len(str(hours)) > 2 or len(str(minutes)) > 2 or len(str(second)) > 2:
        print("ERR_:__:__:__")
    else:
        print("%04d:%02d:%02d:%02d" %(day, hours, minutes, second))
main()
