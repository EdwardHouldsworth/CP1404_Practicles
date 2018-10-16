import shutil
import os


def main():
    print("Starting directory is: {}".format(os.getcwd()))
    os.chdir('Lyrics')
    lyrics_path = os.getcwd()  # store the path so we can get back to it
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        for filename in filenames:
            new_name = get_fixed_filename(filename)
            print("Renaming {} to {}".format(filename, new_name))
            os.rename(os.path.join(directory_name,filename),
                      os.path.join(directory_name,new_name))

    os.chdir(lyrics_path)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    return new_name


main()
