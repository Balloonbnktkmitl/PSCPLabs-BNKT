"""Ejudge"""
def main():
    """BMI"""
    bmi(input(), float(input()), float(input()))
    bmi(input(), float(input()), float(input()))
    bmi(input(), float(input()), float(input()))
    bmi(input(), float(input()), float(input()))
    bmi(input(), float(input()), float(input()))
def bmi(name, weight, height):
    """BMI"""
    bmi1 = weight / ((height/100)**2)
    print("%s's  BMI = %.2f" %(name, bmi1))
main()

