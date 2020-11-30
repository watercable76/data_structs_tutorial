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
        def __init__(self, student, limit):
            self.student = student
            self.limit = limit

    # define the queue
    def __init__(self):
        self.queue = []

    # str constructor to print out data nicely
    def __str__(self):
        result = 'Students in Class: ['
        for node in self.queue:
            result += str(node) + ', '
        result = result[:-2] + ']'
        return result
