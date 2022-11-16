def main():
    N = int(input("Generate pythagorean triple in range 1 to N\n(Enter N): "))
    pythagorean_triples = [(a,b,c) for a in range(1,N) for b in range(a,N) for c in range(b,N) if (a**2 + b**2 == c**2)]
    print(pythagorean_triples)
    print("Program find",len(pythagorean_triples),"pythagorean triples in 1 to",N,"range")

if __name__ == '__main__':
    main()