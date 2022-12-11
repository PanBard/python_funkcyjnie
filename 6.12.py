import itertools
import functools
def main():


    list_2 = ["elo","pamelo","romero"]

    word_1 = "ULAN"

    print(list(itertools.chain(list_2,word_1)))

if __name__ == '__main__':
    main()