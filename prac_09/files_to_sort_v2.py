import shutil
import os


def main():
    os.chdir('FilesToSort2')
    print("Starting directory is: {}".format(os.getcwd()))
    file_catagories = {}
    filenames = os.listdir('.')
    for filename in filenames:
        if os.path.isdir(filename):
            continue
        file_path, file_extension = filename.split('.')
        file_catagories[file_extension] = "default"

    for key in file_catagories:
        file_catagories[key] = input("What category would you like to sort {} files into?".format(key))

    for filename in filenames:
        if os.path.isdir(filename):
            continue
        file_path, file_extension = filename.split('.')
        try:
            os.mkdir(file_catagories[file_extension])
        except FileExistsError:
            pass
        print(os.path.join(file_catagories[file_extension], filename))
        shutil.copy(filename, os.path.join(file_catagories[file_extension], filename))


main()
