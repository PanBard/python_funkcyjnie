import random

def main():
    list_1 = []
    list_2 = []
    for x in range(10):
        rnd_num = random.randint(1,100)
        list_1.append(rnd_num)

    for x in range(10):
        rnd_num = "".join(random.choice("abecadlo" )for i in range(7))
        list_2.append(rnd_num)

    print("Before sorting:")
    print(list_1)
    print(list_2,"\n")
    print("After sorting:")
    sort_1 = list_1.sort()
    sort_2 = list_2.sort()
    print(list_1)
    print(list_2, "\n")


if __name__ == '__main__':
    main()
