import math

def quadratic_equation(a,b,c):

    if a == 0:
        print("You entered the wrong value a=0, co this is no a quadratic equation")
    else:
        discriminant = b**2 - 2*a*c

        if discriminant < 0:
            print("Discriminant of this function is ",discriminant, "so we dont have zero of a function")
        elif discriminant == 0:
            x1 = -b/(2*a)
            print("Discriminant of this function is ", discriminant, "so we have one double zero of a function x1= ",x1)
        else:
            x1 = -b - math.sqrt(discriminant) / (2 * a)
            x2 = -b + math.sqrt(discriminant) / (2 * a)
            print("Discriminant of this function is ", discriminant, "so we have two zero of a function x1=", x1,"and x2=",x2)

def main():
    (a,b,c,) = (6,9,4,)
    quadratic_equation(a,b,c)

if __name__ == '__main__':
    main()

