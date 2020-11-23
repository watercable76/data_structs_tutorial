"""
Date Created: 11/23/2020
Author: Nicholas Cable, el cablecito
Purpose: Create a tutorial about queues that allow the reader to
        understand it's format and have enough functions to
        demonstrate how it works.

"""


import random


class Queue:
    """
    This class holds the basic outline of a queue []. The main functions will
    be declared here.
    """

    class Node:
        """
        This will hold the data of the queue. For now, there will only be one
        value held in the __init__().
        """

        def __init__(self, value):
            self.value = value

        # need __str__ to print out object's value
        # if this is not added, would return place in memory of object
        def __str__(self):
            return f'{self.value}'

    # define the class as being a []
    def __init__(self):
        self.queue = []

    # create a function to add values to a queue
    def enqueue(self, value):
        new_node = Queue.Node(value)
        self.queue.append(new_node)

    # str function overwrite
    # return str(node) to make everything string
    # (who knows what values could be put in here)
    def __str__(self):
        result = '['
        for node in self.queue:
            result += str(node) + ', '
        result += ']'
        return result

    # write a dequeue function
    def dequeue(self):

        # set a var as the value to be removed
        removal = self.queue[0]
        del self.queue[0]
        print(f'The value being removed is {removal}.\n')


# Test Cases!
print(f"{' TEST CASE 1 ':=^40}\n")
q1 = Queue()
q1.enqueue(random.randint(1, 10))
q1.enqueue(random.randint(10, 22))
q1.enqueue(random.randint(20, 30))
print(q1)

# Test case 2
print(f"\n{' TEST CASE 2 ':=^40}\n")
q1.dequeue()
