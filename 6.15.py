import itertools
import functools
def main():

    list_1 = [2,4,5,7,9,10,11]
    print("List:",list_1)

    print(list(itertools.dropwhile(lambda x : x%2==0, list_1)))

if __name__ == '__main__':
    main()