class ProgrammingLanguage:
    max_name_length = 0

    def __init__(self, name="", typing="", reflection=False, year=0):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
        ProgrammingLanguage.max_name_length = len(name) if len(
            name) > ProgrammingLanguage.max_name_length else ProgrammingLanguage.max_name_length

    def __str__(self):
        return "{}, {}, Reflection={}, First appeared in {}".format(self.name, self.typing,
                                                                    self.reflection, self.year)

    def __lt__(self, other):
        return self.year < other.year

    def is_dynamic(self):
        return False if self.typing.lower() == "static" else True
