"""
Filename: class_reg.py
Created by: Nicholas Cable, el cablecito
Date Created: 11/30/2020
Last updated: ...
Purpose: create a template file for people to created a queue based off
        of registering for a class in a university. The first class will be
        Classes, and the second class is Registration. The CLasses class will
        hold the limit of each class, and the Registration class will hold the
        names of students, the teacher, and how many spots are left open.

"""

import random


class Classes:
    """
    This class is a queue that will hold the Registration class. Classes will
    include default constructors to format the output as well as hold the
    list for the queue.
    """

    class Registration:
        """
        Create a Registration class that holds the students in the queue,
        and the max number of students the class supports.
        """

        # define the student names and the max num the class
        # can support
        def __init__(self, student):
            self.student = student

        # string function to print out better
        def __str__(self):
            return f'{self.student}'

    # define the queue
    def __init__(self, limit, teacher):
        self.queue = []
        self.limit = limit
        self.teacher = teacher
        if limit <= 0:
            print("That is not a valid class size!")
            print(f'A random class size will be entered.\n')
            self.limit = random.randint(0, 15)
        if type(teacher) is not str:
            print("That is a not a valid teacher name!")
            print(f'A random teacher will be assigned.\n')
            self.teacher = 'Mister Blue'

    # str constructor to print out data nicely
    def __str__(self):
        result = 'Students in Class: ['
        for node in self.queue:
            result += str(node) + ', '
        result = result[:-2] + ']'
        return result

    # len constructor
    def __len__(self):
        return len(self.queue)

    # show class size and the teacher
    def print_class(self):
        print(f'The class size is {self.limit} and the teacher is {self.teacher}.\n')

    # add students to the list
    def enqueue(self, student):

        if self.limit == len(self.queue):
            print('Error! Class is already full!')
        else:
            new_node = Classes.Registration(student)
            self.queue.append(new_node)
            print(f"Student {student} was added to the course.")

    # dequeue function to remove students
    def dequeue(self):
        if len(self.queue) == 0:
            print('There is no one registered yet!\n')
        else:
            removal = self.queue[0]
            del self.queue[0]
            print(f"The student who dropped the course is {removal}.")


# Test Cases

# If the user inputs a wrong class size and an invalid teacher,
# a size and teacher will be assigned.
print(f"{' TEST CASE 1 ':=^40}\n")
ex1 = Classes(0, 0)
ex1.print_class()

# Test 2
print(f"{' TEST CASE 2 ':=^40}\n")
ex2 = Classes(4, 'Mister Coolio')
ex2.enqueue('Joe Mama')
ex2.enqueue('Jose Santos')
ex2.enqueue('Lucy Gerald')
ex2.enqueue('John Smith')
ex2.print_class()
print(ex2)

# Test 3
print(f"{' TEST CASE 3 ':=^40}\n")
ex2.dequeue()
