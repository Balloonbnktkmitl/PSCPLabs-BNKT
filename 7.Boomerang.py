"""Ejudge"""
def main():
    """Boomerang"""
    numx = int(input())
    numy = int(input())
    numz = int(input())
    funcx(numx)
    funcy(numy)
    funcz(numz)
    funcxy(numx, numy)
    funcxyz(numx, numy, numz)
def funcx(numx):
    """funcx"""
    print(numx+1)
def funcy(numy):
    """funcy"""
    print((7*(numy**3))+(2*(numy**2))-(31*numy)+1)
def funcz(numz):
    """funcz"""
    print(-numz)
def funcxy(numx, numy):
    """funcxy"""
    print((numx+numy)*(numx-numy))
def funcxyz(numx, numy, numz):
    """funcxyz"""
    print((numy-(((numy**2)-(4*numx*numz))**(1/2)))/(2*numx))
main()

