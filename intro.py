
# Object Oriented Programming Python


class Employee:

    raise_amt = 1.05

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('John', 'Smith')


print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname())
