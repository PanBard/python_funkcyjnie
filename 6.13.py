import itertools
import functools
def main():


    list_2 = ["elo","pamelo","romero"]

    word_1 = "ULAN"

    numbers = [123,4556,674,1,2,3,4,54]

    print(list(itertools.chain(list_2,word_1,numbers)))

if __name__ == '__main__':
    main()