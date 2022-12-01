
def main():
    file_name = "3_12.txt"
    new_tuple = (1,2,3,4,)
    print("Tuple before save to file: ",new_tuple)

    with open(f"./txt_folder/{file_name}","w") as file:
        file.write(str(new_tuple))

    read_tuple = ()
    with open(f"./txt_folder/{file_name}","r") as file:
        read_tuple = eval(file.read())

    print("Read from file tuple: ",read_tuple)
if __name__ == '__main__':
    main()