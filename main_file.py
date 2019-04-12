
class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def email(self):
        return '{}.{}@mail.ru'.format(self.first, self.last)

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
