"""Ejudge"""
def main():
    """Elo"""
    numra = int(input())
    numrb = int(input())
    people = input()
    calea = 1/(1+10**((numrb-numra)/400))
    caleb = 1/(1+10**((numra-numrb)/400))
    if people == "A":
        print("%.2f" %(calea))
    elif people == "B":
        print("%.2f" %(caleb))
main()

