"""Word Finder: finds random words from a dictionary."""
import random


class WordFinder:
    ...

    def __init__(self, file_name):
        self.file_name = file_name
        print(f"{len(self.read_file())} words read")

    def read_file(self):
        file = open(self.file_name)
        return file.read().split("\n")

    def random(self):
        return self.read_file()[random.randint(0, len(self.read_file()) - 1)]

    def test(self):
        return self.read_file()


class SpecialWordFinder(WordFinder):
    def __init__(self, file_name):
        super().__init__(file_name)

    def read_file(self):
        file = super().read_file()
        for el in file:
            if el == "":
                file.remove(el)
        for el in file:
            if el.startswith("#") == True:
                file.remove(el)
        return file

    def random(self):
        return super().random()

    def test(self):
        return super().test()