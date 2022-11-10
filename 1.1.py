def sum_list(list):
    sum1 = 0
    sum2 = 0

    for x in list:
            sum1 = sum1+x
    print("suma1",sum1)

    for x in range(len(list)):
        sum2 = sum2 + list[x]
    print("suma2",sum2)
    return sum

def main():

    numbers_list = [2,23,4,2,3,323,3,34,354,3]
    print("Sum of list : ",numbers_list,"in 2 wawys")
    print(sum_list(numbers_list))
    print("Check with build function: ",sum(numbers_list))

if __name__ == '__main__':
    main()