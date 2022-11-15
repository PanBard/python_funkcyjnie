def insert_to_list( name_list,index_number):
    index_number = int(index_number)
    if index_number <= (len(name_list)):
        new_name= input("Ok, now enter new word.\n(Enter new word): ")
        print("List before change: ",name_list)

        name_list.insert(index_number,new_name)
        print("List after change: ",name_list)
    else:
        print("Something wrong with index number!!!")

def main():
    name_list = ["Lubomiła","Jacek","elok","mok","opol"]
    index_number = (input(f"Where you wolud like to insert new word in list above?\n{name_list}\n(enter index number):"))
    insert_to_list(name_list,index_number)

if __name__ == '__main__':
    main()