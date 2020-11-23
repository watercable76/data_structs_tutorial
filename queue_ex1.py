"""
Date Created: 11/23/2020
Author: Nicholas Cable, el cablecito
Purpose: Create a tutorial about queues that allow the reader to
        understand it's format and have enough functions to
        demonstrate how it works.

"""

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
    

    # define the class as being a []
    def __init__(self):
        self.queue = []
    

    # create a function to add values to a queue
    def enqueue(self):
        
