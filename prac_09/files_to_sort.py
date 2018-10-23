import shutil
import os


def main():
    os.chdir('FilesToSort')
    print("Starting directory is: {}".format(os.getcwd()))
    filenames = os.listdir('.')
    for filename in filenames:
        if os.path.isdir(filename):
            continue
        file_path, file_extension = filename.split('.')
        try:
            os.mkdir(file_extension)
        except FileExistsError:
            pass
        print(filename)
        shutil.copy(filename, os.path.join(file_extension, filename))


main()
