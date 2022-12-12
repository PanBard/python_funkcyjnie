
def fast_index(a:float,n:int) -> float:
    if n == 0:
        return 1
    elif n%2 == 1:
        return a*fast_index(a,n-1)
    else:
        t = fast_index(a,n//2)
        return t*t

def main():
    a = 2 #number
    n = 8 #power

    print(f"{a}^{n}={fast_index(a,n)}")

if __name__ == '__main__':
    main()
