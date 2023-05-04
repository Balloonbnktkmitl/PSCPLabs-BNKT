"""Ejudge"""
def main():
    """Future Message"""
    mess = input()
    if mess.istitle() == True:
        print("Title")
    elif mess.isupper() == True:
        print("Uppercase")
    elif mess.islower() == True:
        print("Lowercase")
    elif mess.isdigit() == True:
        print("Number")
    elif mess.isspace() == True:
        print("Space")
    else:
        print("Other")
main()
