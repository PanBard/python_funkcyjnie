import os
import pathlib
import glob


class NewPythonFileMaker:
    parent_directory = str(pathlib.Path(__file__).parent.resolve()) + "\\" + "*.py"
    directory_for_new_folder = str(pathlib.Path(__file__).parent.resolve()) + "\\" +"txt_folder"
    if not os.path.exists(directory_for_new_folder):
        os.mkdir(directory_for_new_folder)

    def make_new_python_file(self):
        all_name_list = self.return_list_of_all_number_file()
        final_file_name = self.extract_last_name_file(all_name_list)
        file = f"./{final_file_name}.py"
        open(file, 'a').close()

    def insert_dot(self,string):
        return string[:1] + '.' + string[1:]

    def return_list_of_all_number_file(self):
        list_file = glob.glob(self.parent_directory)
        new_list_file=[]
        for x in range(len(list_file)-1):
            basename = os.path.splitext(os.path.basename(list_file[x]))[0]
            word = basename.replace('.','')
            nmbr = int(word)
            new_list_file.append(nmbr)
        return new_list_file

    def extract_last_name_file(self,new_list_file):
        kolo = new_list_file.sort()
        index = len(new_list_file) - 1
        old_name_file = new_list_file[index]
        new_name_file = old_name_file + 1
        name = self.insert_dot(str(new_name_file))
        return name


def main():
    m = NewPythonFileMaker()
    m.make_new_python_file()


if __name__ == '__main__':
    main()