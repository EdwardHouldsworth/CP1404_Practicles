"""class: programming language"""


class ProgrammingLanguage:
    max_name_length = 0

    def __init__(self, name="", typing="", reflection=False, year=0):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
        ProgrammingLanguage.max_name_length = len(name) if len(
            name) > ProgrammingLanguage.max_name_length else ProgrammingLanguage.max_name_length
        # i would have to subtract when an instance is destroyed
        # def __delete__(self, instance):?
        # def __del__

    def __str__(self):
        return "{}, {}, Reflection={}, First appeared in {}".format(self.name, self.typing,
                                                                    self.reflection, self.year)

    def __lt__(self, other):
        return self.year < other.year

    # operator.__lt__ is "less than"
    # __le__ "less than or equal to"
    # __ge__ "greater than or equal to"
    # __gt__ "greater than"
    # __eq__ "equal"
    # __ne__ "not equal"

    def is_dynamic(self):
        return self.typing.lower() == "static"
