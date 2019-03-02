""" A test file for theme creation """

from os import listdir


class User:
    def __init__(self, name="user", isAdmin=False):
        # I'm just a sigle line comment, don't mind me
        self.name = name
        self.isAdmin = isAdmin

    def foo(self, bar):
        for v in bar:
            print("Wow such a beautiful file")
        return listdir("/")

    @property
    def age(self):
        return 42


if __name__ == "__main__":
    my_set = {number for number in range(100) if number % 3 == 0}
