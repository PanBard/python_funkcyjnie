import itertools

def main():




    list_2 = ["elo","pamelo","romero"]
    list_3 = [11,12,13,45]
    ret_2 = list(itertools.permutations(list_2))
    print(ret_2)
    print("Amount of (permutations):", len(ret_2), "\n")

    word_1 = "ULAN"
    list_5 = [1,2,3,4]
    ret_3 = list(itertools.permutations(word_1))
    print(ret_3)
    print("Amount of (permutations):", len(ret_3), "\n")

if __name__ == '__main__':
    main()