def cubic(x):
    return x**3


def main():
    F=1
    N=10
    print(f"\nList with map value from range [{F}-{N}]:")
    cubic_numbers = list(map(cubic,range(F,N)))
    print(cubic_numbers)

if __name__ == '__main__':
    main()