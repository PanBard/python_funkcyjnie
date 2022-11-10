import random

def main():
    list_1 = []
    list_2 = []
    for x in range(10):
        rnd_num = random.randint(1,100)
        list_1.append(rnd_num)

    for x in range(10):
        rnd_num = "".join(random.choice("kuba" )for i in range(4))
        list_2.append(rnd_num)
    print(list_1)
    print(list_2)
    konkatenacja_list = list_2 + list_1
    print("Konkatenacja 2 list shown above: ", konkatenacja_list)


if __name__ == '__main__':
    main()
