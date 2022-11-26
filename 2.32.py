import functools
import math

def e(n):
    return functools.reduce(lambda x,y: (x[0]+x[1],x[1]/y),range(1,n),(0,1.0))



def main():

    print("Constant e from our function" , e(20))
    print("Constant e from math", math.e)

if __name__ == '__main__':
    main()


