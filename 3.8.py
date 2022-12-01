
def function(a,b):
    return (a+b)/2.0

def main():
    (a, b,) = (1.34, 3.43,)
    print(type(a),a)
    print(type(b),b)
    print(type((a, b,)))
    print("Function: ",function(a,b))




if __name__ == '__main__':
    main()

