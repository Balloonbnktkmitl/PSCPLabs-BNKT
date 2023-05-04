"""Ejudge(Midterm)"""
def main():
    """Meteorite"""
    weight = float(input())
    metrobreak = int(input())
    save = float(input())
    metro = 1 
    shoot = 0
    while weight >= save:
        shoot += metro
        metro = metrobreak*metro
        weight /= metrobreak
    print(shoot)
main()

