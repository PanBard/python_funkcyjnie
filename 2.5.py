import random

def generate_numbers_in_list(numbers):
    my_list = []
    for x in range(numbers):
        rand_num = random.randint(1,100)
        my_list.append(rand_num)
    return my_list

def find_numbers(number, black_list):
    if number in black_list:
        return True
    else:
        return False

def main():
    while True:
        find_num = int(input("Enter numer, and we check if it has place in ours list: "))
        list_1 = generate_numbers_in_list(100)
        if find_numbers(find_num,list_1):
            print(f"Number {find_num} is in our list!!!!!")
            print(f"Yours number is {list_1.index(find_num)+1} on list")
            print(f"list_1[{list_1.index(find_num)}]={list_1[list_1.index(find_num)]}")
            break
        else:
            print(f"Number {find_num} unfortunately is not in the list :( ")
    print("\nEnd program")
if __name__ == '__main__':
    main()