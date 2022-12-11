import itertools
import functools
def main():


    list_2 = ["elo","pamelo","romero","sor","ekopol","erka"]

    condition = [0,1,1,0,0,0]
    print("List:",list_2)
    print("Condition:",condition)
    print(list(itertools.compress(list_2,condition)))

if __name__ == '__main__':
    main()