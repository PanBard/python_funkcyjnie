def sum_list(list):
    sum1 = 0
    sum2 = 0

    for x in list:
            sum1 = sum1+x
    print("suma1 - imperativ",sum1)

    for x in range(len(list)):
        sum2 = sum2 + list[x]
    print("suma2 - imperativ",sum2)


def main():

    numbers_list = [2,23,4,2,3,323,3,34,354,3]
    print("Sum of list : ",numbers_list,"in 2 wawys")
    sum_list(numbers_list)
    print("Sum with build function 'sum': ",sum(numbers_list))

if __name__ == '__main__':
    main()