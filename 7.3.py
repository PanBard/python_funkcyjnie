
def search_list(serch_list,target,position):
    if serch_list[position]== target:
        print("Target found!! in position:",position)
    elif position == len(serch_list) - 1:
        print("Target not found!")
    else:
        return search_list(serch_list,target,position+1)

def main():

    list_1 = [12,23,434,11234,124,3214,123,23,142,15,2,3,4,5,6,5,4,3,22,2]

    search_list(list_1,15,0)

if __name__ == '__main__':
    main()

