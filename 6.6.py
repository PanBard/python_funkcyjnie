import itertools

def main():

    NUMBER = 3
    list_1 = [1,2,3]

    for x in range(1,NUMBER+1):
        ret = list(itertools.product(list_1,repeat=x))
        print(ret)
        print("Amount of new tuple:", len(ret),"\n")


    list_2 = ["elo","pamelo","romero"]
    list_3 = [11,12,13,45]
    ret_2 = list(itertools.product(list_2,list_3 ))
    print(ret_2)
    print("Amount of new tuple:", len(ret_2), "\n")

    word_1 = "ULAN"
    list_5 = [1,2,3,4]
    ret_3 = list(itertools.product(word_1, list_5))
    print(ret_3)
    print("Amount of new tuple:", len(ret_3), "\n")

if __name__ == '__main__':
    main()