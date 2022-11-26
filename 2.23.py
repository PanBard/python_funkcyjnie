def main():
    N = int(input("Generate pythagorean quartet in range 1 to N\n(Enter N): "))
    pythagorean_triples = [(a,b,c,d,e) for a in range(1,N) for b in range(a,N) for c in range(b,N) for d in range(c,N) for e in range(d,N) if (a**2 + b**2 + c**2 + d**2== e**2 )]
    print(pythagorean_triples)
    print("Program find",len(pythagorean_triples),"pythagorean quartet in 1 to",N,"range")

if __name__ == '__main__':
    main()