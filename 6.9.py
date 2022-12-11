import itertools

def main():
    r = 2

    list_2 = ["elo","pamelo","romero"]
    list_3 = [11,12,13,45]
    ret_2 = list(itertools.combinations_with_replacement(list_2,r))
    print(ret_2)
    print("Amount of (permutations):", len(ret_2), "\n")

    word_1 = "ULAN"
    list_5 = [1,2,3,4]
    ret_3 = list(itertools.combinations_with_replacement(word_1,r))
    print(ret_3)
    print("Amount of (permutations):", len(ret_3), "\n")

if __name__ == '__main__':
    main()