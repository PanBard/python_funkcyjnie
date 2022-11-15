def insert_to_list(name_list):
        print("List before change: ",name_list)
        name_list.reverse()
        print("List after change (reverse): ",name_list)

def main():
    name_list = ["Lubomiła","Jacek","elok","mok","opol"]
    insert_to_list(name_list)

if __name__ == '__main__':
    main()