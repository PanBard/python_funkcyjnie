import itertools
import functools
def main():


    list_2 = ["elo","pamelo","romero"]
    print(list_2)
    ret_2 =list(itertools.accumulate(list_2))
    print("accumulate:")
    print(ret_2)
    print()

    ret_22 = functools.reduce(lambda x,y:x+y,list_2)
    print("reduce:")
    print(ret_22)
    print()


    word_1 = "ULAN"
    print(word_1)
    ret_3 =list(itertools.accumulate(word_1))
    print("accumulate:")
    print(ret_3)
    print()

    ret_3 = functools.reduce(lambda x,y:x+y,word_1)
    print("reduce):")
    print(ret_3)
    print()

if __name__ == '__main__':
    main()