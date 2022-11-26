def print_strange_sequence(N):
    for x in range(1,N+1):
        if x==1:
            print(x,end="",sep="")
        elif(((1-2*(x%2))*x +2) > 0):
            print("+",(1-2*(x%2))*x,end="",sep="")
        else:
            print((1 - 2 * (x % 2)) * x,end="", sep="")
    print()

def sum_of_strange_sequence(N):
    return sum(map(lambda x: (1 - 2 * (x % 2)) * x , range(1,N+1)))+2


def main():
    N=100
    print("Dla N=",N)
    print_strange_sequence(N)
    print("Sum of this sequence:",sum_of_strange_sequence(N))




if __name__ == '__main__':
    main()