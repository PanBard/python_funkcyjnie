def main():
    my_list = list(range(1,10,2))
    print("This list is created by function 'list()' and 'range()': ", my_list)
    print(f"Lenght list: {len(my_list)}")

    print("Simple iterate by list with 'for loop': ")
    for x in my_list:
        print(x)

    print("Use for loop for iterate by list with 'len()' index:")
    for x in range(len(my_list)):
        print(f"my_list[{x}]={my_list[x]}")



if __name__ == '__main__':
    main()