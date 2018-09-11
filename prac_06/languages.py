from prac_06.programming_language import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic 6", "Static", False, 1991)
    java = ProgrammingLanguage("Java", "Static", True, 1995)
    cplusplus = ProgrammingLanguage("C++", "Static", False, 1983)
    languages = [ruby, python, visual_basic, java, cplusplus]

    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)

    print("The years the languages came out are:")
    for language in sorted(languages):
        print("{:{}} in {}".format(language.name, language.max_name_length, language.year))


main()
