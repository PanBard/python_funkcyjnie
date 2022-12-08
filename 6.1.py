import operator

def main():
    print("operator.sub(30,20) =",operator.sub(30,20))


    print("~~Multiplications of lists~~")
    list_1 = [1,2,3,4,5,6]
    list_2 = [7,8,9,10,11,12]
    result = []

    print("List 1:", list_1)
    print("List 2:", list_2)

    for x in range(len(list_1)):
        result.append(list_1[x]*list_2[x])

    print("Naive approach:",result)
    result_2 = list(map(operator.mul , list_1,list_2))
    print("Functional approach:",result_2)

if __name__ == '__main__':
    main()