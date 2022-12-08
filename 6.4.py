import itertools

def main():
    print("~~Showing how cycle() function works~~")

    list_1 = ["a","l","e","jaja"]
    counter = 0
    for x in itertools.cycle(list_1):
        print(x,end="|")
        counter+=1
        if counter == 30:
            print("\ncounter =",counter)
            break
if __name__ == '__main__':
    main()