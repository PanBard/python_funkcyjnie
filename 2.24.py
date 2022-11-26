
class ManagerFiles:
    file_name = "txt_folder/2_24.txt"

    def save_list_in_txt_file(self,list_1):
        with open(self.file_name,'w') as file:
            file.write(str(list_1))

    def read_list_from_txt_file(self):
        with open(self.file_name,'r') as file:
            list_2 = eval(file.read())
        return list_2

def main():
    list_1 = [5,4,6,7,8,3,5,6]
    print(f"List to save: {list_1}")
    mf = ManagerFiles()
    mf.save_list_in_txt_file(list_1)
    list_2 = mf.read_list_from_txt_file()
    print(f"Read list: {list_2}")
    print("Sum numbers in list:",sum(list_2))

if __name__ == '__main__':
    main()