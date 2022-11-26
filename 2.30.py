def print_strange_sequence(N):
    for x in range(1,N+1):
        if x==1:
            print(x,end="",sep="")
        elif((2*x-1) > 0):
            print("+",2*x-1,end="",sep="")
        else:
            print(2*x-1,end="", sep="")
    print()

def sum_of_strange_sequence(N):
    return sum(map(lambda x: 2*x-1, range(1,N+1)))


def main():
    N=100
    print("Dla N=",N)
    print_strange_sequence(N)
    print("Sum of this sequence:",sum_of_strange_sequence(N))




if __name__ == '__main__':
    main()