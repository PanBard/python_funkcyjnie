import random

def find_min_and_max_in_list(name_list):
    print("Max value:",max(name_list))
    print("Min value:",min(name_list))

def generate_list():
    list_with_rand_numbers = []
    for x in range(100):
        list_with_rand_numbers.append(random.randint(1,1000))
    print("Generate list: \n",list_with_rand_numbers)
    return list_with_rand_numbers

def main():


    find_min_and_max_in_list(generate_list())

if __name__ == '__main__':
    main()