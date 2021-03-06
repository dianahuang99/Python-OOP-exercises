"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        self.start = start
        self.new = start

    def __repr__(self):
        return f"<SerialGenerator start = {self.start} new = {self.new}>"

    def generate(self):
        """This will return the start first then count up"""
        self.new += 1
        return self.new - 1

    def reset(self):
        """This will reset the count to the original start"""
        self.new = self.start


serial = SerialGenerator(start=100)
