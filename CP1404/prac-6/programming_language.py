class ProgrammingLanguage:

    def __init__(self, name, typing, is_dynamic, year=0):
        self.name = name
        self.typing = typing
        self.is_dynamic = is_dynamic
        self.year = year

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.is_dynamic}, First appeared in {self.year}"

    def is_dynamic(self):
        return self.is_dynamic


