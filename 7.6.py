
def fibb(n:int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    f_n2,f_n1 = 1,1
    for _ in range(3, n+1):
        f_n2,f_n1 = f_n1,f_n2+f_n1
    return f_n1

def main():
    i = 1000

    print(f"fibbonaci({i})={fibb(i)}")

if __name__ == '__main__':
    main()
