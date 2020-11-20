# Linked List

## What to talk about
 - Design of linked list (include image)
 - How does it link to each other
 - How does it save memory (uses space in memory instead of array of data)
 - When to use it
 - performance


 ## Design of a linked list
 A linked list is a list of values that are not stored in a specific array. Instead, the values are stored in memory  
and are accesed by referencing the other values.


 
 ## Possible Practice Problems
 - Blockchain example of confirming payments (one person buys something, and is confirmed by other person/business)
 - something else :)
 - create a list and add up all values in list

 ## Adding All Values
 - create linked list w/references to everything
 - Create that iter function to run through list
 - create function to sum all values (have them create that function)

 ```python

# refer to list_ex1.py file for full code

class Linked_list:
    """
    Create a linked list that holds the values of the head and the tail. Any other data
    to be held here will be within the inner class Data.
    """

    class Data:
        """
        Here will be the values held in the list. There will also be references to 
        the next itmes in the linked list.
        """

        # define the values held and the references to the next item in the list
        def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


    # define the head and tail of the linked list
    def __init__(self):
        self.head = None
        self.tail = None


    # function to insert into list
    # user will specify if the item is to be placed in head or tail (one function for two purposes)
    def insert(self, value, place):
        # create a var to store the new data
        # change the var name later
        stuff = Linked_list.Data(value)


        # if there is no data, set the head and tail as the new data
        if self.head is None and self.tail is None:
            self.head = stuff
            self.tail = stuff

        else:
            # if place is 'head'
            if place.lower() == 'head':
                stuff.next = self.head    # connnect the old head to the new data
                self.head.prev = stuff    # connect the previous head to the new data
                self.head = stuff         # set the head to the new data

            elif place.lower() == 'tail':
                stuff.prev = self.tail    # connect the old tail to the new data
                self.tail.next = stuff    # connect the previous tail to the new data
                self.tail = stuff         # set the tail to the new data
        




 ```
 
 ## Blockchain Example
 - Maybe scrap this example

 ```python

 class Blockchain:
    """
    Create a blockchain using a linked list. This simple list uses
    other data in the list to confirm transactions between users. 
    """

    class Data:
        def __init__(self, balance):
            # purpose of balance is to confirm balance of user
            # next and prev are to confirm if the transaction is valid
            self.balance = balance
            self.next = None
            self.prev = None

    def __init__(self):
        # what data do I need?
        # make a head and tail (start and stop)
        self.head = None
        self.tail = None

    def create_data(self, value):

        # create Data value
        new_balance = Blockchain.Data(value)

        if self.head is None or self.tail is None:
            self.head = 


 ```
 
 Develop better ideas and think about it a lot. Create new content problems in the week.

Return to [introduction](introduction.md) file.
