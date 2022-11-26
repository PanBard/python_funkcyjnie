def main():
    F=10
    N=25
    print(f"\nFilter of prime numbers from range [{F}-{N}]:")
    f = lambda x: x%2 !=0 and x%3 != 0
    primary_numbers = list(filter(f,range(F,N)))
    print(primary_numbers)

if __name__ == '__main__':
    main()