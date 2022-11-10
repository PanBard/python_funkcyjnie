def fibonacci(N):
    num1 = 0
    num2 = 1

    for x in range(N):
        print(num1,end=" ")
        num1,num2 = num2,num2+num1

def main():
    fibonacci(10)

if __name__ == '__main__':
    main()
