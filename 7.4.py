
def hidden_factorial(N,acum):
    if N==0:
        return acum
    else:
        return hidden_factorial(N-1,N*acum)

def factorial(N:int) -> int:
    return hidden_factorial(N,1)

def main():
    N = 20

    print(f"Result of factorial of {N}! = {factorial(N)}  ")

if __name__ == '__main__':
    main()
