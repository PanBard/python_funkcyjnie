import itertools

def main():
    print("~~Showing how count() function works~~")

    for x in itertools.count(1,3):
        print(x,end="|")
        if x > 30:
            break
if __name__ == '__main__':
    main()