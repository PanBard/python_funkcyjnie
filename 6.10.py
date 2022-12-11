import itertools

def main():


    list_2 = ["elo","pamelo","romero"]
    print(list_2)
    ret_2 = list(itertools.accumulate(list_2))
    print(ret_2)
    print("Amount of (permutations):", len(ret_2), "\n")

    word_1 = "ULAN"
    print(word_1)
    ret_3 = list(itertools.accumulate(word_1))
    print(ret_3)
    print("Amount of (permutations):", len(ret_3), "\n")

if __name__ == '__main__':
    main()