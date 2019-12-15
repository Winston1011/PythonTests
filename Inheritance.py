class Parent():

    def print_last_name(self):
        print('DZ')

class Child(Parent):

    def print_first_name(self):
        print('Winston')
    def print_last_name(self):
        print('Override')

winston = Child()
winston.print_first_name()
winston.print_last_name()