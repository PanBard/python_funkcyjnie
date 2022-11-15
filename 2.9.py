def insert_to_list(searches_element, name_list):
    if searches_element in name_list:
        print("List before change: ",name_list)
        name_list.remove(searches_element)
        print("List after change: ",name_list)
    else:
        print("There is no word in that list!")

def main():
    name_list = ["Lubomiła","Jacek","elok","mok","opol"]
    old_word = input(f"Which word you wolud like to remove in list above?\n{name_list}\n(enter name):")
    insert_to_list(old_word,name_list)

if __name__ == '__main__':
    main()