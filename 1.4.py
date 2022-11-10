def fibonacci(N):
    if N <=1:
        return N
    else:
        return fibonacci(N-2) + fibonacci(N-1)

def main():
    for x in range(10):
        print(fibonacci(x),end=" ")

    

if __name__ == '__main__':
    main()
