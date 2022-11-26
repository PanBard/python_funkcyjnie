import functools
def suma(x,y):
    return x+y



def main():

    print("Sum of number 1 - 100:" , functools.reduce(suma,range(1,101)) )

if __name__ == '__main__':
    main()


