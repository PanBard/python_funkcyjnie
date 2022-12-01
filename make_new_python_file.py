
def return_new_name():
    new_file_name = ""

    with open("spis_tresci.txt", "r") as file:
        last_line = file.readlines()[-1]

    for x in last_line:
        if x != " ":
            new_file_name += x
        else:
            break

    return new_file_name

def make_new_python_file():
    file_name = return_new_name()
    file = f"./{file_name}.py"
    open(file, 'a').close()

def main():
    make_new_python_file()

if __name__ == '__main__':
    main()