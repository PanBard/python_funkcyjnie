def main():

    list_num = [1,3,2,3,4,5,5,54,5,5]
    print("This is a simple list:", list_num)
    tuple_krotka = tuple(list_num)
    print("This is a tuple rom list above:",tuple_krotka)
    new = list(tuple_krotka)
    print("again list:",new)

if __name__ == '__main__':
    main()