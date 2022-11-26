def main():
    F=1
    N=10
    print(f"\nList with map value from range [{F}-{N}]:")
    f = lambda x: x**3
    cubic_numbers = list(map(f,range(F,N)))
    print(cubic_numbers)

if __name__ == '__main__':
    main()