
def add(a,b):
    if a == 0:
        return b
    else:
        return add(a-1,b+1)

def main():

    print(add(4,5))

if __name__ == '__main__':
    main()

