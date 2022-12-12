
def ackermann(j,k):
    if j == 0:
        return k+1
    if j > 0 and k==0:
        return ackermann(j-1,1)
    if j>0 and k>0: return ackermann(j-1,ackermann(j,k-1))

def main():
    m=3
    n=4

    print(f"Ackermann's function for m={m} and n={n} = {ackermann(m,n)}")

if __name__ == '__main__':
    main()
