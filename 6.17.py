import itertools
import functools
def main():

    list_1 = [2,4,5,7,9,10,11]
    print("List:",list_1)

    print(list(itertools.islice(list_1,1,6,2)))

if __name__ == '__main__':
    main()